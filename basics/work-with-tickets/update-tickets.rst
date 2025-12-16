Update Tickets
==============

You found your way into an existing ticket, congratulations! Now let's have a
look what you can do and how to do it.

Generally, working on existing tickets means keeping up with a customer
correspondence in a thread/conversation in the ticket detail view.
Any time you open a ticket, a new tab will appear in your
:doc:`navigation bar </advanced/tabs>` on the left side. To close a tab (in the
sense of remove it from the navigation bar, not setting the ticket state to
closed), just click the ``X`` button in the tab. Zammad automatically saves
your changes in opened ticket tabs, no matter if you already applied the changes
or just edited things and switched to somewhere else. This means it is no
problem to create a new ticket while editing an existing one. Simply switch back
to the other tab.

Changing Ticket Attributes
--------------------------

As you already know, there are additional ticket attributes like group, priority
and owner you can set. Because this works pretty much the same for ticket
creation, this section lives in a :doc:`separate page <attributes>`.

Create a New Article
--------------------

No matter if you create a new article from scratch or respond to a customer
article, you can choose from different article types:

- **Note**: Write a reminder for yourself and other agents, ask a colleague a
  question by mentioning a user or add new information to the ticket. The
  default visibility is "internal", which means the customer can't see the note.
- **Call**: Note down a summary of a phone call you had with the customer.
- **Email**: Send an email to anyone about the ticket. The name of the ticket is
  used for the subject of the email
  (:ref:`click on the title to rename it <rename-ticket>`).

Click the lock button 🔒 to change an article's visibility.
Internal visibility appears as a dashed border in a pale red color.

.. figure:: /images/basics/service-ticket/follow-up-mark-internal.png
   :align: center

Add an Article from Scratch
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the text field at the bottom of the ticket detail view which is labeled
with **Enter Note or select attachment...** to add an article. By default, the
article type "Note" is selected and the visibility is set to "internal."

.. figure:: /images/basics/service-ticket/follow-up-add-note.gif
   :align: center

.. include:: /snippets/editor-features.rst

Respond to an Article
^^^^^^^^^^^^^^^^^^^^^

Use the **⮪ reply** button under a message to reply to it directly.

.. figure:: /images/basics/service-ticket/follow-up-reply-button.png
   :alt: Reply button
   :align: center

   An additional **⮪ reply all** option will appear
   for email messages with multiple recipients.

Like with new messages,
your response will appear at the end of the thread.
Under the hood, responses are sent
**via the same channel as the original message**
(*i.e.,* if the message you replied to was originally a tweet,
the customer will receive your response in a Twitter DM).

You can also **forward messages**, just as you would in any email client
(attachments are included automatically). This way, you can share
correspondences with people who don't have Zammad (like a third-party supplier).

Do you want to see **detailed information of a message**? Just click on it:

.. figure:: /images/basics/service-ticket/follow-up-message-details.gif
   :alt: Message details view
   :align: center

Cite Text from Customer
^^^^^^^^^^^^^^^^^^^^^^^
In many cases you'll want to quote earlier text of your customer. This is
important because especially on long conversations your opponent will easily
loose track.

Referencing on earlier written text helps greatly to keep context and track
of things. By default, Zammad adds no whole quote body (this can be changed
by your administrator).

No matter if the whole quotation is active or not, you can always mark the text
you want to reference and press *reply* or *reply all* after. This will cause
Zammad to add the marked text as quote to the editor. You can break up
quotations by using enter.

.. note::

   This function is limited to one article per operation.
   The article has to be of type *communication* (thus have a *reply* button)
   to function.

.. figure:: /images/basics/service-ticket/mark-to-quote.gif
   :align: center
   :alt: Screencast showing text being marked and quoted after pressing reply

   Mark, press reply and work with quoted text!


Copy Ticket Number
------------------

Use the 🗊 icon next to the ticket title to copy the ticket number to your
clipboard (including ticket hook; e.g. ``Ticket#50071``).


Check Escalations
-----------------

SLAs are optional and require configuration by your instance administrator.
Administrators can learn more about SLAs
:admin-docs:`in our admin documentation </manage/slas/index.html>`. If you
can't see escalation timestamps, it is not configured by your admin.

On the top of every ticket being applicable for SLA escalations, you'll find
two dates next to the ticket number. By hovering the escalation date, Zammad
will display all upcoming escalation times based on the SLA configuration.

.. figure:: /images/basics/service-ticket/show-escalation-times.png
   :alt: Screenshot showing hovering over escalation note and getting
         more detailed escalation information

Simultaneous Processing of a Ticket
-----------------------------------

.. _caution-im-working-here:

Every once in a while, two agents may have the same ticket open at the same
time. When this happens, things can get messy fast:
customers may receive conflicting responses on the same issue from both agents;
or, changes made by one agent may be accidentally undone by the other.

To keep things under control, Zammad will alert you to potential conflicts
by displaying an avatar in the bottom bar (live user section) for every agent
that has that ticket open.

Be sure to communicate with your colleagues to prevent these problems before
they arise.

.. figure:: /images/basics/service-ticket/follow-up-conflict-detection.png
   :alt: Ticket conflict alert
   :align: center

   A ✏️ icon will appear if the agent has made any unsaved changes to the
   ticket.

.. _rename-ticket:

Rename a Ticket
^^^^^^^^^^^^^^^

To rename a ticket, simply click on the title and start typing.

.. figure:: /images/basics/service-ticket/settings-rename-ticket.png
   :align: center

Additional Features
-------------------

Delete articles
^^^^^^^^^^^^^^^

What about the **deletion of articles**? In Zammad, you can only delete articles
that you have created yourself and which are not older than 10 minutes. To see
the "delete" button in articles of the type "communication" (emails, calls),
their visibility has to be switched to internal first.

Highlighting Ticket Text
^^^^^^^^^^^^^^^^^^^^^^^^

Use the highlighter tool in the upper-righthand corner to mark up important
text. (Your highlights are visible to other agents.)

.. figure:: /images/basics/service-ticket/settings-highlight-text.png
   :alt: Ticket highlighter
   :align: center

   Highlight by selecting text, then clicking the highlighter.
   Click again to undo.

Further Ticket Actions
^^^^^^^^^^^^^^^^^^^^^^

.. _ticket-submenu:

Additional actions are available via the **submenu**:

.. figure:: /images/basics/service-ticket/settings-ticket-submenu.png
   :alt: Ticket submenu
   :scale: 60%
   :align: center

   Click the **Ticket ▾** heading to access additional actions.

History
   See a comprehensive list of updates to the ticket,
   performed by any user,
   since its creation.

Merge
   Migrate all messages/notes to another ticket
   (see :doc:`Merging Tickets </advanced/ticket-actions/merge>` for details).

Change Customer
   Reassign the ticket to another customer.

