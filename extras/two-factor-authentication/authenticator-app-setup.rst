Authenticator App Setup
=======================

The authenticator app method is a type of two-factor authentication that uses a
mobile application to generate one-time codes for account verification. After
setting up the authenticator app on your device, you will link it to your Zammad
account.

.. figure:: /images/extras/two-factor-authentication/authenticator-app-setup.png
   :alt: Authenticator App Setup
   :align: center

First, make sure you have installed an authenticator app on your mobile device.
Recommended apps are:

* `Google Authenticator`_
* `Authy`_
* `Microsoft Authenticator`_

Next, open the authenticator app on your device and find a **Scan QR Code**
action, or similar. Point your camera to the Zammad screen and scan the shown QR
code in the middle.

.. hint::
   If your device is not able to scan the QR code, first click on it to reveal
   your secret. Next, add a manual entry to your authenticator app and enter the
   provided secret when asked.

   .. figure:: /images/extras/two-factor-authentication/authenticator-app-reveal-secret.png
      :alt: Authenticator App Secret Revealed
      :align: center

Your authenticator app should immediately add the new entry for your Zammad
account, and a 6-digit code will be displayed next to it together with a timer.

Back in Zammad, enter the provided code to the **Security Code** field and click
on **Set Up**.

.. _`Google Authenticator`: https://support.google.com/accounts/answer/1066447
.. _`Authy`: https://support.authy.com/hc/en-us/articles/115001945848-Installing-Authy-apps/
.. _`Microsoft Authenticator`: https://support.microsoft.com/en-us/account-billing/download-and-install-the-microsoft-authenticator-app-351498fc-850a-45da-b7b6-27e523b8702a
