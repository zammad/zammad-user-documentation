Two-Factor Authentication
=========================

Two-factor authentication (2FA) enhances the security of your Zammad account by
adding an extra layer of verification beyond a password. It requires you to
provide two different types of authentication factors, typically something you
know (like a password) and something you possess (like a mobile device or a
security token), to ensure that you are an authorized individual who can access
the account.

Two-Factor Authentication is an **optional feature**. Administrators can learn
more :admin-docs:`here </settings/security/two-factor.html>`.

Set Up Two-Factor Authentication
--------------------------------

If the system admin has enabled this feature, you can head to "Avatar > Profile
> Password & Authentication" to set it up. Depending on the enabled two-factor
methods, you may see one or more options in the table.

To set up a two-factor method, use the ⋮ **Actions** menu next to it and choose
**Set Up**.

.. figure:: /images/extras/two-factor-authentication/user-profile-set-up.png
   :alt: Set Up Two-Factor Method in Password & Authentication
   :align: center

In a modal dialog, you will be asked to confirm your current password.

.. figure:: /images/extras/two-factor-authentication/password-check.png
   :alt: Password Check Modal Dialog
   :align: center

.. _setup guide:

Depending on the chosen two-factor method, you will be guided through the setup
process, which includes specific steps.

.. toctree::
   :maxdepth: 1

   two-factor-authentication/security-keys-setup
   two-factor-authentication/authenticator-app-setup

Sign-in with a Two-Factor Method
--------------------------------

When you set up two-factor authentication for your Zammad account, during the
next sign-in you will be asked to provide the same two-factor method after
entering correct username and password.

Depending on the chosen two-factor method, this may be a security code, hardware
key, etc.

.. toctree::
   :maxdepth: 1

   two-factor-authentication/security-keys-sign-in
   two-factor-authentication/authenticator-app-sign-in

Trying Another Method
^^^^^^^^^^^^^^^^^^^^^

In case you are having issued during sign-in with your preferred two-factor
authentication method, you can switch to another one, provided you have set it
up previously.

Look for **Try another method** link below the sign in box. In case you don't
see this link, you probably have no other available
two-factor methods set up, or your admin has disabled this feature.

.. figure:: /images/extras/two-factor-authentication/try-another-method-link.png
   :alt: Try Another Method Link
   :align: center

In the new screen, choose another two-factor authentication method and complete
your sign-in.

.. figure:: /images/extras/two-factor-authentication/try-another-method.png
   :alt: Try Another Method
   :align: center

Alternatively, you can also use one of your recovery codes, which are
auto-generated for your account during the initial setup of the two-factor
authentication. Click on **recovery codes**, enter one of your unused recovery
codes and click on **Sign in**.

.. figure:: /images/extras/two-factor-authentication/recovery-codes-sign-in.png
   :alt: Try Another Method
   :align: center

.. warning::
   You can use a single recovery code only once! In case you exhaust the list of
   your recovery codes, it is recommended you regenerate them for your account.

Generate Recovery Codes
-----------------------

Recovery codes are one-time use security codes that can be used to sign in if
you lose access to your other two-factor authentication methods. They can only
be used as a **backup method**.

If the feature is enabled by the admin, recovery codes will be automatically
generated for you during the setup of your initial two-factor authentication
method.

You will be asked to print out or save the generated recovery codes in a safe
place. Once used, a recovery code cannot be reused.

.. figure:: /images/extras/two-factor-authentication/recovery-codes-modal.png
   :alt: Recovery Codes Modal Dialog
   :align: center

You also have an option to regenerate your recovery codes at any time, which
invalidates already existing recovery codes and provides you with a list of
fresh codes. You can do this by clicking on **Regenerate recovery codes** button
in "Avatar > Profile > Password & Authentication".

Set a Two-Factor Method as Default
----------------------------------

To set an already set up two-factor method as default, use the ⋮ **Actions**
menu next to it in "Avatar > Profile > Password & Authentication" and choose
**Set as default**.

.. figure:: /images/extras/two-factor-authentication/user-profile-default.png
   :alt: Edit Two-Factor Method in Password & Authentication
   :align: center

In order to identify your current default two-factor authentication method, look
for a small blue badge next to the method name.

A default two-factor authentication method is just your preferred method during
the sign-in process. You will always have an option to try signing in using
another method.

Edit a Two-Factor Method
------------------------

To edit an already set up two-factor method, use the ⋮ **Actions** menu
next to it in "Avatar > Profile > Password & Authentication" and choose
**Edit**.

.. figure:: /images/extras/two-factor-authentication/user-profile-edit.png
   :alt: Edit Two-Factor Method in Password & Authentication
   :align: center

In a modal dialog, you will be asked to confirm your current password.

Depending on the chosen two-factor method, you will be guided again through the
setup process. Normally, editing a method will simply renew it and replace the
older setup, but some methods do support advanced functions (e.g. adding
multiple security keys).

Remove a Two-Factor Method
--------------------------

To remove an already set up two-factor method, use the ⋮ **Actions** menu
next to it in "Avatar > Profile > Password & Authentication" and choose
**Remove**.

.. figure:: /images/extras/two-factor-authentication/user-profile-remove.png
   :alt: Remove Two-Factor Method in Password & Authentication
   :align: center

In a modal dialog, you will be asked to confirm the removal with your current
password.

Requirement to Set Up a Two-Factor Method
-----------------------------------------

Your system admin may choose to require you to set up at least one two-factor
method for your account. In this case, if you haven't already set up a method,
you will be asked to do so at your next sign-in or application reload.

.. figure:: /images/extras/two-factor-authentication/after-auth-two-factor-set-up.png
   :alt: Remove Two-Factor Method in Password & Authentication
   :align: center

Choose a method of your choice, and then follow its :ref:`setup guide <setup guide>`.

.. warning::
   If you are required to set up a two-factor authentication for your account,
   this will be a mandatory action. You will not be able to use Zammad until you
   set up at least one method.
