State
=====

The **state** of a ticket refers to *its progress toward completion,*
and may be one of the following:

* new
* open
* closed
* pending close
  (*i.e.,* scheduled to automatically close at a later date)
* pending reminder
  (*i.e.,* hidden, but scheduled to reappear at a later date)

.. _new-vs-open:

What’s the difference between “new” and “open”?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

States do more than just indicate progress:
Zammad has a fine-grained time tracking feature
(so-called “\ `service-level agreements <https://admin-docs.zammad.org/en/latest/manage-slas.html>`_\ ”, or SLAs)
that uses state information to measure how long it takes
for customers to get a response on a new ticket
or get their issues resolved entirely.

On a *new* ticket,
the customer still hasn’t received her first response on the issue.

On an *open* ticket,
the customer has received an initial response,
but the issue still hasn’t been resolved.

.. note:: ⏱️ Tickets in a *pending* state do not accumulate time toward their SLA limits.

   So, for instance, a ticket may be marked *pending reminder*
   if it’s waiting on feedback from a third-party supplier
   who’s out of town until next week.

