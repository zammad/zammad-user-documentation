Secure Email
============

Zammad supports two systems of high-security email communication:

   * Pretty Good Privacy (PGP)
   * Secure/Multipurpose Internet Mail Extensions (S/MIME).

.. figure:: /images/extras/secure-email/creating-articles_signed-and-encrypted.gif
   :alt: Screencast demo of S/MIME features for both new tickets and replies
   :scale: 60%
   :align: center

   Use the 🔒 **Encrypt** and ✅ **Sign** buttons to turn on encryption and
   signing of outgoing emails.

Prerequisites
-------------

Both feature are **optional**; if you don't see the
🔒 **Encrypt** and ✅ **Sign** buttons in the ticket composer,
that means your administrator hasn't activated any of them yet.

Administrators can learn more here:

* :admin-docs:`PGP </system/integrations/pgp/index.html>`
* :admin-docs:`S/MIME </system/integrations/smime/index.html>`

PGP and S/MIME are only working if the other party is using them too.

Overview
--------

PGP and S/MIME are the most widely-supported methods for secure email
communication. With each of the systems, you can exchange **signed** and
**encrypted** messages with others.

Signing
   is a proof that a message hasn't been manipulated on its way.

   In other words, it guarantees message **integrity** and **authenticity**.

Encryption
   scrambles a message so that it can only be unscrambled by the intended
   recipient.

   In other words, it guarantees message **privacy** and **data security**.

   Your administrator is responsible for adding all the necessary certificates
   and keys in Zammad's admin panel.

.. note:: In special cases it is possible that both systems are configured in
   your system *and* a customer is using both, as well. In this case, you have
   an additional button to switch between PGP and S/MIME security types.
   Otherwise, you just see the 🔒 **Encrypt** and ✅ **Sign** buttons.

.. figure:: /images/extras/secure-email/pgp_and_smime.png
   :alt: Screenshot of ticket creation with configured PGP and S/MIME
   :scale: 50%
   :align: center

   Ticket creation with configured PGP *and* S/MIME and available
   certificates/keys.

📬 Incoming
^^^^^^^^^^^

The 🔒 and ✅ icons at the top of a message indicate its encryption and signing
status.

.. figure:: /images/extras/secure-email/checking-security-metadata.gif
   :alt: Screencast showing details of encryption and signing status
   :scale: 50%
   :align: center

   Click on an incoming message to expand its details.
   Hover over the security status to show more information.

.. list-table:: Status Icons (Incoming)
   :widths: 5 45

   * - |lock|
     - This message was **encrypted for you**.

       Even if it was intercepted by a third party (hacker, gov't agency, etc.),
       they won't be able to read it.

   * - |encryption-error|
     - This message can **not be decrypted**.

   * - |signed|
     - This message's signature has been **successfully verified**.

       You can be confident that it's authentic and that the content has not
       been modified.

   * - |not-signed|
     - The verification of the signature of this message has **failed**. You
       can find more information by hovering over the icon.

📮 Outgoing
^^^^^^^^^^^

Use the 🔒 **Encrypt** and ✅ **Sign** buttons
to turn on encryption and signing for outgoing emails.

.. note:: Outgoing emails can only be encrypted for *a single recipient*.

.. figure:: /images/extras/secure-email/creating-articles_signed-and-encrypted.gif
   :alt: Screencast showing encryption and signing status for both new tickets and replies
   :scale: 50%
   :align: center

   🔒 **Encrypt** and ✅ **Sign** buttons are present on both new tickets and replies.
   Hover over the buttons to show details.

.. list-table:: Status Icons (Outgoing)
   :widths: 5 45

   * - |lock|
     - This message **will be encrypted**.

       Even if it's intercepted by a third party (hacker, gov't agency, etc.),
       they won't be able to read it.

   * - |open-lock|
     - This message **will not be encrypted**.

   * - |signed|
     - This message **will be signed**.

       Recipients can verify that it came from you and that the content has
       not been modified.

   * - |not-signed|
     - This message **will not be signed**.

.. |lock| image:: /images/extras/secure-email/icon_lock.png
   :width: 24px
   :height: 24px
   :align: top
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

📬 Incoming
^^^^^^^^^^^

“Sign: Unable to find certificate for validation”
   .. figure:: /images/extras/secure-email/verification-not-possible-due-to-missing-certificates.png
      :alt: Ticket article shows a warning for failed verification of a signed message
      :align: center

   Without the sender's certificate, Zammad cannot verify the message signature.

   Ask your administrator to add the sender's certificate to Zammad's certificate store.

   .. warning:: 🕵️ **ALWAYS verify certificates in-person or over the phone!**

      The whole point of signature verification is to alert you
      when someone is trying to pretend to be someone they're not.
      Never accept a certificate from someone online without verifying it first.

“Encryption: Unable to find private key to decrypt”
   .. figure:: /images/extras/secure-email/decryption-not-possible-due-to-missing-certificates.png
      :alt: Ticket article shows a warning for failed verification of a signed message
      :align: center

   This message was encrypted with a certificate that does not match any on file.
   Without a matching private key, Zammad cannot decrypt the message.

   Ask your administrator to verify your organization's private key in Zammad's certificate store,
   and ask the sender to double-check the public key they used to encrypt the message.

   .. hint:: 📢 **Your public key can be safely shared with anyone.**

      (But if they're smart, they'll take extra precautions
      to make sure it really belongs to you.)

📮 Outgoing
^^^^^^^^^^^

The 🔒 **Encrypt** button is disabled
   Ask your administrator to add the recipient's certificate to Zammad's certificate store.

The ✅ **Sign** button is disabled
   Ask your administrator to verify your organization's private key in Zammad's certificate store.
