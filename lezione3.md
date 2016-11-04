# Introduzione a (di) javascript e jquery

## Riassunto delle puntate precedenti


Abbiamo visto come, utilizzando un minimo di elementi `HTML` e di `css` sia
possibile strutturare e presentare una storia non-lineare, ipertestuale.

In particolare, abbiamo utilizzato:

  - link (tag `<a>`) ad elementi della pagina, identificati dalla proprietà
    `id`. Es:

```

<div id="inizio">
  C'era una volta...

</div>

```

  - css, classi

Il trucco che abbiamo usato è:

  - racchiudiamo le unità narrative in `<div>` di appartenenti ad una classe,
    (es: `<div class="section">`)

  - alla fine di ogni segmento, esprimiamo le scelte che decideranno il flusso
    della narrazione con una lista di link alternativi:

```
<div id="inizio" class="section">
  C'era una volta ...
  <ul>
    <li>
      <a href="#regina_si_punge"
        La regina si punse.
      </a>
    </li>
    <li>
      <a href="#regina_non_si_punge"
        La regina, non si punse.
      </a>
    </li>

  </ul>
</div>
```
  - nel css, diamo una regola che nasconde di default le classi:

```
.section {display: none}
```

  - aggiungiamo una regola che renda visibile un oggetto di classe `section`
  quando ci "saltiamo sopra" seguendo un link:

```
.section:target {display: block}

```

In questo modo, otteniamo l'effetto di mostrare soltanto la sezione alla quale
siamo "saltati" per ultimi. Ovviamente, c'è un problema: visto che inizialmente
nessuna sezione è nello stato `:target`, appena caricata la pagina non si vedrà
niente! Il problema è presto risolto con un'accortezza: un link iniziale, non
appartenente ad alcuna sezione, che "punta" alla prima sezione della storia:

```
<a href="#incipit">Cominciamo...</a>
```

Nel _codepen_ qui sotto vedete l'effetto complessivo.

<iframe height='265' scrolling='no'
src='https://codepen.io/fbrusch/embed/qagaXE/?height=265&theme-id=0&default-tab=html,result&embed-version=2'
frameborder='no' allowtransparency='true' allowfullscreen='true' style='width:
100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/qagaXE/'>qagaXE</a> by
Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a
href='http://codepen.io'>CodePen</a>. </iframe>

Ottimo. A parte per il fatto che il link "di startup" rimane costantemente
visibile.

E' possibile farlo sparire, solo tramite css? Non lo so. Mi pare che comunque,
sia piuttosto difficile...

Cos'altro *non* posso fare con css?

  1. far comparire sottostorie
  2. certe meccaniche di avanzamento (tipo: lanciare dadi, oppure
sfidare l'abilità dell'utente)
  3. customizzare il funzionamento dei click
  4. cambiare la pagina dinamicamente (tipo, aggiungendo o togliendo elementi),
     a seconda di quello che "succede"

Tecnicamente, il css mi dice "dimmi cosa vuoi fare (il risultato che vuoi
ottenere), a come farlo ci penso io".

Ma a volte, non è facile (oppure è proprio impossibile) descrivere in css quello
che voglio. Il mio potere espressivo è limitato, come quando ho un pennello
troppo grande, o mi mancano i colori, oppure le parole (o gli strumenti
espressivi).

Per esempio, io vorrei poter dire, ad un elemento: "quando clicco qui sopra,
tu sparisci".

&Egrave; il momento di procurarsi un'altra freccia da scoccare  all'occorrenza:
`javascript`! (sento, silenzioso e ghiacciato, il sudore colarvi lungo la
schiena...)

Per fare questo utilizzeremo `jquery`.

Cos'è `jquery`? Una libreria che ci semplifica il lavoro...
Con essa ossiamo considerare singoli elementi tramite l'id, e farci un sacco di cose:

- cambiare proprietà di un elemento (tipo possiamo muovere un elemento agendo su
un elemento relative, agendo su top e left)
- definire azioni quando ci clicchiamo sopra, o altre amenità (click, hover)
- combinare più comandi in funzioni (sai che spasso)
- inserire il tempo! fare cose a distanza di tempo, oppure fare cose ogni tot
tempo...
- possiamo AUTOMATIZZARE, creare meccanismi meravigliosi, che faranno rimanere i
nostri amici a bocca aperta...


Prendiamo una pagina semplice, su codepen, con un solo elemento:

```html
<p id="messaggio">Ciao</p>
```

