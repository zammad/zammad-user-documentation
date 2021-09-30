Browse for Tickets
==================

Looking for a ticket to work on? Check the **overviews** menu.

.. figure:: /images/basics/find-ticket/browse.jpg
   :alt: Sample view of Overviews
   :align: center

   Click **Overviews** in the main menu to browse tickets.

.. hint:: 📥 Think of overviews as **inboxes**, each with a different filter
   for the tickets it displays.

There are **six built-in overviews**
(Zammad admin may `create more`_ with custom-defined filters):

* **My assigned tickets** (*open/pending* only)
* **Unassigned & Open**
* **My pending reached tickets** (previously marked *pending* and currently due)
* **Open** (system-wide)
* **Pending reached** (system-wide, previously marked *pending* and currently due)
* **Escalated** (system-wide, failing to meet a `service-level agreement`_)

.. _create more: https://admin-docs.zammad.org/en/latest/manage/overviews.html
.. _service-level agreement:
   https://admin-docs.zammad.org/en/latest/manage/slas.html

.. tip:: **🖱️ UI Protip**

   * Click on column headings to change the display order.
   * Click-and-drag column dividers to adjust their width.
   * :doc:`Ticket states </basics/service-ticket/settings/state>` are
     **color-coded:**

     .. include:: /snippets/ticket-state-type-circles.rst
   * :doc:`Ticket priorities </basics/service-ticket/settings/priority>` are
     **color-coded:**

     .. figure:: /images/basics/service-ticket/settings/priority-colors.png
        :alt: Overview showing 3 tickets with different priorities
        :align: center

        Zammad's 3 default priorities allow you to see the importance of
        your tickets better.
