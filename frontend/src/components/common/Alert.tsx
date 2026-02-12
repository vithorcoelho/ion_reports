import { ReactNode } from 'react';
import { clsx } from 'clsx';

interface AlertProps {
  children: ReactNode;
  variant?: 'success' | 'error' | 'warning' | 'info';
  className?: string;
}

export default function Alert({ children, variant = 'info', className }: AlertProps) {
  const variantStyles = {
    success: 'bg-green-50 border-green-400 text-green-800',
    error: 'bg-red-50 border-red-400 text-red-800',
    warning: 'bg-yellow-50 border-yellow-400 text-yellow-800',
    info: 'bg-blue-50 border-blue-400 text-blue-800',
  };

  return (
    <div
      className={clsx(
        'p-4 border-l-4 rounded',
        variantStyles[variant],
        className
      )}
    >
      {children}
    </div>
  );
}
