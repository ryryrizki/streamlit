from PIL import Image
from nbformat import write
from numpy import left_shift
import requests
import streamlit as st
from streamlit_lottie import st_lottie

import time

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#------ LOAD ASSETS ------
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_rnfwc4vj.json")
lottie_hacker = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_x1ikbkcj.json")
img_ransomware_work = Image.open("/Users/ryryrizki/Documents/digitalent/streamlit/Webpage/images/eternalblue-wannacry-2.png")
img_homepage = Image.open("/Users/ryryrizki/Documents/digitalent/streamlit/Webpage/images/img_homepage.png")
img_marcus = Image.open("/Users/ryryrizki/Documents/digitalent/streamlit/Webpage/images/Marcus-Hutchins-Arrested-by-FBI.png")



#------ PAGE ------
st.set_page_config(page_title="WIT N Group 7", page_icon=":closed_lock_with_key:", layout="wide")
st.caption("Women in Tech: Cybersecurity and Python 2022")



#------ HEADER SECTION -------
with st.container():
    st.title("Apa itu Ransomware WannaCry dan Bagaimana Cara Kerjanya?")
    st.write("Serangan ransomware WannaCry 2017 adalah salah satu infeksi komputer paling luas, inilah yang perlu diketahui tentang ransomware WannaCry dan cara melindungi data Anda.")
    st.caption("Kelompok 7 - Triple R")
    st.write("---")
    st.image(img_homepage)
    st.subheader(
    '''**
    Poin Kunci:
    1. Epidemi ransomware WannaCry tahun 2017 mengganggu rumah sakit, bank, dan perusahaan komunikasi di seluruh dunia.
    2. Empat tahun kemudian, cyber criminal  memperbarui upaya untuk menyebarkan ransomware WannaCry selama pandemi COVID-19.
    3. Perusahaan dan individu dapat mengambil langkah-langkah untuk mencegah serangan, dengan pembaruan perangkat lunak yang paling penting.
    **'''
    )
    st.write("Bertanggung jawab atas salah satu infeksi malware paling terkenal di seluruh dunia, ransomware WannaCry masih aktif digunakan oleh para penyerang siber hingga saat ini. Lima tahun lalu bulan Mei, jaringan di seluruh dunia hancur, dari seluruh sistem perawatan kesehatan hingga bank dan perusahaan telekomunikasi nasional.")
    st.write("Itu masih cukup mematikan untuk digunakan sekarang, dan ada peningkatan dalam laporan kemunculannya selama pandemi. Inilah semua yang perlu Anda ketahui tentang ransomware WannaCry hari ini — termasuk cara melindungi organisasi Anda darinya.")

# add link
st.write("[Watch Video about WannaCry >](https://youtu.be/Vkjekr6jacg)")

#isi artikel
with st.container():
    st.header("_Apa Itu Ransomware WannaCry?_")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("WannaCry ransomware adalah worm ransomware kripto yang menyerang PC Windows. Ini adalah bentuk malware yang dapat menyebar dari PC ke PC di seluruh jaringan (oleh karena itu dinamakan **worm**) dan jika sudah ada pada komputer woem tersebut dapat mengenkripsi file penting (bagian **crypto**). Pelaku kemudian meminta uang tebusan untuk membuka kunci file tersebut. Nama itu berasal dari untaian kode yang terdeteksi di beberapa sampel virus pertama.")
        st.write("WannaCry disebut sebagai studi dalam bencana yang dapat dicegah karena dua bulan sebelum ransomware ini pertama kali menyebar ke seluruh dunia pada tahun 2017, Microsoft mengeluarkan patch yang akan mencegah worm menginfeksi komputer [1]. Sayangnya, ratusan ribu sistem tidak diperbarui tepat waktu, dan jumlah yang sangat banyak dari sistem tersebut tetap rentan hari ini.")
        st.markdown("[Watch Video about WannaCry globally attack on 2017...](https://youtu.be/5v5gtycGTps)")    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
