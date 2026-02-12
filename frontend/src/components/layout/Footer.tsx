export default function Footer() {
  return (
    <footer className="bg-gray-800 text-white mt-auto">
      <div className="container mx-auto px-4 py-6 text-center">
        <p className="text-sm">
          &copy; {new Date().getFullYear()} Ion Nutri. Nutrimetabolomic Reports System.
        </p>
      </div>
    </footer>
  );
}
