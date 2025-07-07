AI Features
===========

Introduction
------------

Zammad is getting even smarter! We are expanding Zammad's AI capabilities to
help you manage support tickets even more efficiently. ✨🚀

.. note:: The AI features have to be configured and activated by your
   administrator. If you can't see it, it is not configured. More information
   about how to configure and activate it can be found in the
   :admin-docs:`AI section </ai/provider>` of the admin documentation.

Ticket Summary
--------------

The ticket summary feature does what it says: it summarizes the ticket's
content. This can be a huge time saver when dealing with large tickets and/or
many hand-overs between agents.

If the feature is activated, a summary of the ticket is generated when a ticket
is opened. An indicator shows up on the AI summary sidebar tab to show you that
a summary has been generated.

.. figure:: /images/extras/ai/ticket-summary.png
   :alt: Screenshot shows Zammad's ticket detail view with highlighted ticket summary banner and summary sidebar

Depending on the configuration of your Zammad instance, the summary includes
the following sections:

- Customer intent
- Conversation summary
- Open questions (optional)
- Suggested next steps (optional)

Smart Editor
^^^^^^^^^^^^

The new AI-powered smart editor is designed to simplify and enhance your ticket
response workflow. It helps you with text tools while you create an article.

To use any of the following features, you first have to select text you want to
apply the changes to. After that, click the **Smart Editor** link at the bottom
of the article creation and choose one of the following features, depending on
what you want to perform.

.. figure:: /images/extras/ai/reply-elaboration-tools.png
   :alt: Screenshots shows highlighted article reply elaboration tools
   :scale: 80%
   :align: center

.. warning::
   - Be aware that your text gets replaced when you select one
     of the text tools. If you are not satisfied with the result, try using
     the undo feature by pressing :kbd:`Ctrl` + :kbd:`z`.
   - Always double-check the response. Although the feature was carefully
     developed, there may still be minor problems in individual cases due to
     the nature of neural networks.

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
