# 🌡️ Server Room Thermal Guardian

An autonomous, edge-computed server room thermal management and cooling system built on Raspberry Pi 3B+.

## 🚀 Key Features
- **Automated Cooling Loop:** Monitors CPU/Ambient thermal levels and triggers L293D motor driver fan via GPIO 22/23.
- **24/7 Reliability:** Managed via Linux `systemd` background daemon for instant auto-recovery post-reboot.
- **Web Telemetry Dashboard:** Integrated Flask web interface displaying live metrics and system states.
- **Phase 2 Modular Integration:** Visual camera event snapshots and Telegram alert notification logic.

## 🛠️ Hardware Stack
- Raspberry Pi 3B+
- L293D Motor Driver Board & Cooling Fan
- Transistor Switching Interface

## 💻 Tech Stack
- Python 3, Flask, HTML5/CSS3
- Linux Systemd Daemon & Bash Scripting

