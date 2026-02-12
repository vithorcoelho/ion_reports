import { apiClient } from './client';
import type { TNMExamData } from '../types/exam';
import type { AnamnesisUnion } from '../types/anamnesis';
import type { MarkdownReportOut } from '../types/report';

interface GenerateReportRequest {
  exam_data: TNMExamData;
  anamnesis: AnamnesisUnion;
}

export const reportsApi = {
  generateReport: async (
    exam_data: TNMExamData,
    anamnesis: AnamnesisUnion,
    exam_type?: string
  ): Promise<MarkdownReportOut> => {
    const requestBody: GenerateReportRequest = {
      exam_data,
      anamnesis,
    };

    const response = await apiClient.post<MarkdownReportOut>(
      '/api/v1/reports/',
      requestBody,
      {
        params: exam_type ? { exam_type } : undefined,
      }
    );
    return response.data;
  },

  generatePDF: async (
    markdown_content: string,
    patient_id: string,
    report_id: string
  ): Promise<Blob> => {
    const response = await apiClient.post(
      '/api/v1/reports/pdf',
      {
        markdown_content,
        patient_id,
        report_id,
      },
      {
        responseType: 'blob',
      }
    );
    return response.data;
  },

  healthCheck: async (): Promise<{ status: string }> => {
    const response = await apiClient.get('/health');
    return response.data;
  },
};
