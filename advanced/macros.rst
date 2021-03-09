Macros
======

Macros are **🖱️ one-click shortcuts** for applying changes to a ticket.

If you find yourself making the same changes to lots of tickets
(*e.g.,* close-and-tag-as-spam or reassign-to-another-group),
macros can make the job a whole lot easier.

.. note:: 🤔 **How do I make macros?**

   You don’t – that’s the `administrator’s job
   <https://admin-docs.zammad.org/en/latest/manage/macros.html>`_.
   If you have an idea for a macro you’d like to use,
   your Zammad admin can probably make it happen.

Macros can be applied in one of two ways:
on a single ticket, or in bulk.

On a Single Ticket
------------------

The simplest way to apply a macro is to select it
from the **Update ᐱ** submenu in the Ticket View:

.. figure:: /images/advanced/macros/macro-run-via-ticket-view.gif
   :width: 90%
   :align: center
   :alt: Screencast showing how to run a macro within a ticket view.

.. tip:: 💾 **Macro = Update**

   If you’ve made changes to any other
   :ref:`settings on the ticket <ticket_settings>`
   (including typing up a reply to the customer),
   applying a macro will save them, too.

   ⚠️ **But beware:** in the event of a conflict,
   the macro’s actions override any manual changes –
   including messages to the customer!
   When in doubt, apply your macro and your manual changes *separately.*

   .. figure:: /images/advanced/macros/macro-overwriting-article-sample.gif
      :width: 80%
      :align: center
      :alt: Screencast showing above described effect that overwrites articles.

      If the selected macro adds a note to the ticket, any text entered in the message composer will be lost.

In Bulk
-------

To apply a macro to many tickets at the same time:

1. open a ticket overview;
2. select your desired tickets;
3. click-and-drag to open the “Run Macro” drawer; and
4. drop the tickets on your target macro.

.. figure:: /images/advanced/macros/macro-usage-via-overview.gif
   :width: 90%
   :align: center
   :alt: Screencast showing how to run macros via overviews.

.. note:: ☝️ **There's just one difference...**
   When running a macro from the ticket view, Zammad may automatically open the
   next ticket (or close the current one, or just stay on it), depending on how
   the macro was set up.
   
   When running it from the overviews page, Zammad will always stay on the
   overviews page.
