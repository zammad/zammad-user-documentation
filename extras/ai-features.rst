AI Features
===========

Introduction
------------

Zammad is getting even smarter! We are expanding Zammad's AI capabilities to
help you manage support tickets even more efficiently. ✨🚀

.. note:: The AI features have to be configured and activated by your
   administrator. If you can't see it, it is not configured. More information
   about how to configure and activate it can be found in the
   :admin-docs:`AI section </ai/provider.html>` of the admin documentation.

Ticket Summary
--------------

The ticket summary feature does what it says: it summarizes the ticket's
content. This can be a huge time saver when dealing with large tickets and/or
many hand-overs between agents.

If the feature is activated, a summary of the ticket is generated when the
ticket got updated and you either open the ticket or open the summary sidebar
tab of the ticket, depending on the configuration.

If there is a new summary, you can see a small pulsing indicator on the summary
sidebar tab. This indicator is only displayed if the changes were not made by
you (as you already know what the ticket is about).

.. figure:: /images/extras/ai/ticket-summary.png
   :alt: Screenshot shows Zammad's ticket detail view with highlighted ticket summary banner and summary sidebar

Depending on the configuration of your Zammad instance, the summary includes
the following sections:

- Customer intent
- Conversation summary
- Open questions (optional)
- Suggested next steps (optional)

Smart Editor
------------

The new AI-powered smart editor is designed to simplify and enhance your ticket
response workflow. It helps you with text tools while you create an article.

The following tools are supported:

- **Improve writing**: Uses your text as a base and tries to improve it by
  enhancing clarity, conciseness and structure as well as removing misspellings
  and grammar issues.
- **Fix spelling and grammar**: Just proofreads your text and automatically
  removes spelling and grammar mistakes.
- **Expand**: Expands your text while keeping your message. Useful if your
  customer expects more than some bullet points as an answer. You can even use
  it by providing only basic information (e.g. via bullet points) and let the
  AI write the answer.
- **Simplify**: Does the opposite of the expansion and shrinks your text while
  keeping your message.

To use any of these features, simply select the text you want to
apply the changes to. You can select the whole text or just parts of it.
This automatically opens a menu where you can select one of the available
options:

.. figure:: /images/extras/ai/ticket-text-tools.png
   :alt: Screenshots shows selected text in article with AI text tools
   :scale: 80%
   :align: center

After selecting an option, Zammad shows a dialog where you can compare the
original text and the AI suggestion:

.. figure:: /images/extras/ai/text-tools-approval-dialog.png
   :alt: Screenshots shows AI suggestion dialog
   :scale: 80%
   :align: center

Click on the **Approve** button to accept the changes and to insert it in the
article. After accepting the suggestion, you can still edit the text in the
article editor.

.. warning::
   Always double-check the response. Although the feature was carefully
   developed, there may still be minor problems in individual cases due to
   the nature of neural networks.

AI Agents
---------

This is no feature which allows any agent interaction. However, if the feature
is configured, you may notice it at some points. This is why you can find an
explanation here.

AI agents can be configured to work on certain types of routine tasks. You may
notice the AI agents at different locations:

Ticket history
   If an AI agent applied changes, you can see a ticket history entry telling
   you the name of the AI agent. If you notice ongoing issues with what the
   AI agent did, inform your Zammad admin.

   Example of a history entry of an AI agent:

   .. figure:: /images/extras/ai/ai-agent-ticket-history.png
      :alt: Screenshot shows AI agent ticket history entry

Simultaneous work detection
   AI agents which are currently working on a ticket are displayed like other
   agents in the live user section in the bottom bar. This helps to avoid
   duplicate work as well as losing unsaved changes. If you see an AI agent
   avatar, wait for a moment or head over to another ticket.

   Avatar of AI agent:

   .. figure:: /images/extras/ai/ai-live-user.png
      :alt: Screenshot shows avatar of an AI agent
      :scale: 80%
