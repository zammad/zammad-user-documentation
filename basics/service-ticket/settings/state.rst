State
=====

.. warning:: 🚧 This page is still undergoing revision.

.. |br| raw:: html

   <br />

A Ticket state shows the current working state of a ticket.

The following states can be used:


+------------------+-------------------------------------------------------------------------------------------------+
| State            | Explanation                                                                                     |
+==================+=================================================================================================+
| New              | Ticket hasn't been worked on yet. First reacion time is running on the ticket, as  |br|\        |
|                  | soon asit gets created (if configured). You can't change a ticket state to "new",  |br|\        |
|                  | because the state has to be "open" as soon as somebody worked on the ticket.                    |
+------------------+-------------------------------------------------------------------------------------------------+
| Open             | This ticket needs further work on (or the agent didn't change it's state. |br|\                 |
|                  | The second reaction time (SLA) is running now.                                                  |
+------------------+-------------------------------------------------------------------------------------------------+
| Pending close    | Can be used if the ticket can't be closed just yet, as you may expect a further action |br|\    |
|                  | (e.g. customer response) within the next time. |br|\                                            |
|                  | No reaction times (SLA) will be applied to the ticket. You have to define a date and |br|\      |
|                  | time. The ticket state will change to "closed" automatically when reaching the set |br|\        |
|                  | time.                                                                                           |
+------------------+-------------------------------------------------------------------------------------------------+
| Pending reminder | This state can be used for situation where you await further actions / reactions to |br|\       |
|                  | the ticket (e.g. customer response or feedback of a colleague). At this moment  |br|\           |
|                  | further work on this ticket is not necessary.                                           |br|\   |
|                  | You have to define a date and time. The ticket state will change to "open"  |br|\               |
|                  | automatically when the set time is reached. The ticket owner will get notified if the |br|\     |
|                  | reminder is reached.                                                                            |
+------------------+-------------------------------------------------------------------------------------------------+
| closed           | No escalation times will be applied further. No further work on the ticket is  |br|\            |
|                  | necessary. The ticket will not be shown within the default overviews, you might   |br|\         |
|                  | need to search for the ticket via search function. If enabled, the ticket can be  |br|\         |
|                  | reopened by agents or customer.                                                                 |
+------------------+-------------------------------------------------------------------------------------------------+

The state can be set directly within the ticket information. You can find further information here_ .

.. _here: ticket-information.html 


To improve the overview of Zammad tickets, the ticket states are shown in different colors as follows:

+----------+----------------------------------------------------+----------------------------------------------------+
| |orange| | Ticket is new, open or the reminder |br|\          | The agent has to work on this ticket.              |
|          | time has been reached.                             |                                                    |
+----------+----------------------------------------------------+----------------------------------------------------+
| |grey|   | A pending state is set, but the time |br|\         | The ticket doesn't need any work at the |br|\      |
|          | hasn't been reached yet. |br|\                     | moment.                                            |
|          | (pending close / reminder)                         |                                                    |
+----------+----------------------------------------------------+----------------------------------------------------+
| |red|    | This ticket has escalated (the agent  |br|\        | This ticket needs attention asap |br|\             |
|          | did not work on the ticket according to SLAs.      | (to end the escalation                             |
+----------+----------------------------------------------------+----------------------------------------------------+
| |green|  | The ticket has been closed.                        | The ticket doesn't need any further |br|\          |
|          |                                                    | work/attention                                     |
+----------+----------------------------------------------------+----------------------------------------------------+

.. |orange| image:: /images/rings/orange.png
.. |grey| image:: /images/rings/grey.png
.. |red| image:: /images/rings/red.png
.. |green| image:: /images/rings/green.png

Those colored rings for tickets will be shown on overviews and on the left side of the tab list.


**Hint**

If you see the ticket indicators pulsating, this means that the ticket has been changed and needs attention.
The Pulsating stops as soon as you open the ticket.
