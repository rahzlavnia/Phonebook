""" Tugas 5.2 Proyek 1
Aplikasi Phonebook
Author : Sarah
NIM    : 221524059
Kelas  : 1B-D4 """

import sys
import os

#================Modul Program================

def displayMenu():
    #Menu untuk memilih opsi operasi yang akan dilakukan
    #Create/Insert, Read, Update, Delete, Search
    print("===============================================")
    print("\t\t   Phone Book")
    print("===============================================")
    print("Pilihan Menu Operasi:")
    print("1. Tambah kontak")
    print("2. Hapus kontak yang ada")
    print("3. Cari sebuah kontak")
    print("4. Update sebuah kontak")
    print("5. Tampilkan semua kontak")
    print("99. Keluar")

    pilih = int(input("Masukkan pilihan anda: "))
    return pilih

def tambahKontak():
    file = open("PhoneBook.txt", "r")
    nama = input("Masukkan nama: ")
    lines = file.readlines()
    found = False
    for line in lines:
        if nama in line:
            found = True
            break

    if found:
        print("Nama kontak ada pada PhoneBook, masukkan nama lain")
    else:    
        nomor = input("Masukkan nomor : ")
        found = False
        for line in lines:
            if nomor in line:
                found = True
                break
        if found:
            print("Nomor kontak ada pada PhoneBook, masukkan nomor lain")
        else:    
            file = open("PhoneBook.txt", "a")
            file.writelines(nama + "\t\t" + nomor + "\n")
            print("Kontak berhasil ditambahkan")
    file.close()    

def hapusKontak():
    file = open("PhoneBook.txt", "r")
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    lines = file.readlines()
    found = False
    for line in lines:
        if nama in line:
            found = True
            break
    file.close()

    if found:
        with open("PhoneBook.txt", "w") as file:
            for line in lines:
                if line.split()[0] != nama:
                    file.write(line)
            print("Kontak berhasil dihapus")
    else:
        print("Tidak ada kontak bernama: " + nama)    
    
def cariKontak():
    print("Pilihan Pencarian:")
    print("1. Cari berdasarkan nama")
    print("2. Cari berdasarkan nomor")
    pilih = int(input("Masukkan pilihan anda: "))

    file = open("PhoneBook.txt", "r")
    file_contents = file.readlines()
        
    if pilih == 1:
        searchName = input("Masukkan nama yang ingin dicari: ")
        found = False   
        for line in file_contents:
            if searchName in line:
                print("Kontak yang dicari: ")
                temp = line.split("\t\t")
                print ("Nama\t: "+temp[0]+"\nNomor\t: "+temp[1][:-1])
                found=True
                break
        if  found == False:
            print("Tidak ada kontak bernama: " + searchNama)    
    else :
        searchNomor =  input("Masukkan nomor yang ingin dicari: ")
        found = False
        for line in file_contents:
            if searchNomor in line:
                print("Kontak yang dicari: ")
                temp = line.split("\t\t")
                print ("Nama\t: "+temp[0]+"\nNomor\t: "+temp[1][:-1])
                found=True
                break
        if  found == False:
            print("Tidak ada kontak bernomor: " + searchNomor )
    file.close()

def updateKontak():
     nama = input("Masukkan nama kontak yang ingin diubah: ")
     file = open("PhoneBook.txt", "r+")
     lines = file.readlines()
     found = False
     for i, line in enumerate(lines):
        if nama in line:
            print("Pilihan update kontak:")
            print("1. Update nama")
            print("2. Update nomor")
            pilih = int(input("Masukkan pilihan anda: "))
            if pilih == 1:
                nama_baru = input("Masukkan nama telepon baru: ")
                ketemu = False
                for line in lines:
                    if nama_baru in line:
                        ketemu = True
                        break
                if ketemu:
                    print("Nama kontak ada pada PhoneBook, masukkan nama lain")
                else:    
                    lines[i] = f"{nama_baru}\t\t{line.split()[1]}\n"
                    print("Kontak berhasil diubah")
            elif pilih == 2:
                nomor_baru = input("Masukkan nomor telepon baru: ")
                ketemu = False
                for line in lines:
                    if nomor_baru in line:
                        ketemu = True
                        break
                if ketemu:
                    print("Nomor kontak ada pada PhoneBook, masukkan nomor lain")
                else:    
                    lines[i] = f"{line.split()[0]}\t\t{nomor_baru}\n"
                    print("Kontak berhasil diubah")
            found = True
            file.seek(0)
            file.writelines(lines)
            file.truncate()
     if not found:
        print("Kontak tidak ditemukan")
     file.close()       
        
def displayKontak():
    i=1
    if is_empty_file("PhoneBook.txt"):
        print("File kosong")
    else:
        file = open("PhoneBook.txt", "r")
        print("No".ljust(3,' ')+"Nama".ljust(25,' ') + "Nomor")
        for line in file:
            temp = line.split("\t\t")
            print (str(i) + ". " +temp[0].ljust(25,' ')+temp[1][:-1])
            i=i+1
        file.close()
 
def is_empty_file(file_path):
    return os.path.isfile(file_path) and os.path.getsize(file_path) == 0    

def keluar():
    print("===============================================")
    print("\t\t End Phone Book")
    print("===============================================")
    sys.exit("Goodbye, have a nice day ahead!")
    

#=================Main Program================  
while True:
    choice = displayMenu()
    if choice == 1:
        tambahKontak()
    elif choice == 2:
        hapusKontak()
    elif choice == 3:
        cariKontak()
    elif choice == 4:
        updateKontak()
    elif choice == 5:
        displayKontak()
    elif choice == 99:
        keluar()
        
