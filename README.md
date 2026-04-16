sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y // install python + pip 
pip3 install scapy // instal scapy

nano broadcast_control.py // Create file 
from scapy.all import sniff, Ether
import time

BROADCAST_LIMIT = 10
TIME_WINDOW = 5

broadcast_count = 0
start_time = time.time()

def process_packet(packet):
    global broadcast_count, start_time

    if packet.haslayer(Ether):
        dest_mac = packet[Ether].dst

        if dest_mac == "ff:ff:ff:ff:ff:ff":
            broadcast_count += 1
            print(f"[!] Broadcast Packet Detected ({broadcast_count})")

    if time.time() - start_time > TIME_WINDOW:
        if broadcast_count > BROADCAST_LIMIT:
            print("\n⚠️ ALERT: Broadcast Storm Detected!")
            print("🚫 Limiting traffic (simulation)\n")
        else:
            print("\n✅ Network Stable\n")

        broadcast_count = 0
        start_time = time.time()

print("🔍 Monitoring Broadcast Traffic...\n")
sniff(prn=process_packet, store=False)

sudo python3 broadcast_control.py// RUN the program 
sudo apt install iputils-arping
sudo arping -I eth0 192.168.1.255 // generate boardcast traffic
