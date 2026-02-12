import Input from '../common/Input';
import Select from '../common/Select';

interface PersonalDataFormProps {
  register: any;
  errors: any;
  watch: any;
}

export default function PersonalDataForm({ register, errors, watch }: PersonalDataFormProps) {
  const weight = watch('anamnesis.personal_data.weight');
  const height = watch('anamnesis.personal_data.height');

  const bmi = weight && height ? (weight / (height * height)).toFixed(2) : '';

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">Personal Data</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Input
          label="Age"
          type="number"
          {...register('anamnesis.personal_data.age', { valueAsNumber: true })}
          error={errors.anamnesis?.personal_data?.age?.message}
        />

        <Input
          label="Birth Date"
          type="date"
          {...register('anamnesis.personal_data.birth_date')}
          error={errors.anamnesis?.personal_data?.birth_date?.message}
        />

        <Select
          label="Gender"
          options={[
            { value: '', label: 'Select gender' },
            { value: 'masculino', label: 'Masculino' },
            { value: 'feminino', label: 'Feminino' },
            { value: 'não informado', label: 'Not informed' },
          ]}
          {...register('anamnesis.personal_data.gender')}
          error={errors.anamnesis?.personal_data?.gender?.message}
        />

        <Input
          label="Weight (kg)"
          type="number"
          step="any"
          {...register('anamnesis.personal_data.weight', { valueAsNumber: true })}
          error={errors.anamnesis?.personal_data?.weight?.message}
        />

        <Input
          label="Height (m)"
          type="number"
          step="any"
          {...register('anamnesis.personal_data.height', { valueAsNumber: true })}
          error={errors.anamnesis?.personal_data?.height?.message}
        />

        {bmi && (
          <div className="md:col-span-2">
            <div className="p-4 bg-blue-50 rounded-lg">
              <span className="text-sm font-medium text-gray-700">Calculated BMI: </span>
              <span className="text-lg font-bold text-blue-600">{bmi}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
