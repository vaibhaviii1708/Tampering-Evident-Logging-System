# 🔐 Tamper-Evident Logging System

## 🚀 Overview
A secure logging system that ensures logs cannot be modified without detection using hash chaining.

## 🧠 Key Idea
Each log entry stores the hash of the previous log.  
Any change breaks the chain → tampering detected.

## ⚙️ Features
- Add log entries with timestamp and event details  
- Cryptographic hash linking (SHA-256)  
- Detects:
  - Modified logs  
  - Deleted logs  
  - Reordered logs  

## ▶️ Run
```bash
python main.py
```
## Demo
- Normal logs → ✅ Valid
- Modified log → ❌ Tampering detected
## 🔐 Why It Matters
- Simulates real-world audit logging systems used for integrity and accountability.
