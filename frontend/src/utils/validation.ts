import { z } from 'zod';

export const metaboliteSchema = z.object({
  name: z.string().min(1, 'Metabolite name is required'),
  value: z.number().positive('Value must be greater than 0'),
});

export const examDataSchema = z.object({
  patient_id: z.string().min(1, 'Patient ID is required'),
  exam_date: z.string().min(1, 'Exam date is required'),
  metabolites: z.array(metaboliteSchema).min(1, 'At least one metabolite is required'),
});
