import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat fungsi untuk menghitung rentang (range)
def hitung_rentang(x):
    return x.max() - x.min()

# Load data
# Gantilah 'nama_file.csv' dengan nama file sebenarnya dan sesuaikan path jika diperlukan
bike_sharing = pd.read_csv('day_df_clean.csv')

# Grouping berdasarkan musim dan menghitung beberapa statistik pada kolom tertentu
bike_sharing_stats = bike_sharing.groupby(by="season").agg({
    "workingday": "count",  # Jumlah penyewa pada hari kerja berdasarkan musim
    "windspeed": ["max", "min", "mean", hitung_rentang]  # Menggunakan fungsi kustom hitung_rentang
}).sort_values(by=("workingday", "count"), ascending=False)

# Menampilkan hasil
st.write("Statistik Berdasarkan Musim (Hourly):")
st.write(bike_sharing_stats)

# Grouping berdasarkan musim dan menghitung beberapa statistik pada kolom tertentu
bike_sharing_stats = bike_sharing.groupby(by="season").agg({
    "workingday": "count",  # Jumlah penyewa pada hari kerja berdasarkan musim
    "windspeed": ["max", "min", "mean", hitung_rentang]  # Menggunakan fungsi kustom hitung_rentang
}).sort_values(by=("workingday", "count"), ascending=False)

# Menampilkan hasil
st.write("Statistik Berdasarkan Musim (Daily):")
st.write(bike_sharing_stats)

# Menghitung jumlah nilai unik pada kolom 'cnt' berdasarkan 'weathersit'
unik_per_weathersit = bike_sharing.groupby("weathersit")["cnt"].nunique()

# Menampilkan hasil
st.write("Jumlah nilai unik pada kolom 'cnt' berdasarkan 'weathersit':")
st.write(unik_per_weathersit)

# Menghitung jumlah nilai unik pada kolom 'cnt' berdasarkan 'mnth'
unik_per_mnth = bike_sharing.groupby("mnth")["cnt"].nunique()

# Menampilkan hasil
st.write("Jumlah nilai unik pada kolom 'cnt' berdasarkan 'mnth':")
st.write(unik_per_mnth)

# Mengambil kolom-kolom numerik yang akan dihitung korelasinya
kolom_numerik = ["holiday", "weekday", "workingday", "weathersit", "temp", "atemp", "season", "windspeed", "cnt", "casual", "registered"]

# Menghitung korelasi antar kolom numerik
korelasi = bike_sharing[kolom_numerik].corr()

# Menampilkan matriks korelasi
st.write("Matriks Korelasinya adalah")
st.write(korelasi)

# Pengaruh Weathersit
fig_weathersit = plt.figure(figsize=(10, 6))
sns.boxplot(x="weathersit", y="cnt", data=bike_sharing)
plt.title("Pengaruh Weathersit Terhadap Jumlah Sewa Sepeda Harian")
plt.xlabel("Weathersit")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(fig_weathersit)

# Grafik Distribusi Jumlah sewa Sepeda Berdasarkan Bulan
fig_monthly = plt.figure(figsize=(20, 8))
sns.barplot(data=bike_sharing, x='mnth', y='cnt')
plt.title('Distribusi Jumlah sewa Sepeda Berdasarkan Bulan')
st.pyplot(fig_monthly)
