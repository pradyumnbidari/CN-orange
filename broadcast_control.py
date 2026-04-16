from scapy.all import sniff, Ether
import time

# SETTINGS (you can tweak for demo)
BROADCAST_LIMIT = 5
TIME_WINDOW = 5  # seconds

broadcast_count = 0
start_time = time.time()

def process_packet(packet):
    global broadcast_count, start_time

    if packet.haslayer(Ether):
        dest_mac = packet[Ether].dst

        # Check if broadcast
        if dest_mac == "ff:ff:ff:ff:ff:ff":
            broadcast_count += 1
            print(f"[!] Broadcast Packet Detected ({broadcast_count})")

    # Check time window
    if time.time() - start_time > TIME_WINDOW:
        if broadcast_count >= BROADCAST_LIMIT:
            print("\n⚠️ ALERT: Broadcast Storm Detected!")
            print("🚫 Action: Limiting broadcast traffic (simulation)\n")
        else:
            print("\n✅ Network Stable\n")

        broadcast_count = 0
        start_time = time.time()

# MAIN
print("🔍 Monitoring Broadcast Traffic...\n")

try:
    sniff(prn=process_packet, store=False)
except KeyboardInterrupt:
    print("\n🛑 Stopping monitoring...")