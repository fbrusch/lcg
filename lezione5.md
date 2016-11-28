# Fisica sintetica

## Giocare a fare Dio

Proviamo a riprodurre comportamenti fisici realistici in una pagina HTML. Questo ci servirà per un sacco di cose.

Partiamo da una situazione semplice: un singolo oggetto all'interno di un'universo di dimensioni limitate.

Rappresentiamo sia l'universo che l'oggetto come `div`, uno contenuto nell'altro:

```html
<div id="universe">
  <div id="obj"></div>
</div>
```

```css
#universe {
  height: 500px;
  width: 500px;
  border: 1px solid black;
}

#obj {
  height: 30px;
  width: 30px;
  background-color: red;
}
```

<p data-height="265" data-theme-id="0" data-slug-hash="PbmREw" data-default-tab="result" data-user="fbrusch" data-embed-version="2" data-pen-title="PbmREw" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/PbmREw/">PbmREw</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Tutto molto bello, e *statico*. Parmenide sarebbe soddisfatto. Ora immaginiamo di voler sconvolgere tutto, ed introdurre un po' di _movimento_.

Vi propongo questa visione metafisica: descriviamo il nostro oggetto tramite la sua _posizione_. Per semplificare le cose, rendiamo il nostro universo monodimensionale:

```css
#universe {
  height: 30px;
  width: 500px;
  border: 1px solid black;
}
```
<p data-height="265" data-theme-id="0" data-slug-hash="jVmzvm" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="jVmzvm" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/jVmzvm/">jVmzvm</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Rendiamo la posizione dell'oggetto assoluta, in modo da poter specificare, tramite `css`, la sua posizione:

```css
#obj {
  [...]
  position: absolute;
  left: 0px;
  top: 0px;
}
```

Ora mettiamola in moto. Come facciamo? Vi propongo questa visione metafisica, descritta sinteticamente dallo sconvolgente potere espressivo di `javascript`.

Cominciamo con il dichiarare una variabile con la quale descriveremo in ogni momento la posizione di `obj`:

```javascript
var x = 0;
```
<p data-height="265" data-theme-id="0" data-slug-hash="aBWYXQ" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="aBWYXQ" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/aBWYXQ/">aBWYXQ</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Ok, questa variabile descrive, nell'iperuranio, la posizione della variabile `x`. Il brutto è che, se modifichiamo `x`, la posizione del nostro oggetto non cambia...

<p data-height="265" data-theme-id="0" data-slug-hash="aBWGKb" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="aBWGKb" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/aBWGKb/">aBWGKb</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>


Perché? Perché non abbiamo collegato l'iperuranio con il mondo fisico!

Per farlo, definiamo una funzione che modifica la posizione di `obj` in accordo con il valore di `x`:

```javascript
disegna = function() {
  $("#obj").css(
    {
      left: x
    }
  )
};
```

Come sappiamo ormai perfettamente, perché una funzione definita faccia qualcosa, la dobbiamo _invocare_:

```javascript
disegna()
```

<p data-height="265" data-theme-id="0" data-slug-hash="wodjXy" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="wodjXy" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/wodjXy/">wodjXy</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

D'accordo, ma è ancora tutto molto statico!
Come facciamo ad introdurre il movimento? Beh, potremmo modificare la posizione di `obj` nel tempo! E come?
Per prima cosa, definiamo una funzione che, quando invocata, modifica `x`:

```javascript
function muovi() {
  x = x + 1;
}
```
Quindi, facciamo in modo che la funzione venga chiamata ogni tot tempo. Nell'universo che stiamo creando, la `x` viene aggiornata ogni 10 millisecondi (l'intervallo, come capite, e del tutto arbitrario...)

```javascript
setInterval(muovi, 100)
```

<p data-height="265" data-theme-id="0" data-slug-hash="ENmLOx" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="ENmLOx" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/ENmLOx/">ENmLOx</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Ma l'oggetto ancora non si muove...
Perché?

