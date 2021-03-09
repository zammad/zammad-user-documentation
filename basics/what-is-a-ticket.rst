What is a Ticket?
=================

In Zammad, **tickets** are used to track customer service requests.
The first time a customer emails you (or the company) about something,
Zammad creates a new ticket.
Each message sent between you and the customer is added to that ticket
until the issue is resolved,
the customer is happy,
and the ticket is finally **closed**.

So in a basic sense, a ticket is
**a thread of messages between you and a customer
about a single issue**.

.. figure:: /images/basics/what-is-a-ticket.jpg
   :alt: Ticket thread view
   :align: center

   A ticket is a thread of messages between a customer and an agent.

.. hint:: You know you’re doing a great job when you
   1) respond to tickets quickly and
   2) get them closed in a timely manner.

   👀 :doc:`Keep an eye on your dashboard </extras/dashboard>`
   to see how well you’re keeping up.

.. _ticket_settings:

Ticket Settings
---------------

Tickets also have metadata attached to them to make them easier to manage.
For instance, tickets have a customer and (optionally) an agent;
they can be open or closed (or even be scheduled for later);
they can be organized into groups;
and they can even be flagged for high or low priority.

For the sake of simplicity,
we’ll refer to this metadata as the **settings** of a ticket.
All of these settings can be changed at any time.
Each setting is explained in detail :doc:`here </basics/service-ticket/settings>`,
but for the time being, let’s go over the two most important ones:

Owner *(optional)*
   The **agent currently assigned to** (*i.e.,* responsible for) the ticket.

State
   Is the customer still waiting on an answer (**open**), or has the ticket
   been resolved (**closed**)?

.. include:: /snippets/ticket-settings-link-list.rst
