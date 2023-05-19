Two-Factor Authentication
=========================

Two-factor authentication (2FA) enhances the security of your Zammad account by
adding an extra layer of verification beyond a password. It requires you to
provide two different types of authentication factors, typically something you
know (like a password) and something you possess (like a mobile device or a
security token), to ensure that you are an authorized individual that can access
the account.

.. hint::
   Two-Factor Authentication is an optional feature. Administrators can learn
   more :admin-docs:`here <settings/security/two-factor.html>`.

Set Up Two-Factor Authentication
--------------------------------

If the system admin has enabled this feature, you can head to "Avatar -> Profile
-> Password & Authentication" to set it up. Depending on the enabled two-factor
methods, you may see one or more options in the table.

To set up a two-factor method, use the ⋮ **Actions** menu next to it and choose
**Set Up**.

.. figure:: /images/extras/two-factor-authentication/user-profile-set-up.png
   :alt: Set Up Two-Factor Method in Password & Authentication
   :align: center

In a modal dialog, you will be asked to enter your current password.

.. figure:: /images/extras/two-factor-authentication/password-check.png
   :alt: Password Check Modal Dialog
   :align: center

.. _`two-factor-set-up-method`:

Depending on the chosen two-factor method, you will be guided through the set up
process, which includes specific steps.

.. toctree::
   :maxdepth: 1

   two-factor-authentication/authenticator-app-set-up

Sign-in with a Two-Factor Method
--------------------------------

When you set up two-factor authentication for your Zammad account, during the
next sign-in you will be asked to provide the same two-factor method after
entering correct username and password.

Depending on the chosen two-factor method, this may be a security code, hardware
key, etc.

.. toctree::
   :maxdepth: 1

   two-factor-authentication/authenticator-app-sign-in

Remove a Two-Factor Method
--------------------------

To remove an already set up two-factor method, use the ⋮ **Actions** menu
next to it in "Avatar -> Profile -> Password & Authentication" and choose
**Remove**.

.. figure:: /images/extras/two-factor-authentication/user-profile-remove.png
   :alt: Remove Two-Factor Method in Password & Authentication
   :align: center

You will be asked to confirm the removal.

Requirement to Set Up a Two-Factor Method
-----------------------------------------

You system admin may choose to require you to set up at least one two-factor
method for your account. In this case, if you haven't already set up a method,
you will be asked to do so at your next sign-in or application reload.

.. figure:: /images/extras/two-factor-authentication/after-auth-two-factor-set-up.png
   :alt: Remove Two-Factor Method in Password & Authentication
   :align: center

Choose a method of your choice, and then follow its
`set up guide <two-factor-set-up-method>`_.

.. warning::
   If you are required to set up a two-factor authentication for your account,
   this will be a mandatory action. You will not be able to use Zammad until you
   set up at least one method.
