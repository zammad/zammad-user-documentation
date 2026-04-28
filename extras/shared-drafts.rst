Shared Drafts
=============

Overview
--------

Share drafts for new or existing tickets with other agents of your group.
Load, modify and save an existing draft e.g. as QA process with colleagues.

This feature is **optional**; if you don't see it in the menu,
that means your administrator disabled this function.
Administrators can learn more in our
:admin-docs:`admin documentation </manage/groups/settings.html>`.

.. figure:: /images/extras/shared-drafts/save-draft-submenu-ticket-detail-view.png
   :alt: Screenshot shows highlighted ticket update menu with save draft option in ticket detail view.
   :align: center

   To save a draft, click the ``^`` next to the ``Update`` button. This opens
   a menu where you have the option to save your draft (and thus share it) if
   the option is enabled.

.. hint:: **🤓 Let's be clear up front**

   Zammad technically has two draft functions:

      * Shared drafts (allow others to load the draft)
      * User drafts

   | Every time you change a ticket's field, Zammad will save this in your
     personal draft. You then can share this as a shared draft if you want to.
     User drafts are *always* available!

Handling Drafts
---------------

.. include:: /extras/includes/shared-drafts-overwriting-drafts-warning.include.rst

Load a draft
   .. figure:: /images/extras/shared-drafts/loading-a-shared-draft.png
      :alt: Screenshot shows highlighted "Draft available" button and preview dialog of the shared draft.

   Loading a draft works the same starting from draft previews.

   New Ticket dialog
      If you're in a new ticket dialog *after selecting the ticket group*,
      the 📝 button will indicate the shared drafts function to be available.
      The shared drafts tab is *always* hidden if no group is selected!

      .. figure:: /images/extras/shared-drafts/ticket-create-shows-available-draft.png
         :alt: Screenshot shows the ticket creation dialog with highlighted shared draft after group selection.

   Existing tickets (Ticket zoom)
      In the ticket detail view, a button ``📝 Draft available`` is shown if a
      draft is available by you or another agent (see first screenshot on this
      page). Hovering over the button tells you who created or changed the
      draft.

Remove draft
   You can remove any draft (no matter if for new or existing tickets) from
   within the draft preview screen. Use the ``Delete`` link on the lower end of
   the dialog. This has no effect on local drafts, agents may have loaded
   already.

Saving drafts
   New ticket
      Adding new drafts
         To save a new shared draft, set the ticket settings, customer, ticket
         title and article as desired. Make sure to select a group that supports
         shared drafts.

         If you're ready to save the draft, click on 📝 on the right ticket pane,
         enter a meaningful name and click on the ``Create`` button.

         .. figure:: /images/extras/shared-drafts/new-ticket-create-draft.png
            :alt: Screenshot shows the new ticket dialog with the highlighted "create draft" section.

      Update existing drafts
         In order to update or rename existing shared drafts for new tickets,
         simply load the draft in question. Change the information (e.g. ticket
         settings or content) needed and, if needed, update the drafts name on the
         right hand side of the ticket. This way you can not just update
         existing drafts, but also use existing drafts to create another copy!

         .. figure:: /images/extras/shared-drafts/renaming-shared-drafts-new-ticket-dialogue.gif
            :alt: Screencast showing how to rename / update existing shared drafts

   Existing ticket
      Use the ``^`` button next to the ``Update`` button. If the group of the
      ticket (or in your selection) allows shared drafts, Zammad will provide
      the option **Save Draft**. All current changes on the ticket (ticket
      settings, article and its attachments) will be saved to the shared draft.

      When saving was successful, the button ``📝 Draft available`` will be shown.

      .. figure:: /images/extras/shared-drafts/saving-a-shared-draft-within-ticket-zoom.gif
         :alt: Screencast showing how to save a shared draft within ticket zoom
