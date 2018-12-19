Profile & Settings
==================

Click on your avatar at the bottom of the main menu
to access your **profile and settings**.

.. figure:: /images/extras/profile-and-settings.jpg
   :alt: User submenu
   :align: center
   :scale: 50%

   Find user-specific actions,
   a list of recently opened items,
   and useful reference information.

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

   .. figure:: /images/extras/profile-and-settings-notifications-settings.jpg
      :align: center

      Use the first three columns to choose when to receive **internal
      notifications** (below). The rightmost column enables email notification
      as well.

   .. figure:: /images/extras/profile-and-settings-notifications-center.jpg
      :align: center

      Internal notifications cannot be disabled.

   Consult the `admin documentation <https://admin-docs.zammad.org/en/latest/manage-trigger.html#other-notifications>`_
   for details on how to customize these email notifications.

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
