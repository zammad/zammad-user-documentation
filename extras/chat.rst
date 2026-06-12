Live Chat
=========

Talk to customers in real time from the **Customer Chat** panel.

This feature is optional. If you don't see it in the main menu,
that means your administrator hasn't enabled it yet. Administrators can learn
more in the
:admin-docs:`chat channel documentation of the admin documentation </channels/chat.html>`.

Overview
--------

.. figure:: /images/extras/chat/chat.jpg
   :alt: Screenshot shows chat UI with labeled elements.
   :align: center

+---------------------------------------------------------------------------+
| Chat controls                                                             |
+===========================+===============================================+
| **1. On/Off**             | Enable/disable the chat panel.                |
|                           | When enabled, you will receive notifications  |
|                           | for incoming chats.                           |
+---------------------------+-----------------------------------------------+
| **2. Waiting Customers**  | Lists customers awaiting an agent for chat.   |
|                           | Click to answer a pending chat request.       |
+---------------------------+-----------------------------------------------+
| **3. Chatting Customers** | Lists customers currently in an ongoing chat  |
|                           | session.                                      |
+---------------------------+-----------------------------------------------+
| **4. Active Agents**      | Lists all agents with chat enabled.           |
+---------------------------+-----------------------------------------------+
| **5. Settings**           | Click for chat configuration options (e.g.    |
|                           | auto-greetings and maximum number of          |
|                           | simultaneous chats).                          |
+---------------------------+-----------------------------------------------+
| **6. Count badge**        | Displays the number of users in each section. |
+---------------------------+-----------------------------------------------+
| **7. Info card**          | Hover over for detailed information about the |
|                           | users in each section.                        |
+---------------------------+-----------------------------------------------+

.. warning:: If all agents have the chat panel disabled, customers will **not**
             be able to initiate a chat.

Usage tips
   - Use the :ref:`search bar <search-tickets>` to pull up old chats from the
     archive anytime.
   - Inline images are supported by copy & paste as well as plain text.
   - You can use :doc:`text modules </advanced/text-modules>`.
   - Chats can be renamed or tagged
   - Chats record technical details about the customer's connection.

      .. figure:: /images/extras/chat/chat-details.png
         :alt: Screenshot shows chat details of an opened chat.
         :align: center
         :scale: 30%

         Click on the title at the top of the chat window to edit chat details.

Creating a Ticket from a Chat
-----------------------------

Once your chat is over, you can create a ticket for it with a single click:

.. figure:: /images/extras/chat/chat-create-ticket.jpg
   :alt: Completed chat window
   :align: center

   The ``Turn chat into ticket`` button appears as soon as the chat is finished.

.. figure:: /images/extras/chat/chat-new-ticket-dialog.jpg
   :alt: New ticket view
   :align: center

   A link to the chat is automatically included in the first article of the ticket.

