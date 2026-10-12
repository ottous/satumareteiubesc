"""Evenimentele din Satu Mare în terminal, de pe ilovesm.ro.

Folosire:
    python3 evenimente.py                 # weekendul
    python3 evenimente.py today           # azi
    python3 evenimente.py week teatru     # săptămâna asta, doar teatru

Doar biblioteca standard, fără pachete de instalat.
Datele: ilovesm.ro, licența CC BY 4.0.
"""
import json
import sys
import urllib.parse
import urllib.request

perioada = sys.argv[1] if len(sys.argv) > 1 else "weekend"
categorie = sys.argv[2] if len(sys.argv) > 2 else ""

params = {"date": perioada, "per_page": 50, "lang": "ro"}
if categorie:
    params["cat"] = categorie
url = "https://ilovesm.ro/api/events?" + urllib.parse.urlencode(params)

cerere = urllib.request.Request(url, headers={"User-Agent": "exemplu-evenimente-satu-mare"})
with urllib.request.urlopen(cerere, timeout=20) as raspuns:
    rezultat = json.load(raspuns)

if not rezultat.get("ok"):
    sys.exit("Eroare: " + str(rezultat.get("error")))

evenimente = rezultat["data"]["events"]
if not evenimente:
    print("Nu e nimic în agendă pentru perioada asta.")
for ev in evenimente:
    detalii = [ev["date_label"], ev.get("venue_name") or ""]
    if ev.get("is_free"):
        detalii.append("intrare liberă")
    print(ev["title"])
    print("   " + " · ".join(d for d in detalii if d))
    print("   " + ev["url"])
