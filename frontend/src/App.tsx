import './App.css';

function App() {
  return (
    <div>
      <div>Reports:</div>
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
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>John Doe</td>
            <td>IT</td>
            <td>Perilaku</td>
            <td>Menyontek</td>
            <td>Lab 1</td>
            <td>2021-10-10 10:00</td>
            <td>https://example.com/image.jpg</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Jane Doe</td>
            <td>HR</td>
            <td>Perilaku</td>
            <td>Menyontek</td>
            <td>Lab 1</td>
            <td>2021-10-10 10:00</td>
            <td>https://example.com/image.jpg</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default App;
