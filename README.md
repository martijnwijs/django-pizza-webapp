Web Programming with Python and JavaScript

Deze webapplicatie simuleert (een deel van) de online bezorgservice van een pizzarestaurant.
Dit project was een opdracht van de Minor Programmeren en is in 2-3 weken uitgevoerd.

De applicatie is ontwikkeld in het framework Django.


navigatie door app:

Wanneer de gebruiker naar de app navigeert komt hij/zij bij de login page, je kunt vanaf daar ook op register drukken. 
alle andere pagina's zijn alleen toegankelijk wanneer je ingelogd bent.
wanneer de gebruiker registreert wordt er automatisch een unieke shopping cart voor de gebruiker aangemaakt.
vervolgens wordt de gebruiker naar het menu geleid.

hier kan de gebruiker op de verschillende menu items drukken, waarna hij/ zij een keuze menu krijgt. 
In het keuze menu zijn de specifieke opties horende bij het geklikte item al ingesteld, maar de gebruiker kan deze nog aanpassen.
daarnaast kan de gebruiker aangeven hoeveel keer hij/zij het specifieke item wilt. De totale prijs wordt doormiddel van Javascript telkens opnieuw berekend, maar wordt daarnaast backend ook berekend. Wanneer de gebruiker op Add to Cart drukt wordt het product toegevoegd aan de winkelmand. 

in de winkelmand worden alle items weergegeven en de totale prijs. De gebruiker kan items verwijderen en een order plaatsen. 
waneer de gebruiker een order plaats krijgt hij/zij een melding hiervan en kan hij/zij weer verder winkelen. 

de pagina /orders is alleen toegankelijk voor een superuser. hier kunnen alle geplaatste orders bekeken worden. wanneer een superuser inlogt is deze link ook in de navigatiebar zichtbaar.
