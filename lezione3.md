# Introduzione a (di) javascript e jquery

## Riassunto delle puntate precedenti


Abbiamo visto come sia possibile strutturare e presentare una storia non-lineare, ipertestuale.

In particolare, utilizzando

1. link ad elementi della pagina
2. css, classi

possiamo creare storie multipagina composte da sezioni, alla fine di ognuna delle quali c'è una scelta, che ci fa saltare ad altre sezioni, e così via...
<script>alert("ciao")</script>
<p data-height="265" data-theme-id="0" data-slug-hash="qagaXE" data-default-tab="html,result" data-user="fbrusch" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/fbrusch/pen/qagaXE/">qagaXE</a> by Francesco Bruschi (<a href="http://codepen.io/fbrusch">@fbrusch</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="http://assets.codepen.io/assets/embed/ei.js"></script>


Cosa *non* posso fare con css?

1. nella fiaba ipertestuale: far sparire il primo link
2. far comparire sottostorie
2. certe meccaniche di avanzamento (tipo: lanciare dadi, oppure
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

javascript + jquery -> possiamo manipolare programmaticamente il dom, ovvero: API per il dom
