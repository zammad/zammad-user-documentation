Macros
======

Macros are a great way to reduce your workload by automating specific actions 
with less clicks. 

.. note:: 🤔 **Huh? I can't configure Macros ...**

   Macros are globally configured by administrators. 
   If you're an administrator, you can learn more in our 
   `Admin-Documentation <https://admin-docs.zammad.org/en/latest/manage/macros.html>`_.

... within a ticket view
------------------------

You can run macros from within a ticket view. To do so, click on the △ Arrow 
to open the macro list. After clicking on the desired macro, Zammad will 
automatically run it.

   .. figure:: /images/advanced/macros/macro-run-via-ticket-view.gif
      :width: 90%
      :align: center
      :alt: Screencast showing how to run a macro within a ticket view.


.. tip:: 🤓 **Running a macro does count as "updating".**

   This means: You can always set more :ref:`ticket_settings` *before* running 
   the macro. This allows you to update tickets once, not twice. This also 
   works for articles. 🤟

   | **However, keep in mind...**
   | Macros will always overwrite manual settings. 

   This means: If you're going to write an email article but your macro 
   also adds a note article, the email article will be lost!

      .. figure:: /images/advanced/macros/macro-overwriting-article-sample.gif
         :width: 80%
         :align: center
         :alt: Screencast showing above described effect that overwrites articles.

... within an overview (bulk operation)
---------------------------------------

.. note:: ⚠ **Bulk operations come with a trade...**

   Not for your soul, but some actions will not work. 
   This affects the creation of articles and the "stay on tab" behavior. 

Some operations do not require any deeper checking of tickets in detail. 
This can apply to spam tickets or workflows that are always the same.

In these situations you can run macros on one or more tickets within the 
overviews. To do so, select the tickets in questions and hold your left mouse 
button down. Pull the mouse into any direction. Zammad will now provide bulk 
operation options (running a macro or direct assignment) - in this case we'll 
move up the the macros. As soon as you let go of your mouse button, the macros 
will run.

   .. figure:: /images/advanced/macros/macro-usage-via-overview.gif
      :width: 90%
      :align: center
      :alt: Screencast showing how to run macros via overviews.
