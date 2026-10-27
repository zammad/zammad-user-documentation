i-doit: Track Company Property
==============================

With the `i-doit <https://www.i-doit.com/>`_ integration, you can list which
pieces of your company's property are related to any given ticket. That includes
both physical and digital infrastructure, from servers to meeting rooms to
virtual machines to software licenses. It can help you keep track of
troublesome equipment and find previous tickets about the last time an object
caused problems.

This feature is optional. If you don't see it in the ticket view, that means
your administrator hasn't enabled it yet. Zammad's ticket sidebar and the
ticket list in i-doit are set up separately, so your administrator may enable
one of them without the other. Administrators can learn more in the
:admin-docs:`i-doit integration in the admin documentation </system/integrations/i-doit.html>`.
If your company is using i-doit, ask your administrator / IT personnel to give
you a tour. If your organization isn't already using i-doit, this guide is
not for you.

.. figure:: /images/extras/i-doit-track-company-property/ticket-with-assets.png
   :alt: (Screenshot) The i-doit integration menu in the ticket view
   :scale: 50%
   :align: center

   The **i-doit** panel in the ticket sidebar lists the objects linked to a
   ticket.

Link i-doit Objects to Tickets in Zammad
----------------------------------------

First, add i-doit objects to a ticket in the ticket sidebar. In the printer
tab, select **Change Objects** in the **i-doit** panel, then filter by type and
name. The search matches object names only and returns at most 10 results, so
pick a type to narrow it down.

.. figure:: /images/extras/i-doit-track-company-property/asset-dialog.png
   :alt: (Screenshot) The i-doit object picker with type filter and search field
   :align: center

   Select the objects to link, then use the ``Submit`` button.

Once objects have been linked to a ticket, click an object in the ticket
sidebar to open its page in i-doit. The sidebar always shows the current data
from i-doit: a renamed object appears under its new name, and an object deleted
there drops off the list. Use the **Unlink object** icon next to an entry,
which unlinks it from the ticket in Zammad and doesn't delete anything in
i-doit.

List & Create Tickets in i-doit
-------------------------------

In i-doit, an object's page should contain a list of all the tickets associated
with it. Click **All Tickets** in the object toolbar to list them, then use the
**Open in ticketsystem** link in a ticket row to open the ticket in Zammad. You
can even launch Zammad's new ticket dialog directly from i-doit, with the
object already linked. Use **Create ticket** in the **All Tickets** panel to
start it.