with st.container():
    st.header("_Bagaimana WannaCry Menginfeksi Sistem?_")
    image_column, text_column   = st.columns((1,2))
    with image_column:
        st_lottie(lottie_hacker, height=300, key= "hacker")
    with text_column:
        st.write(
            """
            WannaCry hanya akan menjadi salah satu serangan ransomware jika bukan karena metodenya menginfeksi komputer. Kerentanan kritis sistem Windows ditemukan dan dilaporkan pertama kali dieksploitasi oleh Badan Keamanan Nasional AS. 
            Dijuluki EternalBlue, eksploitasi itu akhirnya dibagikan oleh kelompok peretasan cybercriminal online pada April 2017, dan memungkinkan pembuat WannaCry untuk mengelabui sistem Windows agar menjalankan kodenya menggunakan protokol Blok Pesan Server (SMB). 
            Cara penyebaran WannaCry adalah dengan menggunakan jaringan perusahaan untuk melompat ke sistem Windows lainnya. Tidak seperti serangan phishing, pengguna komputer tidak perlu mengklik tautan atau membuka file yang terinfeksi. 
            WannaCry hanya mencari sistem lain yang rentan untuk dimasuki (dalam beberapa versi menggunakan kredensial curian), kemudian menyalin dan menjalankan program, lagi, dan lagi, dan lagi. Jadi satu komputer rentan di jaringan perusahaan dapat membahayakan seluruh organisasi.
            """)

st.header("_Bagaimana Cara Kerja Serangan WannaCry?_")
with st.container():
    image_column, text_column   = st.columns((1,2))
    with image_column:
        st.image(img_ransomware_work, caption = "Cara Kerja Ransomware WannaCry")

    with text_column:
        st.write(
            """
            Program WannaCry memiliki beberapa komponen. Ada program pengiriman utama yang berisi program lain, termasuk perangkat lunak enkripsi dan dekripsi. Setelah WannaCry berada di sistem komputer, ia mencari lusinan jenis file tertentu, termasuk file Microsoft Office dan file gambar, video, dan suara. 
            Kemudian menjalankan rutinitas untuk mengenkripsi file, yang hanya dapat didekripsi menggunakan kunci digital yang dikirimkan secara eksternal.Jadi satu-satunya cara bagi pengguna yang terinfeksi untuk mengakses file terenkripsi WannaCry adalah jika mereka memiliki salinan cadangan eksternal dari file tersebut. 
            Selama serangan WannaCry awal, satu-satunya jalan yang dimiliki beberapa korban adalah membayar uang tebusan Bitcoin. Sayangnya, laporan menunjukkan bahwa setelah perusahaan membayar, peretas tidak memberikan akses kepada korban ke file mereka.
            """)

st.header("_Dari Mana WannaCry Berasal, dan Apakah Masih Aktif?_")
with st.container():
    image_column, text_column   = st.columns((1,2))
    with image_column:
        st.image(img_marcus, caption = "Marcus Hutchins")

    with text_column:
        st.write(
            """
            Pada Mei 2017, WannaCry menyebarkan kepanikan di seluruh jaringan perusahaan di seluruh dunia karena dengan cepat menginfeksi lebih dari 200.000 komputer di 150 negara. Di antara sistem itu, Layanan Kesehatan Nasional Inggris terganggu, layanan telekomunikasi Telefónica Spanyol terancam dan bank-bank di Rusia terganggu. Sementara virus tampaknya muncul sekaligus, para peneliti kemudian melacak versi sebelumnya ke organisasi Korea Utara yang dikenal sebagai Lazarus Group. Ada banyak petunjuk yang terkubur dalam kode WannaCry tetapi tidak ada yang pernah mengaku bertanggung jawab untuk membuat atau menyebarkan program tersebut. Seorang peneliti menemukan di awal serangan siber bahwa program tersebut awalnya mencoba mengakses alamat web tertentu yang ternyata merupakan nama tidak masuk akal yang tidak terdaftar. Jika program dapat membuka URL, WannaCry tidak akan dijalankan, jadi program ini bertindak sebagai semacam tombol pemutus. 
            
            """)
