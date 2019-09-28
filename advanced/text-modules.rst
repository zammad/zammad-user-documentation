Working with Text Modules
=========================

Zammad offers so-called text modules.
Text modules will help you to improve your workflow, as you don't have to type your answer 
on every ticket by hand. You can simply choose a fitting text module and insert it into the E-Mail.

To access available text modules, simply type ``::`` within an article body. 
If you found the right text module, just press enter or click with your left mouse and Zammad will insert the modules Text at the place your cursor is.

.. image :: /images/advanced/text-modules/choose-text_from_text-module.png


.. Tip:: You can either scroll through all modules (mouse or direction keys), type the module name or enter a keyword (if keywords are set).

.. image :: /images/advanced/text-modules/using-text-modules.gif

.. note:: **🤔 How come some text modules don’t always appear?**
  
   Text modules can be tied to **groups**: that is, they only become active
   once the ticket you’re working on has been assigned to the appropriate
   group.
 
   .. figure:: /images/advanced/text-modules/group-dependent-textmodules.gif
      :alt: Group-dependent text modules

      Text modules are updated immediately when a new group has been
      selected—no need to click **Update**.


Text modules on ticket creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use text modules on ticket creation as well. On ticket creation, our :ref:`ticket_templates` might get handy too.


Changing text modules
^^^^^^^^^^^^^^^^^^^^^

For changing text modules, you need to have the permission to do so. 
Please refer to our `Admin-Documentation <https://admin-docs.zammad.org/en/latest/manage-text-modules.html>`_ for further information.



