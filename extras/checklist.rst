Checklist
=========

General
-------

Use a checklist in tickets to keep track of the tasks to be completed. You can
find the checklist feature in the right sidebar in the "Checklist" tab (unless
your admin has deactivated it). Please note that you can only add or edit a
checklist, if you have the permission to edit the ticket.

.. figure:: /images/extras/checklist/checklist-sidebar-highlight.png
   :alt: Screenshot showing right sidebar with highlighted "Checklist" tab

   Screenshot of ticket view with highlighted checklist sidebar.

Usage
-----

Basics
^^^^^^

If you want to add a checklist to a ticket, go to the "Checklist" tab and click
either on "Add empty checklist" (1) or "Add from template" (2) after selecting
a template. If you can't see the the "Add from template" area, there is no
template available.

.. figure:: /images/extras/checklist/checklist-creation.png
   :alt: Checklist creation dialog
   :align: center
   :scale: 50%

   Screenshot of adding template or new checklist.

Depending on your choice, you can create your own new checklist or use a
predefined template. In both cases, you can:

- Edit the checklist title
- Edit the checklist items (reorder, rename, add, delete)
- Remove the complete checklist
- Add a checklist, if there is no existing one

You can perform most of these edit, add and delete actions on different ways:

- Click on the item text (checklist title or checklist item) to edit it
- Click on the checkbox to check an item
- Click on the ︙ or on the "Checklist" title to select actions from the menu
- To add an item, click on the "+ Add" button
- To reorder them, use the corresponding button. You can then drag & drop the
  items via the ≣ handle.

.. figure:: /images/extras/checklist/checklist-edit.png
   :align: center
   :scale: 80%

   Screenshot of editing an item by simply clicking on it.

Additional Features
^^^^^^^^^^^^^^^^^^^

Refer to other tickets in the checklist
   You can add another ticket as a checklist item by typing or pasting its hook
   and number into the item label (e.g. ``Ticket#423456``). This item is not
   manually checkable but reflects the state of the referenced ticket.

   .. tip:: **Copying ticket hook and number**

      To copy the ticket hook and number from another ticket, click on the copy
      button at the top or use the keyboard shortcut :kbd:`.` in that ticket.

Check of completed checklist
   Zammad includes a feature to automatically check if all checklist items are
   completed. The check is performed when you set a ticket to closed.
   If not all items are completed, Zammad will prompt you to either work on the
   remaining tasks and keep the ticket open or to close it anyway.

   When referencing other tickets in your checklist, only those which are
   closed (with a green circle) are considered as completed.


