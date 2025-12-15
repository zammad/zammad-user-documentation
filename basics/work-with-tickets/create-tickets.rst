Create Tickets
==============

Zammad does its best to create tickets automatically
when new customer issues come your way.
But sometimes,
there's just no way for Zammad to know when an issue arrives –
like when a customer calls on the phone.

In these cases, Zammad needs your help to **create a new ticket**.

.. figure:: /images/basics/service-ticket/create.png
   :alt: New ticket dialog
   :align: center

   Click the **➕ button** to create a new ticket. The default ticket type is
   **Received Call**.

An agent can create three types of tickets:

:Received Call: for issues **initiated by a customer** over the phone.
:Outbound Call: for issues **initiated by an agent** over the phone.
:Send Email:    for issues **initiated by an agent** over email.

Filling Out the Form
--------------------

Here's a quick run-down of each input field in the New Ticket form:

Title
   The title of the ticket will be used as the **subject line**
   for all email correspondences.

Customer
   Enter a name or email address of a customer to search. You can even search
   for organizations and their members. Select an option from the autocomplete
   menu or create a new customer by clicking the "➕ Create new Customer"
   button. A ticket may only have **one** customer.

.. figure:: /images/basics/service-ticket/search-customer.png
   :alt: Screenshot showing customer search while creating a new ticket
   :scale: 80%
   :align: center

   Ticket creation with customer suggestion based on search.

.. tip:: **🖱️ UI Protip**

   Once a customer has been selected,
   her profile will be accessible from the **ticket pane**.

   .. figure:: /images/basics/service-ticket/create-ticket-pane-customer-view.png
      :alt: Ticket pane (Customer view)
      :align: center

Text
   📞 For phone calls, record the details of your conversation.
   These notes will not be sent to the customer
   (though he may be able to see them if he has a Zammad account).

   📧 For emails, this is the body of your outgoing message.

   .. include:: /snippets/ui-protip-message-editor-features.rst

Ticket Attributes
   See :doc:`attributes`.
