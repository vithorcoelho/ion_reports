"""Utility for Generating Reports from MLflow Traces."""

import argparse
import json
import os
import time
import traceback
from datetime import datetime
from typing import Any

import mlflow
from dotenv import load_dotenv
from mlflow import MlflowClient

from app.core.config import settings


def _format_json(value: Any) -> str:
    """Format a value as a well-indented JSON string.

    Args:
        value (Any): The value to format.

    Returns:
        str: The formatted JSON string.

    """
    try:
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
                return json.dumps(parsed, indent=2, ensure_ascii=False)
            except json.JSONDecodeError:
                return value
        return json.dumps(value, indent=2, ensure_ascii=False, default=str)
    except Exception:
        return str(value)


def save_report_locally(content: str, filename: str, output_dir: str | None):
    """Save the report content to a file in the specified directory.

    Args:
        content (str): The report content to save.
        filename (str): The filename for the report.
        output_dir (str | None): The directory where the file will be saved. If None,
                                 saves to the script's directory.

    """
    if output_dir:
        # Ensure the target directory exists
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, filename)
    else:
        # Use the script's directory as default
        file_path = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Local report successfully saved at: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error saving local file at {file_path}: {e}")


def find_structured_report_from_trace(
    trace: Any,
) -> tuple[dict[str, Any] | None, str | None]:
    """Scan the spans in a trace to find the complete structured report.

    Args:
        trace (Any): The trace object containing spans.

    Returns:
        tuple[dict[str, Any] | None, str | None]: A tuple containing the
                                                  structured report and the report type
                                                  ('ionnutri', 'vidanova'), or (None, None).

    """
    print("Searching for the span containing the structured report in the trace...")
    possible_report_span_names = {
        "build_ionnutri_report": "ionnutri",
        "build_vidanova_report": "vidanova",
        "build_structured_report": "ionnutri",  # Default structured to ionnutri
    }

    for span in trace.data.spans:
        if span.name in possible_report_span_names:
            print(f"Structured report span found: '{span.name}'!")
            report_type = possible_report_span_names[span.name]
            outputs = span.outputs

            try:
                if isinstance(outputs, str):
                    structured_data = json.loads(outputs)
                elif isinstance(outputs, dict):
                    structured_data = outputs
                else:
                    return None, None

                return structured_data, report_type

            except json.JSONDecodeError:
                print(f"Error decoding JSON from output of span '{span.name}'.")
                return None, None

    print("No span with the structured report was found in the trace.")
    return None, None


def render_simple_markdown(structured: dict[str, Any]) -> str:
    """Create a simple Markdown report from structured content.

    Args:
        structured (dict[str, Any]): The structured report data.

    Returns:
        str: The Markdown report.

    """
    print("Building the final Markdown report from structured data...")

    if "recommendations" in structured:
        report_title = "IonNutri Report"
        lines = [
            f"# {report_title} - {structured.get('report_id', 'N/A')}",
            "",
            f"**Patient:** {structured.get('patient_id', 'N/A')}",
            f"**Version:** {structured.get('version', 'N/A')}",
            "",
            "---",
            "## Summary",
            structured.get("summary", {}).get("content", "-"),
            "",
            "---",
            "## Findings",
            "```json",
            _format_json(structured.get("findings", {})),
            "```",
            "",
            "---",
            "## Nutritional Recommendations",
            "- **Energetics:**",
            "```json",
            _format_json(
                structured.get("recommendations", {})
                .get("nutritional", {})
                .get("energetics", {})
            ),
            "```",
            "- **Constructors:**",
            "```json",
            _format_json(
                structured.get("recommendations", {})
                .get("nutritional", {})
                .get("constructors", {})
            ),
            "```",
            "- **Regulators:**",
            "```json",
            _format_json(
                structured.get("recommendations", {})
                .get("nutritional", {})
                .get("regulators", {})
            ),
            "```",
            "- **Fats:**",
            "```json",
            _format_json(
                structured.get("recommendations", {})
                .get("nutritional", {})
                .get("fats", {})
            ),
            "```",
            "",
            "---",
            "## Supplementation",
            "```json",
            _format_json(structured.get("recommendations", {}).get("supplements", {})),
            "```",
            "",
            "---",
            "## Lifestyle",
            "```json",
            _format_json(structured.get("recommendations", {}).get("lifestyle", {})),
            "```",
        ]
    elif "diet_suggestions" in structured:
        report_title = "Vida Nova Report"
        lines = [
            f"# {report_title} - {structured.get('report_id', 'N/A')}",
            "",
            f"**Patient:** {structured.get('patient_id', 'N/A')}",
            f"**Version:** {structured.get('version', 'N/A')}",
            "",
            "---",
            "## Summary",
            structured.get("summary", {}).get("content", "-"),
            "",
            "---",
            "## Findings",
            "```json",
            _format_json(structured.get("findings", {})),
            "```",
            "",
            "---",
            "## Diet Suggestions",
            "```json",
            _format_json(structured.get("diet_suggestions", {})),
            "```",
            "",
            "---",
            "## Suggested Supplementation",
            "```json",
            _format_json(structured.get("supplements", {})),
            "```",
            "",
            "---",
            "## Training Tip",
            "```json",
            _format_json(structured.get("training", {})),
            "```",
        ]
    else:
        report_title = "Report"
        lines = [f"# {report_title} {structured.get('report_id', 'N/A')}"]
        for key, value in structured.items():
            lines.append(f"\n## {key.replace('_', ' ').title()}")
            if isinstance(value, dict | list):
                lines.append(f"```json\n{_format_json(value)}\n```")
            else:
                lines.append(str(value))

    return "\n".join(lines)


