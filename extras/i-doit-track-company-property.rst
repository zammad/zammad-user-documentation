i-doit: Track Company Property
==============================

With `i-doit <https://www.i-doit.com/>`_ integration,
you can list which pieces of your company's property
are related to any given ticket.
That includes both physical and digital infrastructure,
from servers to meeting rooms to virtual machines to software licenses.

.. figure:: /images/extras/i-doit-track-company-property/ticket-with-assets.png
   :alt: (Screenshot) The i-doit integration menu in the ticket view
   :scale: 50%
   :align: center

   Use the 🖨 **printer** tab to view or manage a ticket's assets from i-doit.

.. note:: **🤔 Huh? I don't see a 🖨 printer tab...**

   This feature is **optional**;
   if you don't see it in the ticket view,
   that means your administrator hasn't enabled it yet.
   Administrators can learn more
   :admin-docs:`here </system/integrations/i-doit.html>`.

Why?
----

i-doit can help you keep track of troublesome equipment
and find previous tickets from the last time something went wrong with it.

It's also a great way to document quirks in the company's belongings:
Why haven't we upgraded this system from Windows Vista yet?
What did we decide to do about that faulty network switch?
And why does the coffee maker keep shutting off before it's finished? 🤬

So How Does It Work?
--------------------

.. hint:: 👨‍💻 **New to i-doit?**

   Ask your administrator / IT personnel to give you a tour—otherwise,
   the directions below might not make much sense.
   (And if your organization isn't already using i-doit,
   this guide is not for you.)

In Zammad: Link i-doit assets to tickets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, add i-doit assets to a ticket in the ticket pane:

.. figure:: /images/extras/i-doit-track-company-property/add-ticket-with-idoit-asset_via-zammad.gif
   :alt: (Screencast) Create a new ticket and link it to an i-doit asset
   :align: center

   Select **🖨 > i-doit > Change Objects**, then filter by category and/or name.

Once assets have been linked to a ticket, they can be accessed directly from the ticket view:

.. figure:: /images/extras/i-doit-track-company-property/quickjump-ticket-with-idoit-asset_via-zammad.gif
   :alt: (Screencast) Access an i-doit asset directly from the Zammad ticket view
   :align: center

   Click on a linked asset in the ticket pane to open its page in i-doit.

In i-doit: List & create tickets for a given asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your i-doit control panel should contain
a list of all the tickets associated with each asset:

.. figure:: /images/extras/i-doit-track-company-property/quickjump-ticket-with-idoit-asset_via-idoit.gif
   :alt: (Screencast) See a list of all tickets for an asset in i-doit
   :align: center

   Click the 💬 in the toolbar to list an asset's tickets.
   Use the **🔗 Open in ticketsystem** button to open the ticket in Zammad.

You can even launch Zammad's new ticket dialog directly from i-doit,
with the asset already linked for you:

.. figure:: /images/extras/i-doit-track-company-property/add-ticket-with-idoit-asset_via-idoit.gif
   :alt: (Screencast) Launch the new ticket dialog from within i-doit
   :align: center

   Use the **📄 Create ticket** button in the asset ticket list
   to start a new, pre-linked ticket dialog.
