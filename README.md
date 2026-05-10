# SSDD-CCA
Syeda Alishba Liaquat CR-19
Uzma Haneef CR-20
Sarah Zafar CR-25
Hashem CR-50
This repository contains two versions of the same Flask blog application:

- `vulnerable-version/` — intentionally insecure version
- `fixed-version/` — patched version with the vulnerabilities removed

It also includes helper scripts used for the demo:

- `scripts/listener.py` — receives stolen token data during the XSS demo
- `scripts/forged.py` — generates a forged JWT for the API demo
- `scripts/payload.ps1` — sends API requests from PowerShell

## Security issues demonstrated

1. Stored XSS
2. JWT token theft / misuse
3. Broken Object Level Authorization (BOLA / IDOR)
4. Fixed version blocking the same attack chain

---

## Requirements

- Python installed
- PowerShell on Windows
- The Python packages required by the app

Example:

```powershell
pip install flask flask-login flask-bcrypt flask-mail pyjwt bleach
