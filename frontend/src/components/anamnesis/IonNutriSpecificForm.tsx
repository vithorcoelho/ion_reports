import Input from '../common/Input';
import Select from '../common/Select';

interface IonNutriSpecificFormProps {
  register: any;
}

export default function IonNutriSpecificForm({ register }: IonNutriSpecificFormProps) {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">IonNutri Specific Information</h2>

      {/* Family History */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Family History</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Select
            label="Diabetes"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.family_history.diabetes')}
          />

          <Select
            label="Hypertension"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.family_history.hipertensao')}
          />

          <Select
            label="Cancer"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.family_history.cancer')}
          />

          <Select
            label="Cardiovascular Diseases"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.family_history.doencas_cardiovasculares')}
          />

          <Input
            label="Relationship Degree"
            {...register('anamnesis.family_history.grau_parentesco')}
            placeholder="e.g., parent, sibling, não informado"
            className="md:col-span-2"
          />
        </div>
      </div>

      {/* Environmental Exposure */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Environmental Exposure</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Select
            label="Pollution Exposure"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.environmental_exposure.poluicao')}
          />

          <Input
            label="Occupational Exposure"
            {...register('anamnesis.environmental_exposure.exposicao_ocupacional')}
            placeholder="e.g., chemicals, radiation, não informado"
          />
        </div>
      </div>
    </div>
  );
}
