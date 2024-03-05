import requests
import socket

def cek_header(url):
    try:
        response = requests.get(url)
        return response.headers
    except Exception as e:
        return str(e)

def cek_port(host):
    aktif_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            aktif_ports.append(port)
        sock.close()
    return aktif_ports

def dapatkan_ip(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None

def reverse_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

# Uji fungsi
print("\033[1;30;47mDomain Mask\033[0m")  # Output "Domain Mask" dalam warna hitam putih

print("""
////////////////////////////////////////////////////////////////
// ____                        _       __  __           _     //
//|  _ \  ___  _ __ ___   __ _(_)_ __ |  \/  | __ _ ___| | __ //
//| | | |/ _ \| '_ ` _ \ / _` | | '_ \| |\/| |/ _` / __| |/ / //
//| |_| | (_) | | | | | | (_| | | | | | |  | | (_| \__ \   <  //
//|____/ \___/|_| |_| |_|\__,_|_|_| |_|_|  |_|\__,_|___/_|\_\ //
////////////////////////////////////////////////////////////////
""")  # Output "DomainMask" dalam ASCII Art

url = input("Masukkan URL: ")
headers = cek_header(url)
print("\nHeaders:")
for key, value in headers.items():
    print(f"{key}: {value}")

host = input("\nMasukkan host (misalnya, 'www.example.com'): ")
ip = dapatkan_ip(host)
if ip is not None:
    print(f"\nAlamat IP dari {host} adalah {ip}")
    reversed_ip = reverse_ip(ip)
    if reversed_ip is not None:
        print(f"Reverse IP dari {ip} adalah {reversed_ip}")
    else:
        print(f"Tidak dapat melakukan reverse IP dari {ip}")
else:
    print(f"\nTidak dapat mendapatkan alamat IP dari {host}")

aktif_ports = cek_port(host)
print("\nPort aktif:")
for port in aktif_ports:
    print(port)
