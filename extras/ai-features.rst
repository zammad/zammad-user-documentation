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
- Upcoming events (optional)
- Customer sentiment (optional)

Writing Assistant Tools
-----------------------

The AI-powered writing assistant tools are designed to simplify and enhance
your ticket response workflow while you create an article.
To use such a tool, select the text you want to apply the changes to. This
opens a bubble menu in which you can open the list of available tools by
clicking the writing assistant tools button.

.. figure:: /images/extras/ai/ticket-text-tools.png
   :alt: Screenshots shows selected text in editor with opened writing assistant tools menu
   :align: center

Zammad ships default writing assistant tools. The availability depends on the
configuration of your Zammad instance. You might even have additional custom
tools in case your admin added them.

- **Expand draft into well-written section**: Uses your draft as a base and
  tries to elaborate a proper text. It tries to add a structure and to enhance
  clarity and conciseness and as well as removing misspellings and grammar
  errors. You can even use it by providing only basic information (e.g. via
  bullet points) and let the AI write the answer.
- **Fix spelling and grammar**: Proofreads your text and removes spelling
  and grammar mistakes.
- **Summarize section to about half its current size**: Shrinks your text while
  keeping the message and the tone of the text.
- **Rewrite complex section and make it easy to understand**: Removes
  unnecessary parts and rewrites your text in a clear and understandable way.

After selecting a tool, Zammad shows a dialog where you can compare the
original text and the AI suggestion:

.. figure:: /images/extras/ai/text-tools-approval-dialog.png
   :alt: Screenshots shows AI suggestion dialog
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

AI agents can be configured to work on certain types of routine tasks.
In general, this feature operates behind the scenes but if configured, you may
notice it in some situations (see examples below).
In case your admin created a macro with an AI agent action, you can even run it
manually. Ask your admin for details and have a look at the
:doc:`macro page </advanced/macros>` how to use it.

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

Overview indicator
   A running AI agent is indicated in the status column in overviews. The status
   circle changes to a blue/pink gradient circle:

   .. figure:: /images/extras/ai/overview-indicator-ai-agent.png
      :alt: Screenshot shows a status circle in overviews indicating an AI agent is currently working on it