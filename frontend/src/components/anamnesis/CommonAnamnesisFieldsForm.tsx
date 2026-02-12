import { useFieldArray, Control } from 'react-hook-form';
import Input from '../common/Input';
import Select from '../common/Select';
import Button from '../common/Button';

interface CommonAnamnesisFieldsFormProps {
  control: Control<any>;
  register: any;
}

export default function CommonAnamnesisFieldsForm({ control, register }: CommonAnamnesisFieldsFormProps) {
  const { fields: surgeriesFields, append: appendSurgery, remove: removeSurgery } = useFieldArray({
    control,
    name: 'anamnesis.surgeries',
  });

  const { fields: allergyItemsFields, append: appendAllergyItem, remove: removeAllergyItem } = useFieldArray({
    control,
    name: 'anamnesis.food_allergies.allergy_items',
  });

  const { fields: avoidanceItemsFields, append: appendAvoidanceItem, remove: removeAvoidanceItem } = useFieldArray({
    control,
    name: 'anamnesis.food_avoidance.food_items',
  });

  const { fields: supplementsFields, append: appendSupplement, remove: removeSupplement } = useFieldArray({
    control,
    name: 'anamnesis.supplements',
  });

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">Additional Information</h2>

      {/* Surgeries */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Surgeries</h3>
          <Button
            type="button"
            onClick={() => appendSurgery('não informado')}
            size="sm"
          >
            Add Surgery
          </Button>
        </div>
        <div className="space-y-2">
          {surgeriesFields.map((field, index) => (
            <div key={field.id} className="flex gap-2">
              <Input
                placeholder="Surgery description"
                {...register(`anamnesis.surgeries.${index}`)}
              />
              <Button
                type="button"
                variant="danger"
                size="sm"
                onClick={() => removeSurgery(index)}
              >
                Remove
              </Button>
            </div>
          ))}
        </div>
      </div>

      {/* Menopause Age */}
      <div>
        <Input
          label="Menopause Age (if applicable)"
          {...register('anamnesis.menopause_age')}
          placeholder="e.g., 50, não aplicável, não informado"
        />
      </div>

      {/* Tobacco Use */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Tobacco Use</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <Select
            label="Uses or Used Tobacco?"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'ex-fumante', label: 'Former smoker' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.tobacco_use.uses_or_used')}
          />
          <Input
            label="Frequency"
            {...register('anamnesis.tobacco_use.frequency')}
            placeholder="e.g., daily, occasionally, não informado"
          />
        </div>
      </div>

      {/* Food Allergies */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Food Allergies</h3>
        <div className="mb-4">
          <Select
            label="Has Food Allergies?"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.food_allergies.has_allergy')}
          />
        </div>
        <div>
          <div className="flex items-center justify-between mb-3">
            <label className="text-sm font-medium text-gray-700">Allergy Items</label>
            <Button
              type="button"
              onClick={() => appendAllergyItem('')}
              size="sm"
            >
              Add Allergen
            </Button>
          </div>
          <div className="space-y-2">
            {allergyItemsFields.map((field, index) => (
              <div key={field.id} className="flex gap-2">
                <Input
                  placeholder="Food allergen"
                  {...register(`anamnesis.food_allergies.allergy_items.${index}`)}
                />
                <Button
                  type="button"
                  variant="danger"
                  size="sm"
                  onClick={() => removeAllergyItem(index)}
                >
                  Remove
                </Button>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Food Avoidance */}
      <div>
        <h3 className="text-lg font-semibold text-gray-800 mb-3">Food Avoidance</h3>
        <div className="mb-4">
          <Select
            label="Avoids Certain Foods?"
            options={[
              { value: '', label: 'Select option' },
              { value: 'sim', label: 'Yes' },
              { value: 'não', label: 'No' },
              { value: 'não informado', label: 'Not informed' },
            ]}
            {...register('anamnesis.food_avoidance.avoids_food')}
          />
        </div>
        <div>
          <div className="flex items-center justify-between mb-3">
            <label className="text-sm font-medium text-gray-700">Avoided Foods</label>
            <Button
              type="button"
              onClick={() => appendAvoidanceItem('')}
              size="sm"
            >
              Add Food
            </Button>
          </div>
          <div className="space-y-2">
            {avoidanceItemsFields.map((field, index) => (
              <div key={field.id} className="flex gap-2">
                <Input
                  placeholder="Avoided food"
                  {...register(`anamnesis.food_avoidance.food_items.${index}`)}
                />
                <Button
                  type="button"
                  variant="danger"
                  size="sm"
                  onClick={() => removeAvoidanceItem(index)}
                >
                  Remove
                </Button>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Supplements */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-lg font-semibold text-gray-800">Supplements</h3>
          <Button
            type="button"
            onClick={() => appendSupplement('')}
            size="sm"
          >
            Add Supplement
          </Button>
        </div>
        <div className="space-y-2">
          {supplementsFields.map((field, index) => (
            <div key={field.id} className="flex gap-2">
              <Input
                placeholder="Supplement name"
                {...register(`anamnesis.supplements.${index}`)}
              />
              <Button
                type="button"
                variant="danger"
                size="sm"
                onClick={() => removeSupplement(index)}
              >
                Remove
              </Button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
