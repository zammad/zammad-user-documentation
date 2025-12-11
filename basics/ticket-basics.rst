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
complicated. But the opposite is the case:

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

Ticket Attributes
-----------------

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
- **Group**: This ticket attribute is useful for organizations with more than one
  team. Depending on the permissions, you might not see the ticket after
  changing the group and saving the changes.

Depending on the configuration of your Zammad, you might even have more
attributes available. It is even possible to create custom fields for
tickets (e.g. for groups and users too). You think such a custom field makes
sense? Talk with your Zammad admin, it can be set up easily
(:admin-docs:`admins can read more here </system/object/types.html>`).

Now you might wonder where to find and change these attributes. In this case,
head over to the :doc:`zammad-ui` page where it is described.
