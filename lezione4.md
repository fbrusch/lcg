# Flapping birds

Oggi vogliamo arrivare qui:

<p data-height="265" data-theme-id="0" data-slug-hash="xRxybr" data-default-tab="js,result" data-user="fbrusch" data-embed-version="2" data-pen-title="xRxybr" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/xRxybr/">xRxybr</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Partiamo realizzando un semplice contatore: un oggetto che conta quante volte gli clicchiamo sopra.

Per prima cosa nell'html creiamo un oggetto mostri il numero:

```html
<div id="numero">0</div>
```

Diamogli un po' di stile:

```css
#numero {
  font-size: 60px;
  border: 3px solid black;
  font-family:monospace;
  height:70px;
  display:inline-block;
}
```

Ok, ora diamo vita all'oggetto. Cosa vogliamo? Che ogni volta che
ci clicchiamo sopra, questo aumenti il valore di 1. Per farlo, introduciamo le _variabili_! Possiamo vedere le variabili come dei contenitori di valori con un nome. Un esempio vale più
di mille parole:

```javascript
var x = 42;
```

In questo esempio, ho _dichiarato_ una variabile: possiamo pensare la
a questa dichiarazione come alla creazione di un contenitore di nome `x`.
Oltre a creare `x`, gli ho anche assegnato ("messo dentro") un valore, `42`.
Fantastico, e ora che me ne faccio?
Beh, per esempio posso usare `x` come argomento di un'`alert`:

```javascript
alert(x);
```

Inoltre, posso cambiare il valore contenuto in `x`:

```javascript
x = 10;
alert(x);
```

Posso anche cambiare il valore di una variabile _relativamente_ al suo
valore attuale:

```javascript
x = x + 1;
```

La cosa interessante è che anche le funzioni possono usare le variabili:

```javascript
incrementa_x = function() {
  x = x + 1;
}
```

Se chiamo `incrementa_x`, non soprendentemente, `x` aumenta di `1`.

```javascript
incrementa_x();
```

Ok, abbiamo quasi tutto quello che ci serve per finalizzare il nostro contatore.
L'ultimo ingrediente è contettualmente banale: un segnale jquery con cui possiamo cambiare il testo: `text`.

Quindi: scriviamo una funzione che incrementa `x` e che scrive il valore di `x` nell'elemento `#numero`, e diciamo a `#numero` di invocarla ad ogni click:

```javascript
x = 0

incrementa = function() {
  x = x+1;
  $("#numero").text(x)
}

$("#numero").click(incrementa)
```

Ecco il risultato, fino a questo punto:

<p data-height="265" data-theme-id="0" data-slug-hash="NbPgdb" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="NbPgdb" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/NbPgdb/">NbPgdb</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Esercizio: modifica il codice in modo che il numero sia rappresentato, invece
che "testualmente", tramite la lunghezza di una barra.
(suggerimento: create un `<div>` con un certo `background-color`, e giocate sulla `width`).
Una possibile soluzione la trovate

