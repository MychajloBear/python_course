# Übung: Baue deine eigene Streamlit-Datenanalyse-App
**Zeitrahmen: ca. 90 Minuten | Einzel- oder Partnerarbeit**

## Ziel
Ihr habt heute Streamlit anhand des DAX-Projekts kennengelernt. Jetzt seid ihr dran: Baut eine **eigene kleine Analyse-App** mit einem neuen Datensatz. Es geht nicht darum, alles perfekt zu machen – sondern darum, die Bausteine aus der Session an einem unbekannten Datensatz selbst anzuwenden.

---

## Schritt 1: Datensatz wählen (5 Min)
Sucht euch **einen** der folgenden Datensätze aus. Alle sind direkt über eine Python-Bibliothek verfügbar, ihr müsst also nichts herunterladen.

### Option A – Palmer Penguins 🐧 (einsteigerfreundlich)
Körpermaße von drei Pinguin-Arten auf drei Inseln.
```python
import seaborn as sns
df = sns.load_dataset("penguins")
```
Spalten u.a.: `species`, `island`, `bill_length_mm`, `body_mass_g`, `sex`

### Option B – Titanic 🚢 (viele kategoriale Filter)
Passagierdaten der Titanic inkl. Überlebensstatus.
```python
import seaborn as sns
df = sns.load_dataset("titanic")
```
Spalten u.a.: `survived`, `pclass`, `sex`, `age`, `fare`, `embark_town`

### Option C – Gapminder 🌍 (Zeitreihen, für Fortgeschrittene)
Lebenserwartung, BIP und Bevölkerung pro Land und Jahr.
```python
import plotly.express as px
df = px.data.gapminder()
```
Spalten u.a.: `country`, `continent`, `year`, `lifeExp`, `gdpPercap`, `pop`

> `seaborn` bzw. `plotly` ggf. vorher installieren: `pip install seaborn plotly`

---

## Schritt 2: Pflichtaufgaben (ca. 60 Min)
Eure App muss am Ende **alle** der folgenden Punkte erfüllen:

- [ ] **Grundgerüst**: eigene `main.py`, `st.set_page_config()`, ein Titel/Header, der beschreibt worum es geht
- [ ] **Daten laden mit Caching**: Ladefunktion mit `@st.cache_data`
- [ ] **Mindestens 2 Filter-Widgets in der Sidebar** (z.B. `selectbox`, `multiselect`, `pills` oder `slider`), die die Daten einschränken – z.B. nach Kategorie, Zeitraum oder Wertebereich
- [ ] **Mindestens 1 Diagramm**, das sich automatisch aktualisiert, wenn die Filter geändert werden (`st.pyplot`, `st.line_chart` oder `st.bar_chart`)
- [ ] **Rohdaten optional anzeigen**: ein `st.toggle()`, das die gefilterte Tabelle ein-/ausblendet
- [ ] **Seitenstruktur**: nutzt `st.columns()` **oder** `st.tabs()`, um die App übersichtlich zu gliedern (z.B. Graph links, Kennzahlen rechts)

**Tipp:** Baut in genau dieser Reihenfolge – erst Daten laden, dann Filter, dann Diagramm, dann Feinschliff. So habt ihr nach jedem Schritt eine lauffähige App.

---

## Schritt 3: Bonusaufgaben (Restzeit, wenn ihr durch seid)
Wählt aus, was euch interessiert – keine Pflicht, aber gute Übung:

- [ ] **Kennzahlen berechnen**: zeigt zusätzlich Mittelwert, Median oder Standardabweichung einer Spalte an (in einem eigenen Tab, wie im DAX-Projekt)
- [ ] **`st.popover()`** für die Filter-Einstellungen nutzen, statt alles direkt in die Sidebar zu packen
- [ ] **`st.session_state`**: baut einen "Merkliste"-Button, der eine ausgewählte Kategorie in einer Liste speichert, die über Reruns hinweg erhalten bleibt
- [ ] **Theme anpassen**: eigene `.streamlit/config.toml` mit einem selbstgewählten Farbschema
- [ ] **Zweite Seite**: legt einen `pages/`-Ordner an und baut eine zweite, einfache Unterseite (z.B. mit einem anderen Diagrammtyp)

---

## Checkliste zum Abschluss
Bevor ihr fertig seid, testet:
1. Startet die App neu (`streamlit run main.py`) – läuft sie fehlerfrei durch?
2. Ändert ihr eure Filter – reagiert das Diagramm korrekt?
3. Ist ohne jegliche Auswahl (z.B. leere `multiselect`) klar erkennbar, was zu tun ist (kein Absturz, evtl. Hinweistext wie im DAX-Projekt: *"Wähle Aktien aus der Sidebar aus…"*)?

## Für die nächste Session
Bringt eure App (oder zumindest den Code) mit – wir schauen uns kurz ein paar Ergebnisse gemeinsam an und besprechen, wo unterschiedliche Lösungswege gewählt wurden.
