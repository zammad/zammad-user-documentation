State
=====

The **state** of a ticket refers to *its progress toward completion,*
and may be one of the following:

* new
* open
* closed
* merged
  (this Ticket has been merged into another Ticket. Check either the
  :doc:`linked tickets </advanced/ticket-actions/link>` or the
  :ref:`ticket history <ticket-submenu>` to learn more)
* pending close
  (*i.e.,* scheduled to automatically close at a later date)
* pending reminder
  (*i.e.,* hidden, but scheduled to reappear at a later date)

State colors
------------

Zammad states are color-coded. This helps you to understanding the state of
the ticket much faster in general - without having a look into details.

.. include:: /snippets/ticket-state-type-circles.rst

.. _new-vs-open:

What's the difference between “new” and “open”?
-----------------------------------------------

States do more than just indicate progress: Zammad has a fine-grained time
tracking feature (so-called
“:admin-docs:`service-level agreements </manage/slas/index.html>`”,
or SLAs) that uses state information to measure how long it takes for customers
to get a response on a new ticket or get their issues resolved entirely.

On a *new* ticket,
the customer still hasn't received her first response on the issue.

On an *open* ticket,
the customer has received an initial response,
but the issue still hasn't been resolved.

.. note:: ⏱️ Tickets in a *pending* state do not accumulate time toward their SLA limits.

   So, for instance, a ticket may be marked *pending reminder*
   if it's waiting on feedback from a third-party supplier
   who's out of town until next week.

