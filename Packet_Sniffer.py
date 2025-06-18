# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO
from scapy.all import sniff, IP, TCP, UDP, Raw
import threading
import json

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

def detect_protocol(pkt):
    if pkt.haslayer(TCP) or pkt.haslayer(UDP):
        ports = [pkt.sport, pkt.dport]
        if 80 in ports: return "HTTP"
        elif 443 in ports: return "HTTPS"
        elif 53 in ports: return "DNS"
        elif 25 in ports: return "SMTP"
        elif 110 in ports: return "POP3"
        elif 143 in ports: return "IMAP"
        elif 21 in ports: return "FTP"
        else: return f"{pkt.name}:{pkt.dport}"
    return "Other"

def handle_packet(pkt):
    if IP in pkt:
        data = {
            'src': pkt[IP].src,
            'dst': pkt[IP].dst,
            'protocol': detect_protocol(pkt),
            'port': pkt.dport if hasattr(pkt, "dport") else "N/A",
            'payload': ''
        }
        if pkt.haslayer(Raw):
            try:
                payload = pkt[Raw].load.decode('utf-8', errors='ignore')
                data['payload'] = ''.join(c for c in payload if c.isprintable())[:80]
            except:
                data['payload'] = '[unreadable]'

        socketio.emit('packet', data)

        with open("packets_log.txt", "a") as log_file:
            log_file.write(json.dumps(data) + "\n")

def start_sniffing():
    sniff(prn=handle_packet, store=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=start_sniffing, daemon=True).start()
    socketio.run(app, debug=True, host='127.0.0.1', port=5051)
