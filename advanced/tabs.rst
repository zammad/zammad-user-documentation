Tabs
====

As you click through Zammad, you will see a list of entries appear in the main
menu area. These are your **open tabs.**

You can freely switch between open tabs without losing your work -
all unsaved changes are automatically backed up to the server.

.. figure:: /images/advanced/tabs/tabs-list.png
   :alt: Sample view of Tabs

   Tabs appear in the main menu as you visit different parts of the
   application.

**What items open in a new “tab”?**

   1. Existing tickets
   2. New tickets
   3. Users
   4. Organizations
   5. Omnisearch

.. tip:: **🖱️ UI Protip**

   * :doc:`Ticket states </basics/service-ticket/settings/state>` are
     **color-coded:**

     .. include:: /snippets/ticket-state-type-circles.rst

   * A **pulsing dot** means that a ticket has new activity since you last
     viewed it.
   * Drag and drop tabs to rearrange them.

Tab Behavior in Ticket Zooms
----------------------------

You may have noticed the "Stay on tab" button next to "Update" on the lower
right already. This behavior of a tab can be configured by your administrator
globally. You can overrule this setting based on your personal
preference.

.. figure:: /images/advanced/tabs/tab-behavior.png
   :width: 100%
   :alt: Tab behavior can be adjusted in tickets manually

To overrule your administrator's settings, simply choose the action
you prefer. Zammad will remember this preference until you change its setting.

Close tab
   Upon updating the ticket, Zammad will automatically close the tab.
   You'll be returned to the last view that was open.

Close tab on ticket close
   Ticket tabs will be closed only if you change the state to "closed" upon
   ticket update.

   This does not apply for pending states that end in closed states.

Next in overview
   If you opened a ticket from any overview, Zammad will jump to the next
   ticket in said overview. Zammad recycles the open tab.

   This option is only available if you open the ticket from an overview.
   Zammad will ignore the setting if you opened the ticket directly
   and fall back to ``Stay on tab``.

Stay on tab
   Updating the ticket doesn't have any effect on the tab.

   *This is the default setting in Zammad installations.*
