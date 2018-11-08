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

.. tip:: **🖱️ UI Protip**

   * Click on column headings to change the display order.
   * Click-and-drag column dividers to adjust their width.
   * :doc:`Ticket states </basics/service-ticket/settings/state>` are **color-coded:**

     +-------+----------------------------------------------------+
     | |grn| | **Closed**                                         |
     +-------+----------------------------------------------------+
     | |blk| | **Postponed**                                      |
     |       | (Marked as pending; no immediate action required.) |
     +-------+----------------------------------------------------+
     | |ylw| | **New / Open** (Ready for action.)                 |
     +-------+----------------------------------------------------+
     | |red| | **Escalated**                                      |
     |       | (Requires urgent attention.)                       |
     +-------+----------------------------------------------------+

     .. |grn| raw:: html

        <div style="width: 1em; height: 1em; border-radius: 50%; border: 3px solid #31af68; margin: 0 auto"></div>

     .. |blk| raw:: html

        <div style="width: 1em; height: 1em; border-radius: 50%; border: 3px solid #43484c; margin: 0 auto"></div>

     .. |ylw| raw:: html

        <div style="width: 1em; height: 1em; border-radius: 50%; border: 3px solid #fcac01; margin: 0 auto"></div>

     .. |red| raw:: html

        <div style="width: 1em; height: 1em; border-radius: 50%; border: 3px solid #f45801; margin: 0 auto"></div>

.. _create more: https://zammad-admin-documentation.readthedocs.io/en/latest/manage-overviews.html
.. _service-level agreement: https://zammad-admin-documentation.readthedocs.io/en/latest/manage-slas.html
