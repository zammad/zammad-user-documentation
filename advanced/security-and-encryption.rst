Security & Encryption
=====================

Sign, Encrypt and check the state of incoming mails (is it signed or encrypted?) 
within the ticket details and it's articles.

S/MIME (Sign & Encrypt E-Mails)
-------------------------------

.. note:: **🤔 Huh? I don’t see “Sign” or “Encrypt” options within Tickets...** 

   This feature is **optional**; if you don’t see it in the main menu, that
   means it’s not enabled yet. See the `admin documentation <https://admin-docs.zammad.org/en/latest/system/integrations/smime.html>`_ for details.

**But what's S/MIME?**

S/MIME uses certificates that, in the case of the integration, need to be uploaded to Zammad. 
This is a task for your administrator. The key functions of S/MIME are:

   * Authentication
   * Message integrity
   * Privacy
   * Data security (when using encryption)

Receiving signed & encrypted messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If S/MIME is enabled and Zammad is missing a certificate or private key, it may confront you with a warning. 
There are two situations where this might happen:

The public certificate of the sender is missing
   In this case Zammad will not be able to verify if the message has been changed during transmission. 

   As soon as your administrator added the certificate, you can press "retry security process" to check the message again. 
   This option is only available for messages that have been received during enabled S/MIME integration.

   .. figure:: /images/advanced/smime/verification-not-possible-due-to-missing-certificates.png
      :alt: Ticket article shows a warning for failed verification of a signed message
      :align: center

The certificate and key are not available for decryption
   In order to decrypt S/MIME encrypted messages, your sender will encrypt the message with your public certificate. 
   To decrypt the message, Zammad needs this certificate together with its key - otherwise the mail can't be decrypted.

   As soon as your administrator added the certificate and key, you can press "retry security process" to check the 
   message again. This option is only available for messages that have been received during enabled S/MIME integration. 

   .. hint:: This issue could also appear if the sender used the wrong certificate for encryption.

   .. figure:: /images/advanced/smime/decryption-not-possible-due-to-missing-certificates.png
      :alt: Ticket article shows a warning for failed verification of a signed message
      :align: center

If there are no issues with the message received, Zammad will display a closed lock and/or lock. 
By clicking on the article body you can expand the meta information of the article. By hovering the icons, 
you'll see in detail which certificates or CAs have been used for verification.

.. figure:: /images/advanced/smime/checking-security-mata-information.gif
   :alt: Screencast showing on how to verify used certificates
   :align: center

Icons explained
^^^^^^^^^^^^^^^

To help you understanding the used icons, we listed them below. 
Those icons will help you to see on a first glimpse what state the article has.

.. list-table:: S/MIME related icons on top of articles
   :header-rows: 1
   :widths: 5 45
   
   * - icon
     - description
   * - |lock|
     - The message is encrypted (and verified). If you're writing a new article, this means that Zammad will 
       send the message as a signed message.
   * - |open-lock|
     - The message is encrypted and couldn't get verified successfully. If you're writing a new article, this 
       means the message is not sent as a signed message.
   * - |signed|
     - The message is encrypted and was decrypted by Zammad. If you're writing a new article, this means the 
       message is going to be encrypted during sendout.
   * - |not-signed|
     - The message can't be decrypted by Zammad. If you're writing a new article, this means the message 
       is not going to be encrypted during sendout.

.. |lock| image:: /images/advanced/smime/icon_lock.png
   :width: 24px
   :height: 24px
   :align: top
.. |open-lock| image:: /images/advanced/smime/icon_open-lock.png
   :width: 24px
   :height: 24px
.. |signed| image:: /images/advanced/smime/icon_signed.png
   :width: 24px
   :height: 24px
.. |not-signed| image:: /images/advanced/smime/icon_not-signed.png
   :width: 24px
   :height: 24px