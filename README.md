Web Programming with Python and JavaScript

Deze webapplicatie simuleert (een deel van) de online bezorgservice van een pizzarestaurant.
De applicatie omvat registratie, het samenstellen van customizable dishes, een winkelwagen en een orderpagina
Dit project was een opdracht van de Minor Programmeren en is in 2-3 weken uitgevoerd.
In deze opdracht ging het echt om de backend, aan het ontwerp is nauwelijks tijd besteed. Veel tijd is besteed aan het ontwerp en toepassing van de databases, zodat de restauranteigenaar gemakkelijk menuopties kan toevoegen via de admin pagina en de gerechten customizable zijn. 
De applicatie is ontwikkeld in het framework Django.

toelichting belangrijkste bestanden:

__in pizzaapp:__
Models.py bevat al de databases die het complete menu omvatten.
items bestaan uit verschillende subitems, bijvoorbeeld een pizza bestaat uit een bodem, toppings en size.
de winkelwagen bestaat uit items horende bij één specifieke gebruiker.
een order bestaat uit de inhoud vaan een winkelwagen en is definitief.

__views.py__ regelt alle backend logica in de app. 

__ de templates folder zijn de volgende html paginas te vinden:__

__login.html__ 
__register.html__
__failure.html__
__index.html__ - geeft het menu van het restaurant weer
__product.html__ - productpagina, geeft het product met dynamische prijscalculatie.In dezelfde pagina kan het product gecustomized worden (bijv andere toppings)
__shoppingcart.html__ - geeft de winkelwagen van de gebruiker weer. items kunnen worden verwijderd en de totale prijs wordt weergegeven.
__orderplaced.html__ - geeft bevestiging  aan de gebruiker dat de order is geplaatst
__orders.html__ - alleen toegankelijk voor admin, geeft alle orders weer
__template.html__ - de html template voor alle paginas

__navigatie door app:__

Wanneer de gebruiker naar de app navigeert komt hij/zij bij de login page, je kunt vanaf daar ook op register drukken. 
alle andere pagina's zijn alleen toegankelijk wanneer je ingelogd bent.
wanneer de gebruiker registreert wordt er automatisch een unieke shopping cart voor de gebruiker aangemaakt.
vervolgens wordt de gebruiker naar het menu geleid.

Hier kan de gebruiker op de verschillende menu items drukken, waarna hij/ zij een keuze menu krijgt. 
In het keuze menu zijn de specifieke opties horende bij het geklikte item al ingesteld, maar de gebruiker kan deze nog aanpassen.
Daarnaast kan de gebruiker aangeven hoeveel keer hij/zij het specifieke item wilt. De totale prijs wordt doormiddel van Javascript telkens opnieuw berekend, maar wordt daarnaast ook in de backend berekend. Wanneer de gebruiker op Add to Cart drukt wordt het product toegevoegd aan de winkelmand. 

In de winkelmand worden alle items weergegeven en de totale prijs. De gebruiker kan items verwijderen en een order plaatsen. 
waneer de gebruiker een order plaats krijgt hij/zij een melding hiervan en kan hij/zij weer verder winkelen. 

De pagina /orders is alleen toegankelijk voor een superuser. hier kunnen alle geplaatste orders bekeken worden. wanneer een superuser inlogt is deze link ook in de navigatiebar zichtbaar.