st. write("""
        Akibatnya, peneliti Inggris Marcus Hutchins mendaftarkan URL dan secara efektif menumpulkan penyebaran ransomware WannaCry.[2]. Namun demikian, ada gelombang kebangkitan WannaCry di tahun-tahun berikutnya sejak itu. Satu kasus terkenal terjadi pada 2018 di Boeing. Pada akhirnya, hal ini menyebabkan lebih banyak kepanikan daripada kerusakan yang sebenarnya, tetapi produktivitas di pembuat pesawat terganggu. 
        Baru-baru ini, peneliti keamanan telah melihat infeksi WannaCry baru. Satu laporan mencatat peningkatan 53'%' dalam ransomware WannaCry pada Maret 2021 dibandingkan Januari tahun 2021 silam, sementara yang lain menyatakan bahwa WannaCry adalah keluarga ransomware teratas yang digunakan di Amerika pada Januari dengan 1.240 deteksi infeksi. Lebih penting lagi: varian terbaru yang digunakan oleh peretas tidak lagi menyertakan URL tombol pemutus.[3]
        """)

st.header("_Perlindungan Terhadap Ransomware WannaCry_")
with st.container():
        st.write(
            """
            Untungnya, ada langkah-langkah keamanan siber yang dapat dilakukan setiap perusahaan untuk mencegah serangan ransomware WannaCry:
            
            """)
        st. write("""
        1. Instal perangkat lunak terbaru: Jika tiga kata terpenting dalam real estate adalah lokasi, lokasi, lokasi, tiga kata terpenting dalam keamanan siber adalah update, update, update. Infeksi WannaCry global pertama waktu itu sebenarnya dapat dicegah jika perusahaan dan individu telah memperbarui perangkat lunak Windows mereka. Eksploitasi yang memungkinkan penyebaran WannaCry telah ditambal oleh Microsoft dua bulan sebelumnya.
        2. Lakukan Pencadangan: Ini adalah tugas biasa tetapi penting untuk melindungi data-data penting, sehingga perusahaan perlu membuat cadangan informasi secara rutin. Selain itu, cadangan harus disimpan secara eksternal dan terputus dari jaringan perusahaan, seperti dalam layanan cloud, untuk melindunginya dari infeksi.
        3. Pelatihan kesadaran keamanan siber: Karyawan perlu diingatkan secara berkala tentang kebiasaan email yang baik, terutama sekarang karena semakin banyak pekerja yang bekerja dari jarak jauh. Mereka tidak boleh membuka lampiran email yang tidak dikenal, dan mereka tidak boleh mengklik tautan apa pun yang mencurigakan.
        """)





st.header("_Haruskah Membayar Tebusan WannaCry? Apa Yang Terjadi Jika Ransom WannaCry Tidak Dibayar?_")
with st.container():
        st.write(
            """
            Untungnya, ada langkah-langkah keamanan siber yang dapat dilakukan setiap perusahaan untuk mencegah serangan ransomware WannaCry:
            
            """)
        st. write(
            """
            Banyak ahli terkemuka menyarankan untuk tidak  membayar ransomware WannaCry, karena banyak dari mereka yang telah membayar kemudian melaporkan tidak dapat memulihkan file mereka dari penyerang cyber. Ada juga contoh di mana serangan ransomware seperti ransomware WannaCry ini dapat dikalahkan oleh peneliti keamanan karena kode yang salah dari cybercriminal. Tentu saja, cybercriminal terus menerus mengembangkan versi malware yang lebih baru dan lebih kuat, sehingga tidak tepat rasanya untuk hanya mengandalkan kode yang salah jika terjadi serangan di masa mendatang.
            """)

st.header("_Apa praktik terbaik untuk melindungi diri dari ransomware?_")
with st.container():
        st.write(
            """
            Untungnya, ada langkah-langkah keamanan siber yang dapat dilakukan setiap perusahaan untuk mencegah serangan ransomware WannaCry:
            
            """)
        st. write("""
            Beberapa praktik terbaik untuk melindungi diri dari ransomware meliputi:
            1. Pelatihan kesadaran keamanan bagi setiap individu.
            2. Memastikan kata sandi yang kuat digunakan di seluruh organisasi.
            3. Menyimpan data (dan data cadangan) di lokasi aman yang sulit diakses oleh cybercriminals
            """)

