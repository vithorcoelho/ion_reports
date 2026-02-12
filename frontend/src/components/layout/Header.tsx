import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className="bg-blue-600 text-white shadow">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link to="/" className="text-2xl font-bold">
            Ion Nutri
          </Link>
          <nav>
            <Link
              to="/create"
              className="px-4 py-2 rounded hover:bg-blue-700 transition-colors"
            >
              Create Report
            </Link>
          </nav>
        </div>
      </div>
    </header>
  );
}
