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

<!--iframe height='265' scrolling='no'
src='https://codepen.io/fbrusch/embed/qagaXE/?height=265&theme-id=0&default-tab=html,result&embed-version=2'
frameborder='no' allowtransparency='true' allowfullscreen='true' style='width:
100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/qagaXE/'>qagaXE</a> by
Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a
href='http://codepen.io'>CodePen</a>. </iframe-->

Ottimo. A parte per il fatto che il link "di startup" rimane costantemente
visibile.

E' possibile farlo sparire, solo tramite css? Non lo so. Mi pare che comunque,
sia piuttosto difficile...

&Egrave; il momento di procurarsi un'altra freccia da scoccare  all'occorrenza:
`javascript`! (sento, silenzioso e ghiacciato, il sudore colarvi lungo la
schiena...)

`javascript` è un linguaggio di programmazione bla bla bla...

Esiste un modo molto potente per manipolare la nostra pagina html renderizzata,
mentre è visualizzata: javascript+jquery!
Prendiamo una pagina semplice, con un solo elemento:

```
<p id="messaggio">Ciao</p>
```

Ora aggiungiamo questa riga _prima_:
```
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js"
```

e questa riga _dopo_:

```
<script> $("#messaggio").fadeOut()</script>
```

(In _codepen_ è più semplice etc.)

Che cosa abbiamo fatto? Abbiamo aggiunto un _tag_ di tipo _script_. Questo _tag_
contiene una istruzione in javascript. Che cosa dice, questa istruzione?

Spezziamola in due parti: `$("#messaggio")` e `fadeOut()`.

`$("#messaggio")` utilizza l'operatore `$` offerto da jquery per individuare un
elemento della nostra pagina. Lo fa utilizzando la stessa notazione del css: in
questo caso l'argomento `"#messaggio"` indica che ci vogliamo riferire all'elemento
che appunto ha `id` uguale a `"messaggio"`.

Una volta che abbiamo specificato un elemento, possiamo inviargli un _segnale_,
che in questo caso si chiama `fadeOut`. La sintassi è quella della _chiamata a funzione_:
`fadeOut()`.

Ecco quello che succede (cliccate su `rerun` in basso a sinistra per rivedere
l'effetto):

<iframe height='265' scrolling='no'
src='https://codepen.io/fbrusch/embed/GjZKGB/?height=265&theme-id=0&default-tab=html,result&embed-version=2'
frameborder='no' allowtransparency='true' allowfullscreen='true' style='width:
100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/GjZKGB/'>GjZKGB</a> by
Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a
href='http://codepen.io'>CodePen</a>. </iframe>

Ci sono altri segnali? Certamente!

Un altro è `css`, che consente di cambiare proprietà di visualizzazione di un
elemento:

```
$("#messaggio").css({"color":"red"})
```

Ecco che succede:

<iframe height='265' scrolling='no' src='https://codepen.io/fbrusch/embed/ZpPzmW/?height=265&theme-id=0&default-tab=result&embed-version=2' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'>See the Pen <a href='http://codepen.io/fbrusch/pen/ZpPzmW/'>ZpPzmW</a> by Francesco Bruschi (<a href='http://codepen.io/fbrusch'>@fbrusch</a>) on <a href='http://codepen.io'>CodePen</a>.
</iframe>

Cosa *non* posso fare con css?

  1. nella fiaba ipertestuale: far sparire il primo link
  2. far comparire sottostorie
  3. certe meccaniche di avanzamento (tipo: lanciare dadi, oppure
sfidare l'abilità dell'utente)

css è dichiarativo: che è cosa buona, ma in questo caso limitante.

Tecnicamente, il css mi dice "dimmi cosa vuoi fare (il risultato che vuoi
ottenere), a come farlo ci penso io".

Ma a volte, non è facile (oppure è proprio impossibile) descrivere in css quello
che voglio. Il mio potere espressivo è limitato, come quando ho un pennello
troppo grande, o mi mancano i colori, oppure le parole (o gli strumenti
espressivi).

3. customizzare il funzionamento dei click
4. manipolare il dom (e a che cazzo mi serve?)

Io vorrei dire: "quando clicco qui sopra, tu sparisci"

Primo esercizio: far sparire il link "iniziale"

cos'è jquery? una libreria che ci semplifica il lavoro!
possiamo considerare singoli elementi tramite l'id, e farci un sacco di cose:

- cambiare proprietà di un elemento (tipo possiamo muovere un elemento agendo su
un elemento relative, agendo su top e left)
- definire azioni quando ci clicchiamo sopra, o altre amenità (click, hover)
- combinare più comandi in funzioni (sai che spasso)
- inserire il tempo! fare cose a distanza di tempo, oppure fare cose ogni tot
tempo...
- possiamo AUTOMATIZZARE, creare meccanismi meravigliosi, che faranno rimanere i
nostri amici a bocca aperta...

Per prima cosa, vogliamo realizzare un semplice gioco da superare per cominciare
con la storia.

alert("ora cambio la classe del titolo")
$("#titolo").toggleClass()

jquery semplifica, usiamolo

javascript + jquery -> possiamo manipolare programmaticamente il dom, ovvero:
API per il dom
