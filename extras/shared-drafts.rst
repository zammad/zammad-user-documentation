Shared Drafts
=============

Share drafts for new or existing tickets with other agents of your group.
Load, modify and safe an existing draft e.g. as QA process with colleagues.

.. figure:: /images/extras/shared-drafts/ticket-zoom-with-activated-shared-draft-function.png
   :alt: Screenshot showing the sub menu of the Update button with macros and an
         option to save the draft
   :align: center

   By using ᐱ next to the "Update" button Zammad will provide you with an option
   to save your draft (and thus share it) if the option is enabled.

.. note:: **🤔 Huh? I don’t see “Share Draft” option...** 

   This feature is **optional**; if you don’t see it in the menu,
   that means your administrator disabled this function.
   Administrators can learn more in our `admin documentation`_.

.. _admin documentation:
   https://admin-docs.zammad.org/en/latest/manage/groups/settings.html

.. hint:: **🤓 Let's be clear up front**

   Zammad technically has two draft functions:

      * shared draft (allow others to load the draft), and
      * user drafts.

   | Every time you change a tickets field, Zammad will safe this in your
     personal draft. You then can share this as a shared draft if you want to.
   | User drafts are *always* available!

Handling drafts
---------------

.. note::

   Shared draft handling is the same for existing tickets and new tickets. 🙏

Load a draft
   .. figure:: /images/extras/shared-drafts/loading-a-shared-draft-ticket-zoom.gif
      :alt: Screencast showing how to open the shared draft load dialogue within
            the ticket zoom

   Loading a draft works the same starting from draft previews.

      .. include:: /extras/includes/shared-drafts-overwriting-drafts-warning.include.rst

   New Ticket dialogue
      If you're in a new ticket dialogue *after selecting the ticket group*,
      the 📝 button will indicate the shared drafts function to be available.

         .. note::

            The shared drafts tab is *always* hidden if no group is selected!

      .. figure:: /images/extras/shared-drafts/listing-existing-shared-drafts-in-new-ticket-dialogues.png
         :alt: Screenshot highlighting the shared draft pane for new
               ticket dialogues

   Existing tickets (Ticket zoom)
      Within ticket zooms a button "📝 Draft available" will be shown if a
      draft has been shared by either you or another agent on the ticket.

      Hovering over the button will tell you who has changed the draft last.

      .. figure:: /images/extras/shared-drafts/available-shared-draft-in-ticket-zoom.png
         :alt: Screenshot highlighting the Draft available button within
               Ticket zoom

   .. hint::

      Loading a shared draft, (adjusting and) updating the ticket with an
      article will cause Zammad to *remove* the shared draft.

         .. warning::

            This also applies if you're sharing the draft before submitting!
            Zammad expects that the draft is no longer needed.

Remove draft
   You can remove any draft (no matter if for new or existing tickets) from
   within the draft preview screen. Use the "Delete" link on the lower end of
   the dialogue.

      .. hint::

         This has no effect on local drafts agents may have loaded already.

   .. figure:: /images/extras/shared-drafts/remove-shared-drafts.png
      :alt: Screenshot highlighting the removal option in shared draft preview

Saving drafts
-------------

.. include:: /extras/includes/shared-drafts-overwriting-drafts-warning.include.rst

New ticket
   Adding new drafts
      To save a new shared draft, set the ticket settings, customer, ticket
      title and article as desired. Make sure to select a group that supports
      shared drafts.

      If you're ready to save the draft, click on 📝 on the right ticket pane,
      enter a meaning full name and click on the "Create" button.

      .. figure:: /images/extras/shared-drafts/saving-current-new-ticket-dialogue-as-shared-draft.gif
         :alt: Screencast showing how to save new ticket dialogues as a
               shared draft

   Update existing drafts
      In order to update or rename existing shared drafts for new tickets,
      simply load the draft in question. Change the information (e.g. ticket
      settings or content) needed and, if needed, update the drafts name on the
      right hand side of the ticket.

      .. tip::

         This way you can not just update existing drafts, but also use existing
         drafts to create another copy!

      .. figure:: /images/extras/shared-drafts/renaming-shared-drafts-new-ticket-dialogue.gif
         :alt: Screencast showing how to rename / update existing shared drafts

Existing ticket
   Use the ᐱ button next to the update button. If the group of the ticket
   (or in your selection) allows shared drafts, Zammad will provide the option
   "Save Draft".

   All current changes on the ticket (ticket settings,
   article and it's attachments) will be saved to the shared draft.

   When saving was successful, the button "📝 Draft available" will be shown.

   .. figure:: /images/extras/shared-drafts/saving-a-shared-draft-within-ticket-zoom.gif
      :alt: Screencast showing how to save a shared draft within ticket zoom
