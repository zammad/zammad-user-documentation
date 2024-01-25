Suggested Workflows
===================

.. _sharing-work:

Sharing Work on a Ticket
------------------------

Some tickets require attention from more than one agent
(or even more than one department!).
In these cases, there are three ways to assign the work to the right people:

1. If a ticket is really about two different problems,
   you can :doc:`split it in two </advanced/ticket-actions/split>`,
   then assign each ticket to its respective “group” (department).
2. If you've done all you can on a ticket
   and it's now another agent's (or department's) responsibility,
   **reassign it** to a new owner (or group).
3. If you just need another agent's input on something, you can **@mention** 
   them. (And if *you* want to get notifications for *someone else's* ticket,
   use the **subscribe button**.)

Reassigning tickets
^^^^^^^^^^^^^^^^^^^

.. figure:: /images/advanced/suggested-workflows/sharing-work.png
   :alt: Reassigning tickets in the ticket pane
   :align: center

   Reassign a ticket (via the *Group* and *Owner* settings)
   to let colleagues know you're done with your part.

Suppose a call comes into the sales department.
A sales rep takes the call, creates a ticket,
and looks up some prices for the customer.
After recording his notes,
the rep then decides that this ticket needs to be passed onto customer service.

Our sales rep can simply un-assign himself as the **owner** of the ticket
and re-assign the ticket to the Customer Service **group**.
*All customer service agents will be notified of the incoming ticket*,
and the first available agent can assign herself
to pick up where the sales rep left off.

.. tip::

   Be sure to leave notes with as much information as possible for the
   next agent!

.. _mentions:

@mentions & the Subscribe Button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now suppose you've reassigned the ticket to customer service.
You won't receive notifications for this ticket anymore,
but maybe this is a really important contract,
and you want to make sure they have an A+ experience from start to finish.

To enable notifications for a ticket that doesn't belong to you,
simply click the **Subscribe** button at the bottom of the ticket pane:

.. figure:: /images/advanced/suggested-workflows/mention-subscribe-yourself-to-a-ticket.gif
   :alt: Screencast of the Subscribe button feature
   :width: 90%
   :align: center

   A list of all tickets you're subscribed to
   can be found in the **My mentioned Tickets** overview.

Or, suppose you *don't* want to reassign the ticket to customer service—you
just have one quick question for them, and then you can take it from there.

To start sending someone else notifications for your own ticket,
type ``@@`` in the message composer and select their name from the pop-up menu:

.. figure:: /images/advanced/suggested-workflows/mention-other-agents.gif
   :alt: Screencast of the @mention feature
   :width: 90%
   :align: center

   @mentioning a colleague in a message
   will automatically subscribe them to your ticket.

.. hint:: ⚙️ **Notification settings**

   Check your :doc:`/extras/profile-and-settings`
   to customize how you receive notifications.

   **Can't see a ticket, in which a colleague @mentioned you?**

   Is the ticket assigned to a group that you don't belong to?
   @mentions and subscriptions only work for tickets that you already have
   access to.

Quickly assign in ticket listings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within overviews and detailed searches you can run bulk operations on tickets.
This means you can adjust the following ticket information:

   * group
   * owner
   * state (with pending time if applicable)
   * priority

After pressing "Confirm", Zammad also allows you to provide an internal or
public note of why you adjusted the settings.

Zammad *will not* ask for
:doc:`time accounting values </advanced/time-accounting>` in bulk actions.

Bulk action via drop-downs:
   .. figure:: /images/advanced/suggested-workflows/bulk-operations-on-ticket-lists.gif
      :alt: Bulk operations in overviews and detailed searches
      :align: center

      Use the check boxes in ticket listings to select a bunch of tickets.
      Now use below drop-downs to change ticket settings, press confirm and
      provide a note if you'd like.

Bulk action via drag and drop:
   **🤓 You can change owners and groups even faster 🚀**

   .. figure:: /images/advanced/suggested-workflows/drag-bulk-operation_assign-owner.gif
      :alt: Drag selected tickets and drop then on a group or agent to change
            ticket group / owner
      :align: center

   Instead of using the drop-downs on the bottom of Zammad, you can also
   drag tickets. A new modal will appear and allow you to drop your
   selection on either just a group or agents. This operation allows you to
   quickly change the group and owner without further hassle!

   This functionality is only available in ticket overviews.
