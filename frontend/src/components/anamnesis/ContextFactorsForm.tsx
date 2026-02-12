import { useFieldArray, Control } from 'react-hook-form';
import Input from '../common/Input';
import Select from '../common/Select';
import Button from '../common/Button';

interface ContextFactorsFormProps {
  control: Control<any>;
  register: any;
}

export default function ContextFactorsForm({ control, register }: ContextFactorsFormProps) {
  const { fields: medicalHistoryFields, append: appendMedicalHistory, remove: removeMedicalHistory } = useFieldArray({
    control,
    name: 'anamnesis.context_factors.medical_history',
  });

  const { fields: intolerancesFields, append: appendIntolerance, remove: removeIntolerance } = useFieldArray({
    control,
    name: 'anamnesis.context_factors.intolerances',
  });

  const { fields: sleepIssuesFields, append: appendSleepIssue, remove: removeSleepIssue } = useFieldArray({
    control,
    name: 'anamnesis.context_factors.sleep.issues',
  });

  const { fields: medicationsFields, append: appendMedication, remove: removeMedication } = useFieldArray({
    control,
    name: 'anamnesis.context_factors.medications',
  });

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">Context Factors</h2>

      {/* Medical History */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Medical History</h3>
          <Button
            type="button"
            onClick={() => appendMedicalHistory('não informado')}
            size="sm"
          >
            Add Condition
          </Button>
        </div>
        <div className="space-y-2">
          {medicalHistoryFields.map((field, index) => (
            <div key={field.id} className="flex gap-2">
              <Input
                placeholder="Medical condition"
                {...register(`anamnesis.context_factors.medical_history.${index}`)}
              />
              <Button
                type="button"
                variant="danger"
                size="sm"
                onClick={() => removeMedicalHistory(index)}
              >
                Remove
              </Button>
            </div>
          ))}
        </div>
      </div>

      {/* Intolerances */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Food Intolerances</h3>
          <Button
            type="button"
            onClick={() => appendIntolerance('')}
            size="sm"
          >
            Add Intolerance
          </Button>
        </div>
        <div className="space-y-2">
          {intolerancesFields.map((field, index) => (
            <div key={field.id} className="flex gap-2">
              <Input
                placeholder="Food intolerance"
                {...register(`anamnesis.context_factors.intolerances.${index}`)}
              />
              <Button
                type="button"
                variant="danger"
                size="sm"
                onClick={() => removeIntolerance(index)}
              >
                Remove
              </Button>
            </div>
          ))}
        </div>
      </div>

      {/* Physical Activity */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Physical Activity</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <Input
            label="Frequency"
            {...register('anamnesis.context_factors.physical_activity.frequency')}
            placeholder="e.g., 3x per week, daily"
          />
          <Input
            label="Type"
            {...register('anamnesis.context_factors.physical_activity.type')}
            placeholder="e.g., running, weightlifting"
          />
          <Input
            label="Intensity"
            {...register('anamnesis.context_factors.physical_activity.intensity')}
            placeholder="e.g., light, moderate, intense"
          />
        </div>
      </div>

      {/* Sleep */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Sleep</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
          <Input
            label="Quality"
            {...register('anamnesis.context_factors.sleep.quality')}
            placeholder="e.g., good, fair, poor"
          />
          <Input
            label="Hours per Night"
            type="number"
            step="0.1"
            min="0"
            max="24"
            {...register('anamnesis.context_factors.sleep.hours', { valueAsNumber: true })}
          />
        </div>

        <div>
          <div className="flex items-center justify-between mb-3">
            <label className="text-sm font-medium text-gray-700">Sleep Issues</label>
            <Button
              type="button"
              onClick={() => appendSleepIssue('não informado')}
              size="sm"
            >
              Add Issue
            </Button>
          </div>
          <div className="space-y-2">
            {sleepIssuesFields.map((field, index) => (
              <div key={field.id} className="flex gap-2">
                <Input
                  placeholder="Sleep issue"
                  {...register(`anamnesis.context_factors.sleep.issues.${index}`)}
                />
                <Button
                  type="button"
                  variant="danger"
                  size="sm"
                  onClick={() => removeSleepIssue(index)}
                >
                  Remove
                </Button>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Alcohol Consumption */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Alcohol Consumption</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Input
            label="Frequency"
            {...register('anamnesis.context_factors.alcohol_consumption.frequency')}
            placeholder="e.g., never, occasionally, weekly"
          />
          <Input
            label="Amount"
            {...register('anamnesis.context_factors.alcohol_consumption.amount')}
            placeholder="e.g., 1-2 drinks per occasion"
          />
        </div>
      </div>

      {/* Medications */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Medications</h3>
          <Button
            type="button"
            onClick={() => appendMedication({ name: '', frequency: 'não informado', dosage: 'não informado' })}
            size="sm"
          >
            Add Medication
          </Button>
        </div>
        <div className="space-y-3">
          {medicationsFields.map((field, index) => (
            <div key={field.id} className="border border-gray-200 rounded p-4">
              <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-3">
                <Input
                  label="Name"
                  placeholder="Medication name"
                  {...register(`anamnesis.context_factors.medications.${index}.name`)}
                />
                <Input
                  label="Frequency"
                  placeholder="e.g., daily, as needed"
                  {...register(`anamnesis.context_factors.medications.${index}.frequency`)}
                />
                <Input
                  label="Dosage"
                  placeholder="e.g., 10mg, 1 tablet"
                  {...register(`anamnesis.context_factors.medications.${index}.dosage`)}
                />
              </div>
              <Button
                type="button"
                variant="danger"
                size="sm"
                onClick={() => removeMedication(index)}
              >
                Remove Medication
              </Button>
            </div>
          ))}
        </div>
      </div>

      {/* Stress Level */}
      <div>
        <Select
          label="Stress Level"
          options={[
            { value: '', label: 'Select stress level' },
            { value: 'baixo', label: 'Low' },
            { value: 'mediano', label: 'Medium' },
            { value: 'alto', label: 'High' },
            { value: 'não informado', label: 'Not informed' },
          ]}
          {...register('anamnesis.context_factors.stress_level')}
        />
      </div>
    </div>
  );
}
