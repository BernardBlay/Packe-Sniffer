# 🕵️‍♂️ Python Packet Sniffer with HTML Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Scapy](https://img.shields.io/badge/Scapy-Network_Tools-orange)](https://scapy.net/)

This project is a lightweight **network packet sniffer** written in **Python** using the **Scapy** library. It captures real-time TCP and UDP packets and prints out the source and destination IP addresses. It includes an optional **HTML dashboard** that can be used to visualize stats like protocol counts or traffic flows.

---

## 🚀 Features

- ✅ Live packet sniffing with Scapy  
- ✅ Captures and displays TCP/UDP packets  
- ✅ Shows source → destination IPs  
- ✅ Minimal setup, beginner-friendly  
- ✅ HTML dashboard for traffic visualization (pie chart, tables, etc.)  
- ✅ Easy to expand with ARP, ICMP, filtering, etc.

---

## 📂 Project Structure

packet-sniffer/
├── packet\_sniffer.py         # Python script for live packet capture
├── dashboard.html            # Simple visual dashboard (static)
├── requirements.txt          # Python dependencies
└── README.md                 # You're here


## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/packet-sniffer.git
cd packet-sniffer
````

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

> Only `scapy` is required if you’re not using Flask or real-time web updates.

---

## ▶️ Usage

### Run the packet sniffer

```bash
python packet_sniffer.py
```

If you're on Linux or macOS, and need elevated privileges:

```bash
sudo python packet_sniffer.py
```

> This will start sniffing packets and printing live output like:

```
Sniffing... Press Ctrl+C to stop.
TCP Packet: 192.168.1.10 -> 142.250.195.78
UDP Packet: 192.168.1.10 -> 8.8.8.8
```

---

### Open the Dashboard (Optional)

Just open `dashboard.html` in your browser:

text
packet-sniffer/dashboard.html


Use it to visualize packet stats in a pie chart, log table, or protocol distribution. You can update it to pull from a file or API if needed.



## 🔐 Ethical Disclaimer

This tool is strictly for **educational purposes** and testing on **authorized networks** only. Unauthorized sniffing is illegal and unethical. Use responsibly.

---

## 🧠 How It Works

1. Scapy sniffs network traffic using `sniff()`.
2. It filters TCP and UDP packets.
3. Packet info is displayed in the terminal.
4. The dashboard can be used to visualize or extend this data.

---

## 📈 Future Improvements

* [ ] Add ARP, ICMP support
* [ ] Write packet logs to a file
* [ ] Integrate Flask for live dashboard updates
* [ ] Display ports, flags, and protocol-specific data
* [ ] Add GeoIP/IP location lookup

---

## 🧱 Built With

* [Python 3](https://www.python.org/)
* [Scapy](https://scapy.net/)
* HTML5 + CSS + (optionally Chart.js)

---

## 📄 License

**MIT License**
Use it freely, but don’t use it for harm. Respect the tech. ✌️

---

## 💬 Author

**Bernard Blay**
Cybersecurity Enthusiast
*"Protect, Educate, Defend."*

```
