from datetime import datetime

stack = []

def push (nama,spend):
        spend=int(spend)
        waktu = datetime.now().strftime("%H:%M:%S")
        lelang = f"{nama}\t\t{spend}\t\t{waktu}"
        stack.append(lelang)
        print(f"{lelang}")

def pop():
    if stack:
        lelang = stack.pop()
        print(f"{lelang}")
    else:
        print("Tidak ada data")

def tampilkan():
    if stack:
        print("No","\t","Nama","\t\t","Spend","\t\t","Waktu")
        for i in range (len(stack) -1,-1,-1):
            print(f"{i+1}.\t{stack[i]}")
    else:
        print("Tidak Ada Data Yang Masuk")

while True:
    print("="*50)
    print("Sistem pelelangan")
    print("="*50)
    print("1.Masukkan spend")
    print("2.Hapus data spend terakhir")
    print("3.Tampilkan Daftar pelelang")
    print("4.Keluar")
    print("="*50)

    pilih = input("Masukkan Pilihan:")
    if pilih == "1":
        nama = input("Masukkan Nama:")
        spend = input("Masukkan spend:")
        push(nama,spend)
    elif pilih == "2":
        pop()
    elif pilih == "3":
        print("="*50)
        print("Daftar Pelelang")
        print("="*50)
        tampilkan()
        print("="*50)
    elif pilih == "4":
        print("Terima Kasih")
        break
    else:
        print("pilihan salah")