# EduCluster Dashboard v5

Versi ini mengikuti alur yang dimaksud:

1. **Dashboard / Welcome**
   - Pengguna membuka aplikasi.
   - Muncul welcome dan penjelasan singkat.
   - Tombol **Pilih Jenjang** menjadi CTA utama.

2. **Pilih Jenjang**
   - Halaman baru.
   - SD, SMP, SMA berupa kartu interaktif.
   - Lingkaran kuning di kanan kartu menjadi indikator/tombol pilihan.
   - Klik kartu/lingkaran untuk pilih atau unselect.
   - "Jenjang terpilih" berubah langsung.
   - Tidak ada tombol simpan terpisah.
   - Tombol **Lanjutkan** menyimpan pilihan dan membuka tahap berikutnya.

3. **Data Pendidikan**
   - Halaman baru.
   - Hanya jenjang yang dipilih yang ditampilkan sebagai kartu upload.
   - Contoh pilih SD + SMP -> hanya kartu SD dan SMP yang muncul.
   - Masing-masing file tetap terpisah: SD.xlsx dan SMP.xlsx.
   - Tombol lanjut menuju IPM & Kemiskinan.

4. **IPM & Kemiskinan**
   - Satu halaman.
   - Dua form upload terpisah: IPM dan Kemiskinan.
   - Tombol lanjut menuju Review.

5. **Review Data**
   - Ringkasan pilihan dan semua file.
   - Tombol mulai analisis menuju Hasil Analisis.

6. **Hasil Analisis**
   - Placeholder untuk integrasi backend penelitian.

## Sidebar

Sidebar bukan kumpulan fitur yang terpisah. Sidebar berfungsi sebagai **progress/navigation tahapan**:
- Dashboard
- 1. Pilih Jenjang
- 2. Data Pendidikan
- 3. IPM & Kemiskinan
- 4. Review Data
- 5. Hasil Analisis

Tahap aktif ditandai dan tahap berikutnya tetap terlihat sebagai alur.

## Menjalankan

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Buka `http://127.0.0.1:5000`.
