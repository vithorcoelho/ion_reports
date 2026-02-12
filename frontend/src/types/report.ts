export interface MarkdownReportOut {
  report_id: string;
  patient_id: string;
  anamnesis_id: string;
  exam_id: string;
  version: string;
  timestamp: string;
  report: string; // markdown content
}
