# 📦 FritzShark 1.1
#### (c) Paci, 2025

> Lightweight, automated traffic capture tool for AVM Fritz!Box devices.

### 📁 Default Paths

- `~/.config/FritzShark/` – user configuration file (`config.env`)
- `/tmp/fritzcap/` – temporary capture data
- `~/FritzShark/` – default working directory (installation folder)

> 📦 The application runs directly from the folder where it was extracted.  
> You can place it anywhere (e.g. `~/FritzShark/`), no system-wide install is required.

---

### 🛠️ Installation

```bash
tar -xzvf FritzShark-1.1.tar.gz   # where you want to install it
cd FritzShark
chmod +x install.sh
./install.sh
```

> ✅ `install.sh` is the main installer script.  
> It **must be run with user privileges** (do not use `sudo`).  
>  
> The script will ask root privilegie when needed, while keeping user-level configuration files accessible.

---

### ⚙️ Configuration

A file named `config.env` will be created during installation.  
It contains the following default values:

```bash
FRITZBOX_USER=Shark
FRITZBOX_PASS=Shark666
CERT_PATH=
CAPTURE_FILTER=not (port 80 or port 443)
```

> 💡 **Tip**: If you have trouble with capture filters, check the official list:  
> https://wiki.wireshark.org/CaptureFilters

---

### ▶️ Usage

```bash
fritzshark [runtime] [iface]
```

- `runtime` = capture time in seconds (default: `300`)  
- `iface` = interface ID (default: `1-lan`)  
  → The full interface list can be found in https://github.com/jpluimers/fritzcap/blob/master/fritzcap-interfaces-table.md.

---

### ✅ Examples

```bash
fritzshark 120 1-wlan
```
This starts a 2-minute capture on the Wi-Fi interface.

```bash
fritzshark 900 2-1
```
This starts a 15-minute capture on the currently active Internet interface.

---

## 📎 Notes

- You can re-run `install.sh` anytime to reconfigure.  
- All user-specific settings are stored under `~/.config/FritzShark/config.env`  
- Captures are temporarily stored in `/tmp/fritzcap/` and removed automatically.

> 🧹 To uninstall, simply delete the extracted folder and the config file at `~/.config/FritzShark/`.
