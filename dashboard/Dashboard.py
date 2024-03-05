import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


st.header('Tugas Penyewaan Sepeda')
st.text('Question : ')
st.text('Bagaimana perbedaan rata - rata penyewaan sepeda di akhir pekan jika dilihat')
st.text('berdasarkan musim pada tahun pertama(2011)?')
def hubungkan_csv():
    all2_df = pd.read_csv("dashboard/all_data2.csv")
    return all2_df

def bar_char(products_df):
    tahun_pertama = products_df[products_df['yr'] == 0]
    weekday_df = tahun_pertama[tahun_pertama['weekday'] == True]
    average_penyewa_weekday = weekday_df.groupby('season')['cnt'].mean()

    plt.bar(x=average_penyewa_weekday.index, height=average_penyewa_weekday.values)
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Penyewa')
    plt.title('Rata-rata penyewa sepeda di hari kerja (Tahun 2011)')
    plt.xticks(ticks=[1, 2, 3, 4], labels=['Spring', 'Summer', 'Fall', 'Winter'])
    for i, value in enumerate(average_penyewa_weekday.values):
        plt.text(i + 1, value, str(round(value, 2)), ha='center', va='bottom')

    return plt

def pie_char(pieChar1, pieChar2):
    flavors = ('Registered', 'Casual')
    votes = (pieChar1, pieChar2)
    colors = ('#98FB98', '#FFF8DC')
    explode = (0.1, 0)

    fig, ax = plt.subplots()
    ax.pie(
        x=votes,
        labels=flavors,
        autopct='%1.1f%%',
        colors=colors,
        explode=explode
    )
    plt.title('Persentase Pendaftar vs. Pengguna Casual')
    ax.axis('equal')
    return fig

st.set_option('deprecation.showPyplotGlobalUse', False)

all2_df = hubungkan_csv()

total_casual = all2_df['casual'].sum()
total_cnt = all2_df['cnt'].sum()
persen_casual=total_casual/total_cnt*100
persen_registered = 100 - persen_casual


st.pyplot(bar_char(all2_df))
st.text('Jika dilihat dari data yang ada hasil tabel yang ada maka dapat disimpulkan')
st.text('bahwa pada tahun 2011 musim gugur adalah musim dengan rata - rata penyewaan')
st.text('sepeda terbanyak dan musim semi adalah musim dengan penyewaan sepeda paling sedikit.')
st.text('Musim dingin menempati posisi dengan tingkat penjualan terbanyak kedua dan')
st.text('musim panas menempati posisi dengan tingkat penjualan terbanyak ketiga')
st.text('')
st.text('')
st.text('')

st.text('Question : ')
st.text('Berapakah perbandingan persentase casual user dan register user?')
st.pyplot(pie_char(persen_registered, persen_casual))
st.text('Perbandingan persentase casual user dan register user mencapai sekitar 2 : 9.')
st.text('Cara mendapatkan angka ini adalah dengan menghitung cnt atau total dari casual user')
st.text('dan register user.')
st.text('Casual user merupakan pengguna yang tidak memiliki akun atau tidak memiliki keanggotaan tetap')
st.text('atau tidak memiliki keanggotaan tetap')
st.text('sedangkan register user merupakan pengguna yang telah mendaftar dan memiliki akun.')
st.text('Sehingga dapat disimpulkan dari data yang ada bahwa kebanyakan atau ')
st.text('81% penyewa sepeda adalah mereka yang memiliki akun')



# Perbandingan persentase casual user dan register user mencapai sekitar 2 : 9. Cara mendapatkan angka ini adalah dengan menghitung cnt atau total dari casual user dan register user. Casual user merupakan pengguna yang tidak memiliki akun atau tidak memiliki keanggotaan tetap sedangkan register user merupakan pengguna yang telah mendaftar dan memiliki akun. Sehingga dapat disimpulkan dari data yang ada bahwa kebanyakan atau 81% penyewa sepeda adalah mereka yang memiliki akun