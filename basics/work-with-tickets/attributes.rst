Attributes
==========

.. _ticket-attributes:

Ticket Attributes
-----------------

Use the **ticket sidebar** to view and change ticket attributes.

.. figure:: /images/basics/service-ticket/settings-ticket-pane.png
   :alt: Default ticket pane view
   :align: center

   Click the **→** button in the corner to hide the ticket pane. Click the 💬
   tab to bring it back.

The available options depend on your privileges and the configuration of your
system.

Priority
--------

A ticket’s **priority** is simply a ranking (from 1 to 3)
of *how urgent or important it is*.

.. figure:: /images/basics/service-ticket/settings/priority-colors.png
   :alt: Overview showing 3 tickets with different priorities
   :align: center

   Zammad's 3 default priorities allow you to see the importance of
   your tickets better.

But what does it do, and how should I use it?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Out of the box, **ticket priority doesn’t actually do anything**.
However, Zammad administrators can set up all sorts of automated hooks
that fire off based on this value, like:

   * :admin-docs:`service-level agreements </manage/slas/index.html>`,
   * :admin-docs:`triggers </manage/trigger.html>`, and
   * :admin-docs:`scheduled events </manage/scheduler.html>`.

Priority can also be used as a ticket filter when creating
:admin-docs:`custom overviews </manage/overviews.html>`.

In other words, **consult your administrator**
for details on how he’d like you to use it.

.. hint::
   Customers can't set a priority for their own tickets.
   For more context, have a look at the `Github-Issue <https://github.com/zammad/zammad/issues/814>`_.

Tags
----

**Tags** are custom-defined labels that can be applied to tickets
to make it easier to find them in the future.

.. figure:: /images/basics/service-ticket/settings-tags.png
   :alt: Ticket pane (tags)
   :align: center

   Click on a tag name to view other tickets with the same tag.

.. hint:: :ref:`Search for tickets with a given tag <search-tickets>`
   with the ``tags:`` search filter.
   For instance, find all tickets with the **order** tag
   by searching for ``tags: order``.

State
-----

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

State Colors
^^^^^^^^^^^^

Zammad states are color-coded. This helps you to understanding the state of
the ticket much faster in general - without having a look into details.

.. include:: /snippets/ticket-state-type-circles.rst

.. _new-vs-open:

What's the Difference Between “New” and “Open”?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

