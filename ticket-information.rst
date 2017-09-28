Ticketinformationen
====================
Innerhalb jedes Tickets können Informationen zum Ticket, Kunden und der Organisation hinterlegt und bearbeitet werden. 

Nach Klick auf das Nachrichten-Icon auf der rechten Seite werden Detailinformationen des Tickets eingeblendet:

.. image:: images/gettingstarted/Abb20-Ticket-Informationen.jpg

Bei entsprechenden Benutzerrechten können in diesem Schritt die Gruppe, der Besitzer, der Status und die Priorität geändert werden. Doch was bedeuten diese Eingaben?

Gruppe
----------
Die Tickets gelangen über verschiedene Kanäle ins Zammad und sind durch verschiedene Regeln nach Gruppen sortiert.
Gruppen sind im Zammad wie Arbeitsgruppen zu verstehen, die sich innerhalb eines Unternehmens mit verschiedenen Themen beschäftigen. Die für das Sales-Team relevanten Tickets sind z. B. in der Gruppe' Sales' verfügbar, während die Tickets für die Support-Abteilung in der Gruppe' Support' verfügbar sind.
Alle Tickets (Kundenanfragen) werden so den Mitarbeitern des entsprechenden Teams zur Verfügung gestellt.

Eine Gruppe kann mit einem Schrank verglichen werden, in dem alle Mappen mit den zu bearbeitenden Fällen (Tickets) einsortiert sind.
Jeder Agent des Teams hat Zugriff auf diesen Schrank und kann die Fälle (Tickets) bearbeiten.

Ein Agent sieht im Zammad nur die Tickets der Gruppen, für die er verantwortlich ist. Es gibt jedoch verschiedene Berechtigungen - je nach Einstellung des Admins kann ein Agent nur Lese- Verschiebe- oder Erstell-Rechte für eine Gruppe haben. 

Besitzer
----------
Wenn wir mit der eben genannten Metapher weiterarbeiten, dann haben wir eine Mappe (Ticket) in einem Schrank, für den ich verantwortlich bin (meine zugewiesene Gruppe) und diese möchte ich bearbeiten. In diesem Fall nehme ich mir die Mappe und arbeite den Fall ab. Dadurch steht den Kollegen diese Mappe nicht mehr zur Bearbeitung zur Verfügung. Genau das gleiche erreicht man im Zammad, indem man sich selbst als Besitzer des Tickets einträgt. Stellt man fest, dass der Kollege vom Nachbarraum für das Ticket verantwortlich ist, gibt man ihm die Mappe auf den Schreibtisch, trägt ihn also in unserem Fall als Besitzer des Tickets ein. Er kann diese Tickets in der Übersicht "Meine zugewiesenen Tickets" finden und sich über diese Aktion informieren lassen. (Benachrichtigungs-Einstellungen im Profil)

Status
----------
Dazu gibt es hier mehr zu erfahren:
http://zammad-user-documentation.readthedocs.io/de/latest/zammad-ticket-states.html?highlight=status

Priorität
----------
Prioritäten am Ticket ermöglichen es diese "Ticket-Kategorien" individuell zu bearbeiten. So können dadurch zum Beispiel unterschiedliche Service-Zeiten realisiert werden. Sofern vom Administrator eine Unterscheidung der Tickets in Prioritäten eingerichtet wurde, gelten für höher priorisierte Tickets andere Regelungen wie z.B. kürzere Bearbeitungszeiten.

Für unterschiedlich priorisierte Tickets können vom Admin verschiedene Automatismen eingestellt werden. Das sind zum Beispiel automatische Nachrichten, Zuweisung zu Gruppen/ Besitzern, Setzen von Status ... 


Tags und Verknüpfungen
----------
Zu diesen Themen finden sie unter den folgenden Links weitere Infos:

http://zammad-user-documentation.readthedocs.io/de/latest/zammad-ticket-tags.html?highlight=tags

http://zammad-user-documentation.readthedocs.io/de/latest/working-ticket-links.html


weitere Ticketaktionen
----------

Nach dem Klick auf "Ticket" stehen noch weitere Aktionen zur Verfügung: 

- Historie anzeigen (wer hat wann, was am Ticket gemacht)
- Tickets zusammenfassen (aus zwei Tickets eins machen)
- Kunde ändern (den korrekten Kunden für das Ticket eintragen)

.. image:: images/gettingstarted/Abb21-moegliche_Ticket-Aktionen.jpg

Dazu mehr in den folgenden Kapiteln.


