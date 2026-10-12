Mobile View
===========

Zammad provides a dedicated mobile view for working on the go. The mobile
view offers a focused, touch-friendly interface for your daily tasks,
with a modern design and improved accessibility.

.. tabs::

   .. tab:: Login & Home

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-login.png
           :alt: Mobile View Login Screen
           :align: center
           :width: 80%

           Login Screen

     .. container:: cfloat-right


        .. figure:: /images/extras/mobile-view/mobile-view-home.png
           :alt: Mobile View Home Page
           :align: center
           :width: 80%

           Home Page

     .. container:: cfloat-clear

        x

   .. tab:: Search & Overview

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-search.png
           :alt: Mobile View Search Results
           :align: center
           :width: 80%

           Search Results

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-ticket-overview.png
           :alt: Mobile View Ticket Overview
           :align: center
           :width: 80%

           Ticket Overview

     .. container:: cfloat-clear

        x

   .. tab:: Ticket Details

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-ticket-detail-view.png
           :alt: Mobile View Ticket Detail View
           :align: center
           :width: 80%

           Ticket Detail View

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-ticket-information.png
           :alt: Mobile View Ticket Information
           :align: center
           :width: 80%

           Ticket Information

     .. container:: cfloat-clear

        x

   .. tab:: Notifications & Account

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-notifications.png
           :alt: Mobile View Notifications
           :align: center
           :width: 80%

           Notifications

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-account-overview.png
           :alt: Mobile View Account Overview
           :align: center
           :width: 80%

           Account Overview

     .. container:: cfloat-clear

        x

.. hint::

   We intentionally do not provide specific instructions for the mobile view.
   The overall UX should be intuitive and self-explanatory in most cases.

Features
--------

Mobile view provides you with a way to do your common Zammad daily tasks while
on the go:

- Manage & use your ticket overviews
- Search for existing records
- Create a new ticket
- Reply in an already existing ticket
- Modify ticket attributes
- Modify customer attributes
- Modify organization attributes
- Track time on ticket articles

Mobile view also has some exclusive features:

- Innovative Zammad UX
- Next-level accessibility
- Ready for multi-device usage
- Progressive web app (PWA) support

Push Notifications
------------------

The mobile view can notify you about your tickets on your mobile device, even
when the app is not open. Push notifications are turned on per device, not for
your account as a whole: you can have them on your phone and leave them off on
a tablet.

Turn them on with the **Push notifications on this device** switch in the
**Notifications** section of your account page. If the switch is locked, the
text below it tells you what is missing.

Every notification Zammad creates for you is also sent to your device, for
example about new tickets, ticket updates, reached reminders or escalations.
A push shows the same text as the entry in the notification list, and tapping
it opens the ticket in the app.

On iPhone and iPad, push notifications are only available in the app added to
the home screen with iOS or iPadOS 16.4 or later. Open the mobile view in
Safari, tap ``Share`` and then ``Add to Home Screen``. On Android, the
installed app and the browser can both receive them.

If you turned notifications off for the app in the settings of your device, the
switch stays locked until you allow them there again. A browser whose push
service Zammad does not support cannot enable push notifications at all. Turn
the switch off again to stop receiving them; signing out removes the device as
well.

Push notifications are delivered by the push service of your browser and not by
Zammad, so they can be delayed, for example by battery optimization on Android
devices. While you are working in the desktop view, Zammad does not send push
notifications to your devices.

Limitations
-----------

Mobile view is also currently missing some features which are provided by the
desktop view:

- Ticket Article **Split** Action
- Linked Tickets & Ticket **Link** Action
- Ticket Macros
- Ticket History
- Ticket Create Templates & Shared Drafts

Additionally, certain features were intentionally omitted in order to improve
the focus on important information:

- Most Management Features (except ticket user and organization management)
- Most Knowledge Base Features (except ticket integration)
- Most User Profile Functions (except avatar and language preferences)
- Reports
- Caller Log
- Live Chat

Access
------

Zammad now implements a mobile device detection, which results in automatic
redirection to mobile view. Even with this mechanism in place it's possible to
explicitly switch between the views by using app links:

Continue to Desktop Link in Mobile View
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the login screen, use the **Continue to desktop** link below the ``Sign in``
button. While you are signed in, open your account page with the avatar in the
bottom navigation and use the **Continue to desktop** entry there.

.. container:: cfloat-left

   .. figure:: /images/extras/mobile-view/mobile-view-login.png
      :alt: Continue to Desktop Link on Login Screen
      :align: center
      :width: 80%

      Login Screen

.. container:: cfloat-right

   .. figure:: /images/extras/mobile-view/mobile-view-account-overview.png
      :alt: Continue to Desktop Link in User Account Overview
      :align: center
      :width: 80%

      User Account Overview

.. container:: cfloat-clear

   x

Continue to Mobile Link in Desktop View
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the login screen of the desktop view, use the **Continue to mobile** link
below the ``Sign in`` button. While you are signed in, use the
**Continue to mobile** entry in the user menu, which your avatar at the bottom
of the navigation sidebar opens.

.. container:: cfloat-left

   .. figure:: /images/extras/mobile-view/mobile-view-desktop-login-continue-to-mobile.png
      :alt: Continue to Mobile Link in Desktop Login Screen
      :align: center
      :width: 80%

      Login Screen

.. container:: cfloat-right

   .. figure:: /images/extras/mobile-view/mobile-view-desktop-user-menu-continue-to-mobile.png
      :alt: Continue to Mobile Link in Desktop User Menu
      :align: center
      :width: 80%

      User Avatar Menu

.. container:: cfloat-clear

   x

Whenever an app link is used, the choice will be remembered by the user's device
and the next time the automatic redirection will behave accordingly.
