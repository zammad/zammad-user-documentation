MCP Server
==========

Zammad has its own server for the *Model Context Protocol* (MCP). Connect an
AI client you already use to it, for example a chat application or a coding
tool, and read, find and update your tickets from there. The server is part of
every installation, you do not install or run anything in addition.

Whether the server accepts connections is a decision of your admin, see the
:admin-docs:`API settings </system/api.html>`. If a connection to
``https://zammad.example.com/mcp`` fails, ask your admin whether the server is
enabled.

Connect an AI Client
--------------------

Connecting takes a personal access token and the address of the server in your
client.

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

Add Zammad to the client as an MCP server. The client needs the MCP transport
*Streamable HTTP* and the ability to send a fixed ``Authorization: Bearer``
header with every request. Supporting the transport alone is not enough. Such a
client asks for the same three entries:

Server address
   The domain you open Zammad with, with ``/mcp`` after it:
   ``https://zammad.example.com/mcp``.

Transport
   Streamable HTTP.

Token
   ``Authorization: Bearer {your token}``, sent as an HTTP header with every
   request.

Clients that read a JSON configuration, as many do, take Zammad as a server
with the address and the header. Replace ``zammad.example.com`` with the
domain you open Zammad with and ``{your token}`` with the token you copied:

.. code-block:: json

   {
     "mcpServers": {
       "zammad": {
         "url": "https://zammad.example.com/mcp",
         "headers": {
           "Authorization": "Bearer {your token}"
         }
       }
     }
   }

.. warning::
   The token works like your password. Do not put it in a configuration file
   that others can read or that ends up in a repository. Keep the file private,
   or use the reference to a stored secret where your client supports one.

Other clients ask for the same three entries in their own form. Once the
connection works, a first request such as "Show my assigned tickets" shows
whether the client reaches Zammad.

Zammad answers only under the address it is configured for, the one you open
Zammad with. If the connection fails, check that the client uses exactly that
address.

What the Client Can Do
----------------------

The connected client works with your permissions: it can do exactly what the
token and your account may do, nothing more, and it records its changes as
made by you. A user without agent permissions, such as a customer, gets no
tools from the server. The complete list of the tools, with the access of each
and its limits, is in the :docs:`MCP tool reference </api/mcp.html>`.

- Open a ticket by its number, its ID or a pasted link, and read its messages,
  internal notes, attachments, history and shared draft.

- Read a ticket's customer and organization.

- Find tickets by words and by names, such as the customer, organization,
  state, owner, group or priority of a ticket.

- List your own overviews and their tickets, and sort the lists, for example
  by creation or last update, so that the client can start at the oldest
  ticket.

- Search users, organizations and the knowledge base.

- Read the text of files attached to a message: text files up to 10 MB, other
  files come back as a link to download them.

- Change ticket attributes, set tags and add internal notes.

- Save and send shared drafts, and link tickets and knowledge base answers.

- Create tickets and write messages.

Messages, notes and drafts can be written as plain text or as HTML. Zammad
removes unsafe markup from the latter. SMS, Telegram, WhatsApp and Facebook
accept plain text only, HTML is refused there. Files cannot be sent through the
client: if you want to send one, add it to the message in Zammad itself.

Where a ticket asks for time accounting, the client asks you for the time and
records it. You can also tell it that you account no time, and Zammad then
records the message without accounted time.

Approval of Outgoing Messages
-----------------------------

Where the client can show it, Zammad asks you to approve a message before it
reaches a customer. The approval request shows the complete text of the
message, the recipients and the visibility, and Zammad sends only after you
accept.

If you decline, Zammad sends nothing and changes nothing on the ticket. The
client can then offer to save the text as the ticket's shared draft, where the
group allows shared drafts, for you to send it from Zammad itself.

A client that cannot show the approval form relies on its own approval of the
tool call, as it does for every change, and Zammad does not ask a second time.
Zammad still wants your yes for two changes: replacing a shared draft that is
already saved and closing a ticket whose checklist is incomplete. Keep the
approval of tool calls enabled in your client, because a client that runs them
without a prompt sends a message without any further question.
