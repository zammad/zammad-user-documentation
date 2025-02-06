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
---------------------------------------------

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

.. hint:: :doc:`
   Customers can´t set priority for their own tickets #814
   For more context https://github.com/zammad/zammad/issues/814#issuecomment-2640152413
   