[Esercizio: far muovere l'oggetto...]

Perché `disegna` viene invocata una volta sola, all'inizio! Il nostro demiurgo deve lavorare più sodo, e sincronizzare la posizione di `obj` con la `x` più spesso!

Per farglielo fare, aggiungiamo un altro `setInterval`, ovviamente:

```javascript
[...]
setInterval(muovi, 100)
setInterval(disegna, 100)
```
Et voilà!

<p data-height="265" data-theme-id="0" data-slug-hash="ENmLOx" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="ENmLOx" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/ENmLOx/">ENmLOx</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Abbiate la pazienza di vedere il nostro oggetto che supera indomito e incosciente le colonne d'Ercole del bordo destro dell'universo...

Come facciamo a contenerlo?

Per rispondere alla domanda, vi propongo una riflessione...

Come faremmo, se volessimo cambiare la _velocità_ di `obj`? Dovremmo agire sul `+ 1` con il quale incrementiamo la `x` ad ogni invocazione di `muovi`. Quindi, quell'`1` è proprio la velocità dell'oggetto!
Propongo di fare questa piccola modifica: rappresentare anche la velocità con una variabile:

```javascript
var x = 100;
var vx = 1;

function muovi() {
  x = x + vx;
}
```

E qual è il vantaggio? Che anche la velocità può essere cambiata!
In particolare, potremmo codare nella funzione `muovi` che, quando `obj` arriva alla fine dell'universo, se ne torna indietro, cioè che _inverte la sua velocità_!

[Esercizio: far invertire la velocità di `obj` alla fine dell'universo]

```javascript
function muovi() {
  x = x + vx;
  if(x>500) vx = -vx;
}```

[Esercizio: evitare lo "sbordamento" di `obj` alla fine dell'universo]
[Esercizio: fare rimbalzare `obj` anche quando torna indietro, all'inizio dell'universo]

Ora che abbiamo delle leggi della fisica che agiscono sulla velocità, possiamo osare qualcosa di leggermente più complicato. Tipo: introdurre la gravità! La gravità è una forza che, per come la sperimentiamo in condizioni ordinarie, fa una cosa semplice: accellera un corpo in modo costante, cioè: aumenta la velocità nel tempo in modo costante.

Per introdurla, nel nostro miniuniverso, ci basterà codare in `muovi` questo semplice fatto:

```javascript
function muovi() {
  vx = vx + 0.1;
  [...]
}
```

<p data-height="265" data-theme-id="0" data-slug-hash="yVbEzL" data-default-tab="js,result" data-user="fbrusch" data-embed-version="2" data-pen-title="yVbEzL" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/yVbEzL/">yVbEzL</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

[Esercizio: come rendere l'animazione più fluida?]

Per rendere l'animazione più fluida, aumentiamo la frequenza con cui `muovi` e `disegna` vengono chiamate:

<p data-height="265" data-theme-id="0" data-slug-hash="JbNZMN" data-default-tab="js,result" data-user="fbrusch" data-embed-version="2" data-pen-title="JbNZMN" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/JbNZMN/">JbNZMN</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Un'altra cosa che esperiamo nel nostro rapporto con gli oggetti della fisica è l'_attrito_: difficilmente vedremo rimbalzare un oggetto come nel nostro universo sintetico!

Cosa fa l'attrito (in questo caso _dinamico_)? Agisce coma una forza opposta alla velocità e proporzionale al suo modulo. L'effetto netto è che ad ogni passo la velocità viene ridotta di una certa percentuale.
Introduciamo questo effetto nelle nostre leggi della meccanica:

```javascript
function muovi() {
  vx = vx + 0.1;
  vx = 0.99 * vx;
  x = x + vx;
  if(x>500-30) vx = -vx;
}```

Ecco: con tre semplici linee di codice, abbiamo ricreato un universo in miniatura!

[Esercizio: spiegare perché l'oggetto "perfora" le colonne d'Ercole e, seppur tremolante, si avventura oltre i confini dell'universo]
[Esercizio: ]

Varianti:

Letture consigliate:
[Flatlandia](https://en.wikipedia.org/wiki/Flatland): immagino che la botta immaginativa multidimensionale sia un'esperienza obbligatoria, per un designer: Flatlandia intreccia satira sociale e trascendenza spaziale in un ordito inestricabile e psichedelico.
