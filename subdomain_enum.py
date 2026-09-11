import socket
import sys

def enumerate_subdomains(domain, wordlist_file):
    print("=" * 60)
    print(f"MOON Subdomain Enumerator (Hood_4) - Target: {domain}")
    print("=" * 60)

    try:
        with open(wordlist_file, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: File wordlist '{wordlist_file}' tidak ditemukan.")
        return

    found_subdomains = []

    print(f"[+] Memulai pemindaian menggunakan {len(subdomains)} kata dari wordlist...\n")
    print(f"{'SUBDOMAIN':<35} | {'IP ADDRESS':<20}")
    print("-" * 60)

    for sub in subdomains:
        target_subdomain = f"{sub}.{domain}"
        try:
            # Mencoba resolusi DNS untuk mendapatkan IP Address
            ip_address = socket.gethostbyname(target_subdomain)
            print(f"[✓] {target_subdomain:<31} | {ip_address:<20}")
            found_subdomains.append((target_subdomain, ip_address))
        except socket.gaierror:
            # Subdomain tidak ditemukan / tidak aktif
            pass

    print("-" * 60)
    print(f"[+] Pemindaian Selesai! Ditemukan {len(found_subdomains)} subdomain aktif.")
    print("=" * 60)

if __name__ == "__main__":
    target_domain = sys.argv[1] if len(sys.argv) > 1 else input("Masukkan Domain Utama (contoh: github.com): ")
    wordlist = sys.argv[2] if len(sys.argv) > 2 else "wordlist.txt"

    if target_domain:
        enumerate_subdomains(target_domain, wordlist)
    else:
        print("Domain tidak boleh kosong.")