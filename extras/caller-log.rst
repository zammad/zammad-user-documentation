Caller Log
==========

View and manage call logs from the **phone** panel.

.. figure:: /images/extras/caller-log/call-entries.png
   :alt: Sample view of Caller Log
   :align: center

   Enable the **Phone** panel to receive notifications for incoming calls.

.. note:: **🤔 Huh? I don’t see “Phone” in the menu...** 

   This feature is **optional**;
   if you don’t see it in the main menu,
   that means your administrator hasn’t enabled it yet.
   Administrators can learn more on our
   :admin-docs:`admin documentation </system/integrations.html#integrations-for-phone-systems>`.

.. hint::
   🏢 The caller log shows all incoming and outgoing calls
   **for the entire instance**. The number of entries shown depends on the
   configuration your admin chose.

The caller log offers a lot more than just the last call entries.
If your administrator configured "Phone Extension to Agent Mapping", Zammad
will also help you during answering calls.

   New Ticket dialogue
      Zammad will open a new ticket dialogue if:

         * it's able to either guess a single user (see `maybe entries`_)
         * the callers number belongs to a user known to Zammad
         * the callers number is yet unknown

      If the user is known to Zammad it will automatically set the ticket
      customer for you. You can correct this at any time if needed.

   User profile
      Zammad will open the users profile if your user had a customer ticket that
      has been updated within the last 30 days. This also applies for calling
      users that Zammad guesses are a specific user
      (only if it's one guessed user).

   Quick dial
      You can click on phone numbers (user profiles and caller log) to dial
      the number in question quickly.

         .. note::

            This requires either a soft phone client or CTI client on your
            computer that supports this action.

.. _maybe entries:

.. note:: **😕 What are these "maybe" entries?**

   During your day by day communication you may also stumble over new customers.
   Usually business users send their phone numbers in their signature.

   Zammad collects and aggregates these information and tries to guess the
   customer in case it receives a call from an unknown number.

   .. figure:: /images/extras/caller-log/maybe-entries.png
      :alt: Screenshot showing a caller log entry that's classified with "maybe:"

.. tip::

   👤 Click on unrecognized numbers to **create a new customer** or maybe
   entries to **update an existing customer**.

   (Unrecognized phone numbers cannot be added to existing customers in
   this way. Copy and pasting is required.)

      .. note::

         Existing caller log entries *are not* updated.

