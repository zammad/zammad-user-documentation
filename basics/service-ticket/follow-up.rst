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

.. figure:: /images/basics/what-is-a-ticket.png
   :alt: Ticket summary view
   :align: center

   Tickets are threads of messages & notes about a customer service issue.
   :doc:`⚙️ Manage a ticket's settings <settings>` in the
   **ticket pane** on the right.

.. hint:: 📇 Any time you open a ticket, a new entry will appear in your
   :doc:`tab list</advanced/tabs>` in the main menu.

   Zammad **automatically backs up your unsaved changes** in all open tabs.

Responding to Individual Messages
---------------------------------

Use the **⮪ reply** button under a message to reply to it directly.

.. figure:: /images/basics/service-ticket/follow-up-reply-button.jpg
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

.. hint:: ⏩ You can also **forward messages**,
   just as you would in any email client
   (attachments are included automatically).

   This way, you can share correspondences
   with people who don't have Zammad
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

What about the **deletion of articles**? In Zammad, you can only delete articles
that you have created yourself and which are not older than 10 minutes. To see
the "delete" button in articles of the type "communication" (emails, calls),
their visibility has to be switched to internal first.

.. include:: /snippets/ui-protip-message-editor-features.rst

Using quotation
---------------

In many cases you'll want to quote earlier text of your customer. This is
important because especially on long conversations your opponent will easily
loose track.

Referencing on earlier written text helps greatly to keep context and track
of things. By default Zammad adds no whole quote body (this can be changed
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

🔥 Keeping an eye on escalations
---------------------------------

.. note:: **🧐 Huh? I can't see escalation timestamps!**

   SLAs are optional and require configuration by your instance administrator.
   Administrators can learn more about SLAs
   :admin-docs:`in our admin documentation </manage/slas/index.html>`.

On the top of every ticket being applicable for SLA escalations, you'll find
two dates next to the ticket number. By hovering the escalation date, Zammad
will display all upcoming escalation times based on the SLA configuration.

.. figure:: /images/basics/service-ticket/show-escalation-times.gif
   :alt: Screencast showing agent hovering the escalation time and receiving
         a more detailed escalation information

--------------------------------------------------------------------------------

.. _caution-im-working-here:

.. caution:: **🙅 I'm working here!**

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

   .. figure:: /images/basics/service-ticket/follow-up-conflict-detection.png
      :alt: Ticket conflict alert
      :align: center

      A ✏️ icon will appear if the agent has made any unsaved changes to
      the ticket.
