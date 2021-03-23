Issue Trackers
==============

Zammad currently supports GitHub and GitLab both as hosted or self-hosted 
variants. This functionality is currently limited to Issues.

.. note:: **🤔 Huh? I don’t see “GitHub” or “GitLab” in the ticket settings...** 

   | This feature is **optional**; if you don’t see it in the main menu, 
     that means your administrator hasn’t enabled it yet. 
   | Administrators can learn more on the admin documentation:
   | `GitHub <https://admin-docs.zammad.org/en/latest/system/integrations/github.html>`_ &
     `GitLab <https://admin-docs.zammad.org/en/latest/system/integrations/gitlab.html>`_

.. figure:: /images/extras/issue-trackers/ticket-settings-with-github-issues.png
   :alt: Ticket detail view showing activated GitHub & GitLab function
   :align: center

   The GitHub and GitLab tabs within any ticket allow you to keep track on 
   relevant issues to that ticket.

Usage
-----

   .. note::

      Usage for GitHub and GitLab are exact the same. 
      This is why screencasts will show one version, but not both.

Use the tabs |github| and |gitlab| to open the issue sub menu. 
The tab will show a counter with the number of linked issues if applicable.

To link a new issue to the ticket, click on **GitHub ▼** or **GitLab ▼** to 
open the issue dialog. On the new modal provide the issue URL in question and 
press **Submit**.

   .. note:: **⏳ Adding new issues may take a moment...**

If you have a ticket opened in the detail view, Zammad will regularly poll the 
linked issues. If the issue changes (e.g. is being closed) Zammad will update 
this state automatically for you.

.. figure:: /images/extras/issue-trackers/list-and-add-new-issues-to-ticket.gif
   :alt: Screencast showing how to list and add new issues to a ticket
   :width: 90%
   :align: center

.. |github| image:: /images/icons/github-64px.png
   :alt: GitHub logo
   :width: 16px

.. |gitlab| image:: /images/icons/gitlab-64px.png
   :alt: GitLub logo
   :width: 16px
