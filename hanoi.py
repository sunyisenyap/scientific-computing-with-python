def hanoi_solver(n):
    # Inisialisasi 3 tiang (rods). 
    # Tiang pertama berisi piringan dari terbesar (n) ke terkecil (1).
    rods = [list(range(n, 0, -1)), [], []]
    
    # Simpan keadaan awal (starting arrangement)
    states = [f"{rods[0]} {rods[1]} {rods[2]}"]
    
    # Fungsi rekursif untuk memindahkan piringan
    def solve(num_disks, source, target, auxiliary):
        if num_disks > 0:
            # 1. Pindahkan n-1 piringan teratas dari source ke auxiliary
            solve(num_disks - 1, source, auxiliary, target)
            
            # 2. Pindahkan piringan terbesar (paling bawah dari tumpukan yang diproses) ke target
            disk = rods[source].pop()
            rods[target].append(disk)
            
            # 3. Rekam keadaan tiang setelah perpindahan
            states.append(f"{rods[0]} {rods[1]} {rods[2]}")
            
            # 4. Pindahkan n-1 piringan dari auxiliary ke target
            solve(num_disks - 1, auxiliary, target, source)
            
    # Mulai penyelesaian dari tiang 0 (source) ke tiang 2 (target) dengan tiang 1 sebagai auxiliary
    solve(n, 0, 2, 1)
    
    # Gabungkan semua keadaan menjadi satu string dengan pemisah baris baru (\n)
    return "\n".join(states)