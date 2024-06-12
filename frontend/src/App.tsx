import axios from 'axios';
import { useEffect, useState } from 'react';
import './App.css';
import { Report } from './types';

function App() {
  const [reports, setReports] = useState<Report[]>([]);
  const fetchReports = async () => {
    try {
      const response = await axios.get('http://localhost:5000/reports');
      setReports(response.data.chain);
      console.log(reports);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchReports();
  }, []);

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nama</th>
            <th>Departemen</th>
            <th>Kategori</th>
            <th>Deskripsi</th>
            <th>Lokasi</th>
            <th>Waktu</th>
            <th>Bukti</th>
          </tr>
        </thead>
        <tbody>
          {reports.map((report: Report) => (
            <tr key={report.index}>
              <td>{report.index}</td>
              <td>{report.suspect_name}</td>
              <td>{report.dept}</td>
              <td>{report.action_category}</td>
              <td>{report.description}</td>
              <td>{report.location}</td>
              <td>{report.time_of_occurence}</td>
              <td>
                {report.evidence.map((evidence, index) => (
                  <a
                    key={index}
                    href={evidence}
                    target="_blank"
                    rel="noreferrer"
                  >
                    {index + 1}
                  </a>
                ))}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
