Using i-doit assets on Tickets
==============================

Zammad allows you to combine i-doit assets with tickets. 
This way you'll be able to see if a device is especially unreliable.

.. figure:: /images/extras/i-doit/ticket-with-assets.png
   :alt: Screenshot showing a ticket with assigned i-doit assets
   :scale: 50%
   :align: center

   Use the 🖨 **printer** tab to display or add i-doit assets of a ticket.

.. note:: **🤔 Huh? I don’t see a 🖨 printer icon...** 

   This feature is **optional**;
   if you don’t see it in the ticket view,
   that means your administrator hasn’t enabled it yet.
   Administrators can learn more
   `here <https://admin-docs.zammad.org/en/latest/system/integrations/i-doit.html>`_.

What is i-doit?
---------------

i-doit is an assesment management tool that helps you to document your infrastructure. 
This is not just useful for IT departments, but in general every apartment that does have 
assets in some way (even air condition does count as asset!).

It basically helps you to overview those little things and fine tune it with additional 
information that help you to understand e.g. why a system has had a specific style of 
installation, even though it's not your company standard. 🙌

Adding i-doit assets on new or existing tickets
-----------------------------------------------

There are two ways to add i-doit assets to a Zammad ticket:

via Zammad
   .. hint:: Adding assets via Zammad doesn't just work for new tickets, but also 
      existing ones. Just use the 🖨 printer icon on the right to do so!

   During creation of a new ticket, you can switch to the 🖨 i-doit tab. 
   Here you can click on "i-doit ▼" → "Change Objects". Within the new dialogue you can 
   then filter for a category or search for the name of an asset directly on the right site.

   .. figure:: /images/extras/i-doit/add-ticket-with-idoit-asset_via-zammad.gif
      :alt: Screencast showing how to create a new ticket together with an i-doit asset.
      :align: center

via i-doit
   If you're working in i-doit right now but need to create a ticket in Zammad, you 
   can start that process via i-doit right away. To do so, click on 💬 to view the 
   ticket list of that asset. You can then click on "📄 Create ticket" to create a 
   new Zammad ticket. During this process, i-doit already provided the assets name - 
   you won't have to add it manually!

   .. figure:: /images/extras/i-doit/add-ticket-with-idoit-asset_via-idoit.gif
      :alt: Screencast showing how to create a new ticket via i-doit.
      :align: center

Quick jumping between i-doit and Zammad
---------------------------------------

Sometimes the bare asset or ticket information is not enough. This is why Zammad and 
i-doit allow you two directly jump to the asset or ticket in question, allowing you 
to work as fast as possible.

via Zammad
   Zammad will list all connected i-doit assets of a specific ticket within the details view. 
   To jump directly to a specific assets, simply press on the 🖨 printer tab to show all assets. 
   If you found the asset of your interest, click on it's name to jump to your i-doit instance.

   .. figure:: /images/extras/i-doit/quickjump-ticket-with-idoit-asset_via-zammad.gif
      :alt: Screencast showing how to clickly jump to an i-doit asset from a Zammad ticket.
      :align: center

via i-doit
   i-doit allows you to list asset specific tickets in it's interface. 
   To do so, click on 💬 to view the ticket list of that asset. 
   If you found the ticket you were looking for, just click on "🔗 Open in ticketsystem" 
   to show the ticket within Zammad.

   .. figure:: /images/extras/i-doit/quickjump-ticket-with-idoit-asset_via-idoit.gif
      :alt: Screencast showing how to clickly jump to existing Zammad tickets from i-doit.
      :align: center