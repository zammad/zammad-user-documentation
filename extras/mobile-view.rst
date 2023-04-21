Mobile View
===========

The need for a dedicated mobile view of Zammad arose from the ever-changing life
on the go. Even though the desktop application might be responsive enough for
small screens, it proved to be too cluttered and was simply not designed
primarily for mobile devices.

By limiting the amount of information to only the most important, the mobile
view strives to provide you, the user, with a more focused window into your
daily tasks. All packaged in a touch-friendly and modern design with great user
experience, of course!

.. tabs::

   .. tab:: Login & Home

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-login.png
           :alt: Mobile View Login Screen
           :align: center

           Login Screen

     .. container:: cfloat-right


        .. figure:: /images/extras/mobile-view/mobile-view-home.png
           :alt: Mobile View Home Page
           :align: center

           Home Page

     .. container:: cfloat-clear

        x

   .. tab:: Search & Overview

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-search.png
           :alt: Mobile View Search Results
           :align: center

           Search Results

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-ticket-overview.png
           :alt: Mobile View Ticket Overview
           :align: center

           Ticket Overview

     .. container:: cfloat-clear

        x

   .. tab:: Ticket Details

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-ticket-detail-view.png
           :alt: Mobile View Ticket Detail View
           :align: center

           Ticket Detail View

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-ticket-information.png
           :alt: Mobile View Ticket Information
           :align: center

           Ticket Information

     .. container:: cfloat-clear

        x

   .. tab:: Notifications & Account

     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-notifications.png
           :alt: Mobile View Notifications
           :align: center

           Notifications

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-account-overview.png
           :alt: Mobile View Account Overview
           :align: center

           Account Overview

     .. container:: cfloat-clear

        x

.. hint::

   We intentionally do not provide specific instructions and comprehensive
   documentation for the mobile view! The overall UX should be intuitive and
   self-explanatory in most cases.

Features
--------

Mobile view provides you with a way to do your common Zammad daily tasks while
on the go:

   * Manage & use your ticket overviews
   * Search for existing records
   * Create a new ticket
   * Reply in an already existing ticket
   * Modify ticket attributes
   * Modify customer attributes
   * Modify organization attributes

Mobile view also has some exclusive features:

   * Innovative Zammad UX
   * Next-level accessibility
   * Ready for multi-device usage
   * Progressive web app (PWA) support

Limitations
-----------

Mobile view is also currently missing some features which are provided by the
desktop view:

   * Ticket Article Time Accounting
   * Ticket Article **Split** Action
   * Linked Tickets & Ticket **Link** Action
   * Ticket Macros
   * Ticket History
   * Ticket Create Templates & Shared Drafts

Additionally, certain features were intentionally omitted in order to improve
the focus on important information:

   * Most Management Features (except ticket user and organization management)
   * Most Knowledge Base Features (except ticket integration)
   * Most User Profile Functions (except avatar and language preferences)
   * Reports
   * Caller Log
   * Live Chat

Access
------

Zammad now implements a mobile device detection, which results in automatic
redirection to mobile view. Even with this mechanism in place it's possible to
explicitly switch between the views by using app links:

   Continue to desktop link in mobile view
     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-login-continue-to-desktop.png
           :alt: Continue to Desktop Link on Login Screen
           :align: center

           Login Screen

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-account-continue-to-desktop.png
           :alt: Continue to Desktop Link in User Account Overview
           :align: center

           User Account Overview

     .. container:: cfloat-clear

        x

   Continue to mobile link in desktop view
     .. container:: cfloat-left

        .. figure:: /images/extras/mobile-view/mobile-view-desktop-login-continue-to-mobile.png
           :alt: Continue to Mobile Link in Desktop Login Screen
           :align: center

           Login Screen

     .. container:: cfloat-right

        .. figure:: /images/extras/mobile-view/mobile-view-desktop-user-menu-continue-to-mobile.png
           :alt: Continue to Mobile Link in Desktop User Menu
           :align: center

           User Avatar Menu

     .. container:: cfloat-clear

        x

Whenever an app link is used, the choice will be remembered by the user's device
and the next time the automatic redirection will behave accordingly.
