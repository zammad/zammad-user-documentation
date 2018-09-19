Ticket View
===========

Manage ticket details from the ticket pane’s **ticket view**.

.. figure:: /images/ticket-pane/ticket-view.jpg
   :alt: Ticket pane: Ticket view
   :align: center

   Ticket view is the default view mode. Most ticket management tasks are performed from here.

.. note:: Some options may not be available to you if you have insufficient permissions.

Ticket Settings
---------------

:Group:

   hello

:Owner:

   hello

:State:

   :doc:`Learn more </working-with-zammad/ticket-states>`.

:Priority:

   hello

:Tags:

   :doc:`Learn more </working-with-zammad/ticket-tags>`.

:Links:

   :doc:`Learn more </working-with-tickets/links>`.

More Actions
------------

Additional actions are available via the **ticket submenu**:

.. figure:: /images/ticket-pane/ticket-view-submenu.jpg
   :alt: Ticket submenu
   :align: center

   Click the **Ticket ▾** heading to access additional actions.

History
^^^^^^^

View a comprehensive list of updates to the ticket, performed by any user, since its creation.

.. figure:: /images/ticket-pane/ticket-view-history.png
   :alt: Ticket history summary
   :align: center
   :scale: 70%

   Each entry in a ticket’s history includes a timestamp and a record of who
   performed the change.

Merge
^^^^^

Merge multiple tickets into one.

.. figure:: /images/ticket-pane/ticket-view-merge.jpg
   :alt: Ticket merge dialog
   :align: center

   Select a ticket to merge with by (1) entering the ticket number, or (2) selecting from the list.

.. note:: Merging a ticket migrates all messages and notes **out of the original**
   and into the one selected in the dialog above.

   (That is, if you’re viewing Ticket A and :menuselection:`Ticket -->
   Merge` into Ticket B, then **Ticket A will be emptied, archived, and linked
   as a child of Ticket B**.)

Change Customer
^^^^^^^^^^^^^^^

Reassign the ticket to another customer.

.. figure:: /images/ticket-pane/ticket-view-change-customer.png
   :alt: Change Customer dialog
   :align: center
   :scale: 70%

   Search for a customer by name or by organization, or use the shortcut to create a new customer on the fly.

..
   Group
   -----

   Tickets can get into Zammad via different Channels and can be sorted into different groups each by different criteria.
   Within Zammad, you can see groups like working groups or departments within a company that can work on different topics.

   **As example:** All Tickets for the Sales-Team can be found within the group "Sales", while the Support-Devision (e.g. for your IT) can find their tickets within the group "Support".
   By dividing your departments, your agents only can see what they need and won't get distracted by other tickets.
   This can also come in handy in case you have departments like legal or accounting that work on information the Sales-Team or Support-Team are not supposed to see.

   You can compare a group to a big cupboard where you sort all your records (Tickets) you need to work on.
   Every Agent of the Team (Group) has access to this cupboard and can work on your cases (Tickets).

   You can use Roles within Zammad to ensure that your agents can only see groups contents that they are responsible for. 
   An agent can have different rights on groups: You can determine if the agents shall only have read-, move- or creation-rights on a group.

   Owner
   -----

   Let's stick with the metaphor from before: We have a file (Ticket) in our cupboard that I'm responsible for - I want to work on that file.
   In this case I'll take the care and I'll work on it. My colleagues can't work on this case.
   With Zammad, you can assign yourself as an owner of the ticket and you'll get a similar result. 
   *(Side note: Zammad doesn't show the Ticket as "unassigned" - other agents can always take a look into the case and add notes or answers if they have the needed rights to do so)*

   Let's say you notice that you can't process the ticket further, because your colleague is responsible for this. You can then change the owner to them and the ticket shows up in his overview.
   This is similar to handing him over your file / putting it onto his desk.
   He'll find the ticket within the overview "my assigned Tickets" and also get notified about this action. (please see noification settings within profile)

   Priority
   --------

   You can use priorities to realize e.g. reaction times or have special overviews only showing the really important stuff you have to solve before anything else.
   You can define Service Level Agreements (SLAs) to filter for ticket priorities  and escalate the ticket if the initial answer took too long or to ensure the solving time is respected.
   This can help you to consider the service contracts of your customers correctly.

   The Admin can create triggers and/or automations that can do several things, if a ticket reaches a certain priority. 
   For example, those actions can be an automated message (customer, agent), the change of a group/owner, setting states and much more...! 
   Here you can find more about Triggers_ and Automations_.

   .. _Triggers: https://zammad-admin-documentation.readthedocs.io/de/latest/manage-trigger.html
   .. _Automations: https://zammad-admin-documentation.readthedocs.io/de/latest/manage-scheduler.html

   ORGANIZATION PROFILE PAGE
   -------------------------

   This detail view contains information about open and closed tickets of all members of the organization (if it is a sharing organization). In addition, a statistic of open and closed tickets of the past 12 months is shown.

   .. image:: /images/ticket-pane/organization-view-stats.jpg

   By clicking "Action" on the upper right, you can edit organization-details and show the history of previous changes in the organization-details.



