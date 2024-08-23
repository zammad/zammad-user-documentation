Keyboard Shortcuts
==================

Zammad supports a wide array of keyboard shortcuts to expedite your workflow as
an expert user. But don't be afraid, you don't have to remember all of them.

Overview
--------

Click on your avatar at the bottom of the main menu and select "Keyboard
Shortcuts" or just press :kbd:`?` to open the keyboard shortcut overview.

.. figure:: /images/advanced/profile-shortcuts.png
   :alt: User submenu
   :align: center
   :scale: 85%

This will open an overview of available keyboard-shortcuts as in the following
screenshot:

.. figure:: /images/advanced/keyboard-shortcuts.png
   :alt: Keyboard shortcut cheat sheet
   :align: center
   :scale: 85%

   The keyboard shortcut overview.

Settings
--------

At the top of the dialog, you can:

- Enable or disable the shortcuts in general by switching the toggle on the
  left side.
- Switch to the old shortcuts if you got used to them by
  clicking on "Switch back to old layout" on the right side.

.. note:: Be aware that
   these old shortcuts don't work as reliable as the new ones because browsers
   and operating systems could jam the key press signal. And the shortcut for
   opening this overview differs as well.

These settings are currently only saved in the browser and not in your user
profile. If you need to deactivate it or switch to the old layout, you should
make sure to not delete your browser cache / session cookies for your Zammad
instance.

.. figure:: /images/advanced/keyboard-shortcuts-settings.png
   :alt: Keyboard shortcut settings
   :align: center
   :scale: 85%

   The keyboard shortcut settings.

List of Available Keyboard Shortcuts
------------------------------------

Navigation
^^^^^^^^^^

========================================   =================================================
Key / key combination                      Function
========================================   =================================================
:kbd:`h`                                   Show dashboard
:kbd:`o`                                   Show overviews
:kbd:`s`                                   Open the search
:kbd:`a`                                   Open notifications
:kbd:`n`                                   Create a new ticket
:kbd:`u`                                   Open user menu
:kbd:`?`                                   Open shortcuts overview
:kbd:`shift` :kbd:`l`                      Log out
:kbd:`shift` :kbd:`w`                      Close current tab
:kbd:`shift` :kbd:`→`                      Show next tab
:kbd:`shift` :kbd:`←`                      Show previous tab
:kbd:`shift` :kbd:`enter`                  Confirm/submit in dialogs
:kbd:`▲` / :kbd:`▼`                        Move selection/cursor up and down
:kbd:`◀` / :kbd:`▶`                        Move selection/cursor left and right
:kbd:`enter`                               Select item / confirm
:kbd:`.`                                   Copy current object number (e.g. ticket number)
:kbd:`..`                                  Add the title of the object to the number
:kbd:`...`                                 Add the object link URL to the number and title
========================================   =================================================


Translations
^^^^^^^^^^^^
Note: you need to have admin permissions to use this.

========================================   =================================================
Key / key combination                      Function
========================================   =================================================
:kbd:`t`                                   Enable or disable the inline translation
========================================   =================================================


Appearance
^^^^^^^^^^

========================================   =================================================
Key / key combination                      Function
========================================   =================================================
:kbd:`d`                                   Switch between dark and light mode
========================================   =================================================

Tickets
^^^^^^^

========================================   =================================================================
Key / key combination                      Function
========================================   =================================================================
:kbd:`x`                                   Create a new note article
:kbd:`r`                                   Reply to the last article
:kbd:`i`                                   Switch the visibility of the article between internal and public
:kbd:`shift` :kbd:`c`                      Set state of the ticket to "closed"
:kbd:`◀` / :kbd:`▶`                        Navigate through article
:kbd:`::`                                  Insert text module (while composing an article)
:kbd:`??`                                  Insert knowledge base article (while composing an article)
:kbd:`@@`                                  Mention a user (while composing an article)
========================================   =================================================================

Text Editing
^^^^^^^^^^^^

How
   You can apply a text format *before* typing or *after* typing. Example:

   Before typing:

   * Press :kbd:`ctrl` :kbd:`i` to enter *italics* mode,
   * enter your desired text, and
   * press :kbd:`ctrl` :kbd:`i` again to return to normal text mode.

   After typing:

   * Enter your desired text,
   * click-and-drag with the mouse to select it, and
   * press :kbd:`ctrl` :kbd:`i` to set the text in *italics*.

Key Combinations
   ========================================   =================================================
   Key / key combination                      Function
   ========================================   =================================================
   :kbd:`ctrl` :kbd:`u`                       Format text underlined
   :kbd:`ctrl` :kbd:`b`                       Format text in **bold**
   :kbd:`ctrl` :kbd:`i`                       Format text in *italics*
   :kbd:`ctrl` :kbd:`s`                       Format text as  ̶s̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶
   :kbd:`ctrl` :kbd:`v`                       Paste text from clipboard
   :kbd:`ctrl` :kbd:`shift` :kbd:`v`          Paste text from clipboard (as plain text)
   :kbd:`shift` :kbd:`ctrl` :kbd:`f`          Remove formatting of text
   :kbd:`shift` :kbd:`ctrl` :kbd:`y`          Remove formatting of the whole text
   :kbd:`shift` :kbd:`ctrl` :kbd:`z`          Insert a horizontal line
   :kbd:`shift` :kbd:`ctrl` :kbd:`l`          Format as unordered list
   :kbd:`shift` :kbd:`ctrl` :kbd:`k`          Format as ordered list
   :kbd:`shift` :kbd:`ctrl` :kbd:`1`          Format as h1 heading
   :kbd:`shift` :kbd:`ctrl` :kbd:`2`          Format as h2 heading
   :kbd:`shift` :kbd:`ctrl` :kbd:`3`          Format as h3 heading
   :kbd:`shift` :kbd:`ctrl` :kbd:`x`          Remove any hyperlink
   ========================================   =================================================

.. tip:: If you are a Mac user, use :kbd:`cmd` instead of :kbd:`ctrl` and
   :kbd:`ctrl` :kbd:`option` instead of :kbd:`ctrl` :kbd:`shift`.
