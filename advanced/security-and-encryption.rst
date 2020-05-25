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
