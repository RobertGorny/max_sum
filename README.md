# max_sum
## Aus der Vorlesung: Problem der Maximale Summe

Quelle: [hier](https://elearning.uni-bayreuth.de/pluginfile.php/2415891/mod_resource/content/6/1handout.pdf) (s. Seite 7)

Die Funktion 
```python
  def max_sum(arr):
    // ...
```
aus der Hauptdatei `main.py` erhält als Eingabe ein Array von reellen Zahlen, bzw. Fließkommazahlen, und gibt ein Objekt der Klasse `Solution` (siehe `main.py`) aus, welches folgende Informationen als Attrubute enthält:

* `i`: Der Index der Anfangszahl (startet bei `1`)
* `j`: Der Index der Endzahl (startet bei `1`)
* `sum`: Die Summe von der `i`-ten Zahl (inklusiv) bis zur `j`-ten Zahl (inklusiv)

Die Bedingungen, unter der die Funktion eine solche Ausgabe erzeugt, lauten folgendermaßen: 

* Eingabe `arr` ist ein Array von `n` Fließkommazahlen `(z<sub>1</sub>, ..., z<sub>n</sub)`, `n >= 1`
* Es muss gelten: `0 < i <= j < n`

Die Testdatei `test.py` ist dafür gedacht, die Funktion `max_sum(arr)`  zu testen. Dafür werden für verschiedene Eingaben überprüft, ob die Funktion jeweils eine korrekte Ausgabe erzeugt.

Eine dieser Eingaben ist die aus der Vorlesung bekannte Tabelle:

| z<sub>1</sub> | z<sub>2</sub> | z<sub>3</sub> | z<sub>4</sub> | z<sub>5<sub> | z<sub>6</sub> | z<sub>7</sub> | z<sub>8</sub> | z<sub>9</sub> | z<sub>10</sub>
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -28 | -54 | 88 | -83 | 51 | 56 | -57 | 0 | 82 | -68



## Installation und Verwendung

Um die Tests auf der Maschine auszuführen, müssen sowohl `main.py`, als auch `test.py` in einem gemeinsamen Ordner gespeichert werden und `test.py` muss in diesem Ordner durch folgenden Befehl ausgeführt werden:

```
python3 test.py 
```

Voraussetzung ist, dass Python 3 auf der lokalen Maschine installiert ist.

