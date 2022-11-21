.. _ticket_templates:

Ticket Templates
================

If you find yourself creating lots of tickets with the same basic attributes,
use **ticket templates** to fill them in with a single click next time.

.. figure:: /images/advanced/ticket-templates.png
   :alt: Ticket template selection in new ticket dialog
   :align: center

   Use the ticket pane to load ticket templates.

On any *new ticket* dialogue use the 🗒️ tab on the right to display the
*Templates* column. If Zammad has any templates for you to apply, you'll
be provided with a drop down list to choose from.

Select a fitting template and press *Apply*.
The configured ticket fields will be populated with the data from the template.

.. warning::

   With version 5.3 Zammad is able to detect "dirty fields".
   This means: If you previously filled in data in a field that's supposed to be filled
   by the template, Zammad *will not* overwrite the field with the template data.

   Instead it will keep your version of the field.
   This allows you to e.g. fill in the customer before applying the template. 🎉

.. note:: **😖 I can't add or adjust templates?!**

   Managing templates requires additional permissions.
   Please ask your administrator to provide you with the needed permission.

   `Learn more about ticket templates in the admin documentation`_.

   This permission was introduced with Zammad 5.3.

   .. These version notes will be removed on later documentation versions.

.. _Learn more about ticket templates in the admin documentation:
   https://admin-docs.zammad.org/en/latest/manage/templates.html
