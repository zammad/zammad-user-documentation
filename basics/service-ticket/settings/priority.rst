Priority
========

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

   * `service-level agreements`_,
   * `triggers`_, and
   * `scheduled events`_.

Priority can also be used as a ticket filter when creating `custom overviews`_.

.. _service-level agreements:
   https://admin-docs.zammad.org/en/latest/manage/slas.html
.. _triggers: https://admin-docs.zammad.org/en/latest/manage/trigger.html
.. _scheduled events:
   https://admin-docs.zammad.org/en/latest/manage/scheduler.html
.. _custom overviews: 
   https://admin-docs.zammad.org/en/latest/manage/overviews.html

In other words, **consult your administrator**
for details on how he’d like you to use it.
