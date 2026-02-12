import Input from '../common/Input';
import Select from '../common/Select';

interface VidaNovaSpecificFormProps {
  register: any;
  errors: any;
}

export default function VidaNovaSpecificForm({ register, errors }: VidaNovaSpecificFormProps) {
  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-bold text-gray-900">VidaNova Specific Information</h2>

      <div className="grid grid-cols-1 gap-4">
        <Input
          label="Diet Type"
          {...register('anamnesis.diet_type')}
          error={errors.anamnesis?.diet_type?.message}
          placeholder="e.g., omnivorous, vegetarian, vegan"
        />

        <Input
          label="Energy Level"
          {...register('anamnesis.energy_level')}
          error={errors.anamnesis?.energy_level?.message}
          placeholder="e.g., high, moderate, low"
        />

        <Input
          label="Muscle Gain Goal"
          {...register('anamnesis.muscle_gain_goal')}
          error={errors.anamnesis?.muscle_gain_goal?.message}
          placeholder="Describe muscle gain objective"
        />

        <Select
          label="Following Nutritionist Plan?"
          options={[
            { value: '', label: 'Select option' },
            { value: 'Sim', label: 'Yes' },
            { value: 'Não', label: 'No' },
          ]}
          {...register('anamnesis.nutritionist_plan')}
          error={errors.anamnesis?.nutritionist_plan?.message}
        />

        <Select
          label="Difficulty Gaining Muscle?"
          options={[
            { value: '', label: 'Select option' },
            { value: 'Sim, percebo muita dificuldade', label: 'Yes, significant difficulty' },
            { value: 'Alguma dificuldade', label: 'Some difficulty' },
            { value: 'Não', label: 'No difficulty' },
          ]}
          {...register('anamnesis.difficulty_muscle_gain')}
          error={errors.anamnesis?.difficulty_muscle_gain?.message}
        />
      </div>
    </div>
  );
}