def build_markdown_from_trace(trace: Any) -> str:
    """Create a detailed Markdown debug report from a trace object.

    Args:
        trace (Any): The trace object.

    Returns:
        str: The Markdown debug report.

    """
    info = trace.info
    trace_id = getattr(info, "trace_id", getattr(info, "request_id", "unknown"))
    state = str(getattr(info, "state", getattr(info, "status", "UNKNOWN")))
    start_time_ms = getattr(info, "start_time_ms", getattr(info, "timestamp_ms", None))
    end_time_ms = getattr(info, "end_time_ms", None)
    if end_time_ms is None and start_time_ms is not None:
        duration_ms = getattr(info, "execution_duration_ms", 0)
        end_time_ms = start_time_ms + duration_ms

    header = [
        "# MLflow Trace Report",
        "",
        f"**Trace ID:** `{trace_id}`",
        f"**State:** `{state}`",
    ]
    if start_time_ms:
        header.append(
            f"**Start:** `{datetime.fromtimestamp(start_time_ms / 1000).isoformat()}`"
        )
    if end_time_ms:
        header.append(
            f"**End:** `{datetime.fromtimestamp(end_time_ms / 1000).isoformat()}`"
        )

    token_usage = getattr(info, "token_usage", None)
    if token_usage:
        usage_dict = (
            token_usage
            if isinstance(token_usage, dict)
            else token_usage.to_dictionary()
        )
        header.append(
            f"**Token Usage:** input={usage_dict.get('input_tokens', 'N/A')}, "
            f"output={usage_dict.get('output_tokens', 'N/A')}, "
            f"total={usage_dict.get('total_tokens', 'N/A')}"
        )

    lines = header + ["", "---", "## Spans", ""]
    spans = sorted(list(trace.data.spans), key=lambda s: s.start_time_ns)

    for idx, span in enumerate(spans, start=1):
        lines.append(f"### {idx}. {span.name}")
        lines.extend(
            [f"- **Type:** `{span.span_type}`", f"- **State:** `{span.status}`"]
        )
        if span.parent_id:
            lines.append(f"- **Parent:** `{span.parent_id}`")

        if idx == 1:
            if span.attributes:
                lines.append(
                    f"- **Attributes:**\n```json\n{_format_json(span.attributes)}\n```"
                )
        else:
            filtered_attributes = {}
            if span.attributes:
                for key, value in span.attributes.items():
                    if key not in ["mlflow.spanInputs", "mlflow.spanOutputs"]:
                        filtered_attributes[key] = value

            if filtered_attributes:
                lines.append(
                    f"- **Attributes:**\n```json\n{_format_json(filtered_attributes)}\n```"
                )
            if span.inputs:
                lines.append(
                    f"- **Inputs:**\n```json\n{_format_json(span.inputs)}\n```"
                )
            if span.outputs:
                lines.append("- **Outputs:**")
                try:
                    output_data = (
                        json.loads(span.outputs)
                        if isinstance(span.outputs, str)
                        else span.outputs
                    )
                    if isinstance(output_data, dict) and "markdown" in output_data:
                        lines.append(f"\n{output_data['markdown']}\n")
                    else:
                        lines.append(f"```json\n{_format_json(output_data)}\n```")
                except (json.JSONDecodeError, TypeError):
                    lines.append(f"```json\n{_format_json(span.outputs)}\n```")

        lines.append("\n" + "---" + "\n")

    return "\n".join(lines)


