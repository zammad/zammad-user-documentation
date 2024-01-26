GitHub / GitLab Integration
===========================

With issue tracker integration,
you can monitor GitHub / GitLab issues right from within a Zammad ticket.

This feature is **optional**; if you don't see it in the ticket pane,
that means your administrator hasn't enabled it yet.
Administrators can learn more
:admin-docs:`here </system/integrations.html#integrations-for-issue-trackers>`.

.. figure:: /images/extras/issue-trackers/ticket-settings-with-github-issues.png
   :alt: Ticket detail view showing activated GitHub & GitLab function
   :align: center

   Use the |github| and |gitlab| tabs on the ticket pane
   for an overview of issues related to the ticket.

What can it do?
---------------

View related issues
   Use the |github| and |gitlab| tabs on the ticket pane to see linked issues,
   along with metadata like status (open/closed), assignee, labels, and more.
   Or, simply click the title to view the issue on GitHub / GitLab.

   A badge on the tab icon indicates how many issues are linked to this ticket.

Link a new issue
   At the top of the ticket pane, select **GitHub / GitLab > Link Issue**,
   then enter a valid issue URL. Please note that linking a new issue can be
   slow sometimes.

   .. figure:: /images/extras/issue-trackers/list-and-add-new-issues-to-ticket.gif
      :alt: Screencast showing how to list and add new issues to a ticket
      :width: 90%
      :align: center

Remove an issue
   Click the ✕ button next to an issue title to unlink it.

.. |github| image:: /images/icons/github-64px.png
   :alt: GitHub logo
   :width: 16px

.. |gitlab| image:: /images/icons/gitlab-64px.png
   :alt: GitLub logo
   :width: 16px
