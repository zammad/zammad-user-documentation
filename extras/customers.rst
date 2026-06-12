Customers
=========

Use the customer tab in the ticket sidebar to view and manage customer profiles.

Overview
--------

.. figure:: /images/extras/customers/customers.png
   :alt: Ticket sidebar (customer view)
   :align: center

   Click the 👨 tab in the ticket sidebar to see the customer's profile.

If the customer has other tickets too, you can see a summary when you
hover over the **open/closed** labels:

.. figure:: /images/extras/customers/customers-tickets-mouseover.png
   :alt: Customer ticket summary (mouseover)
   :align: center
   :scale: 80%

   Hover over the **open/closed** labels to see a summary of the customer's 
   other tickets.

Editing a Customer
------------------

To edit the customer's profile, use the ``Customer`` submenu and select
``Edit Customer``:

Customer submenu
   .. figure:: /images/extras/customers/customers-submenu.png
      :alt: Customer submenu
      :align: center
      :scale: 100%

      Click the ``Customer ▾`` heading to access additional actions.

Customer edit dialog
   .. figure:: /images/extras/customers/customers-edit-dialog.png
      :alt: Edit customer dialog
      :align: center
      :scale: 80%

      The edit customer dialog.

Most customer attributes are self-explanatory, but here are a couple that could
be unclear:

:Organization:

   Customers can optionally belong to organizations. Head over to the 
   :doc:`organization page <organizations>` to learn more.

:Secondary Organizations:

   Unlike (primary) organizations, you can assign several organizations to the
   user. These secondary organizations are not as highlighted as the primary
   ones in Zammad. However, the same behavior applies.

:VIP:

   Like the ticket priority, the VIP state doesn't actually do anything
   out-of-the-box. But admins can set up automation rules based on this value
   or use it as a filter for custom :ref:`overviews <overviews>`.
   Ask your administrator about how you should use this attribute.
