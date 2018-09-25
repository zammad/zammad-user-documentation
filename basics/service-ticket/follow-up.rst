Following Up
============

Generally, “working on existing tickets” means
keeping up with a customer correspondence in the **thread view**.
You can do this by:

* 📧 responding to an **individual message**, or
* 📝 adding a message/note to the **whole ticket**.

Read on to learn more,
or skip ahead to find out about :doc:`managing ticket settings <settings>`
(which is the other half of “working on existing tickets”).

.. figure:: /images/basics/what-is-a-ticket.jpg
   :alt: Ticket summary view
   :align: center

   Tickets are threads of messages & notes about a customer service issue.
   :doc:`⚙️ Manage a ticket’s settings <settings>` in the
   **ticket pane** on the right.

.. hint:: 📇 Any time you open a ticket, a new entry will appear in your
   :doc:`tab list</advanced/tabs>` in the main menu.

   Zammad **automatically backs up your unsaved changes** in all open tabs.

Responding to Individual Messages
---------------------------------

.. note:: 💡 When taking action on a new ticket,
   remember to :ref:`change the state from new to open <new-vs-open>`.

Use the **⮪ reply** button under a message to reply to it directly.

.. figure:: /images/basics/service-ticket/follow-up-reply-button.jpg
   :alt: Reply button
   :align: center

   An additional **⮪ reply all** option will appear
   for email messages with multiple recipients.

Like with new messages,
your response will appear at the end of the thread.
Outside of Zammad, however,
it will be **delivered on the same channel** as the original message
(*i.e.,* if the message you replied to was originally a tweet,
the customer will receive your response in a Twitter DM).

.. hint:: ⏩ You can also **forward messages**,
   just as you would in any email client
   (attachments are included automatically).

   This way, you can share correspondences
   with people who don’t have Zammad
   (like a third-party supplier).

.. tip:: **🖱️ UI Protip**

   Click on a message to see detailed information about it.

   .. figure:: /images/basics/service-ticket/follow-up-message-details.gif
      :alt: Message details view
      :align: center

Adding New Messages/Notes
-------------------------

Click on the text field at the end of the thread to add a follow-up.

.. figure:: /images/basics/service-ticket/follow-up-add-note.gif
   :align: center

   The default follow-up type is “note”. Click the 📝 to select another type.

There are three types of follow-ups:

:📝 Note:

   Jot down a reminder for yourself and other agents
   when new information comes in
   (hidden from the customer by default).

:📞 Call:

   Record a summary of a phone call you had with the customer.

:📧 Email:

   Send an email *to anyone* about the ticket.
   The name of the ticket will be used for the subject line
   (:ref:`click on the title to rename it <rename-ticket>`).

.. hint:: Click the 🔒 button to change the visibility of a note or message.

   .. figure:: /images/basics/service-ticket/follow-up-mark-internal.png
      :align: center

      “Internal” messages are outlined with a salmon border,
      and **can only be viewed by other agents**.

.. include:: /snippets/ui-protip-message-editor-features.rst

----

.. caution:: **🙅 I’m working here!**

   Every once in a while,
   two agents may have the same ticket open at the same time.
   When this happens,
   things can get messy fast:
   customers may receive conflicting responses
   on the same issue
   from both agents; or,
   changes made by one agent may be accidentally undone by the other.

   To keep things under control,
   Zammad will alert you to potential conflicts
   by displaying an avatar in the lower-lefthand corner
   for every agent that has that ticket open.

   Be sure to communicate with your colleagues
   to prevent these problems before they arise.

   .. figure:: /images/basics/service-ticket/follow-up-conflict-detection.jpg
      :alt: Ticket conflict alert
      :align: center

      A ✏️ icon will appear if the agent has made any unsaved changes to the ticket.