[qui](http://codepen.io/fbrusch/pen/rWaGmW).

E se invece volessimo fare un contatore temporizzato, che aumenta automaticamente?

Potremmo avvalerci di un paio di notevoli funzioni che ci vengono fornite:
`setTimeout` e `setInterval`.

`setTimeout` consente di chiamare una funzione, ma nel futuro!

Esempio: questa chiamata a funzione:

```javascript
setTimeout(incrementa_x, 1000)
```

significa: "tra 1000 millisecondi (cioè tra un secondo), per favore chiama la funzione incrementa_x"

Ora prendiamo questa sequenza di istruzioni:

```javascript
setTimeout(incrementa_x, 1000)
setTimeout(incrementa_x, 2000)
setTimeout(incrementa_x, 3000)
```

Attenzione: le tre istruzioni vengono eseguite una dopo l'altra, immediatamente, senza aspettare il tempo di timeout di ciascuna. Ogni chiamata "si segna" da qualche parte che tra un certo tempo dovrà fare qualcosa, e poi si prosegue con l'istruzione seguente (tecnicamente, si dice che setTimeout non è _bloccante_, oppure anche che è _asincrona_).

Se volessimo far continuare il contatore fino a 100, o a 1000, cosa dovremmo fare? Mettere 100 o 1000 chiamate a `setTimeout`?
Ovviamente no! Ci sono un paio di sistemi che possiamo utilizzare.
Il primo è uno dei _trucchi_ più potenti e devastanti dell'informatica, che fa deragliare da decenni le coscienze degli studenti più sensibili. Quindi, tenetevi forte! Ve lo propongo così, a crudo, in tutto il suo diabolico splendore:

```javascript
var x = 0;

incrementa_per_sempre = function() {
  x = x+1;
  $("#numero").text(x)
  setTimeout(incrementa_per_sempre, 1000)
}

incrementa_per_sempre()
```

<p data-height="265" data-theme-id="0" data-slug-hash="MbYEvy" data-default-tab="js,result" data-user="fbrusch" data-embed-version="2" data-pen-title="MbYEvy" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/MbYEvy/">MbYEvy</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Il trucco è fare in modo che la funzione di incremento, prima di terminare,
programmi di richiamare sé stessa, in questo caso dopo un secondo!
Prendetevi qualche minuto per rifletterci, e vedrete che la cosa ha senso...

L'altro sistema è utilizzare `setInterval`, un'altra funzione fornita da javascript`.
`setInterval` significa
"chiama questa funzione ogni tot tempo, a partire da ora".

In questo caso, per far avanzare indefinitamente il nostro contatore,
ci basterà questa istruzione:

```javascript
setInterval(incrementa_x, 1000)
```

Esercizio: realizza un contatore che incrementa automaticamente ogni secondo,
e che decrementa di uno quando ci si clicca sopra.
Soluzione: http://codepen.io/fbrusch/pen/eBmeVK

## Scelte

Immaginiamo di voler fare qualcosa quando il contatore arriva ad un certo
valore... per esempio, vogliamo visualizzare un messaggio.
Vorremmo poter mettere nella funzione un'istruzione del tipo "se x vale 20,
alert('ciao')".
Vogliamo cioè che venga eseguita un'istruzione solo se una certa _condizione_
è vera. Questo è possibile con i _costrutti condizionali_, dei quali il più
fondamentale è l'`if-else`.
Come al solito, due righe di codice valgono 1000 parole:

```javascript
incrementa_x = function() {
  x = x+1;
  if(x==20) {alert("e con questo sono 20!")}
  $("#numero").text(x)
}
```
<p data-height="265" data-theme-id="0" data-slug-hash="MbYOPG" data-default-tab="result" data-preview="true" data-user="fbrusch" data-embed-version="2" data-pen-title="MbYOPG" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/MbYOPG/">MbYOPG</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

## Birds

Ok, abbiamo tutti gli strumenti concettuali per costruire il nostro minigioco.

Partiamo costruendo il campo (il cielo). Cerchiamo un'immagine che ci piaccia,
segnamoci l'url e mettiamolo come sfondo di un `div`:

```html
<div id="sky"></div>
```

```css
#sky {
  background-image:url("http://orig15.deviantart.net/e5c9/f/2008/046/d/f/clouds___high_speed_pixel_art_by_harunaakatsuki.gif");
  height:100vh;
  background-size:cover;
}
```

<p data-height="265" data-theme-id="0" data-slug-hash="GNgObN" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="Birds1" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/GNgObN/">Birds1</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Ok, ora popoliamo il cielo. Anche il nostro uccellino sarà un `div` con
l'immagine che vogliamo come sfondo.

```html
<div id="sky">
  <div id="bird"></div>
