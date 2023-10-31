#Input Nilai
a=input("Masukan Nilai a : ")
b=input("Masukan Nilai b : ")

#print variabel
print("Variabel a : ",a)
print("Variabel b : ",b)
print("Hasil Penggabungan {0} & {1} = ".format(a,b)+(a+b))

#konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil Penjumlahan {0} + {1} = %d".format(a,b) %(a+b))
print("Hasil Pembagian {0}/{14} = %d".format(a,b) %(a/b))