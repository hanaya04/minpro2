from prettytable import PrettyTable

print("Nama : Marza Hanaya Melodya Goga")
print("NIM/Kelas : 2409116103/C")
print("Program : Mini Project 2 Dasar Pemrograman")
print("--------------------------------")

courses = [
    {"judul": "Kursus Bahasa Asing"},
    {"judul": "Kursus Pemrograman"},
    {"judul": "Kursus Desain Grafis"},
    {"judul": "Kursus Fotografi"}
]

def main():
    print("=== Selamat Datang di Platform Pembelajaran Hana ===")
    print("Pilih Status Anda")
    print("1. Admin")
    print("2. Pengguna")
    
    status = input("Masukkan Pilihan Anda: ")

    if status == '1':
        login("admin")
    elif status == '2':
        login("user")
    else:
        print("Pilihan tidak valid.")

def login(user_type):
    if user_type == "admin":
        username = input("Masukkan ID Anda: ")
        password = input("Masukkan Password: ")
        if username == "admin1" and password == "admin0101":
            print("Login admin berhasil!")
            admin_menu()
        else:
            print("Login admin gagal!")
    elif user_type == "user":
        username = input("Masukkan ID Anda: ")
        password = input("Masukkan Password: ")
        if username == "user2" and password == "user243":
            print("Login pengguna berhasil!")
            user_menu()
        else:
            print("Login pengguna gagal!")

def user_menu():
    while True:
        print("\n=== Menu Pengguna ===")
        print("1. Lihat Kursus")
        print("2. Daftar Kursus")
        print("3. Keluar")
        
        pilihan_pengguna = input("Silakan tentukan pilihan Anda: ")

        if pilihan_pengguna == '1':
            lihat_kursus()
        elif pilihan_pengguna == '2':
            daftar_kursus()
        elif pilihan_pengguna == '3':
            print("Terima kasih telah menggunakan platform kami!")
            break
        else:
            print("Pilihan tidak valid.")

def daftar_kursus():
    print("=== Pendaftaran Kursus ===")
    nama = input("Nama Anda: ")
    ID = input("ID Anda: ")
    password = input("Password Anda: ")
    kursus = input("Kursus yang Anda inginkan (1-4): ")
    print(f"Selamat, {nama}! Anda telah tergabung dalam kursus yang anda inginkan!")
    
def admin_menu():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Kursus")
        print("2. Lihat Kursus")
        print("3. Hapus Kursus")
        print("4. Update Kursus")
        print("5. Keluar")

        pilihan_admin = input("Silakan tentukan pilihan Anda: ")
        if pilihan_admin == '1':
            tambah_kursus()
        elif pilihan_admin == '2':
            lihat_kursus()
        elif pilihan_admin == '3':
            hapus_kursus()
        elif pilihan_admin == '4':
            update_kursus()
        elif pilihan_admin == '5':
            print("Keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak valid.")

def lihat_kursus():
    tabel = PrettyTable()
    tabel.title = "Berikut Kursus yang tersedia saat ini"
    tabel.field_names = ["No", "Judul Kursus"]

    for i, kursus in enumerate(courses):
        tabel.add_row([i + 1, kursus['judul']])

    print(tabel)

def tambah_kursus():
    judul_kursus = input("Masukkan Judul Kursus yang ingin ditambahkan: ")
    courses.append({"judul": judul_kursus})
    print(f"Kursus '{judul_kursus}' berhasil ditambahkan!")

def hapus_kursus():
    lihat_kursus()
    try:
        index = int(input("Nomor kursus yang ingin dihapus: ")) - 1
        if 0 <= index < len(courses):
            removed = courses.pop(index)
            print(f"Kursus '{removed['judul']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def update_kursus():
    lihat_kursus()
    try:
        index = int(input("Nomor kursus yang ingin diupdate: ")) - 1
        if 0 <= index < len(courses):
            judul_baru = input("Judul Baru: ")
            courses[index] = {"judul": judul_baru}
            print("Kursus berhasil diupdate!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")

def admin_menu():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Kursus")
        print("2. Lihat Kursus")
        print("3. Hapus Kursus")
        print("4. Update Kursus")
        print("5. Keluar")

        pilihan_admin = input("Silakan tentukan pilihan Anda: ")
        if pilihan_admin == '1':
            tambah_kursus()
        elif pilihan_admin == '2':
            lihat_kursus()
        elif pilihan_admin == '3':
            hapus_kursus()
        elif pilihan_admin == '4':
            update_kursus()
        elif pilihan_admin == '5':
            print("Keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()