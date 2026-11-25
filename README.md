# LUMAR Watches — website

Live op https://lumarbusiness.github.io/lumar-website/

- `index.html` is de complete website (één bestand). GitHub Pages zet elke wijziging automatisch online.
- `bron/src.html` is de broncode zonder ingevoegde foto's; `bron/img/` bevat de demofoto's.
  Na een wijziging in `bron/src.html`: `python3 bron/build.py` maakt een nieuwe `index.html`.
- De voorraad, aanbiedingen, zoekopdrachten en status komen live uit de LUMAR-app (Supabase).