def main():
    """Generate debug and final reports from an MLflow trace.

    Parses command-line arguments, fetches the trace, and logs both debug and simple reports as MLflow artifacts.
    Also saves the reports locally if an output directory is specified.
    """
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Generate debug and final reports from an MLflow trace."
    )
    parser.add_argument("--run-id", help="Run ID to fetch the trace.")
    parser.add_argument("--trace-id", help="Specific Trace ID to fetch.")
    parser.add_argument(
        "--output-dir", help="Local directory to save the Markdown reports."
    )

    args = parser.parse_args()

    mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
    client = MlflowClient()

    try:
        experiment = client.get_experiment_by_name(settings.MLFLOW_EXPERIMENT_NAME)
        if not experiment:
            print(f"Experiment '{settings.MLFLOW_EXPERIMENT_NAME}' not found.")
            return

        target_trace_id = args.trace_id
        target_run_id = args.run_id

        if not target_run_id:
            print("No Run ID provided, searching for the most recent...")
            latest_runs = client.search_runs(
                experiment_ids=[experiment.experiment_id],
                order_by=["start_time DESC"],
                max_results=1,
            )
            if not latest_runs:
                print("No runs found in the experiment.")
                return
            target_run_id = latest_runs[0].info.run_id
            print(f"Using the most recent run: {target_run_id}")

        trace = None
        for attempt in range(5):
            print(
                f"Fetching traces for Run ID: {target_run_id} (Attempt {attempt + 1})"
            )
            try:
                if target_trace_id:
                    trace = client.get_trace(trace_id=target_trace_id)
                else:
                    traces_info = client.search_traces(
                        run_id=target_run_id, experiment_ids=[experiment.experiment_id]
                    )
                    if traces_info:
                        target_trace_id = traces_info[0].info.trace_id
                        trace = client.get_trace(trace_id=target_trace_id)

                if trace:
                    print(f"Trace found: {trace.info.trace_id}")
                    break
            except Exception as e:
                print(f"Warning: Attempt failed with error: {e}")

            if not trace:
                print("Trace not yet available, retrying in 3 seconds...")
                time.sleep(3)

        if not trace:
            print(f"No trace found for Run ID '{target_run_id}'.")
            return

        # 1. Generate reports and determine output directory
        print("\n" + "=" * 50)

        # Generate debug report content first
        print("Generating debug report from trace...")
        trace_report_md = build_markdown_from_trace(trace)
        mlflow.log_text(trace_report_md, "trace_report_debug.md", run_id=target_run_id)
        print("Artifact 'trace_report_debug.md' saved to MLflow!")

        # Find structured data and the report type
        structured_report_data, report_type = find_structured_report_from_trace(trace)

        # Determine the final save directory
        base_dir = args.output_dir or os.path.dirname(os.path.abspath(__file__))
        final_output_dir = (
            os.path.join(base_dir, report_type) if report_type else base_dir
        )

        # Save the debug report locally
        save_report_locally(trace_report_md, "trace_report_debug.md", final_output_dir)

        # 2. Generate and save the SIMPLE (final) report
        if structured_report_data:
            print("\n" + "=" * 50)
            simple_report_md = render_simple_markdown(structured_report_data)
            mlflow.log_text(simple_report_md, "simple_report.md", run_id=target_run_id)
            print("Artifact 'simple_report.md' saved to MLflow!")

            # Save the simple report to the same final directory
            save_report_locally(simple_report_md, "simple_report.md", final_output_dir)
        else:
            print(
                "Could not generate 'simple_report.md' because structured data was not found."
            )
        print("=" * 50)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
