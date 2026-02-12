export interface PersonalData {
  age: number;
  birth_date?: string;
  age_detail?: string;
  gender: string;
  weight: number;
  height: number;
  bmi?: number;
}

export interface PhysicalActivity {
  frequency: string;
  type: string;
  intensity: string;
}

export interface Sleep {
  quality: string;
  hours: number;
  issues: string[];
}

export interface AlcoholConsumption {
  frequency: string;
  amount: string;
}

export interface Medication {
  name: string;
  frequency: string;
  dosage: string | null;
}

export interface ContextFactors {
  medical_history: string[];
  intolerances: string[];
  physical_activity: PhysicalActivity;
  sleep: Sleep;
  alcohol_consumption: AlcoholConsumption;
  medications: Medication[];
  stress_level: string;
}

export interface TobaccoUse {
  uses_or_used: string;
  frequency: string;
}

export interface FoodAllergies {
  has_allergy: string;
  allergy_items: string[];
}

export interface FoodAvoidance {
  avoids_food: string;
  food_items: string[];
}

interface BaseAnamnesis {
  patient_id: string;
  objective: string;
  personal_data: PersonalData;
  context_factors: ContextFactors;
  surgeries: string[];
  menopause_age: string;
  tobacco_use: TobaccoUse;
  food_allergies: FoodAllergies;
  food_avoidance: FoodAvoidance;
  supplements: string[];
}

export interface IonNutriAnamnesis extends BaseAnamnesis {
  anamnesis_type: 'ionnutri';
  family_history: Record<string, string>;
  environmental_exposure: Record<string, string>;
}

export interface VidaNovaAnamnesis extends BaseAnamnesis {
  anamnesis_type: 'vidanova';
  diet_type: string;
  energy_level: string;
  muscle_gain_goal: string;
  nutritionist_plan: string;
  difficulty_muscle_gain: string;
}

export type AnamnesisUnion = IonNutriAnamnesis | VidaNovaAnamnesis;

export type AnamnesisType = 'ionnutri' | 'vidanova';
