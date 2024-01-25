Profile & Settings
==================

Click on your avatar or initials at the bottom of the main menu
to access your **profile and settings**.

.. figure:: /images/extras/profile-and-settings/profile-and-settings.png
   :alt: User submenu
   :align: center
   :scale: 50%

   Find user-specific actions,
   a list of recently opened items,
   and useful reference information.

User Menu
---------

Clicking on your avatar picture provides the following three sections in the
user menu:

Recently viewed
   All information you've viewed previously (tickets, users, organizations).
   Helps you to jump back quick and easy without searching or looking in your
   overviews. Note that this list is limited, old entries will automatically
   vanish.

Further actions
   Dark mode
      Quickly toggle dark and light mode without using keyboard bindings.

      .. figure:: /images/extras/profile-and-settings/darkmode-switch-profile.gif
         :alt: Screencast showing the dark mode button being toggled

   Keyboard shortcuts
      :doc:`Opens the keyboard shortcut section </advanced/keyboard-shortcuts>`.

   Profile
      This will open your :ref:`user-profile-settings` and provide further
      options for customers and agents. Customers do not have access to all
      areas, even if you provide them the permissions to those areas.

Sign out
   Finished working with Zammad? Use the sign out button to end your user
   session.

   If you didn't tick "Remember me" during login or used a third party login,
   your session will automatically be invalidated if you close and reopen your
   browser.

.. _user-profile-settings:

Profile Settings
----------------

Clicking on "Profile" in the user menu opens the profile settings.

:Appearance:

   Select how Zammad should look. Zammad will remember the setting you choose here.

      * Dark
      * Light
      * Sync with computer

   For dark and light you'll fix the dark or light mode to your taste.

   If you choose sync with computer, Zammad will dynamically select the mode
   depending on what your client prefers at that moment.

   Note that this sync option highly depends on your browser.
   If your browser does not support syncing, this setting basically
   has no effect. Most common modern Browsers are capable to do so
   (e.g. Firefox, Google Chrome).

:Language:

   Set the system display language.

:Avatar:

   Upload an avatar image.

:Password & Auth:

   Change your login password and manage your two-factor authentication methods
   (both may be disabled by system admin).

   .. hint::
      :doc:`Two-Factor Authentication </extras/two-factor-authentication>` is an
      optional feature. Administrators can learn more
      :admin-docs:`here </settings/security/two-factor.html>`.

:Notifications:

   Notifications
      Select where, when, and for which groups you want to receive notifications,
      or choose a new notification sound. Notifications are available to agents
      only.

      You can always reset your notification settings to system defaults
      by clicking on the button at the bottom of the screen.

      .. figure:: /images/extras/profile-and-settings/profile-and-settings-notifications-settings.jpg
         :align: center

         Use the first three columns to choose when to receive **internal
         notifications** (below). The rightmost column enables email notification
         as well.



   Limit Groups
      .. figure:: /images/extras/profile-and-settings/profile-and-settings-notifications-limit-groups.png
         :align: center

      By default, you will receive notifications for all tickets in every group
      you belong to - even for tickets that are assigned to other agents. Use
      the **Limit Groups** switch and settings below it to disable such
      notifications on a per-group basis. You will continue to receive
      notifications for your own tickets.

      If you turn on **Limit Groups** feature, but disable the notifications
      from all groups, you may receive the following warning.

      .. figure:: /images/extras/profile-and-settings/profile-and-settings-notifications-limit-groups-warning.png
         :align: center

      In this case, saving your settings will implicitly turn off **Limit
      Groups** feature, since no limits will be left in effect.

   .. hint:: The contents of these email notifications
      can be customized on self-hosted installations.
      Administrators can learn more
      :admin-docs:`here </manage/trigger/system-notifications.html>`.

:Out of Office:

    Schedule absence periods in advance, and designate a substitute to
    handle your tickets while you're gone.

    Your substitute will receive all your ticket notifications during your
    absence, and have a custom :doc:`overview </basics/find-ticket/browse>`
    created to help keep track of your tickets.

    You will reveive notifications while you are absent.

:Overviews:
   Tired of the overview order your admin decided on? This section allows
   you to choose an overview order that fits you the best.

   You can revert to the default instance ordering at any time by using
   the upper right button "Reset overview order".

   .. hint::

      This option is only visible to agents by default. It can be
      completely deactivated by your admin.

      If it is activated, the order does not change, even if your admin
      renames or reorders the overviews. The overview order is stored in your
      profile and thus applies to any device you use with your account.


   .. figure:: /images/extras/profile-and-settings/custom-overview-order-users.gif
      :alt: Screencast showing how to drag & drop overviews order and reset the
            order back to default

:Calendar:

   Add your ticket deadlines to your own favorite calendar app with the ICAL
   link listed at this setting's panel.

:Devices:

   See a list of all devices logged into your Zammad account (and revoke
   access, if necessary).

:Token Access:

   Generate personal access tokens for third party applications to use the
   Zammad API.

   .. tip::
      Always generate a new token for each application you connect to
      Zammad! (This makes it possible to revoke access one
      application at a time if a token is ever compromised.)

:Linked Accounts:

   See a list of third party services (*e.g.,* Facebook or Twitter) linked to
   your Zammad account.
