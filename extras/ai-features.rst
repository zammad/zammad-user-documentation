AI Features
===========

Introduction
------------

Zammad offers AI-powered features to help you manage support tickets more
efficiently.

.. note:: The AI features have to be configured and activated by your
   administrator. If you can't see these features, they are not configured. More
   information about how to configure and activate them can be found in the
   :admin-docs:`AI section </ai/provider.html>` of the admin documentation.

Many AI features in Zammad include a feedback mechanism. If you notice issues or
are unsatisfied with the results, please use the feedback option to let your
Zammad admin know. You can like (thumbs up) or dislike (thumbs down) the
AI-generated content. The dislike option allows you to leave an optional comment.

.. warning::
   Always double-check the AI responses. Although the features were developed
   carefully, there still might be minor inaccuracies in individual cases due to
   the nature of neural networks.

Ticket Summary
--------------

The ticket summary feature does what it says: it summarizes the ticket's
content. This can be a huge time saver when dealing with large tickets and/or
many hand-overs between agents.

If the feature is activated, summaries are generated when tickets are updated
and you either open the ticket or the summary sidebar tab, depending on
your administrator's configuration. Your admin can also set conditions that
restrict which tickets display summaries.

When a summary is newly generated, a small pulsing indicator appears on the
summary sidebar tab. This indicator only shows up if changes were made by
someone other than you (since you already know the updated state).

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
   :alt: Screenshot shows selected text in editor with opened writing assistant tools menu
   :align: center

Zammad ships default writing assistant tools. The availability depends on the
configuration of your Zammad instance. You might even have additional custom
tools in case your admin added them.

- **Expand draft into well-written section**: Uses your draft as a base and
  produces a well-written response. It adds structure and enhances clarity and
  conciseness, as well as removing misspellings and grammar errors. You can even
  use it by providing only basic information (e.g. via bullet points) and let
  the AI write the answer.
- **Fix spelling and grammar**: Proofreads your text and removes spelling
  and grammar mistakes.
- **Summarize section to about half its current size**: Shrinks your text while
  keeping the message and the tone of the text.
- **Rewrite a complex section and make it easy to understand**: Removes
  unnecessary parts and rewrites your text in a clear and understandable way.

After selecting a tool, Zammad shows a dialog where you can compare the
original text and the AI suggestion:

.. figure:: /images/extras/ai/text-tools-approval-dialog.png
   :alt: Screenshot shows AI suggestion dialog
   :align: center

Click on the ``Approve`` button to accept the suggestion and insert it in the
article. After accepting the suggestion, you can still edit the text in the
article editor.

Knowledge Base Assistant
------------------------

.. figure:: /images/extras/ai/related-knowledge-ticket-sidebar.png
   :alt: Related knowledge section of the ticket sidebar with "+ AI draft" button and AI-suggested answer.
   :align: center

Knowledge Base Answer Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This feature allows you to trigger an AI-based generation of a
:doc:`knowledge base <knowledge-base>` answer from a ticket. This is
useful if you often get similar tickets and want to quickly create a knowledge
base article for such cases. Doing so helps you and your colleagues solve
similar tickets more efficiently in the future. It might even reduce incoming
ticket volume when customers can resolve their issues directly from the
published knowledge base.

This feature is available in the **Related knowledge** section of the ticket
sidebar. Click the ``+ AI draft`` button to trigger the answer generation.

Things to consider:

- The knowledge base answer is generated as draft and not published
  automatically.
- You are set as the answer's author.
- The answer is generated in the default language of your knowledge base.
- The answer includes a note in the content and a tag (``ai-generated``) about
  the AI generation.
- A link to the answer is added to the ticket from which you triggered the
  answer generation.
- The answer is created in a knowledge base category for which you have editor
  permissions. The AI chooses one of these categories.

If a similar knowledge base answer already exists, Zammad shows it in a dialog
before creating a new one. This gives you the chance to check whether the answer
matches and to prevent duplicate answers.

Knowledge Base Answer Suggestion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This feature uses the ticket's content and compares it with the available
knowledge base answers. If there is a matching answer above a configurable
relevance score, it is shown under **Suggested by AI**. Each suggestion shows
the title of the answer and more details on hover. An additional relevance score
is only shown to users with the corresponding admin permissions. Click on the
title to open the answer in the knowledge base. Click the ``+`` on the right
side to link it to the ticket. 

If no suggestions are available, the message "No suggestions." is displayed
instead.

.. _ai-agents:

AI Agents
---------

AI agents can be configured to work on certain types of routine tasks.
In general, this feature operates behind the scenes, but if configured, you may
notice it in some situations (see examples below).
If your admin has created a macro with an AI agent action, you can even run it
manually. Ask your admin for details and have a look at the
:doc:`macro page </advanced/macros>` to see how to use it.

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
   duplicate work and prevent losing unsaved changes. If you see an AI agent
   avatar, wait for a moment or head over to another ticket.

   Avatar of AI agent:

   .. figure:: /images/extras/ai/ai-live-user.png
      :alt: Screenshot shows avatar of an AI agent

Overview indicator
   A running AI agent is indicated in the status column in overviews. The status
   circle changes to a blue/pink gradient circle:

   .. figure:: /images/extras/ai/overview-indicator-ai-agent.png
      :alt: Screenshot shows a status circle in overviews indicating an AI agent is currently working on it