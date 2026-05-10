# Laporan Praktikum: Analisis Performa Penjualan E-commerce

**Nama:** Danendra Bagas  
**Asal Sekolah:** SMK Telkom Malang  

---

## 1. Business Question (Tujuan Praktikum)
Laporan ini disusun untuk menjawab beberapa persoalan utama dalam performa penjualan, yaitu:
* **Analisis Korelasi:** Apakah biaya iklan berpengaruh langsung pada total penjualan?
* **Efisiensi Kategori:** Kategori produk apa yang paling untung jika dilihat dari modal iklannya?
* **Segmentasi Pelanggan:** Siapa pelanggan yang paling loyal (skor RFM tinggi) untuk target program voucher?
* **Identifikasi Underperformer:** Mencari produk mahal yang penjualannya rendah.
* **Uji Hipotesis:** Apakah benar budget iklan yang di atas rata-rata (median) pasti menghasilkan penjualan yang jauh lebih tinggi?

## 2. Data Wrangling (Pembersihan Data)
Langkah-langkah yang saya lakukan untuk memastikan data siap diolah adalah:
* **Perbaikan Data Kosong:** Saya mengisi data yang kosong di kolom `Total_Sales` dengan rumus: `Quantity * Price_Per_Unit`.
* **Konversi Waktu:** Mengubah kolom `Order_Date` menjadi format waktu (*datetime*) agar tren penjualan bisa dihitung per bulan.
* **Validasi Angka:** Memastikan kolom `Ad_Budget` dan harga sudah terbaca sebagai format angka supaya proses perhitungan korelasi dan rata-rata tidak error.

## 3. Insights (Hasil Analisis)
Berdasarkan pengolahan data menggunakan Python, didapatkan hasil sebagai berikut:
* **Peta Korelasi (Heatmap):** Terlihat ada hubungan positif antara anggaran iklan dan total penjualan. Semakin tinggi anggaran yang dikeluarkan, kecenderungan penjualannya juga meningkat.
* **Grafik Efisiensi Kategori:** Melalui grafik bar chart horizontal, saya menemukan bahwa kategori seperti **Gadget** (contoh) lebih efisien karena menghasilkan penjualan tinggi dengan budget iklan yang lebih hemat dibanding kategori lain.
* **Produk Underperformer:** Scatter plot menunjukkan ada beberapa produk yang harganya tinggi tapi penjualannya sangat sedikit. Ini indikasi kalau harga tersebut mungkin terlalu mahal bagi pelanggan.
* **Hasil Uji Hipotesis:** Setelah data dibagi menjadi kelompok "Iklan Tinggi" dan "Iklan Rendah" (berdasarkan nilai tengah/median), rata-rata penjualan pada kelompok iklan tinggi terbukti jauh lebih besar. Artinya, iklan memang sangat berpengaruh pada pendapatan.

## 4. Recommendation (Rekomendasi Strategis)
Dari temuan di atas, saran saya untuk pihak manajemen adalah:
1. **Fokus Anggaran:** Sebaiknya budget iklan diprioritaskan untuk kategori produk yang memiliki rasio efisiensi paling tinggi di bar chart.
2. **Evaluasi Harga:** Produk yang masuk kategori *underperformer* perlu ditinjau kembali harganya atau dibuatkan promo khusus agar stok barang tidak mengendap di gudang.
3. **Targeting Pelanggan:** Untuk pelanggan dengan skor RFM terbaik (kategori *Champions*), perusahaan perlu memberikan reward seperti voucher atau poin loyalti agar mereka tetap berbelanja.
4. **Optimasi Iklan:** Karena uji hipotesis membuktikan iklan efektif, perusahaan disarankan meningkatkan budget iklan secara bertahap namun tetap dipantau efisiensinya per kategori.