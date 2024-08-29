Group
=====

**Groups** are a form of access control
that allows you to dictate *which agents are allowed to do what*
to a given ticket.

What?
-----

Suppose your organization uses Zammad for both sales and customer support.
You've got ten different agents spread across two teams,
handling dozens of tickets a day.

Without groups,
all ten agents can see (and respond to) every single ticket that comes in,
regardless of which department it's for.
This isn't problematic *per se,*
but it does lead to a lot of unnecessary clutter
in the :doc:`overviews menu </basics/find-ticket>`.
(It can be much worse when, for example,
a customer service rep sees tickets meant for your HR department,
and finds out how much their colleagues in sales are making! 💸💸💸)

If, instead, each agent were assigned to an appropriate group,
then they'd only ever see the tickets that belong to their own group.

Managing Groups
---------------

So how do I manage which team I'm on? You don't - that's the
:admin-docs:`administrator's job </manage/groups/index.html>`.

However, you can *check* which teams you're on
in the Notifications section of
your :doc:`user settings </extras/profile-and-settings>`:

.. figure:: /images/basics/service-ticket/settings/group-user-list.png
   :alt: Profile > Notifications menu
   :align: center
   :scale: 70%

   This user belongs to only one group (“Users”).

So Where Do I Come In?
----------------------

If you belong to more than one group,
you may re-assign a ticket from one of your groups to another.
In general, though, you won't need to do this unless you're an admin,
or an admin has discussed the procedure with you beforehand.
