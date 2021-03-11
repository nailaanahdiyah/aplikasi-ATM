import random
import datetime
from customer import Customer

atm = Customer(id) #membuat var class Customer di file customer.py (instance object)

#jika kodingan di pada Class Customer berhasil maka while di jalankan
while True:
    ketikPin = int(input('Masukkan PIN: '))
    id = ketikPin
    trial = 0

    #verifikasi pin
    while(id != int(atm.cekPin()) and trial < 3): #jika id tidak sama dengan Pin yang disiapkan dan trial masih kurang dari 3
        id = int(input('PIN salah. Silahkan masukkan kembali: '))
        trial += 1
        if trial == 3:
            print('Error. Silahkan ambil kartu dan coba kembali')
            exit()
    while True:
            print('Selamat datang di ATM Saya')
            print('\n1 - Cek Saldo \t2 - Debet \t3 - Simpan \n4 - Ganti PIN \t5 - Keluar')
            pilih = int(input('Silahkan pilih menu: '))

            #cek saldo
            if pilih == 1:
                print('Saldo pada ATM anda sebesar: Rp.' + str(atm.cekBalance())) #memanggil method cekBalance yg terdapat pada class Customer

            #debet
            elif pilih == 2:
                nominal = int(input('Masukkan nominal saldo: Rp.'))
                verifikasi = int(input('Konfirmasi: Anda akan melakukan debet sebesar Rp.' +str(nominal)+'. Lanjutkan? 1.Ya \t 2.Tidak \n'))

                if verifikasi == 1:
                    print('Saldo awal: Rp. ' +str(atm.cekBalance()))
                else:
                    break

                if nominal < atm.cekBalance():
                    atm.debetProses(nominal)
                    print('Transaksi Berhasil')
                    print('\nSaldo saat ini sebesar: Rp.' + str(atm.cekBalance()) +'\n')
                else:
                    print("Saldo anda tidak cukup\n")

            #simpan
            elif pilih == 3:
                nominal = int(input('Masukkan nominal yang akan di simpan: '))
                verifikasi = int(input('Konfirmasi: Anda akan melakukan penyimpanan uang sebesar Rp.' +str(nominal)+'. Lanjutkan? 1.Ya \t 2.Tidak \n'))

                if verifikasi == 1:
                    atm.simpanProses(nominal)
                    print('Berhasil')
                    print('Saldo anda saat ini sebesar: ' +str(atm.cekBalance()))
                else:
                    break

            #ganti pin
            elif pilih == 4:
                verifikasi = int(input('Masukkan PIN lama: '))

                while verifikasi != int(atm.cekPin()):
                    print('PIN salah, masukkan PIN kembali')

                update_pin = int(input('Masukkan PIN baru: '))
                verifikasi_pin_baru = int(input('Masukkan kembali PIN baru: '))
                if verifikasi_pin_baru == update_pin:
                    print('PIN baru berhasil disimpan')
                else:
                    print('PIN salah')
            #keluar
            elif pilih == 5:
                jawab = int(input('Apakah anda yakin keluar? 1. Ya \t2.Tidak \n'))
                if jawab == 1:
                    print('===========Resi tercetak otomatis saat keluar===========')
                    print(' Harap simpan tanda terima ini sebagai bukti transaksi.')
                    print('\tNo. Record: ' + str(random.randint(100000, 1000000))) #mengambil angka acak antara 100000 s.d 1000000
                    print('\tTanggal: ' + str(datetime.datetime.now())) #menampilakan jam saat ini
                    print('\tSaldo akhir: ' + str(atm.cekBalance()))
                    print('=========Terima kasih telah menggunakan ATM Saya========')
                    exit()
                else:
                    break
            else :
                print('Error. Menu tidak tersedia \n')
                
    
