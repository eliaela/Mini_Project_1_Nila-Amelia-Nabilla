data_spesifikasi = []

while True:
    print("\n=======================================================")
    print("  STUDIO ANIMASI & MOTION GRAPHIC - SPECIFICATION SYSTEM")
    print("=======================================================")
    print("1. Tambah Spesifikasi Aset Baru")
    print("2. Tampilkan Seluruh Spesifikasi Aset")
    print("3. Ubah Spesifikasi Aset")
    print("4. Hapus Spesifikasi Aset")
    print("5. Keluar Dari Program")
    print("=======================================================")
        
    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == "1":
        print("\n=== TAMBAH SPESIFIKASI ASET BARU ===")

        while True:
            id_aset = input("ID Aset: ").strip().upper()
            if id_aset:
                break
            print("ID Aset tidak boleh kosong!")

        while True:
            nama = input("Nama Aset/Scene: ").strip()
            if nama:
                break
            print("Nama tidak boleh kosong!")

        print("\nPilih Tipe Aset:")
        print("1. Karakter 3D / 2D")
        print("2. Background / Environment")
        print("3. Motion Graphic Element")
        print("4. Visual Effects (VFX)")

        while True:
            tipe = input("Pilih tipe (1-4): ").strip()
            if tipe == "1":
                tipe_aset = "Karakter"
                break
            elif tipe == "2":
                tipe_aset = "Background"
                break
            elif tipe == "3":
                tipe_aset = "Motion Graphic"
                break
            elif tipe == "4":
                tipe_aset = "VFX"
                break

            else:
                print("Tipe tidak valid!")

        while True:
            resolusi = input("Resolusi: ").strip()
            if resolusi:
                break
            print("Resolusi tidak boleh kosong!")

        data_spesifikasi.append(
            (id_aset, nama, tipe, resolusi, "Draft Spec")
        )
        print(f"\n[BERHASIL] Spesifikasi aset '{nama}' ({id_aset}) telah disimpan.")


    elif pilihan == "2":
        print("\n=== DATA ASET ===")

        if not data_spesifikasi:
            print("Belum ada data.")
        else:
            for i, data in enumerate(data_spesifikasi, 1):
                print(i, data)

    elif pilihan == "3":
        print("\n=== UBAH SPESIFIKASI ASET ===")

        if not data_spesifikasi:
            print("Belum ada data.")
        else:
            for i, data in enumerate(data_spesifikasi, 1):
                print(i, data)

            while True:
                nomor = input("Nomor data: ").strip()

                if nomor.isdigit() and 1 <= int(nomor) <= len(data_spesifikasi):
                    nomor = int(nomor) - 1
                    break
                print("Nomor tidak valid!")

            data_lama = data_spesifikasi[nomor]

            nama = input("Nama baru: ").strip()
            if not nama:
                nama = data_lama[1]

            resolusi = input("Resolusi baru: ").strip()
            if not resolusi:
                resolusi = data_lama[3]

            print("1. Draft Spec")
            print("2. Ready for Modeling/Anim")
            print("3. In Rendering")
            print("4. Approved / Final")

            while True:
                status = input("Pilih status: ").strip()

                if status == "1":
                    status = "Draft Spec"
                    break
                elif status == "2":
                    status = "Ready for Modeling/Anim"
                    break
                elif status == "3":
                    status = "In Rendering"
                    break
                elif status == "4":
                    status = "Approved / Final"
                    break
                else:
                    print("Status tidak valid!")

            data_spesifikasi[nomor] = (
                data_lama[0], nama, data_lama[2], resolusi, status
            )
            print(f"\n[BERHASIL] Spesifikasi aset [{data_lama[0]}] telah diperbarui.")


    elif pilihan == "4":
        print("\n=== HAPUS SPESIFIKASI ASET ===")

        if not data_spesifikasi:
            print("Belum ada data.")
        else:
            for i, data in enumerate(data_spesifikasi, 1):
                print(i, data)

            while True:
                nomor = input("Nomor data: ").strip()

                if nomor.isdigit() and 1 <= int(nomor) <= len(data_spesifikasi):
                    data = data_spesifikasi.pop(int(nomor) - 1)
                    print(f"\n[BERHASIL] Aset [{data[0]}] '{data[1]}' berhasil dihapus dari sistem.")
                    break

                print("Nomor tidak valid!")

    elif pilihan == "5":
        print("\nTerima kasih! Sistem spesifikasi produksi dihentikan.")
        break

    else:
            print("\n[ERROR] Pilihan menu tidak valid! Silakan pilih angka 1 sampai 5.")
