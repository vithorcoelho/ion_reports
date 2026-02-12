import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import Container from '../components/layout/Container';
import Button from '../components/common/Button';
import Input from '../components/common/Input';
import Select from '../components/common/Select';
import Alert from '../components/common/Alert';
import Spinner from '../components/common/Spinner';
import FileUpload from '../components/common/FileUpload';
import LoadingDialog from '../components/common/LoadingDialog';
import ExamDataForm from '../components/exam/ExamDataForm';
import PersonalDataForm from '../components/anamnesis/PersonalDataForm';
import ContextFactorsForm from '../components/anamnesis/ContextFactorsForm';
import CommonAnamnesisFieldsForm from '../components/anamnesis/CommonAnamnesisFieldsForm';
import VidaNovaSpecificForm from '../components/anamnesis/VidaNovaSpecificForm';
import IonNutriSpecificForm from '../components/anamnesis/IonNutriSpecificForm';
import { reportsApi } from '../api/reports';
import type { TNMExamData } from '../types/exam';
import type { AnamnesisUnion, AnamnesisType } from '../types/anamnesis';

interface FormData {
  exam_data: TNMExamData;
  anamnesis: AnamnesisUnion;
}

const getDefaultAnamnesis = (type: AnamnesisType): AnamnesisUnion => {
  const baseAnamnesis = {
    patient_id: '',
    objective: '',
    personal_data: {
      age: 0,
      birth_date: '',
      age_detail: '',
      gender: '',
      weight: 0,
      height: 0,
      bmi: 0,
    },
    context_factors: {
      medical_history: [],
      intolerances: [],
      physical_activity: {
        frequency: '',
        type: '',
        intensity: '',
      },
      sleep: {
        quality: '',
        hours: 0,
        issues: [],
      },
      alcohol_consumption: {
        frequency: '',
        amount: '',
      },
      medications: [],
      stress_level: '',
    },
    surgeries: [],
    menopause_age: '',
    tobacco_use: {
      uses_or_used: '',
      frequency: '',
    },
    food_allergies: {
      has_allergy: '',
      allergy_items: [],
    },
    food_avoidance: {
      avoids_food: '',
      food_items: [],
    },
    supplements: [],
  };

  if (type === 'vidanova') {
    return {
      ...baseAnamnesis,
      anamnesis_type: 'vidanova',
      diet_type: '',
      energy_level: '',
      muscle_gain_goal: '',
      nutritionist_plan: '',
      difficulty_muscle_gain: '',
    };
  } else {
    return {
      ...baseAnamnesis,
      anamnesis_type: 'ionnutri',
      family_history: {
        diabetes: '',
        hipertensao: '',
        cancer: '',
        doencas_cardiovasculares: '',
        grau_parentesco: '',
      },
      environmental_exposure: {
        poluicao: '',
        exposicao_ocupacional: '',
      },
    };
  }
};

