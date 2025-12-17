Work with Tickets
=================

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

For the most changes (except tags or rename title, for example), an explicit
update of the ticket is needed. So make sure to click the **Update** button
on the right side of the footer bar when you are happy with your changes.

Changing Ticket Attributes
--------------------------

As you may know, there are additional ticket attributes such as group, priority
and owner that you can set. If you haven't read :doc:`ticket-basics` yet, check
it out to learn more.

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
   :alt: Screenshot shows article editor with highlighted lock button to change visibility of article.
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

Zammad even allows you to **quote text** from an existing article. This is
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

.. _rename-ticket:

Rename a Ticket
---------------

To rename a ticket, simply click on the title in the header bar and start
typing. This title is used as subject in email communication and shows up in
several places like overviews.

.. figure:: /images/basics/service-ticket/settings-rename-ticket.png
   :width: 70%
   :align: center

Copy Ticket Number
------------------

If you often need the ticket number (e.g. to paste it in a third party chat
app), use the 🗊 icon next to the ticket title to copy the ticket number to your
clipboard. This includes the complete ticket identifier, including the ticket
hook, e.g. ``Ticket#50071``. In case you scrolled down in the ticket, you can
find the button on the left side of the header bar.

But wait, there is even a
:doc:`keyboard shortcut </advanced/keyboard-shortcuts>` for that. Simply press
:kbd:`.` and the ticket number is copied to your clipboard. To include the
ticket title as well, press :kbd:`.` twice. Example:
``Ticket#50071: Coffee grinder broken``.

Simultaneous Ticket Processing
------------------------------

.. _caution-im-working-here:

It can happen that two or more agents open a ticket at the same time. To prevent
edit conflicts and customers receiving contradictory answers, Zammad shows you
who is viewing or editing the ticket currently. You can find this information
in the bottom bar where avatars of all agents are displayed.
Be sure to communicate with your colleagues to prevent these problems before
they arise.

Depending on the additional icon and if the avatar icon is faded, it means:

- Avatar: Another agent is viewing the ticket.
- Faded avatar: Another agent opened the ticket but is currently not actively
  viewing it.
- Avatar with pencil icon: Another agent is currently actively working on this
  ticket.

.. figure:: /images/basics/service-ticket/follow-up-conflict-detection.png
   :alt: Ticket conflict alert
   :width: 70%
   :align: center

Ticket Actions
--------------

.. _ticket-submenu:

Additional actions are available in the ticket submenu. You can find it in the
ticket sidebar. To open it, click the **Ticket ▾** heading to access additional
actions.

.. figure:: /images/basics/service-ticket/settings-ticket-submenu.png
   :alt: Ticket submenu
   :width: 40%
   :align: center

History
   See a comprehensive list of updates to the ticket, performed by any user,
   since its creation. Useful to check who did what and when.

Merge
   Migrate all messages/notes to another ticket. Useful if you have more than
   one ticket about a single customer issue. See
   :doc:`Merging Tickets </advanced/ticket-actions/merge>` for details.

Change Customer
   Reassign the ticket to another customer.

Check Escalations
-----------------
.. Rework and add link after adding SLA to docs: https://github.com/zammad/zammad-user-documentation/issues/480

The SLA feature (Service Level Agreement) is optional and must be
:admin-docs:`configured by your Zammad administrator </manage/slas/index.html>`.
SLAs are to track the time for a first response and/or to solving the issue.
If a ticket is in danger to reach the agreed deadline, it will escalate.

For tickets which already reached the deadline or will reach it soon, you can
find an addition date next to the ticket number. By hovering the escalation date,
Zammad will display all upcoming or reached escalation times based on the SLA
configuration. If you can't see escalation timestamps, it is not configured by
your admin.

.. figure:: /images/basics/service-ticket/show-escalation-times.png
   :alt: Screenshot showing hovering over escalation note and getting more detailed escalation information.
   :align: center
   :width: 70%

Highlight Text in a Ticket
--------------------------

Use the highlighter tool in the upper right corner to mark up important text.
This feature is not about highlighting text in the editor to send it to
customers. It is just about highlighting important parts for other agents.

First select the text you want to highlight, then click on the highlighter
button with the pencil. In case you want to use a different color, open the
color menu by clicking on the down arrow in the split button.
To remove the highlighting, click on the button again with the selected text.

.. figure:: /images/basics/service-ticket/settings-highlight-text.png
   :alt: Ticket highlighter
   :width: 70%
   :align: center

-----

You now know the basics and how to work with tickets in general. However, there
are many more features in Zammad which can be very useful in your daily
work. Have a look at the **Advanced Topics** and **Extra** sections in the left
navigation menu where you can find more information.
