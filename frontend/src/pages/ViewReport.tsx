import { useParams, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Container from '../components/layout/Container';
import Button from '../components/common/Button';
import Alert from '../components/common/Alert';
import MarkdownViewer from '../components/report/MarkdownViewer';
import type { MarkdownReportOut } from '../types/report';
import { reportsApi } from '../api/reports';

export default function ViewReport() {
  const { reportId } = useParams<{ reportId: string }>();
  const navigate = useNavigate();
  const [report, setReport] = useState<MarkdownReportOut | null>(null);
  const [isGeneratingPDF, setIsGeneratingPDF] = useState(false);
  const [pdfError, setPdfError] = useState<string | null>(null);

  useEffect(() => {
    if (reportId) {
      const storedReport = sessionStorage.getItem(`report_${reportId}`);
      if (storedReport) {
        setReport(JSON.parse(storedReport));
      }
    }
  }, [reportId]);

  const handleDownloadPDF = async () => {
    if (!report) return;

    setIsGeneratingPDF(true);
    setPdfError(null);

    try {
      // Call backend to generate PDF
      const pdfBlob = await reportsApi.generatePDF(
        report.report,
        report.patient_id,
        report.report_id
      );

      // Create download link
      const url = window.URL.createObjectURL(pdfBlob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `report_${report.report_id}.pdf`;
      document.body.appendChild(link);
      link.click();

      // Cleanup
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    } catch (err: any) {
      console.error('Error generating PDF:', err);
      const errorMessage = err.response?.data?.detail || err.message || 'Failed to generate PDF';
      setPdfError(errorMessage);
    } finally {
      setIsGeneratingPDF(false);
    }
  };

  if (!report) {
    return (
      <Container>
        <Alert variant="warning">Report not found.</Alert>
        <Button onClick={() => navigate('/')} className="mt-4">
          Go Home
        </Button>
      </Container>
    );
  }

  return (
    <Container>
      <div className="max-w-4xl mx-auto">
        <div className="mb-6 no-print">
          <Button onClick={() => navigate('/')} variant="secondary">
            &larr; Back to Home
          </Button>
        </div>

        {pdfError && (
          <Alert variant="error" className="mb-4">
            <strong>PDF Generation Error:</strong> {pdfError}
            {pdfError.includes('wkhtmltopdf') && (
              <p className="mt-2 text-sm">
                wkhtmltopdf is not installed on the server. You can still use the "Print to PDF" option in your browser.
              </p>
            )}
          </Alert>
        )}

        <div className="bg-white p-8 rounded-lg shadow">
          <div className="border-b pb-4 mb-6">
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Report for Patient {report.patient_id}
            </h1>
            <div className="grid grid-cols-2 gap-4 text-sm text-gray-600">
              <div>
                <strong>Report ID:</strong> {report.report_id}
              </div>
              <div>
                <strong>Version:</strong> {report.version}
              </div>
              <div>
                <strong>Generated:</strong>{' '}
                {new Date(report.timestamp).toLocaleString()}
              </div>
            </div>
          </div>

          <MarkdownViewer content={report.report} />
        </div>

        <div className="mt-6 flex gap-4 no-print">
          <Button
            onClick={handleDownloadPDF}
            disabled={isGeneratingPDF}
          >
            {isGeneratingPDF ? '⏳ Generating PDF...' : '⬇️ Download PDF'}
          </Button>
          <Button onClick={() => window.print()} variant="secondary">
            🖨️ Print to PDF
          </Button>
          <Button
            variant="secondary"
            onClick={() => {
              navigator.clipboard.writeText(report.report);
              alert('Report copied to clipboard!');
            }}
          >
            📋 Copy to Clipboard
          </Button>
        </div>
      </div>
    </Container>
  );
}
