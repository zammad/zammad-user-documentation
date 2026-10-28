GitHub / GitLab Integration
===========================

With the issue tracker integration, you can link GitHub and GitLab issues to a
ticket and follow their state while you work on it. Zammad stores only the
issue URLs on the ticket. Title, state, type, milestone, assignees and labels
are read from GitHub or GitLab each time you open the panel. Nothing is
written back to the tracker. Issues only: pull requests and merge requests
cannot be linked.

The panels are optional. If you don't see them in the ticket sidebar, your
administrator hasn't enabled the integration yet. Customers don't see the links
either. Administrators can learn more in the
:admin-docs:`GitHub </system/integrations/github.html>` and
:admin-docs:`GitLab </system/integrations/gitlab.html>` integration pages.

.. figure:: /images/extras/issue-trackers/ticket-sidebar-linked-github-issue.png
   :alt: Sidebar with opened GitHub panel and linked issue.
   :align: center

View Linked Issues
------------------

Open the **GitHub** or **GitLab** tab in the ticket sidebar of a ticket that
already has issues linked. Each entry starts with an icon for the issue state,
followed by the issue number and title. Click the title to open the issue on
GitHub or GitLab. Each entry also shows the issue's **Milestone**, **Assignees**
and **Labels**. GitHub issues show a **Type** as well. A field appears only
when the issue has one. The badge on the tab counts all linked issues, not
only the open ones. Zammad reads the state when the panel loads and doesn't
watch the issues, so no notification is sent when an issue changes. If the
panel shows ``Loading failed.`` instead of the issues, ask your administrator
to check the token.

Link an Issue
-------------

Select **Link issue** from the menu next to the panel title, then enter the URL
of a single issue and confirm. Zammad accepts links like
``https://github.com/organization/repository/issues/42`` or
``https://git.example.com/group1/project1/-/issues/1``. While you create a
ticket, you can link issues too. They are saved with the new ticket.

Zammad ignores a URL that is already linked to the ticket. It also rejects a
URL it cannot resolve, usually because the issue doesn't exist or because the
API token cannot read its repository or project. Ask your administrator to
check the token in that case.

Unlink an Issue
---------------

Click the ``X`` button next to an issue title. Unlinking removes the reference
from the ticket and leaves the issue untouched in GitHub or GitLab. Other
tickets that link the same issue keep their own reference.
