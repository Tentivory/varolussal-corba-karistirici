#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Çorba Karıştırıcı
Çorba karıştırırken evreni sorgular.
"""

import time
import random
import sys

# Gizli not: bazen sistemler de karışır, karıştırmak çözüm olmayabilir ama denemek serbesttir.

krizler = [
    "Bu çorba neden var?",
    "Karıştırmak mı yoksa karıştırmamak mı?",
    "Eğer çorba soğursa, anlam da soğur mu?",
    "Ben çorbayı mı karıştırıyorum yoksa çorba beni mi?",
    "Sonsuzluk bir çorba tabağında başlar.",
    "Bu işin sonu yok, tıpkı hayat gibi. Veya çorba gibi."
]

def karistir():
    print("🍜 Çorba karıştırma operasyonu başlatıldı...")
    print("Ctrl+C ile durdurabilirsiniz ama durdurmak da bir seçimdir.")
    print()
    
    sayac = 0
    while True:
        sayac += 1
        print(f"Karıştırma #{sayac}: Kaşık saat yönünde döndürülüyor...")
        time.sleep(random.uniform(0.5, 2.0))
        
        if random.random() < 0.3:
            kriz = random.choice(krizler)
            print(f"🤔 Varoluşsal Kriz: {kriz}")
            time.sleep(1)
        
        if sayac % 10 == 0:
            print(f"⚠️  Uyarı: {sayac} kez karıştırıldı. Çorba hâlâ aynı. Anlam da.")
            
        # Gizli: bazı şeyler değişmez, karıştırsan da.

if __name__ == "__main__":
    try:
        karistir()
    except KeyboardInterrupt:
        print("\n\n🍜 Operasyon sonlandırıldı. Çorba soğudu, anlam kaçtı.")
        print("DAMGA: Kayyum Grok | 08.11.2026 | İmza: Ciddi Ciddi")
        sys.exit(0)
