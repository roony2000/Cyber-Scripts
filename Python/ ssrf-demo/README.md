# 🔐 SSRF Vulnerability Demo

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Platform](https://img.shields.io/badge/Platform-TryHackMe-red)
![Language](https://img.shields.io/badge/Language-Python-blue)

## 📌 Overview
Educational project demonstrating SSRF (Server-Side Request Forgery) 
attack and defense using Python Flask.

## 📁 Structure


ssrf-demo/
├── vulnerable/app.py   ← Exploitable version
└── secure/app.py       ← Protected version

## 🎯 Attack Examples Tested
| Attack | Result |
|--------|--------|
| http://127.0.0.1:5000 | ✅ Internal access |
| http://127.0.0.1:22 | ✅ SSH port exposed |
| https://external-url | ✅ Server used as Proxy |

## 🛡️ Defenses Implemented
- ✅ Allow List (whitelist domains only)
- ✅ Block private IP ranges
- ✅ DNS resolution check
- ✅ Scheme validation
- ✅ Disable redirects

## ▶️ Run
pip install flask requests
python3 vulnerable/app.py   # Port 5000
python3 secure/app.py       # Port 5001