export default function CreateReport() {
  const navigate = useNavigate();
  const [isGenerating, setIsGenerating] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loadSuccess, setLoadSuccess] = useState<string | null>(null);
  const [anamnesisType, setAnamnesisType] = useState<AnamnesisType>('vidanova');

  const {
    register,
    control,
    handleSubmit,
    watch,
    reset,
    formState: { errors },
  } = useForm<FormData>({
    defaultValues: {
      exam_data: {
        patient_id: '',
        exam_date: new Date().toISOString().slice(0, 16),
        metabolites: [],
      },
      anamnesis: getDefaultAnamnesis('vidanova'),
    },
  });

  // Handle anamnesis type change manually
  const handleTypeChange = (newType: AnamnesisType) => {
    const currentFormData = watch();
    setAnamnesisType(newType);
    reset({
      exam_data: currentFormData.exam_data,
      anamnesis: getDefaultAnamnesis(newType),
    });
  };

  const onSubmit = async (data: FormData) => {
    setIsGenerating(true);
    setError(null);

    try {
      // Ensure patient IDs match
      data.anamnesis.patient_id = data.exam_data.patient_id;

      const result = await reportsApi.generateReport(
        data.exam_data,
        data.anamnesis,
        anamnesisType
      );

      // Store report in session storage for viewing
      sessionStorage.setItem(`report_${result.report_id}`, JSON.stringify(result));

      // Navigate to report view
      navigate(`/report/${result.report_id}`);
    } catch (err: any) {
      console.error('Error generating report:', err);
      setError(err.response?.data?.detail || err.message || 'Failed to generate report');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleJsonLoad = (data: any) => {
    try {
      setError(null);
      setLoadSuccess(null);

      // Validate that the JSON has the expected structure
      if (!data.exam_data || !data.anamnesis) {
        throw new Error('Invalid JSON structure. Expected "exam_data" and "anamnesis" fields.');
      }

      // Transform numeric frequency values to strings (backend expects strings)
      const transformedAnamnesis = { ...data.anamnesis };
      if (transformedAnamnesis.context_factors) {
        if (transformedAnamnesis.context_factors.physical_activity) {
          const freq = transformedAnamnesis.context_factors.physical_activity.frequency;
          if (typeof freq === 'number') {
            transformedAnamnesis.context_factors.physical_activity.frequency = freq.toString();
          }
        }
        if (transformedAnamnesis.context_factors.alcohol_consumption) {
          const freq = transformedAnamnesis.context_factors.alcohol_consumption.frequency;
          if (typeof freq === 'number') {
            transformedAnamnesis.context_factors.alcohol_consumption.frequency = freq.toString();
          }
        }
      }

      // Reset form with loaded data FIRST
      reset({
        exam_data: data.exam_data,
        anamnesis: transformedAnamnesis,
      });

      // Then update anamnesis type (this won't trigger form reset anymore)
      if (data.anamnesis.anamnesis_type) {
        setAnamnesisType(data.anamnesis.anamnesis_type);
      }

      setLoadSuccess(`Successfully loaded data for patient ${data.exam_data.patient_id || 'unknown'}`);
    } catch (err: any) {
      console.error('Error loading JSON:', err);
      setError(err.message || 'Failed to load JSON data');
    }
  };

  return (
    <Container>
      <LoadingDialog isOpen={isGenerating} estimatedMinutes={3} />

      <div className="max-w-4xl mx-auto">
        <div className="flex items-center justify-between mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Create New Report</h1>
          <FileUpload
            onFileLoad={handleJsonLoad}
            label="Load JSON Data"
          />
        </div>

        {loadSuccess && (
          <Alert variant="success" className="mb-6">
            <strong>Success:</strong> {loadSuccess}
          </Alert>
        )}

        {error && (
          <Alert variant="error" className="mb-6">
            <strong>Error:</strong> {error}
          </Alert>
        )}

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-8">
          {/* Anamnesis Type Selector */}
          <div className="bg-white p-6 rounded-lg shadow">
            <Select
              label="Anamnesis Type"
              options={[
                { value: 'vidanova', label: 'VidaNova' },
                { value: 'ionnutri', label: 'IonNutri' },
              ]}
              value={anamnesisType}
              onChange={(e) => handleTypeChange(e.target.value as AnamnesisType)}
            />
          </div>

          {/* Exam Data */}
          <div className="bg-white p-6 rounded-lg shadow">
            <ExamDataForm control={control} errors={errors} register={register} />
          </div>

          {/* Personal Data */}
          <div className="bg-white p-6 rounded-lg shadow">
            <PersonalDataForm register={register} errors={errors} watch={watch} />
          </div>

          {/* Patient Objective */}
          <div className="bg-white p-6 rounded-lg shadow">
            <Input
              label="Patient Objective"
              {...register('anamnesis.objective')}
              placeholder="e.g., Improve body composition and gain muscle mass"
            />
          </div>

          {/* Context Factors */}
          <div className="bg-white p-6 rounded-lg shadow">
            <ContextFactorsForm control={control} register={register} />
          </div>

          {/* Common Anamnesis Fields */}
          <div className="bg-white p-6 rounded-lg shadow">
            <CommonAnamnesisFieldsForm control={control} register={register} />
          </div>

          {/* Type-Specific Forms */}
          <div className="bg-white p-6 rounded-lg shadow">
            {anamnesisType === 'vidanova' ? (
              <VidaNovaSpecificForm register={register} errors={errors} />
            ) : (
              <IonNutriSpecificForm register={register} />
            )}
          </div>

          {/* Action Buttons */}
          <div className="flex gap-4 justify-end">
            <Button
              type="button"
              variant="secondary"
              onClick={() => navigate('/')}
            >
              Cancel
            </Button>
            <Button
              type="submit"
              disabled={isGenerating}
              className="min-w-[200px]"
            >
              {isGenerating ? (
                <span className="flex items-center justify-center gap-2">
                  <Spinner size="sm" />
                  Generating Report...
                </span>
              ) : (
                'Generate Report'
              )}
            </Button>
          </div>
        </form>
      </div>
    </Container>
  );
}
