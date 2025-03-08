nama = input("Masukkan Nama : ")
nik = input("Masukkan NIK : ")
status = input("Masukkan Status (Pegawai Tetap/Honor) : ")
golongan = input("Masukkan Golongan (A/B/C) : ")

if status == "Tetap" or status == "Honor":
    if golongan == "A" or golongan == "B" or golongan == "C":
        if status == "Tetap":
            gaji = 1000000
            if golongan == "A":
                bonus = 200000
            elif golongan == "B":
                bonus = 400000
            else:
                bonus = 550000
        else:  # status == "Honor"
            gaji = 750000
            if golongan == "A":
                bonus = 150000
            elif golongan == "B":
                bonus = 275000
            else:
                bonus = 480000

        total_gaji = gaji + bonus

        print("\n===Hasil===")
        print("Nama: " + nama)
        print("NIK: " + nik)
        print("Status: " + status)
        print("Golongan: " + golongan)
        print("Gaji Pokok: Rp " + str(gaji))
        print("Bonus Golongan " + golongan + ": Rp " + str(bonus))
        print("Total Gaji: Rp " + str(total_gaji))

    else:
        print("Golongan tidak valid!")
else:
    print("Status tidak valid!")
