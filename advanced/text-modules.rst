Working with Text Modules
=========================

Zammad offers so-called text modules.
Text modules will help you to improve your workflow, as you don't have to type
your answer on every ticket by hand. You can simply choose a fitting text
module and insert it into the e-mail.

To access available text modules, simply type ``::`` within an article body.
If you found the right text module, just press enter or click with your left
mouse and Zammad will insert the modules Text at the place your cursor is.

.. figure:: /images/advanced/text-modules/choose-text_from_text-module.png
   :alt: Screenshot shows text module selection menu in editor after typing "::" followed by "tf".
   :align: center

You can either scroll through all modules by using the mouse or arrow keys, type
the name or a keyword (if keywords are set) to find the text module you want to
use.

Text Modules Missing?
---------------------

You noticed that some text modules don't always appear?
Text modules can be tied to **groups**: if that's the case, they are only
available once the ticket you're working on has been assigned to the appropriate
group. The group dependent text modules are available immediately when a new
group has been selected, you don't have to click ``Update``.

But how do you know which groups go with which text modules? Ask your
administrator!

Text Modules on Ticket Creation
-------------------------------

You can use text modules on ticket creation as well. On ticket creation,
our :ref:`ticket_templates` might get handy too.

Customizing Text Modules
------------------------

Administrators can learn more about customizing text modules
:admin-docs:`here </manage/text-modules.html>`.
