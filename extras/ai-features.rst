AI Features
===========

Introduction
------------

Zammad is getting even smarter! We are expanding Zammad's AI capabilities to
help you manage support tickets even more efficiently. The initial focus is on
Ticket Summaries, but more features will arrive soon! ✨🚀

.. note:: The AI features have to be configured and activated by your
   administrator. If you can't see it, it is not configured. More information
   about how to configure and activate it can be found in the
   :admin-docs:`AI section </ai/index>` of the admin documentation.

Ticket Summary
--------------

The ticket summary feature does what it says: it summarizes the ticket's
content. This can be a huge time saver when dealing with large tickets and/or
many hand-overs between agents.

If the feature is activated, a banner is shown below the articles in the ticket
detail view. By clicking the ``See Summary`` button, the **Summary** sidebar
tab is opened and you can read the summary. The summary is created when you
open a ticket.

.. figure:: /images/extras/ai/ticket-summary.png
   :alt: Screenshot shows Zammad's ticket detail view with highlighted ticket summary banner and summary sidebar

Depending on the configuration of your Zammad instance, the summary includes
the following sections:

- Customer intent
- Conversation summary
- Open questions (optional)
- Suggested next steps (optional)

If you don't want to see the banner below the articles, you can **Hide** it. To
get the banner again, go to **Appearance** in your
:doc:`profile settings <profile-and-settings>` and re-activate it by toggling the
checkbox.
