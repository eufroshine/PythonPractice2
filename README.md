# PythonPractice2

* Latihan 1
<img src="ss/sslat1.png" width="500">

* Latihan 2
<img src="ss/sslat2.png" width="500">

**Input nilai**

Kode ini meminta pengguna untuk memasukkan dua nilai, a dan b, menggunakan fungsi input(). Nilai-nilai ini dimasukkan sebagai string.


**Input Variabel**

Ini mencetak nilai a dan b yang dimasukkan oleh pengguna.


**Hasil Penggabungan**

Kode ini mencoba menggabungkan nilai a dan b sebagai string menggunakan format().


**Konversi Nilai Variabel**

Kode ini mengonversi nilai a dan b dari string ke integer menggunakan fungsi int().


**Print Penjumlahan dan Pembagian**

Kode ini mencetak hasil penjumlahan dan pembagian dari nilai a dan b.

* Latihan 3
<img src="ss/sslat3.png" width="500">

**Membuat Fungsi print_diamond**

    def print_diamond(rows):


Pertama-tama, kita mendefinisikan fungsi print_diamond yang akan mencetak pola berlian. Fungsi ini menerima satu parameter, yaitu jumlah baris dari berlian yang akan dicetak.

**Loop Pertama (Baris ke-atas)**

    for i in range(1, rows + 1):


Kita menggunakan loop for untuk membuat pola dari atas ke bawah. Loop ini akan berjalan dari 1 hingga rows + 1.

**Leading Spaces (Spasi Awal**

    for j in range(rows - i):
        print(" ", end="")


Di dalam loop pertama, kita tambahkan loop untuk mencetak spasi sebelum bintang, berdasarkan posisi baris. Ini akan mencetak spasi dari rows - i.

**Bintang**

    for k in range(1, 2 * i):
        print("*", end="")


Kita tambahkan loop untuk mencetak bintang, yang akan mencetak bintang sebanyak 2 * i - 1.

**Pindah Baris**

    print()


Setelah mencetak spasi dan bintang di setiap baris, kita pindah ke baris baru.

**Loop Kedua (Baris ke-bawah):**

    for i in range(rows - 1, 0, -1):

Selanjutnya, kita menggunakan loop for yang serupa untuk membuat pola dari bawah ke atas. Loop ini akan berjalan dari rows - 1 hingga 0.

**Leading Spaces (Spasi Awal) untuk Loop Kedua**

    for j in range(rows - i):
        print(" ", end="")


Seperti pada loop pertama, kita tambahkan loop untuk mencetak spasi sebelum bintang.

**Bintang untuk Loop Kedua**

    for k in range(1, 2 * i):
        print("*", end="")


Kita tambahkan loop untuk mencetak bintang, yang akan mencetak bintang sebanyak 2 * i - 1.

**Pindah Baris untuk Loop Kedua**

    print()


Setelah mencetak spasi dan bintang di setiap baris, kita pindah ke baris baru.

**Input Jumlah Baris**

    num_rows = int(input("Enter the number of rows: "))


 Di luar fungsi, kita minta pengguna untuk memasukkan jumlah baris yang diinginkan.

 **Memanggil Fungsi dan Mencetak Berlian**

    print_diamond(num_rows)


  Terakhir, kita memanggil fungsi print_diamond dengan jumlah baris yang dimasukkan oleh pengguna.

  *INI OUTPUTNYA*
  
  <img src="ss/outputlat3.png" width="500">

* Menghitung Luas dan Keliling Lingkaran

<img src="ss/lingkaran.png" width="500">

**Import Library 'math'**

Ini mengimpor modul math, yang memberikan akses ke fungsi-fungsi matematika, termasuk pi (π).

**Fungsi untuk Menghitung Luas Lingkaran**

    def hitung_luas_lingkaran(r):
        luas = math.pi * r**2
        return luas

Fungsi ini menerima jari-jari (r) sebagai parameter, menghitung luas lingkaran menggunakan rumus πr², dan mengembalikan nilai luas.

**Fungsi untuk Menghitung Keliling Lingkaran**

    def hitung_keliling_lingkaran(r):
        keliling = 2 * math.pi * r
        return keliling

Fungsi ini menerima jari-jari (r) sebagai parameter, menghitung keliling lingkaran menggunakan rumus 2πr, dan mengembalikan nilai keliling.

**Input dari Pengguna**

    luas_lingkaran = hitung_luas_lingkaran(r)
    keliling_lingkaran = hitung_keliling_lingkaran(r)

Fungsi-fungsi yang didefinisikan sebelumnya dipanggil dengan jari-jari yang dimasukkan oleh pengguna. Hasilnya disimpan dalam variabel luas_lingkaran dan 

**Menampilkan Hasil**

    print(f"Luas lingkaran: {luas_lingkaran:.2f}")
    print(f"Keliling lingkaran: {keliling_lingkaran:.2f}")

Hasil luas dan keliling lingkaran ditampilkan ke layar dengan dua angka desimal.

*INI OUTPUTNYA*

<img src="ss/outputlingkaran.png" width="500">

* Flowchart

<img src="ss/flowchart.png" width="50%">

