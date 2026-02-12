"""PDF generation service for reports.

This service converts markdown reports to PDF format using wkhtmltopdf.
"""

import shutil
from pathlib import Path

import pdfkit
from markdown2 import Markdown

from app.core.logging import logger


class PDFService:
    """Service for generating PDF files from markdown reports."""

    def __init__(self):
        """Initialize PDF service and check for wkhtmltopdf."""
        self.wkhtmltopdf_path = shutil.which("wkhtmltopdf")
        self.markdown_converter = Markdown(
            extras=[
                "fenced-code-blocks",
                "tables",
                "header-ids",
                "toc",
                "strike",
                "task_list",
            ]
        )

        if not self.wkhtmltopdf_path:
            logger.warning(
                "wkhtmltopdf not found in PATH. PDF generation will not work. "
                "Install it with: sudo apt-get install wkhtmltopdf (Ubuntu/Debian) "
                "or brew install wkhtmltopdf (macOS)"
            )

    def is_available(self) -> bool:
        """Check if PDF generation is available (wkhtmltopdf installed)."""
        return self.wkhtmltopdf_path is not None

    def markdown_to_html(
        self, markdown_content: str, patient_id: str, report_id: str
    ) -> str:
        """Convert markdown to HTML with proper styling.

        Args:
            markdown_content: The markdown content to convert
            patient_id: Patient ID for header
            report_id: Report ID for header

        Returns:
            HTML string with styles

        """
        # Convert markdown to HTML
        html_body = self.markdown_converter.convert(markdown_content)

        # Create full HTML with styling
        html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório TNM - {patient_id}</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
            @bottom-center {{
                content: "Página " counter(page) " de " counter(pages);
                font-size: 9pt;
                color: #666;
            }}
        }}

        body {{
            font-family: 'Roboto', 'Helvetica', 'Arial', sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }}

        /* Header */
        .report-header {{
            border-bottom: 2px solid #2563eb;
            padding-bottom: 1rem;
            margin-bottom: 2rem;
        }}

        .report-header h1 {{
            margin: 0;
            font-size: 20pt;
            color: #1e40af;
        }}

        .report-meta {{
            display: flex;
            gap: 2rem;
            margin-top: 0.5rem;
            font-size: 9pt;
            color: #666;
        }}

        /* Headings */
        h1 {{
            font-size: 18pt;
            color: #1e40af;
            margin-top: 2rem;
            margin-bottom: 1rem;
            page-break-after: avoid;
        }}

        h2 {{
            font-size: 14pt;
            color: #2563eb;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            page-break-after: avoid;
        }}

        h3 {{
            font-size: 12pt;
            color: #3b82f6;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            page-break-after: avoid;
        }}

        /* Paragraphs */
        p {{
            margin-bottom: 0.75rem;
            text-align: justify;
            orphans: 3;
            widows: 3;
        }}

        /* Lists */
        ul, ol {{
            margin-bottom: 1rem;
            padding-left: 2rem;
            page-break-inside: avoid;
        }}

        li {{
            margin-bottom: 0.5rem;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            page-break-inside: avoid;
        }}

        th {{
            background-color: #e0e7ff;
            padding: 0.5rem;
            text-align: left;
            border: 1px solid #c7d2fe;
            font-weight: 600;
        }}

        td {{
            padding: 0.5rem;
            border: 1px solid #e5e7eb;
        }}

        /* Code */
        code {{
            background-color: #f3f4f6;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
        }}

        pre {{
            background-color: #f9fafb;
            padding: 1rem;
            border-radius: 5px;
            overflow-x: auto;
            page-break-inside: avoid;
            border-left: 3px solid #3b82f6;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
        }}

        /* Blockquotes */
        blockquote {{
            border-left: 4px solid #d1d5db;
            padding-left: 1rem;
            margin: 1rem 0;
            color: #6b7280;
            font-style: italic;
            page-break-inside: avoid;
        }}

        /* Strong text */
        strong {{
            font-weight: 600;
            color: #1f2937;
        }}

        /* Links */
        a {{
            color: #2563eb;
            text-decoration: none;
        }}

        /* Horizontal rules */
        hr {{
            border: none;
            border-top: 1px solid #e5e7eb;
            margin: 2rem 0;
        }}
    </style>
</head>
<body>
    <div class="report-header">
        <h1>IONNUTRI | NUTRIÇÃO DE PRECISÃO LTDA</h1>
        <div class="report-meta">
            <div><strong>Paciente:</strong> {patient_id}</div>
            <div><strong>Relatório:</strong> {report_id}</div>
        </div>
    </div>

    {html_body}
</body>
</html>
"""
        return html

    def generate_pdf(
        self,
        markdown_content: str,
        patient_id: str,
        report_id: str,
        output_path: Path | None = None,
    ) -> bytes:
        """Generate PDF from markdown content.

        Args:
            markdown_content: The markdown report content
            patient_id: Patient ID
            report_id: Report ID
            output_path: Optional path to save PDF file

        Returns:
            PDF file content as bytes

        Raises:
            RuntimeError: If wkhtmltopdf is not installed
            Exception: If PDF generation fails

        """
        if not self.is_available():
            raise RuntimeError(
                "wkhtmltopdf is not installed. "
                "Install it with: sudo apt-get install wkhtmltopdf (Ubuntu/Debian) "
                "or brew install wkhtmltopdf (macOS)"
            )

        logger.info(f"Generating PDF for report {report_id}")

        try:
            # Convert markdown to HTML
            html_content = self.markdown_to_html(
                markdown_content, patient_id, report_id
            )

            # Configure PDF options
            options = {
                "page-size": "A4",
                "margin-top": "2cm",
                "margin-right": "2cm",
                "margin-bottom": "2cm",
                "margin-left": "2cm",
                "encoding": "UTF-8",
                "enable-local-file-access": None,
                "print-media-type": None,
                "no-outline": None,
                "quiet": None,
            }

            # Generate PDF
            if output_path:
                # Save to file
                pdfkit.from_string(
                    html_content,
                    str(output_path),
                    options=options,
                    configuration=pdfkit.configuration(
                        wkhtmltopdf=self.wkhtmltopdf_path
                    ),
                )
                logger.info(f"PDF saved to {output_path}")
                return output_path.read_bytes()
            else:
                # Return as bytes
                pdf_bytes = pdfkit.from_string(
                    html_content,
                    False,  # False means return bytes instead of saving
                    options=options,
                    configuration=pdfkit.configuration(
                        wkhtmltopdf=self.wkhtmltopdf_path
                    ),
                )
                logger.info(f"PDF generated successfully for report {report_id}")
                return pdf_bytes

        except Exception as e:
            logger.error(f"Error generating PDF for report {report_id}: {str(e)}")
            raise


# Global instance
pdf_service = PDFService()
