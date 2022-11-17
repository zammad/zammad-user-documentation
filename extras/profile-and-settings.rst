Profile & Settings
==================

Click on your avatar at the bottom of the main menu
to access your **profile and settings**.

.. figure:: /images/extras/profile-and-settings/profile-and-settings.png
   :alt: User submenu
   :align: center
   :scale: 50%

   Find user-specific actions,
   a list of recently opened items,
   and useful reference information.

Clicking on your avatar picture provides the following three sections.

Recently viewed
   All information you've viewed previously (Tickets, Users, Organizations).
   Helps you to jump back quick and easy without searching or looking in your
   overviews.

   .. note:: This list is limited, old entries will automatically vanish.

Further actions
   Dark mode
      Quickly toggle dark and light mode without using keyboard bindings.

      .. figure:: /images/extras/profile-and-settings/darkmode-switch-profile.gif
         :alt: Screencast showing the dark mode button being toggled

   Keyboard shortcuts
      :doc:`Opens the keyboard shortcut section </advanced/keyboard-shortcuts>`.

   Profile
      This will open your :ref:`user-profile-settings` and provide further
      options for customers and agents.

      .. note::

         Customers do not have access to all areas, even if you provide them
         the permissions to those areas.

Sign out
   Finished working with Zammad? Use the sign out button to destroy your user
   session.

   .. hint::

      If you didn't tick "Remember me" during login or used a Third-Party login,
      your Session automatically gets invalid if you close and reopen your
      Browser.

.. _user-profile-settings:

Profile Settings
----------------

:Language:

   Set the system display language.

:Avatar:

   Upload an avatar.

:Password:

   Change your login password (may be disabled by system admin).

:Notifications:

   Select where, when, and for which groups you want to receive notifications,
   or choose a new notification sound.

   .. figure:: /images/extras/profile-and-settings/profile-and-settings-notifications-settings.jpg
      :align: center

      Use the first three columns to choose when to receive **internal
      notifications** (below). The rightmost column enables email notification
      as well.

   .. figure:: /images/extras/profile-and-settings/profile-and-settings-notifications-center.jpg
      :align: center

      Internal notifications cannot be disabled.

   .. figure:: /images/extras/profile-and-settings/profile-and-settings-notifications-limit-groups.png
      :align: center

      By default, you will receive notifications for all tickets on every group
      you belong to—even for tickets that are assigned to other agents. Use the
      **Limit Groups** box to disable such notifications on a per-group basis.
      (You will continue to receive notifications for your own tickets.)

   .. hint:: The contents of these email notifications
      can be customized on self-hosted installations.
      Administrators can learn more
      `here <https://admin-docs.zammad.org/en/latest/manage/trigger/system-notifications.html>`_.

:Out of Office: 

    Schedule out-of-office periods in advance, and designate a substitute to
    handle your tickets while you’re gone.
    
    Your substitute will receive all your ticket notifications during your
    absence, and have a custom :doc:`overview </basics/find-ticket/browse>`
    created to help keep track of your tickets.
	
    .. note:: 🔔 You **will** continue to receive notifications while you are
              out-of-office!

:Calendar:

   Add your ticket deadlines to your own favorite calendar app with the ICAL
   link listed at this settings panel.

:Devices:

   See a list of all devices logged in to your Zammad account (and revoke
   access, if necessary).

:Token Access:

   Generate personal access tokens for third-party applications to use the
   Zammad API.

   .. caution:: Always generate a new token for each application you connect to
                Zammad! (This makes it possible to revoke access one
                application at a time if a token is ever compromised.)

:Linked Accounts:

   See a list of third-party services (*e.g.,* Facebook or Twitter) linked to
   your Zammad account.
