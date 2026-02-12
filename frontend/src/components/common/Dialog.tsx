import { ReactNode, useEffect } from 'react';

interface DialogProps {
  isOpen: boolean;
  onClose?: () => void;
  children: ReactNode;
  closeOnOutsideClick?: boolean;
}

export default function Dialog({ isOpen, onClose, children, closeOnOutsideClick = false }: DialogProps) {
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }

    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  const handleBackdropClick = () => {
    if (closeOnOutsideClick && onClose) {
      onClose();
    }
  };

  const handleContentClick = (e: React.MouseEvent) => {
    e.stopPropagation();
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm"
      onClick={handleBackdropClick}
    >
      <div
        className="bg-white rounded-lg shadow-2xl max-w-md w-full mx-4 p-6 animate-fade-in"
        onClick={handleContentClick}
      >
        {children}
      </div>
    </div>
  );
}