Nella finestra "js", clicchiamo sull'icona di configurazione e aggiungiamo
`jQuery` tra i file.

Nell'editor `js` di codepen, scriviamo.

```javascript
$("#messaggio").fadeOut()
```
<iframe height='265' scrolling='no' src='https://codepen.io/fbrusch/embed/wzOXyE/?height=265&theme-id=0&default-tab=html,result&embed-version=2' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/wzOXyE/'>wzOXyE</a> by Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a href='http://codepen.io'>CodePen</a>.
</iframe>

Visto che succede? Il paragrafo con id `messaggio` sparisce!

Come è fatta l'istruzione in javascript/jQuery?

Spezziamola in due parti: `$("#messaggio")` e `fadeOut()`.

`$("#messaggio")` utilizza l'operatore `$` per individuare un elemento della nostra pagina. Lo fa utilizzando la stessa notazione del css: in
questo caso l'argomento `"#messaggio"` indica che ci vogliamo riferire all'elemento
che appunto ha `id` uguale a `"messaggio"`.

Una volta che abbiamo specificato un elemento, possiamo inviargli un _segnale_ (anche detto _metodo_),
che in questo caso si chiama `fadeOut`. La sintassi è quella della _chiamata a funzione_:
`fadeOut()`.

Ci sono altri segnali? Certamente!

Un altro è `css`, che consente di cambiare proprietà di visualizzazione di un
elemento:

```
$("#messaggio").css({"color":"red"})
```

<iframe height='265' scrolling='no' src='https://codepen.io/fbrusch/embed/ZpPzmW/?height=265&theme-id=0&default-tab=result&embed-version=2' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/ZpPzmW/'>ZpPzmW</a> by Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a href='http://codepen.io'>CodePen</a>.
</iframe>

Per ora, mandare segnali agli oggetti non è una cosa di originalità devastante: tutto quello che abbiamo fatto avremmo potuto farlo con regole css!

Ora però immaginiamo di voler fare succedere qualcosa (la scomparsa di un elemento) tipo quando gli clicchiamo sopra. Questo in css non è facile (dobbiamo sbatterci con :target, link id etc).

In javascript la cosa è semplice! Ci serve solo un ulteriore strumento: le funzioni (sento il sudore ghiacciare definitivamente...)

Cos'è una funzione? Per ora è una sequenza di comandi raggruppati, che possiamo eseguire come vogliamo! Facciamo subito un esempio:

```javascript

function saluta() {
  alert("ciao");
  alert("a tutti");
}
```

Abbiamo definito la funzione `saluta`. D'ora in poi, possiamo invocare la funzione, in questo modo:

```javascript
saluta()
```

Quello che succede è che, quando viene invocata la funzione, le istruzioni
che abbiamo specificato nella definizione vengono eseguite.

Ed eccoci al punto cruciale: è possibile legare il verificarsi di un evento
(ad esempio il click su un'elemento) all'invocazione di una funzione.

```html
<p id="clickme">Cliccami</p>
```

```javascript
$("#clickme").click(saluta);
```

<iframe height='265' scrolling='no' title='GNRBGj' src='https://codepen.io/fbrusch/embed/GNRBGj/?height=265&theme-id=0&default-tab=result&embed-version=2' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/GNRBGj/'>GNRBGj</a> by Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a href='http://codepen.io'>CodePen</a>.
</iframe>

Finalmente possiamo risolvere il problema da cui siamo partiti: far sparire
il link di startup iniziale. Basterà collegare il suo evento di click ad una
funzione che lo faccia scomparire.

Per farlo, ci basta:

  1. dare un id al link iniziale (per esempio, "startup")
  2. definire una funzione che faccia scomparire il link iniziale:
     ```javascript
     svanisce_startup = function () {
       $("#startup").fadeOut()
     }
     ```
  3. collegare l'evento di click sul link alla sua sparizione:
     ```javascript
     $("#startup").click(svanisce_startup)
     ```

<iframe height='265' scrolling='no' title='rWNrqP' src='https://codepen.io/fbrusch/embed/rWNrqP/?height=265&theme-id=0&default-tab=html,result&embed-version=2' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/rWNrqP/'>rWNrqP</a> by Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a href='http://codepen.io'>CodePen</a>.
</iframe>

Ci sono altri messaggi interessanti:

  - `hover`: lega l'evento di passaggio del puntatore su un elemento ad una
funzione
  - `animate`: è come `css`, ma consente di animare la transizione

In generale, [qui](http://api.jquery.com/) trovate tutti i segnali che si
possono inviare ad un elemento.
