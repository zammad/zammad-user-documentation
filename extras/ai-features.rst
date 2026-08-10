AI Features
===========

Introduction
------------

Zammad offers AI-powered features to help you manage support tickets more efficiently.

.. note:: The AI features have to be configured and activated by your
   administrator. If you can't see it, it is not configured. More information
   about how to configure and activate it can be found in the
   :admin-docs:`AI section </ai/provider.html>` of the admin documentation.

Many AI features in Zammad include a feedback mechanism. If you notice issues or
are unsatisfied with the results, please use the feedback option to let your
Zammad admin know. You can like (thumb up) or dislike (thumb down) the AI
generated content. The dislike option allows you to leave an optional comment.

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

Click on the ``Approve`` button to accept the changes and to insert it in the
article. After accepting the suggestion, you can still edit the text in the
article editor.

Knowledge Base Answer Generation
--------------------------------

This feature allows you to trigger an AI-based generation of a
:doc:`knowledge base <knowledge-base>` answer out of a ticket. This can be
useful if you often get similar tickets and want to quickly create a knowledge
base article for such cases. Doing so helps you and your colleagues to solve
similar tickets more efficiently in the future and might even reduce the ticket
volume in the long run when customers can resolve their issues directly from
the published knowledge base.

This feature is available in the **Related knowledge** section of the ticket
detail view sidebar. Your KB editor permissions are required for the ``+ AI
draft`` button to show here.

Important information:

- You need knowledge base editor permission (``knowledge_base.editor``) as well
  as an active AI provider configured by your administrator.
- The knowledge base answer is generated as draft and doesn't get published
  automatically. The user who triggered the generation is set as the author of
  the new answer.
- The answer is generated in the configured default language of your knowledge
  base.
- The answer includes a note in the content and a tag (``ai-generated``) about
  the AI generation.
- A link to the answer is added to the ticket from which the answer was
  triggered.
- The AI request includes a list of the knowledge base categories in which you
  have editor permissions. The AI then chooses one of these categories.

To trigger a generation, click the ``+ AI draft`` button in the **Related
knowledge** section:

.. figure:: /images/extras/ai/kb-answer-ticket-tab.png
   :alt: KB answer generation in ticket tab
   :align: center

Always make sure to check the generated answer. This is especially important if
you want to publish the article. Even though the AI is instructed to remove
personal and/or company-specific information, it can't be guaranteed that this
is the case.

Suggested by AI
~~~~~~~~~~~~~~~

Alongside **Related knowledge**, you will see a list of existing knowledge base
articles suggested by AI for this ticket. These suggestions are based on the
ticket content and use an embedding-based search to find relevant articles.

Each suggestion shows:

- The title of the article, linking to its full text.
- The relevance score as a percentage (for administrators who have enabled AI
  feature feedback).
- Knowledge base category name.
- A ``+`` button to link the answer in the **Related knowledge** section below.

If no suggestions are available the message ``No related knowledge base answers
found`` will be displayed instead. If the AI service fails you will get an error
message with a **Retry** button to try again.

To use this feature, your administrator needs to have configured an active AI
provider and enabled it for knowledge base suggestions. Your KB editor permission
is not required for viewing or linking suggested answers, but is needed for the
``+ AI draft`` button described above.

.. _ai-agents:

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