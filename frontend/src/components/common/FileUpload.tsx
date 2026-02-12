import { ChangeEvent, useRef } from 'react';
import Button from './Button';

interface FileUploadProps {
  onFileLoad: (data: any) => void;
  accept?: string;
  label?: string;
}

export default function FileUpload({ onFileLoad, accept = '.json', label = 'Load JSON File' }: FileUploadProps) {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = async (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    try {
      const text = await file.text();
      const data = JSON.parse(text);
      onFileLoad(data);
    } catch (error) {
      console.error('Error parsing JSON file:', error);
      alert('Error: Invalid JSON file. Please check the file format.');
    }

    // Reset input so the same file can be loaded again
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const handleClick = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="inline-block">
      <input
        ref={fileInputRef}
        type="file"
        accept={accept}
        onChange={handleFileChange}
        className="hidden"
        aria-label="Upload JSON file"
      />
      <Button type="button" onClick={handleClick} variant="secondary">
        📁 {label}
      </Button>
    </div>
  );
}
