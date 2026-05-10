import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. LOAD DATA
file_name = 'data_praktikum_analisis_data - data_praktikum_analisis_data.csv'
df = pd.read_csv(file_name)

# 2. DATA CLEANING
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price_Per_Unit'])
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print("--- 5 Data Pertama ---")
print(df.head())

# 3. VISUALISASI: TREN PENJUALAN BULANAN
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('tren_penjualan.png')
plt.show()

# 4. VISUALISASI: KORELASI (HEATMAP)
plt.figure(figsize=(8,6))
correlation = df[['Total_Sales', 'Ad_Budget', 'Price_Per_Unit', 'Quantity']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Peta Korelasi Variabel')
plt.tight_layout()
plt.savefig('korelasi.png')
plt.show()

# 5. STUDI KASUS: PRODUK UNDERPERFORMER (SCATTER PLOT)
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Price_Per_Unit', y='Quantity', hue='Product_Category')
plt.axvline(df['Price_Per_Unit'].mean(), color='red', linestyle='--', label='Rata-rata Harga')
plt.title('Analisis Produk: Harga vs Volume Penjualan')
plt.legend()
plt.tight_layout()
plt.savefig('underperformer.png')
plt.show()

# 6. ANALISIS RFM (SEGMENTASI PELANGGAN)
snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

print("\n--- Hasil Segmentasi RFM (5 Data Teratas) ---")
print(rfm.head())
rfm.to_csv('hasil_rfm.csv')

# 7. REGRESI LINEAR (PREDIKSI PENJUALAN DARI IKLAN)
X = df[['Ad_Budget']]
y = df['Total_Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nKoefisien Iklan: {model.coef_[0]}")
print(f"Akurasi Model (R2 Score): {model.score(X_test, y_test)}")

# 8. ANALISIS KONTRIBUSI KATEGORI (BAR CHART HORIZONTAL)
cat_efficiency = df.groupby('Product_Category').agg({
    'Total_Sales': 'sum',
    'Ad_Budget': 'sum'
})

cat_efficiency['Efficiency_Ratio'] = cat_efficiency['Total_Sales'] / cat_efficiency['Ad_Budget']

cat_efficiency = cat_efficiency.sort_values('Efficiency_Ratio')

plt.figure(figsize=(10,6))
cat_efficiency['Efficiency_Ratio'].plot(kind='barh', color='coral')
plt.title('Efisiensi Kategori (Total Sales per Ad Budget)')
plt.xlabel('Rasio Efisiensi')
plt.ylabel('Kategori Produk')
plt.tight_layout()
plt.savefig('efisiensi_kategori.png')
plt.show()


# 9. UJI HIPOTESIS SEDERHANA (PENGARUH IKLAN TINGGI VS RENDAH)
median_ad = df['Ad_Budget'].median()

rata_penjualan_iklan_tinggi = df[df['Ad_Budget'] > median_ad]['Total_Sales'].mean()
rata_penjualan_iklan_rendah = df[df['Ad_Budget'] <= median_ad]['Total_Sales'].mean()

print("\n--- Hasil Uji Hipotesis Pengaruh Iklan ---")
print(f"Nilai Tengah (Median) Iklan: Rp {median_ad:,.2f}")
print(f"Rata-rata Penjualan (Iklan Tinggi) : Rp {rata_penjualan_iklan_tinggi:,.2f}")
print(f"Rata-rata Penjualan (Iklan Rendah) : Rp {rata_penjualan_iklan_rendah:,.2f}")

if rata_penjualan_iklan_tinggi > rata_penjualan_iklan_rendah:
    print("Kesimpulan: Ya, peningkatan Ad_Budget di atas median menghasilkan penjualan yang lebih tinggi!")
else:
    print("Kesimpulan: Tidak, iklan tinggi tidak menjamin penjualan lebih tinggi.")