import { Link } from 'react-router-dom';
import Container from '../components/layout/Container';
import Button from '../components/common/Button';

export default function Home() {
  return (
    <Container>
      <div className="max-w-4xl mx-auto text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-6">
          Welcome to Ion Nutri
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Nutrimetabolomic Reports System
        </p>
        <p className="text-gray-700 mb-12">
          Generate comprehensive nutrimetabolomic reports by analyzing patient exam data
          and anamnesis information. Our system supports both IonNutri and VidaNova workflows.
        </p>

        <div className="flex gap-4 justify-center">
          <Link to="/create">
            <Button size="lg">Create New Report</Button>
          </Link>
        </div>

        <div className="mt-16 grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
          <div className="p-6 bg-blue-50 rounded-lg">
            <h3 className="text-xl font-semibold text-blue-900 mb-3">IonNutri</h3>
            <p className="text-gray-700">
              Comprehensive nutritional assessment including family history and environmental
              factors for detailed metabolic analysis.
            </p>
          </div>

          <div className="p-6 bg-green-50 rounded-lg">
            <h3 className="text-xl font-semibold text-green-900 mb-3">VidaNova</h3>
            <p className="text-gray-700">
              Performance and fitness-focused analysis with emphasis on muscle gain
              goals and nutritional planning.
            </p>
          </div>
        </div>
      </div>
    </Container>
  );
}
