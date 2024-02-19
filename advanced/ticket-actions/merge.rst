Merging Tickets
===============

If you have two or more tickets about the same issue, you may want to merge
those tickets into one.

This might be the case if a customer sends you a new email which can't be
assigned to the existing ticket (e.g. the ticket reference is missing because
the customer sends you a completely new email instead of answering in the
existing thread).

What is merged where?
   Merging a ticket migrates all messages and notes of the ticket from where
   you select the merging into the selected one.

   Let's assume you already worked on a ticket and you get another ticket about
   the same issue and want to merge them.
   Let's call the ticket you already worked on the *original* one and the new
   one *duplicate*.
   Then the way to go is to open the duplicate ticket and execute the merging
   from there so it will be merged into the original.

How to merge tickets?
   To merge a ticket, access the **Ticket ▾** submenu in the ticket pane.

   .. figure:: /images/advanced/ticket-actions/ticket-menu-merge.png
     :alt: Ticket menu with highlighted "merge"
     :align: center

Merge dialog
   You can either enter the ticket number of the ticket you want to merge the
   current one into (see 1). Alternatively, you can choose from the list below
   (see 2).

   If the customer has an existing ticket, it will show up under "Recent
   customer tickets". You can see your last viewed tickets under "Recently
   viewed tickets" anyway.

   After entering a ticket number or choosing one of the offered tickets from
   the list, click on the submit button and the tickets will be merged.

.. figure:: /images/advanced/ticket-actions/merge-dialog.png
   :alt: Merge ticket dialog
   :align: center
   :scale: 80%

Result after merging
   The articles are moved into the chosen tickets. The ticket in which you
   executed the merging still exists with the following changes:

   - The articles have been replaced by a "merged" label
   - The state has changed to "merged"
   - The ticket is :doc:`linked <link>` to its "parent" ticket