</div>
```

```css
#bird {
  position: absolute;
  background-image:url("http://4.bp.blogspot.com/-K4EwEffuk5Q/VTVBf8Wq-8I/AAAAAAAACZ0/IYLT3b-Xkko/s1600/flappybird.png");
  height:200px;
  width:300px;
  background-size:cover;
  image-render:pixelated;
}
```

Facciamo attenzione alla proprietà `position`, settata ad `absolute`: questo
fa sì che potremo specificare, tramite le proprietà `top` e `left`, la posizione
del nostro oggetto all'interno dell'elemento contenitore. Agendo su queste
proprietà potremo muovere il nostro uccellino!

<p data-height="265" data-theme-id="0" data-slug-hash="aBzVgr" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="Birds2" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/aBzVgr/">Birds2</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Ok, ora facciamolo muovere. Partiamo con una meccanica semplice: ogni 500 millisecondi due variabili `x` e `y` vengono cambiate casualmente, e le coordinate `left` e `top` dell'uccellino cambiate di conseguenza.

Per generare le posizioni casuali, usiamo `Math.random`:

```javascript

var x = 0;
var y = 0;

move_bird = function() {
  x = Math.random()*1000;
  y = Math.random()*500;
  $("#bird").animate({
    top:y,
    left:x
  },500)
}

setInterval(move_bird, 500)
```

<p data-height="265" data-theme-id="0" data-slug-hash="qqEpEB" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="Birds2" data-preview="true" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/qqEpEB/">Birds2</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Esercizi:

  1. Fai in modo quando si becca l'uccellino compaia un messaggio
     (per esempio tramite `alert`)
  2. Introdurre un numero massimo di tentativi: dopo 3 tentativi in cui non
     si colpisce l'uccellino, far comparire un altro messaggio


## Sprite

Ok, ora rilassiamoci con un'impresa tipicamente da designer: facciamo sbattere le ali al nostro uccellino! Cominciamo con una questione di leggerezza parmenidea: che cos'è il movimento?
Immaginiamo quello che Zenone tendeva ad escludere, (ma i fratelli Lumiere no!): che il movimento sia una successione di stati diversi in istanti successivi. Procuriamoci gli stati dell'uccellino nel suo regale battere d'ali, tutti nella stessa immagine:

<p data-height="265" data-theme-id="0" data-slug-hash="VmYyXp" data-default-tab="result" data-preview="true" data-user="fbrusch" data-embed-version="2" data-pen-title="VmYyXp" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/VmYyXp/">VmYyXp</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Abbiamo dimesionato il `div` di classe `flapping-bird` in modo da "inquadrare" soltanto il primo frame del battito. Ora faremo in modo di far "spostare" nel tempo l'inquadratura sugli altri frame. Per fare questo utilizziamo le animazioni css. &Egrave; semplicissimo!
Per prima cosa, si definisce l'animazione, con il costrutto "@keyframes":

```css
@keyframes flap {
    0% {background-position: 0px 0px;}
    100% {background-position: 0px -184px;}
}
```

Quindi, si indica che questa animazione verrà usata nella class `flapping-bird`:

```css

.flapping-bird {
  [...]
  animation: flap 0.5s infinite;
}
```

Ecco il risultato:

<p data-height="265" data-theme-id="0" data-slug-hash="jVEYXJ" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="jVEYXJ" data-preview="true" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/jVEYXJ/">jVEYXJ</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

C'è qualcosa che non va! Non vogliamo che l'inquadratura scorra da un frame all'altro, vogliamo che uno scompaia e che l'altro appaia! Possiamo ottenere questo risultato utilizzando il modificatore `steps` nell'animazione, che dice di spezzare l'animazione in un certo numero di passi discreti:

```css

  [...]
  animation: flap 0.5s infinite steps(2);
  [...]
```

Ora forse va meglio:
<p data-height="265" data-theme-id="0" data-slug-hash="bBNaZQ" data-default-tab="css,result" data-user="fbrusch" data-embed-version="2" data-pen-title="bBNaZQ" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/bBNaZQ/">bBNaZQ</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

Esercizi:

  1. modifica il css in modo da sfruttare tutti e tre i frame
  2. trasporta il flapping bird animato nel gioco
