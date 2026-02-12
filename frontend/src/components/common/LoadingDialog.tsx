import { useEffect, useState } from 'react';
import Dialog from './Dialog';
import Spinner from './Spinner';

interface LoadingDialogProps {
  isOpen: boolean;
  estimatedMinutes?: number;
}

export default function LoadingDialog({ isOpen, estimatedMinutes = 3 }: LoadingDialogProps) {
  const [elapsedSeconds, setElapsedSeconds] = useState(0);

  useEffect(() => {
    if (!isOpen) {
      setElapsedSeconds(0);
      return;
    }

    const interval = setInterval(() => {
      setElapsedSeconds(prev => prev + 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [isOpen]);

  const formatTime = (seconds: number): string => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const estimatedSeconds = estimatedMinutes * 60;
  const progress = Math.min((elapsedSeconds / estimatedSeconds) * 100, 100);

  return (
    <Dialog isOpen={isOpen} closeOnOutsideClick={false}>
      <div className="text-center">
        <div className="mb-6">
          <Spinner size="lg" className="mx-auto" />
        </div>

        <h2 className="text-2xl font-bold text-gray-900 mb-2">
          Generating Report
        </h2>

        <p className="text-gray-600 mb-6">
          Please wait while we analyze the data and generate your personalized nutrimetabolomic report.
        </p>

        <div className="bg-gray-100 rounded-lg p-4 mb-4">
          <div className="flex items-center justify-center gap-3 mb-3">
            <svg
              className="w-6 h-6 text-blue-600"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <div className="text-lg font-semibold text-gray-700">
              {formatTime(elapsedSeconds)}
            </div>
          </div>

          <div className="w-full bg-gray-300 rounded-full h-2 mb-2">
            <div
              className="bg-blue-600 h-2 rounded-full transition-all duration-1000 ease-linear"
              style={{ width: `${progress}%` }}
            />
          </div>

          <p className="text-sm text-gray-600">
            Estimated time: ~{estimatedMinutes} minute{estimatedMinutes !== 1 ? 's' : ''}
          </p>
        </div>

        <div className="text-sm text-gray-500 italic">
          This process may take a few minutes as we leverage AI to analyze your metabolomic data and generate personalized recommendations.
        </div>
      </div>
    </Dialog>
  );
}
