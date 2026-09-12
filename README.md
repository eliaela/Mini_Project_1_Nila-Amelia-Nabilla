Nama: Nila Amelia Nabilla
 
Nim: 2609116102

Tema: Sistem Spesifikasi Produksi Aset Studio Animasi & Motion Graphic

Fungsi: Aplikasi CRUD (Create, Read, Update, Delete) berbasis terminal untuk mengelola data spesifikasi aset produksi animasi.

# PENJELASAN PROGRAM #
<img width="400" height="188" alt="N1" src="https://github.com/user-attachments/assets/08c86307-cdf6-4820-bc0e-565204313432" />

Basis utama program ini adalah memakai dua tipe data Python, yaitu List sama Tuple. Jadi, ada satu List utama bernama data_spesifikasi.  List ini dipakai sebagai wadah utama penampung data karena sifatnya yang gampang ditambah atau dihapus. di dalam List, tiap unit aset disimpan dalam bentuk Tuple dengan lima elemen: ID Aset, Nama Aset, Tipe, Resolusi, dan Status Produksi.

Untuk alur kerjanya, program ini dibungkus dengan satu loop utama while True. Tujuannya biar program tetap jalan terus dan menampilkan pilihan menu 1 sampai 5 sampai kita sendiri yang milih keluar di menu 5.

# Create #

<img width="331" height="436" alt="N2" src="https://github.com/user-attachments/assets/e09c2ccd-9bbc-49bb-bae2-9916d6dd0fff" />

Ketika milih menu 1, program bakal minta input ID, Nama, Tipe, sama Resolusi. Di sini ada validasi loop di tiap inputan. Jadi jika asal tekan Enter atau mengngisi tipe di luar angka 1-4, program ngeluarin peringatan dan minta input ulang tanpa bikin program mati crash. Setelah semua aman, data langsung dibungkus jadi Tuple dengan status awal "Draft Spec" terus dimasukin ke List pake .append().

# Read #

<img width="369" height="131" alt="N3" src="https://github.com/user-attachments/assets/ffd9de8c-5d9a-4f13-972a-ea324e9b8215" />

Di menu 2, program bakal mengecek menggunakan kondisi if not data_spesifikasi. jika List masih kosong, program menampilkan "Belum ada data". tetapi jika ada isinya, program bakal nampilkan seluruh aset berurutan lengkap dengan nomor indeksnya pakai perulangan enumerate().

# Update #

<img width="363" height="462" alt="N4" src="https://github.com/user-attachments/assets/eceda92e-29d9-493d-b664-1d0e3c03dd8e" />

menu 3, Bagian ini digunakan untuk mengubah data aset yang sudah ada. Pengguna memilih nomor data, kemudian dapat mengganti nama, resolusi, dan statusnya. Data yang sudah diperbarui kemudian dimasukkan kembali ke posisi data sebelumnya.

# Delete #

<img width="488" height="197" alt="N5" src="https://github.com/user-attachments/assets/24ba1a7c-ba4a-477a-a189-b63e5284a85b" />

pada menu 4, Bagian ini digunakan untuk menghapus data aset berdasarkan nomor yang dipilih pengguna. Fungsi pop() menghapus data dari list dan data yang dihapus disimpan ke variabel data agar bisa ditampilkan pada pesan berhasil.

# Validasi Looping #

<img width="528" height="51" alt="N7" src="https://github.com/user-attachments/assets/275f6e80-19fc-4056-a4ad-447bbffb2930" />

Bagian ini merupakan validasi menggunakan looping. Program akan terus meminta input selama data yang dimasukkan belum benar. Misalnya pengguna memasukkan huruf atau nomor yang tidak tersedia, program tidak langsung error atau berhenti, tetapi menampilkan "Nomor tidak valid!" dan meminta pengguna memasukkan nomor kembali. Looping berhenti dengan break setelah input yang diberikan sudah valid.

# Keluar dari Program #

<img width="445" height="58" alt="N6" src="https://github.com/user-attachments/assets/f062202a-6b28-4a4b-b1a8-00a6950b8dae" />

Menu 5, digunakan untuk mengakhiri program. Ketika pengguna memilih menu 5, program menampilkan pesan bahwa sistem dihentikan. Perintah break kemudian menghentikan while True, sehingga program tidak kembali menampilkan menu dan langsung selesai.

# FLOWCHART #

<img width="1397" height="1752" alt="MINPRODDP drawio" src="https://github.com/user-attachments/assets/3c2e1921-3e11-4dc4-ba82-9e0b6508df7e" />

# OUTPUT DARI PROGRAM #

# Create #

<img width="436" height="333" alt="MP1" src="https://github.com/user-attachments/assets/a36dc316-244d-45fe-ab56-9c1397dd7a4c" />

Ini adalah hasil output ketika memilih menu Tambah Spesifikasi Aset Baru. Pengguna memasukkan ID aset, nama aset, tipe aset, dan resolusi. Setelah semua data berhasil dimasukkan, program menampilkan pesan “Spesifikasi aset telah disimpan”, yang berarti data berhasil ditambahkan ke dalam sistem.
# Read #

<img width="331" height="162" alt="o1" src="https://github.com/user-attachments/assets/82c39afa-0548-4426-b212-65981331d849" />

Ini adalah hasil output ketika memilih menu Tampilkan Seluruh Spesifikasi Aset. Program menampilkan seluruh data aset yang sebelumnya sudah ditambahkan, sehingga pengguna dapat melihat informasi seperti ID, nama aset, tipe, resolusi, dan status dari setiap aset.

# Update #

<img width="324" height="263" alt="02" src="https://github.com/user-attachments/assets/a149147b-9dd5-492b-862b-b04b6d3db338" />

Ini adalah hasil output ketika memilih menu Ubah Spesifikasi Aset. Pengguna memilih data yang ingin diubah, kemudian memasukkan informasi baru seperti nama, resolusi, dan status. Setelah berhasil diubah, program menampilkan pesan “Spesifikasi aset telah diperbarui”, yang menunjukkan bahwa data lama sudah diperbarui.

# Delete #

<img width="373" height="190" alt="03" src="https://github.com/user-attachments/assets/ea1c9e32-fda4-4a11-9187-01c0ddf30358" />

Ini adalah hasil output ketika memilih menu Hapus Spesifikasi Aset. Pengguna memilih nomor data yang ingin dihapus, kemudian program menghapus data tersebut dari sistem. Setelah berhasil, muncul pesan “Aset berhasil dihapus dari sistem”, yang menandakan bahwa data sudah tidak tersimpan lagi.

# Validasi Looping #

<img width="437" height="414" alt="04" src="https://github.com/user-attachments/assets/f191a987-29b4-45f4-98eb-0122d217ae6d" />

Ini adalah hasil output ketika pengguna memasukkan input yang salah. Misalnya pengguna memasukkan huruf ABC atau No 7, padahal data yang tersedia hanya sampai nomor 5. Program akan menampilkan "Nomor tidak valid!" lalu meminta pengguna memasukkan nomor lagi.
