Find Tickets
============

There are different ways to find tickets, depending on your use case.

.. _overviews:

Via Overviews
-------------

If you search for new tickets to work on, your first look should be in the
overview section.  This section gives you a rough overview. More details are
covered in a separate overview page.

You can either open it by clicking the **Overviews** button
in the navigation bar or use the keyboard shortcut :kbd:`o`. You can think of
overviews as some kind of ticket lists.
By default, there are some built in overviews. For example, there is
an overview called "Unassigned & Open Tickets" which might be a good starting
point.

- My Assigned Tickets: open tickets in which you are set as owner.
- Unassigned & Open Tickets: open tickets which don't have an owner set.
- My Pending Reached Tickets: tickets in which you are the owner, have
  the *pending reminder* state and the pending reminder time is reached.
- Open Tickets: open tickets.
- Pending Reached Tickets: tickets which have the *pending reminder* state and
  the pending reminder time is reached.
- Escalated Tickets: tickets which are escalated or will escalate in the next
  10 minutes.

Your Zammad admin may have created additional overviews. These are based on
conditions, which are basically rules, to define which ticket appears in which
overview.

.. figure:: /images/basics/find-ticket/browse.jpg
   :alt: Sample view of Overviews
   :align: center

   Click **Overviews** in the main menu to browse tickets.

You can adjust the overviews in some aspects:

- Click on a column heading to change the sorting.
- Click and drag column dividers to adjust the column's width.
- Adjust the order of the overviews in your
  :doc:`user profile </extras/profile-and-settings>`.

The need for action is color coded and reflects mainly the
:doc:`ticket states </basics/service-ticket/settings/state>`:

.. include:: /snippets/ticket-state-type-circles.rst

If you spot a circle with a blue/pink gradient, it indicates that an
:doc:`AI agent </extras/ai-features>` is currently working on the ticket.

:doc:`Ticket priorities </basics/service-ticket/settings/priority>` are
color-coded as well and help you to distinguish between the different
priorities:

.. figure:: /images/basics/service-ticket/settings/priority-colors.png
   :alt: Overview showing 3 tickets with different priorities
   :align: center

.. _search-tickets:

Via Search
----------

Looking for an a specific ticket? Use the **search bar**:

.. figure:: /images/basics/find-ticket/search.png
   :align: center
   :scale: 80%

   Results appear immediately under the search bar as you type.

It's not just for tickets! Results cover 💬 **chat logs**,
👨 **customers**, and 🏢 **organizations**, too.

**🔍 Here are just a few of the places the search engine will look:**

* 📝 message subject/content
* 👩 recipient names & email addresses
* 📎 text in file attachments (really!)
* 🏷️ user/organization metadata (e.g. notes stored on customer profiles)

You can find a detailed search document in our
`Advanced Search <../../advanced/search.html>`_ page.


.. figure:: /images/basics/find-ticket/search-details.png
   :align: center

   For detailed results,
   click the **Show Search Details →** link
   just above the autocomplete list.

.. tip:: **🖱️ UI Protip**

   Click on column headings to change the display order.