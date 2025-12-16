Ticket Basics
=============

Introduction
------------

In Zammad, **tickets** are used to track customer service requests.
The first time a customer contacts you (or the company) about something,
Zammad creates a new ticket. Each message sent between you and the customer is
added to that ticket until the issue is resolved, the customer is happy and the
ticket is finally closed. Such a single message in a ticket is called
**article**. So basically, you can see a **ticket** as a **conversation**
between you and a customer about a single issue.

.. figure:: /images/basics/what-is-a-ticket.png
   :alt: Zammad UI with ticket detail view
   :align: center

   A ticket is a conversation between a customer and one or more agents.

If you're completely new to a ticket system and handled your customer requests
with an email client so far, you might think that a ticket system is
complicated. But the opposite is true:

- All emails are now collected in Zammad (and requests from other channels might
  be as well).
- You and your colleagues can see who is working on which customer request
  ("ticket").
- The state of each request as well as the history (who did what?) is
  transparent.
- There is no duplicate work and nothing gets overlooked.
- You can ask your colleagues directly in the ticket for help in difficult
  cases.
- With Zammad's intuitive UI, you can focus on what matters: to resolve customer
  issues and answer customer questions.

So, basically you can work with Zammad similar as with your email client. Except
that a ticket has additional attributes. Read on to learn more.

.. _ticket-attributes:

Ticket Attributes
-----------------

Introduction
^^^^^^^^^^^^

In addition to article, tickets have some additional meta information which are
called attributes. The most important ones are:

- **State**: reflects the current state of a ticket (mainly if a customer
  request is resolved or not). By default, there are the following states:

  - New: State for new tickets on which no one has worked on. When updating a
    ticket the first time, it automatically switches to open.
  - Open: State for tickets which aren't resolved yet and some work needs to be
    done.
  - Pending Close: State for tickets which are basically resolved but you don't
    want to close immediately. This state requires you to enter a date and time
    at which the ticket automatically switches to closed.
  - Pending Reminder: State for open tickets which you want to get reminded to a
    certain date and time. Requires you to enter a date and time at which you
    want to get notified. For example useful if you had a question to a third
    party and want to make sure that this issue won't be forgotten.
- **Owner**: This is the person who is currently responsible for the ticket. In
  case you need information from another colleague, you can either change
  the owner to this person or mention the person in an article by typing
  :kbd:`@` :kbd:`@` and selecting the user. In the latter case, the user gets
  notified and is automatically subscribed to receive notifications on ticket
  updates.
- **Group**: This ticket attribute is useful for organizations with more than
  one team. A common way to use groups is to have one for each department of the
  company. Depending on the permissions, you might not see the ticket after
  changing the group and saving the changes. In case you can't see the group
  field, either there is only one group in your Zammad system or you don't have
  the permission to create a ticket in other groups.

Depending on the configuration of your Zammad, you might even have more
attributes available. It is possible to create custom fields for
tickets (e.g. for groups and users too). You think such a custom field makes
sense? Talk with your Zammad admin, it can be set up easily
(:admin-docs:`admins can read more here </system/object/types.html>`).

Now you might wonder where to find and change these attributes. In this case,
head over to the :doc:`zammad-ui` page where it is described.

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

