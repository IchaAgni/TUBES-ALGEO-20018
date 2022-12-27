print ("============================================================ ")
print ("                        Kelompok 4                           ")
print ("Azky Ali Nuryafi(10220018)                                   ")
print ("Nisa Agni Afifah(10220020)                                   ")
print ("Wiwin Suminar   (10220022)                                   ")
print ("============================================================ ")
print (" ___________________________________________________________ ")
print ("|        Selamat datang di Aplikasi SPL & Matriks           |")
print ("|___________________________________________________________|")
print ("                                                             ")

a11=int(input("Masukkan nilai untuk a11:"))
a12=int(input("Masukkan nilai untuk a12:"))
a21=int(input("Masukkan nilai untuk a21:"))
a22=int(input("Masukkan nilai untuk a22:"))
print ("[a11 a12]")
print ("[a21 a22]")
print ("[",a11, a12,"]")
print ("[",a21, a22,"]")

def MenuUtama():
    print ("Menu pilihan :")
    print ("1. Penjumlahan dan pengurangan Matriks 2 x 2")
    print ("2. Matriks Transpose 2 x 2")
    print ("3. Matriks Balikan 2 x 2")
    print ("4. Determinan Matriks 2 x 2")
    print ("5. Sistem Persamaan Linier 2 x 3")
    print ("6. Keluar")
    pilihan=int(input("Silahkan dipilih sesuai daftar menu:"))
    if pilihan==1:
        penjumlahan_matriks()
    elif pilihan==2:
        transpose_matriks()
    elif pilihan==3:
        matriks_balikan()
    elif pilihan==4:
        determinan_matriks()
    elif pilihan==5:
        sistem_Persamaan_Linear()
    elif pilihan==6:
        exit()
    else:
        print ("Input yang Anda Masukkan Salah!")
        MenuUtama()

def ulang():
    kembali=int(input("Apakah kalian akan menghitung lagi\n(1=ya, 2=tidak :)"))
    if kembali==1:
        MenuUtama()
    elif kembali==2:
        exit()
    else:
        print ("Input yang anda masukkan salah!")
        ulang()

def penjumlahan_matriks():
    print ("Menu pilihan:")
    print ("1. Penjumlahan matriks 2 x 2")
    print ("2. Pengurangan Matriks 2 x 2")
    pilihan1=int(input("Silahkan pilih sesuai pilihan menu :"))
    print ("Berikut Tampilan untuk matriks B")
    print ("[b11 b12]")
    print ("[b21 b22]")
    b11=int(input("Masukkan nilai untuk b11:"))
    b12=int(input("Masukkan nilai untuk b12:"))
    b21=int(input("Masukkan nilai untuk b21:"))
    b22=int(input("Masukkan nilai untuk b22:"))
    print ("Hasil matriks yang telah dimasukkan\n untuk matriks A adalah :")
    print ("[",a11, a12, "]")
    print ("[",a21, a22, "]")
    print ("Hasil matriks yang telah dimasukkan\n untuk matriks B adalah :")
    print ("[",b11, b12, "]")
    print ("[",b21, b22, "]")
    if pilihan1==1:
        print ("Hasil penjumlahan kedua matriks tersebut adalah")
        print ("[",a11+b11, a12+b12, "]")
        print ("[",a21+b21, a22+b22, "]")
        ulang()
    
    elif pilihan1==2:
        print ("Hasil pengurangan kedua matriks tersebut adalah")
        print ("[",a11-b11, a12-b12, "]")
        print ("[",a21-b21, a22-b22, "]")
        ulang()
    else :
        pilihan1
    
def transpose_matriks():

    print ("Berikut hasil matriks sebelum transpose :")
    print ("[",a11, a12, "]")
    print ("[",a21, a22, "]")

    print ("Hasil matriks setelah transpose :")
    print ("[",a11,a21, "]")
    print ("[",a12,a22, "]")

    ulang()

def matriks_balikan():
    print ("Berikut Rumus untuk menentukan matriks balikan (invers)")
    print ("(1/determinan matriks) x [adjoin Matriks]")
    a=(a11*a22)-(a12*a21)
    print("determinan dari matriks tersebut:",a)
    print("Adjoint Matriks tersebut adalah :")
    print ("[",a22, -a12, "]")
    print ("[",-a21, a11, "]")
    a1=(1/a)*a22
    a2=(1/a)*(-a12)
    a3=(1/a)*(-a21)
    a4=(1/a)*a11
    print ("Hasil dari perhitungan invers tersebut adalah:")
    print ("[",a1, a2, "]")
    print ("[",a3, a4, "]")

    ulang()

def determinan_matriks():
    print ("Berikut rumus untuk menentukan determinan")
    print ("[",a11, a12,"]")
    print ("[",a21, a22,"]")
    print ("(a11 x a22) - (a12 x a21) = ",(a11*a22),"-",(a12*a21),"=",(a11*a22)-(a12*a21))
    
    ulang()

def sistem_Persamaan_Linear():
    print("Masukan nilai b1 dan b2  ")
    b1 = int(input("Masukan nilai untuk b1 : "))
    b2 = int(input("Masukan nilai untuk b2 : "))
    print(a11,"x +",a21,"y = ", b1)
    print(a12,"x +",a22,"y = ", b2)

    print("Matrik yang dibentuk adalah sbb : ")
    print("==================================")
    print("[",a11, a12,"] [y] = [",b1,"]")
    print("[",a21, a22,"] [x] = [",b2,"]")

    adj = 1/((a11*a22)-(a12*a21))
    print ("[",a22, -a12, "]")
    print ("[",-a21, a11, "]")

    print("Hasil dari adjoin Matrik :")
    print("[x] = ",adj,"[",a22, -a12, "] [",b1,"]")
    print("[y] = ",adj,"[",-a21, a11, "] [",b2,"]")

    c=adj*((a22*b1)+(-a12*b2))
    d=adj*((-a21*b1)+(a11*b2))
    print("solusi dari SPL ini adalah :")
    print("==================================")
    print("[x] = [",c,"]") 
    print("[y] = [",d,"]")
    ulang()

MenuUtama()
pilihan=int(input("Silahkan dipilih sesuai daftar menu:"))
if pilihan==1:
  penjumlahan_matriks()
elif pilihan==2:
  transpose_matriks()
elif pilihan==3:
  matriks_balikan()
elif pilihan==4:
  determinan_matriks()
elif pilihan==5:
    sistem_Persamaan_Linear()
elif pilihan==6:
    exit()
else:
    print ("Input yang Anda Masukkan Salah!")
    MenuUtama()