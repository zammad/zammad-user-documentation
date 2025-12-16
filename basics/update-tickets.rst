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
and owner you can set. Visit :doc:`ticket-basics` to learn more about them.

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
   :alt: Screenshot shows article editor with highlighted lock icon to change visibility of article.
   :width: 70%
   :align: center

.. include:: /snippets/editor-features.rst

Every new article appears at the end of the conversation, which means below
the existing articles. To see detailed information of a message, just click on
an article. This opens additional meta information:

.. figure:: /images/basics/service-ticket/follow-up-message-details.gif
   :alt: Screenshot shows article detail view.
   :width: 70%
   :align: center

You might wonder how to delete articles. The answer is you can only delete
articles that you have created yourself and which are not older than 10 minutes.
To see the **delete** button in articles of a communication type (emails, calls),
their visibility has to be switched to internal first.

.. figure:: /images/basics/service-ticket/delete-article.png
   :alt: Screenshot shows an internal article with highlighted delete button.
   :align: center
   :width: 50%

Add an Article from Scratch
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the text field at the bottom of the ticket detail view which is labeled
with **Enter Note or select attachment...** to add an article. By default, the
article type "Note" is selected and the visibility is set to "internal".

.. figure:: /images/basics/service-ticket/follow-up-add-note.gif
   :align: center
   :width: 70%

Respond to an Article
^^^^^^^^^^^^^^^^^^^^^

To forward or reply to an article, use one of the response buttons under an
article. The behavior is similar to an email client

- **Reply**: Allows you to answer the article. The recipient is automatically
  pre-filled. The reply is sent via the same channel as the original message.
  This lets you easily send an answer to a customer or third party, if involved.
- **Reply all**: Same as above but uses all recipient addresses from the
  original message as recipients for your new article. Only available for email
  channels.
- **Forward**: This means you can forward the original message to a third party
  or anybody else. The original message and attachments are included in your
  new article.

.. figure:: /images/basics/service-ticket/follow-up-reply-button.png
   :alt: Screenshots shows response buttons below an article.
   :width: 70%
   :align: center

Zammad even allows you to quote text from an existing article. This is
especially helpful if an answer refers to different parts of the original
message or the text is pretty long. This feature is limited to communication
type articles like email where the response buttons are available.

To quote text, simply select the text you want to quote and use the **Reply**
or **Reply all** function. This adds the selected text as quote in your new
article. You can do this even multiple times to quote different parts. Just
select another part of the text, click on the same response action as before
and it gets added as another quote to your editor. You can split quotations by
using enter in the editor.

.. figure:: /images/basics/service-ticket/mark-to-quote.gif
   :align: center
   :width: 70%
   :alt: Screencast showing text being marked and quoted after pressing reply

Copy Ticket Number
------------------

Use the 🗊 icon next to the ticket title to copy the ticket number to your
clipboard (including ticket hook; e.g. ``Ticket#50071``).

Additional Features
-------------------

Check Escalations
^^^^^^^^^^^^^^^^^

SLAs are optional and require configuration by your instance administrator.
Administrators can learn more about SLAs
:admin-docs:`in our admin documentation </manage/slas/index.html>`. If you
can't see escalation timestamps, it is not configured by your admin.

On the top of every ticket being applicable for SLA escalations, you'll find
two dates next to the ticket number. By hovering the escalation date, Zammad
will display all upcoming escalation times based on the SLA configuration.

.. figure:: /images/basics/service-ticket/show-escalation-times.png
   :alt: Screenshot showing hovering over escalation note and getting more detailed escalation information.
   :align: center
   :width: 70%

Simultaneous Ticket Processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
   :width: 70%
   :align: center

   A ✏️ icon will appear if the agent has made any unsaved changes to the
   ticket.

.. _rename-ticket:

Rename a Ticket
^^^^^^^^^^^^^^^

To rename a ticket, simply click on the title and start typing.

.. figure:: /images/basics/service-ticket/settings-rename-ticket.png
   :width: 70%
   :align: center


Highlighting Ticket Text
^^^^^^^^^^^^^^^^^^^^^^^^

Use the highlighter tool in the upper-righthand corner to mark up important
text. (Your highlights are visible to other agents.)

.. figure:: /images/basics/service-ticket/settings-highlight-text.png
   :alt: Ticket highlighter
   :width: 70%
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

