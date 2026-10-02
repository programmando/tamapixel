# TamaPixel 🥚

Un cucciolo virtuale in pixel, ispirato ai Tamagotchi degli anni '90.
È una **web app** (PWA): si apre nel browser e sull'iPhone si installa nella schermata Home come una vera app.

## Come si gioca

- Tocca le icone sullo schermo, oppure usa i tasti come l'originale: **A** scorre, **B** conferma, **C** annulla.
- Vive in tempo reale: ha fame, si annoia, fa la cacca, si ammala e la sera va a nanna (anche ad app chiusa).
- Cresce: uovo → Pallino → Antennino → Ciuffetto → adulto. Che adulto diventa dipende da come lo curi.
- Le regole complete sono nel pulsante **?** dentro l'app.

## Provarlo sul PC

```
python serve.py
```

Poi apri http://localhost:8123 nel browser.
Per aprirlo anche dall'iPhone sulla stessa rete Wi-Fi: `python serve.py --lan`.

## Installarlo sull'iPhone

Apri l'indirizzo del sito con **Safari** → **Condividi** → **Aggiungi alla schermata Home**.

## I file

| File | A cosa serve |
|---|---|
| `index.html` | tutta l'app: grafica, regole del gioco, animazioni e suoni |
| `manifest.webmanifest` | nome e icone per installarla come app |
| `sw.js` | la fa funzionare anche senza internet |
| `icon-180.png`, `icon-512.png` | le icone |
| `serve.py` | mini server per provarla sul PC |

Il cucciolo viene salvato solo sul telefono: nessun dato viene inviato altrove.
