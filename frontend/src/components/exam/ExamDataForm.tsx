import { useFieldArray, Control } from 'react-hook-form';
import Input from '../common/Input';
import Button from '../common/Button';

interface ExamDataFormProps {
  control: Control<any>;
  errors: any;
  register: any;
}

export default function ExamDataForm({ control, errors, register }: ExamDataFormProps) {
  const { fields, append, remove } = useFieldArray({
    control,
    name: 'exam_data.metabolites',
  });

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">Exam Data</h2>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <Input
          label="Patient ID"
          {...register('exam_data.patient_id')}
          error={errors.exam_data?.patient_id?.message}
        />

        <Input
          label="Exam Date"
          type="datetime-local"
          {...register('exam_data.exam_date')}
          error={errors.exam_data?.exam_date?.message}
        />
      </div>

      <div>
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold">Metabolites</h3>
          <Button
            type="button"
            onClick={() => append({ name: '', value: 0 })}
            size="sm"
          >
            Add Metabolite
          </Button>
        </div>

        <div className="space-y-3">
          {fields.map((field, index) => (
            <div key={field.id} className="flex gap-3 items-start">
              <div className="flex-1">
                <Input
                  placeholder="Metabolite name"
                  {...register(`exam_data.metabolites.${index}.name`)}
                  error={errors.exam_data?.metabolites?.[index]?.name?.message}
                />
              </div>
              <div className="w-32">
                <Input
                  type="number"
                  step="any"
                  placeholder="Value"
                  {...register(`exam_data.metabolites.${index}.value`, { valueAsNumber: true })}
                  error={errors.exam_data?.metabolites?.[index]?.value?.message}
                />
              </div>
              <Button
                type="button"
                variant="danger"
                size="sm"
                onClick={() => remove(index)}
              >
                Remove
              </Button>
            </div>
          ))}
        </div>

        {fields.length === 0 && (
          <p className="text-gray-500 text-sm">No metabolites added yet. Click "Add Metabolite" to start.</p>
        )}
      </div>
    </div>
  );
}
