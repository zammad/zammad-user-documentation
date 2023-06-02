Authenticator App Sign-in
=========================

To sign-in with authenticator app two-factor method, first enter your username
and password and click **Sign in**.

Then, open authenticator app on your device, and get the 6-digit code next to
your Zammad account.

.. figure:: /images/extras/two-factor-authentication/authenticator-app-security-code.png
   :alt: Security Code in Google Authenticator App
   :align: center
   :width: 30%

Back in Zammad, enter the provided code to the **Security Code** field and click
on **Sign in**.

.. figure:: /images/extras/two-factor-authentication/authenticator-app-sign-in.png
   :alt: Authenticator App Security Code during Sign-in
   :align: center

.. warning::
   Entering security codes from your authenticator app is a time-sensitive
   operation! Each code is valid for up to 30 seconds, so if you are near the
   end of the time window (timer will show you this), it is better to wait for
   it to refresh.
