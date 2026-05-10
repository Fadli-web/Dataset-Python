Tentu, ini adalah versi yang telah disesuaikan bahasanya agar tetap profesional namun terasa lebih segar, khas gaya anak SMK Telkom yang sistematis:

---

## Laporan Praktikum: Analisis Performa Penjualan E-commerce

**Nama:** Mohammad Faddli

**Asal Sekolah:** SMK Telkom Malang

### 1. Tujuan Praktikum

Laporan ini disusun guna membedah beberapa poin krusial terkait performa penjualan, di antaranya:

* **Analisis Korelasi:** Menelaah apakah besaran biaya iklan berdampak langsung terhadap perolehan total penjualan.
* **Efisiensi Kategori:** Menentukan kategori produk mana yang memberikan profit paling optimal dibandingkan modal iklannya.
* **Segmentasi Pelanggan:** Mengidentifikasi pelanggan paling loyal (berdasarkan skor RFM) sebagai kandidat utama program loyalitas.
* **Identifikasi Underperformer:** Melacak produk dengan harga premium namun memiliki volume penjualan yang minim.
* **Uji Hipotesis:** Memvalidasi anggapan apakah anggaran iklan di atas median secara otomatis menjamin angka penjualan yang lebih signifikan.

### 2. Data Wrangling (Pembersihan Data)

Tahapan pengolahan data yang saya lakukan untuk menjamin keakuratan hasil adalah:

* **Penanganan Missing Values:** Mengatasi data kosong pada kolom `Total_Sales` dengan kalkulasi: `Quantity * Price_Per_Unit`.
* **Transformasi Tipe Data:** Mengonversi kolom `Order_Date` ke format *datetime* untuk memudahkan pemetaan tren penjualan bulanan.
* **Sinkronisasi Format:** Memastikan kolom `Ad_Budget` dan harga sudah dalam format numerik agar perhitungan korelasi dan statistik tidak mengalami *error*.

### 3. Insights (Hasil Analisis)

Melalui pemrosesan data menggunakan Python, ditemukan beberapa poin penting berikut:

* **Visualisasi Heatmap:** Terdapat korelasi positif yang nyata antara biaya iklan dan pendapatan. Secara umum, peningkatan budget iklan diikuti dengan kenaikan total penjualan.
* **Analisis Efisiensi:** Berdasarkan bar chart, kategori seperti Gadget menunjukkan tingkat efisiensi tinggi, di mana penjualan yang dihasilkan tetap besar meski dengan biaya iklan yang relatif lebih rendah.
* **Deteksi Underperformer:** Lewat *scatter plot*, ditemukan beberapa produk mahal yang penjualannya lesu, mengindikasikan adanya ketidakcocokan harga dengan daya beli pasar.
* **Hasil Uji Hipotesis:** Perbandingan antara grup iklan "High" dan "Low" menunjukkan bahwa rata-rata pendapatan kelompok iklan tinggi jauh melampaui kelompok rendah. Ini membuktikan iklan sebagai pendorong utama pendapatan.

### 4. Recommendation (Rekomendasi Strategis)

Berdasarkan temuan tersebut, berikut rekomendasi yang saya ajukan kepada manajemen:

* **Alokasi Anggaran Tepat Sasaran:** Memfokuskan pengeluaran iklan pada kategori produk yang terbukti memiliki rasio efisiensi tertinggi.
* **Strategi Pricing & Promo:** Melakukan evaluasi harga atau pemberian promo khusus untuk produk *underperformer* guna mempercepat perputaran stok di gudang.
* **Apresiasi Pelanggan:** Memberikan insentif berupa voucher atau sistem poin bagi segmen pelanggan *Champions* agar loyalitas mereka tetap terjaga.
* **Skalabilitas Iklan:** Mengingat efektivitas iklan sudah teruji, disarankan untuk menambah anggaran secara terukur dengan tetap melakukan monitoring performa di tiap kategori.

---

Semoga laporan versi ini membantu tugasmu di SMK Telkom, Danendra! Ada bagian spesifik yang ingin kamu pertajam lagi?
