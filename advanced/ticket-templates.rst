.. _ticket_templates:

Ticket Templates
================

If you find yourself creating lots of tickets with the same basic attributes,
use **ticket templates** to apply them with a single click. Templates can be
used to pre-fill not only the article text. It is also possible to pre-fill
ticket attributes like title, customer, organization, group, owner, state,
priority and tags. Ask your administrator if you think such a template makes
sense for your workflow.

.. figure:: /images/advanced/ticket-templates.png
   :alt: Ticket template selection in new ticket dialog
   :align: center

In any **New Ticket** dialog, the right sidebar will display the
**Templates** tab if the feature is enabled and a template present. You can
choose from a drop down list to select the desired template.
Select a fitting template and click ``Apply``. The configured ticket fields
will be populated with the data from the template.

Field collisions
   Zammad detects field collisions. This means: If you already filled in data
   in a field that would be filled by the template, Zammad will not overwrite
   the data present.

Can't add or adjust templates?
   Managing templates requires additional permissions.
   Please ask your administrator to provide you with the needed permission or
   to create or adjust a template for you.

   Admins can learn more in the
   :admin-docs:`ticket templates section of the admin docs </manage/templates.html>`.
