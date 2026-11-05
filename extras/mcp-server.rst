MCP Server
==========

Zammad has its own server for the *Model Context Protocol* (MCP). Connect an
AI client you already use to it, for example a chat application or a coding
tool, and read, find and update your tickets from there. The server is part of
every installation, you do not install or run anything in addition.

Whether the server accepts connections is a decision of your admin, see the
:admin-docs:`API settings </system/api.html>`. If a connection to
``https://<fqdn>/mcp`` fails, ask your admin whether the server is enabled.

Connect an AI Client
--------------------

Connecting takes a personal access token and two entries in your client: the
address of the server and the token itself.

Create a Personal Access Token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The client connects with a personal access token of your account. Open your
profile (*Avatar > Profile > Token Access*, see
:doc:`Personal settings </extras/user-menu-profile-settings>`) and create a
token with the ``ticket.agent`` permission, so that the client can work with
tickets. You can give the token an expiration date. Copy the token that Zammad
shows you when the token is created.

Add Zammad to Your Client
^^^^^^^^^^^^^^^^^^^^^^^^^

Add Zammad to the client as an MCP server with:

- the server address, ``https://<fqdn>/mcp``, where ``<fqdn>`` is the domain
  you open Zammad with

- the token, sent as an HTTP header with every request:
  ``Authorization: Bearer <token>``

For the Claude Code client, the connection is one command:

.. code-block:: console

   $ claude mcp add --transport http zammad https://<fqdn>/mcp --header "Authorization: Bearer <token>"

Zammad answers only under the address it is configured for, the one you open
Zammad with. If the connection fails, check that the client uses exactly that
address.

What the Client Can Do
----------------------

The connected client works with your permissions: it can do exactly what the
token and your account may do, nothing more, and it records its changes as
made by you. A user without agent permissions, such as a customer, gets no
tools from the server.

- Open a ticket by its number, its ID or a pasted link, and read its messages,
  internal notes, attachments, history and shared draft.

- Read a ticket's customer and organization.

- Find tickets by words and by names, such as the customer, organization,
  state, owner, group or priority of a ticket.

- List your own overviews and their tickets, and sort the lists, for example
  by creation or last update, so that the client can start at the oldest
  ticket.

- Search users, organizations and the knowledge base.

- Change ticket attributes, set tags and add internal notes.

- Save and send shared drafts, and link tickets and knowledge base answers.

- Create tickets and write messages.

Messages, notes and drafts can be written as plain text or as HTML, Zammad
removes unsafe markup from the latter. Where a ticket requires time
accounting, the client records the time you name. Without it, Zammad refuses
the message from the client, so the client has to ask you first. In Zammad
itself you can still skip the accounting.

Approval of Outgoing Messages
-----------------------------

Where the client supports it, Zammad asks you to approve a message before it
reaches a customer. The approval request shows the complete text of the
message, the recipients and the visibility, and Zammad sends nothing without
your approval.

If you decline, Zammad sends nothing and changes nothing on the ticket. The
same happens where a client does not show the approval form, for example
because it does not support it: Zammad tells the client that nothing was
changed, and the client can then offer to save the text as the ticket's shared
draft, where the group allows shared drafts, for you to send it from Zammad
itself.
