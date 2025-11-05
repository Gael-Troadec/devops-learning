#!/usr/bin/env python3
import platform
import datetime

print("=" * 50)
print("✅ WSL2 FONCTIONNE PARFAITEMENT")
print("=" * 50)
print(f"\n📅 Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print(f"💻 OS: {platform.system()}")
print(f"🐍 Python: {platform.python_version()}")
print(f"📂 Dossier: /home/{platform.node()}/devops-learning")
print("\n🚀 Prêt pour mercredi !")
print("=" * 50)
