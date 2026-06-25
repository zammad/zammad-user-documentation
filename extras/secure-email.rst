Secure Email
=============

Zammad supports two systems for secure email communication:

- **PGP** (Pretty Good Privacy)
- **S/MIME** (Secure/Multipurpose Internet Mail Extensions)

Both systems allow you to exchange **signed** and **encrypted** messages
with others.

Prerequisites
-------------

- Both features are optional. If you don't see the ``Encrypt`` and ``Sign``
  buttons in the email article editor, your administrator hasn't activated them
  yet.
- PGP and S/MIME only work if the other party is using them too.
- Your administrator is responsible for adding all necessary certificates
  and keys in Zammad's admin settings.

.. hint::
   Administrators can find configuration details in the admin documentation:

   - :admin-docs:`PGP </system/integrations/pgp/index.html>`
   - :admin-docs:`S/MIME </system/integrations/smime/index.html>`

If these requirements are met, the feature should work out of the box and
Zammad encrypts, decrypts, signs and verifies signatures of emails if possible.
Your admin can define a default behavior for each group. However, you can
override the default for each outgoing email article on your own by switching
encryption and signing on or off (see example in screenshot below with turned
off encryption and activated signing). Read on to learn more about it and to
find common errors.

.. figure:: /images/extras/secure-email/editor-buttons.png
   :alt: Screenshot shows editor for outgoing email with disabled encryption and enabled signing.
   :align: center

Signing & Encryption
--------------------

Signing
   Signing is a proof that a message hasn't been manipulated on its way. It
   guarantees message **integrity** and **authenticity**.

Encryption
   Encryption scrambles a message so that it can only be unscrambled by the
   intended recipient. It guarantees message **privacy** and **data security**.

Incoming Email
--------------

The lock and check icons at the top of a message indicate its encryption
and signing status. Click on an incoming message article to expand its details.
In the details, you can hover over the security status to see more information.

.. list-table:: Status Icons for Incoming Emails
   :widths: 20 80

   * - |lock|
     - **Encrypted for you.** Even if intercepted by a third party, they won't be able to read it.
   * - |encryption-error|
     - **Cannot be decrypted.** Zammad lacks the required key to decrypt this message.
   * - |signed|
     - **Successfully verified.** You can be confident it's authentic and the content has not been modified.
   * - |not-signed|
     - **Signature verification failed.** Hover over the icon for more information.

Outgoing Email
--------------

Use the ``Encrypt`` and ``Sign`` buttons to turn on encryption and signing
for outgoing emails. They are available for new tickets and replies. Hover over
the buttons to show details.

.. note::
   Outgoing emails can only be encrypted for *a single recipient*.

.. list-table:: Status Icons for Outgoing Emails
   :widths: 20 80

   * - |lock|
     - **Will be encrypted.** Even if intercepted by a third party, they won't be able to read it.
   * - |open-lock|
     - **Will not be encrypted.**
   * - |signed|
     - **Will be signed.** Recipients can verify that it came from you and that the content has not been modified.
   * - |not-signed|
     - **Will not be signed.**

.. |lock| image:: /images/extras/secure-email/icon_lock.png
   :width: 24px
   :height: 24px
.. |open-lock| image:: /images/extras/secure-email/icon_open-lock.png
   :width: 24px
   :height: 24px
.. |signed| image:: /images/extras/secure-email/icon_signed.png
   :width: 24px
   :height: 24px
.. |not-signed| image:: /images/extras/secure-email/icon_not-signed.png
   :width: 24px
   :height: 24px
.. |encryption-error| image:: /images/extras/secure-email/icon_encryption-error.png
   :width: 24px
   :height: 24px

Troubleshooting
---------------

Incoming Email
^^^^^^^^^^^^^^

Sign: Unable to find certificate for validation
   .. figure:: /images/extras/secure-email/verification-not-possible-due-to-missing-certificates.png
      :alt: Ticket article shows a warning for failed verification of a signed message
      :align: center

   Without the sender's certificate, Zammad cannot verify the message signature.
   Ask your administrator to add the sender's certificate to Zammad's
   certificate store.

   .. warning:: Always verify certificates in-person or over the phone!
      The whole point of signature verification is to alert you when someone is
      trying to pretend to be someone they're not. Never accept a certificate
      from someone online without verifying it first.

Encryption: Unable to find private key to decrypt
   .. figure:: /images/extras/secure-email/decryption-not-possible-due-to-missing-certificates.png
      :alt: Ticket article shows a warning for failed decryption of an encrypted message
      :align: center

   This message was encrypted with a certificate that does not match any on
   file. Without a matching private key, Zammad cannot decrypt the message.
   Ask your administrator to verify your organization's private key in Zammad's
   certificate store, and ask the sender to double-check the public key they
   used to encrypt the message.

Outgoing Email
^^^^^^^^^^^^^^

The ``Encrypt`` button is disabled
   Ask your administrator to add the recipient's certificate to Zammad's
   certificate store.

The ``Sign`` button is disabled
   Ask your administrator to verify your organization's private key in Zammad's
   certificate store.

I can see a ``PGP`` and ``S/MIME`` button. What should I do?
   In special cases, both systems may be configured in your system and a
   customer may be using both as well. In this case, you have an additional
   button to switch between PGP and S/MIME security types. Just pick one,
   make sure encryption and signing is enabled and send your email.
