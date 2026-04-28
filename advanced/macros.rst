Macros
======

If you have many steps you do over and over again, you should use a macro for
that. In such a macro, your admin can pre-define different ticket actions you
can apply with just a click. As an example, Zammad ships a
**Close & Tag as Spam** macro by default. If applied, the user who executes the
macro is assigned as owner, a tag ``spam`` is added and the ticket is closed.
It is even possible to run an :ref:`AI agent <ai-agents>` within a macro on
demand.

Macros can be applied in two ways: on a single ticket or in bulk.

On a Single Ticket
------------------

The simplest way to apply a macro is to select it from the **Update ^** submenu
in the ticket detail view:

.. figure:: /images/advanced/macros/macro-run-via-ticket-view.png
   :align: center
   :alt: Screenshot shows the ticket update menu with to run a macro.

.. tip:: 💾 **Macro = Update**

   If you've made any changes (including typing up a reply to the customer),
   applying a macro will save/send them too.

   ⚠️ **But beware:** in the event of a conflict,
   the macro's actions override any manual changes -
   including messages to the customer!
   When in doubt, apply your macro and your manual changes *separately.*


In Bulk
-------

To apply a macro to many tickets at the same time:

1. Open a ticket overview
2. Select your desired tickets
3. Drag the tickets to the top and hover over the **Run Macro** action
4. Drop the tickets on your target macro.

.. figure:: /images/advanced/macros/macro-usage-via-overview.gif
   :width: 90%
   :align: center
   :alt: Screencast showing how to run macros via overviews.

.. note:: ☝️ **There's just one difference...**
   When running a macro from the ticket detail view, Zammad may automatically
   open the next ticket (or close the current one, or just stay on it),
   depending on how the macro was set up. When running it from the overviews
   page, Zammad will always stay on the overviews page.
