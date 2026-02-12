import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import CreateReport from './pages/CreateReport';
import ViewReport from './pages/ViewReport';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<CreateReport />} />
        <Route path="/report/:reportId" element={<ViewReport />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
