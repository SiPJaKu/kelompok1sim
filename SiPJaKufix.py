from ast import If
from typing import Any
import streamlit as st

st.header("Selamat Datang di SiPJaKu")
st.header("Sistem Pengecekan Jadwal Kuliah")
st.header("Jadwal kuliah Jurusan Akuntansi")
st.subheader("Rombel Akuntansi A 2021") 
st.subheader("Mata Kuliah Dasar")

nama = st.text_input("Nama")
presen = st.text_input("Nomor Presensi")

pw = st.text_input("Password")
pw1 = ("AKTA")
if (pw==pw1):
    st.write("Password Anda Benar")
    st.write("Helloo", nama)
    st.write("Nomor Presensi anda adalah", presen)
    st.write("-----------------------------------")
    st.write("Silahkan Pilih Hari")
    st.write("Senin")
    st.write("Selasa")
    st.write("Rabu")
    st.write("Kamis")
    st.write("Jumat")
    option = st.text_input("Masukkan Hari :")

#Jadwal senin
    option1 =("Senin")
    if option==option1:
        st.success("Jadwal Kuliah Hari Senin adalah:")
        st.write("Hukum Bisnis")
        st.write("Dosen Prabowo Yudo Jayanto, S.E.,M.S.A.")
        st.write("Pk 15:00 WIB-2 SKS")
        st.write("Ruang L2-302")
    
#jadwal selasa
    option2 =("Selasa")
    if option==option2:
        st.success("Jadwal Kuliah Hari Selasa adalah:")
        st.write("Ekonomi Mikro")
        st.write("Dosen Dr. Murwatingsih, M.M. dan Widya Prananta, S.ST., M.M")
        st.write("Pk 15:00 WIB-2 SKS")
        st.write("Ruang C3-202")

#jadwal rabu
    option3 =("Rabu")
    if option==option3:
        st.success("Jadwal Kuliah Hari Rabu adalah:")
        st.write("Bahasa Inggris Bisnis")
        st.write("Dosen Tusyanah, S.Pd., M.Pd.")
        st.write("Pk 11:00 WIB-2 SKS")
        st.write("Ruang C6-345")
        st.write("---------------------------------------------")
        st.write("Perpajakan")
        st.write("Dosen Kriswanto, S.E., M.Si, CMA, CIBA, SERA. dan Ain Hajawiyah, S.Ak., M.S.Ak.")
        st.write("Pk 13:00 WIB-3 SKS")
        st.write("Ruang L2-303")

#jadwal kamis
    option4 =("Kamis")
    if option==option4:
        st.success("Jadwal Kuliah Hari Kamis adalah:")
        st.write("Manajemen Keuangan")
        st.write("Henny Murtini,S.E.,M.Si.")
        st.write("Pk 10:00 WIB-2 SKS")
        st.write("Ruang C6-345")
        st.write("---------------------------------------------")
        st.write("Sistem Informasi Manajemen")
        st.write("Dosen Maylia Pramono Sari,,S.E.,M.Si dan Atta Putra Harjanto,S.E.,M.Ak.")
        st.write("Pk 13:00 WIB-2 SKS")
        st.write("Ruang L2-303") 

#jadwal jumat
    option5 =("Jumat")
    if option==option5:
        st.success("Jadwal Kuliah Hari Jumat adalah:")
        st.write("Akuntansi Keuangan Menengah 1")
        st.write("Dosen Drs.Fachrurrozie,M.Si.")
        st.write("Pk 15:30 WIB-2 SKS")
        st.write("Ruang L2-303")

#jadwal sabtu
    option6 =("Sabtu")
    if option==option6:
        st.success("Libur")

#jadwal minggu
    option7 = ("Minggu")
    if option==option7:
        st.success("Libur")