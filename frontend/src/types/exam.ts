export interface Metabolite {
  name: string;
  value: number;
}

export interface TNMExamData {
  patient_id: string;
  exam_date: string; // ISO 8601 format
  metabolites: Metabolite[];
}
