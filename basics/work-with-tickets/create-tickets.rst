Create Tickets
==============

When a customer messages you over a channel which is fetched by Zammad, a ticket
is created automatically (except Zammad recognizes it as a follow-up, then it
gets added as an article to an existing ticket). However, there might be cases
where you need to create a ticket manually. Examples:

- A customer calls you by phone.
- You receive a paper letter from a customer.
- A customer comes to a physical service desk.
- You proactively have to inform a customer by sending out a message.

In situations like these, you need to create a new ticket manually and click the
``+`` button at the bottom of the navigation bar. This shows a ticket create
screen where you can add all needed information.

.. figure:: /images/basics/service-ticket/create.png
   :alt: New ticket dialog
   :align: center

Type
----

In the ticket create dialog, you can choose from different article types:

- Received Call: for issues initiated by a customer over the phone.
- Outbound Call: for issues initiated by an agent over the phone.
- Send Email: for issues initiated by an agent over email.

When choosing **Send Email**, the customer receives an email with the title as
subject and the text as email content.

Title
-----

This is the title of a ticket which is shown in many places in Zammad.
For example this gets displayed in overviews. It is also used as the subject
for email communication. For emails, a ticket identifier is automatically
appended (e.g. ``Ticket#901234 - I need help!``).

Customer
--------

Enter a name or email address of a customer to search for existing accounts.
You can even search for organizations and their members. Select an option from
the autocomplete menu or create a new customer by clicking the
**+ Create new Customer** button. This opens a dialog where you can provide
all relevant information of the customer. A ticket can only have one customer.

.. figure:: /images/basics/service-ticket/search-customer.png
   :alt: Screenshot showing customer search while creating a new ticket
   :align: center
   :scale: 80%

   Ticket creation with customer suggestion based on search.

After setting a customer in the ticket create dialog, the customer sidebar
automatically opens. You can see additional customer information including a
hint about the currently opened tickets of the customer.

.. figure:: /images/basics/service-ticket/create-ticket-customer-sidebar.png
   :alt: Screenshot shows "Customer" sidebar after setting a customer.
   :align: center

Text
----

This is the content section where the currently known details of the issue
gets written down. For the "Send Email" type, this is the content/message of
the email.

.. include:: /snippets/editor-features.rst

Ticket Attributes
-----------------

As you already know, there are additional ticket attributes like group, priority
and owner you can set. Because this works pretty much the same for ticket
updates, this section lives in a :doc:`separate page <attributes>`.
