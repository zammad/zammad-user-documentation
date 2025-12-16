Zammad Glossary
===============

Ever wondered what we mean by a specific term?
We've been collecting the most relevant terms below for your insight.

.. note::

   Due to translation alphabetical sorting may be off in non english versions
   of this page.

Quickly jump to...
   `A`_ `B`_ `C`_ `D`_ `E`_ `F`_ `G`_ `H`_ `I`_ `J`_ `K`_ `L`_ `M`_
   `N`_ `O`_ `P`_ `Q`_ `R`_ `S`_ `T`_ `U`_ `V`_ `W`_ `X`_ `Y`_ `Z`_

--------------------------------------------------------------------------------

A
-

Admin
   An admin(istrator) is a user in Zammad who has special rights.
   Admins can configure user accesses, time recording settings, templates,
   and text modules and, on a higher level, integrations, reporting, etc.
   So if you're looking to make a change within your Zammad and you find that
   it doesn't work, find an admin in your organization and ask them - chances
   are, they can help.

Agent
   An agent is what we call a user in Zammad who processes tickets/inquiries.
   There are usually several or many agents who use Zammad regularly and
   sometimes even consider it their main tool. Some of them are admins,
   meaning that they can change settings, user rights, and so on (see above).

API
   An API (Application Programming Interface) is a connection that allows you
   to create or modify business objects. Zammad has a REST
   (`Representational State Transfer <https://en.wikipedia.org/wiki/Representational_state_transfer>`_)
   API that allows our users, among other things, to connect third-party systems
   to their instance (such as social media or messengers).

   You can learn more on our
   `API landing page <https://zammad.com/en/product/features/rest-api>`_.

Article
   Each correspondence within a ticket is called an article. Ticket articles
   can be internal (so only agents can see them) or public
   (e.g. emails to your customers, which they receive, too).

Auto Response
   Zammad can send automatically generated responses to customers. By
   default, this is configured for newly created tickets (to confirm that the
   email was received and to provide the ticket number to the customer). Your
   admin may change this or even add more auto generated messages.

Automation
   There are many processes that can be automated with Zammad.
   This means that certain steps or actions take place automatically,
   hence no further action is required from the agents.
   One example would be the weekly deletion of tickets at a pre-defined time.

Autosave
   Autosave might be one of the coolest traits of Zammad:
   It saves all your work as you go along, so if you ever log out unexpectedly
   or your browser crashes (we've all been there…) none of your work gets lost!

   You can learn more on our
   `Autosave landing page <https://zammad.com/en/product/features/autosave>`_.

.. _glossary-avatar:

Avatar
   An avatar is basically a graphical representation of a user. By defaults
   the user's avatar consists of the initials of the user. It can be an image,
   too. To customize it, go to the avatar section in your
   :doc:`user profile </extras/profile-and-settings>`.

   The avatar of an user is visible in different places in Zammad. For example
   you can see it next to an article in a ticket or in the bottom bar if
   another agent is viewing or editing the same ticket.


B
-

Branding
   Every company has a different identity, and Zammad accommodates this in
   various ways, e.g. by letting you design your signatures freely and add
   your company logo to the platform.

   Learn more about branding options
   :admin-docs:`in the admin documentation </settings/branding.html>`.

C
-

Changelog
   With every new release comes a new changelog. It is basically a list of all
   the things that have changed, from new enhancements to bug fixes.

   You can find them all on our `GitHub <https://github.com/zammad/zammad/blob/stable/CHANGELOG.md>`_!

Channel
   A channel is a way how customers can get in touch with you. Standard channels
   are email and phone. Additional channels can be configured by your admin.

Checkmk
   Checkmk is a powerful IT monitoring tool that can send real-time status
   alerts to Zammad via email or REST API. Set these alerts up in Checkmk,
   and Zammad will automatically create, update, and close tickets based on
   the health of your system.

   Learn more about checkmk integration
   :admin-docs:`in the admin documentation </system/integrations/checkmk/index.html>`.

Clearbit
   Clearbit is a marketing data engine designed to collect information on your
   contacts. Thus, new queries from unknown users in Zammad can be automatically
   enriched with information such as company, number of employees,
   annual turnover, industry, and much more.

   Learn more about clearbit integration
   :admin-docs:`in the admin documentation </system/integrations/clearbit.html>`.

Conflict Warning
   When two agents edit the same ticket at the same time, a lot can go wrong -
   from duplicate replies to overwritten messages. Zammad helps you to avoid
   this with its integrated conflict warning. So if you see another agents
   avatar and a little pen at the bottom of your ticket, it means they are
   currently editing it.

   Learn more on our :ref:`following up page <caution-im-working-here>`.

Core Workflows
   This feature allows every organization to configure their individual dynamic
   fields and ticket masks based on their specific workflows.
   This way, certain Groups will only (or always) see certain fields.
   You can even set up dependencies, as in, if one field is filled in,
   another one opens up or becomes mandatory.

   Learn more about Core Workflows
   :admin-docs:`in the admin documentation </system/core-workflows.html>`.

CTI
   CTI stands for Computer Telephony Integration and allows you to collect
   detailed information on all your incoming and outgoing calls.
   This includes, for example, a call log, an overview of which agent is
   currently on a call, a caller ID search, and even a Do-Not-Disturb-Mode.

   You can learn more on our `CTI landing page <https://zammad.com/en/product/features/cti-integration>`_.

   Here you can find the fitting documentation pages:

      * :admin-docs:`generic CTI </system/integrations/cti/generic.html>`
      * :admin-docs:`placetel CTI </system/integrations/cti/placetel.html>`
      * :admin-docs:`sipgate CTI </system/integrations/cti/sipgate.html>`

Custom Development (CD)
   We are constantly working on improving Zammad, and we keep adding new
   features with every single release. However, sometimes our customers might
   require a very specific new feature, addition, or adjustment that is either
   very urgent or very particular to their individual use case.
   This is when a custom development can take place: We offer the customer to
   develop the desired feature at a price that we agree upon previously
   (which is based on the expected hours needed for completion).

Custom Object Attributes
   Zammad allows the creation of custom object attributes by admins. This can be
   done on ticket level, user level, organization level or group level.

   You can think of such a custom object attribute as a new field which has
   a pre-defined format and optionally selectable values.

Customer
   A customer is a person that you communicate with from within Zammad.
   Every customer receives a profile page, which we call the
   `Customer Information Page <https://user-docs.zammad.org/en/latest/extras/customers.html>`_,
   and it shows all the tickets of this particular customer.
   Various customers can be assigned to the same organization.
   Each customer can access their individual
   `Customer Interface <https://zammad.com/en/product/features/customer-interface>`_,
   where they see all their tickets with the current status and live updates.


D
-

Dashboard
   The dashboard is every agent's individual Welcome Page in Zammad and gives
   you feedback on your situation by collecting information and statistics
   about your work.
   Here you can find all sorts of overviews, such as the open tickets,
   the average waiting time, or the reopening rate. You can also see what your
   colleagues are doing by checking the Activity Stream.

   Learn more on :doc:`/extras/dashboard`.

Documentation
   If this Glossary isn't enough already (just kidding, it won't be),
   our Documentation is the place to head to for all information on Zammad,
   especially when it comes to the more technical aspects,
   such as settings or installations.

   We have three different ones:
   :doc:`/index`, :admin-docs:`Zammad Admin Documentation </>`, and the
   :docs:`Zammad System Documentation </>`.

E
-

Elasticsearch
   Zammad offers an Elasticsearch integration (a free and open search engine)
   that makes the search process within Zammad super fast
   (even for data sets of several terra bytes!).

   Spoiler: Zammad is currently the only helpdesk system with a search function
   that combs attachments, too!

   .. note:: **🤓 This affects hosted environments only!**

      Via a read-only user in Elasticsearch, you can also integrate your
      favorite reporting tool (e.g. like Grafana).

      ..
         While technically self hosted users can enable such a behavior
         as well it is out of our application scope. By default SaaS Plus
         in Zammad universe is the only part that does this automatically.

Escalation
   An escalation is what happens after the deadline for a ticket has passed and,
   for example, no update to the customer has been created. The ticket is marked
   in red in your taskbar and the overviews and everyone else who is involved in
   its process gets very sad. So don't let tickets escalate! Also, in order to
   prevent escalations, you can use our SLAs
   (see :ref:`SLAs <glossary-sla>`).

Exchange Integration
   The Exchange integration allows users to sync their contacts from their
   Exchange address book with Zammad. This way, every time a contact is updated
   in Exchange, the iteration will be reflected in Zammad, giving you direct
   access to all your Exchange contacts from within your helpdesk.

   Learn more about the exchange integration
   :admin-docs:`in our admin documentation </system/integrations/exchange.html>`.

External Authentication
   External authentication is an easy, one-click option for your users to log
   into Zammad. It has various benefits: not only is it faster but it also
   means that your users will have to remember fewer passwords.
   Zammad currently supports more than ten login providers, such as Facebook,
   GitHub, GitLab, Google, or Microsoft / Office365.

   See our :admin-docs:`admin documentation </settings/security/third-party.html>`
   for all third party authentication providers.

F
-

Feature
   A feature is what we call the different functionalities of Zammad,
   such as our integrations, productivity tools, or time-saving aspects.
   We keep adding new features with every release.

Feature request
   Users can let us know if they are missing a particular feature in Zammad.
   We collect all of their wishes
   `in our Community in the Feature Request category <https://community.zammad.org/c/stuff-you-like-zammad-to-have-feel-free-to-discuss-and-add-proposals/6>`_.
   If a request comes in regularly and we feel that it would be a
   great addition, we'll put it on our roadmap and start working on it.


Feature sponsoring
   If an organization urgently requires one of the features on the list,
   they can fast-forward the development and put it on top of the list by
   sponsoring it, which means that they cover the costs for the development.

G
-

GitHub
   GitHub is a service for the version management of software development
   projects. It uses Git, a software that tracks changes in file sets.
   Here at Zammad, we use it to maintain our repository.

   As Zammad in an open-source project, many developers and tech-lovers from all
   over the world contribute to it. GitHub is where we coordinate all of this.

   You can find the repository `here <https://github.com/zammad/zammad>`_.

   Besides our own repo, Zammad also has an integration for GitHub.
   It creates a data exchange that shows you all relevant information about your
   issues directly in the helpdesk, such as status or assignees.

   Administrators can learn more about GitHub
   :admin-docs:`in the admin documentation </system/integrations/github.html>`,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/github-gitlab-integration`.

GitLab
   GitLab is similar to GitHub.
   Here at Zammad, we use it for our internal development.

   There is also an integration that allows users to connect GitLab to Zammad
   so that all their issues and their corresponding changes are reflected in
   both systems.

   Administrators can learn more about GitLab
   :admin-docs:`in the admin documentation </system/integrations/gitlab.html>`,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/github-gitlab-integration`.

Grafana
   Grafana is an open-source reporting tool.
   Zammad users on the Plus plan can integrate it into their instance and
   receive detailed analytics on their performance.

   .. hint:: **🤓 Self Hosted users**

      Hooking up Grafana to Elasticsearch is an possibility you can do on your
      own as well.

   Learn more on how to add Grafana dashboards for Zammad
   :docs:`in our documentation </appendix/reporting-tools-thirdparty/grafana.html>`.

Groups
   Groups are a synonym for departments or processing groups.
   The incoming tickets are assigned to them.
   The corresponding group is responsible for the processing.
   Within the group, an owner can be defined, who is then responsible for
   this ticket. Access rights to tickets are also controlled via the groups.
   The possible permissions are "full access", "read-only" and "no access".

   If you have worked with the OTRS system in the past,
   you might remember the principle of "queues".
   The groups in Zammad are the same as the queues in OTRS.

   You can learn more on our `group landing page <https://zammad.com/en/product/features/groups>`_.


H
-

.. include:: /basics/emptiness.include.rst

I
-

Icinga
   Icinga is a monitoring system that supervises the availability of an
   organization's entire system infrastructure.
   It can be integrated into Zammad so that it triggers a ticket in case
   of a warning situation.

   You can learn more on our `Icinga landing page <https://zammad.com/en/product/features/icinga-integration>`_.

Issue-tracking system
   Issue trackers are usually systems that track processes on a technical level.
   Two of the best-known examples are GitHub and GitLab.

   Zammad is also often referred to as an issue-tracking system.
   However, as a helpdesk, it focuses on communication at the customer
   level rather than the technical level.

i-doit
   i-doit is a CMDB (Configuration Management Data Base).
   It helps you to keep an eye on every piece of the physical and digital
   infrastructure. A corresponding integration makes it possible to connect
   it to Zammad, where it adds a new tab to Zammad's ticket sidebar so
   you can link to existing i-doit objects for easy reference.
   It also allows you to create Zammad tickets in i-doit.

   Administrators can learn more about i-doit
   :admin-docs:`in the admin documentation </system/integrations/i-doit.html>`,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/i-doit-track-company-property`.

J
-

.. include:: /basics/emptiness.include.rst

K
-

Kibana
   Kibana is a browser-based, open-source reporting tool that focuses on data
   evaluation. It was developed by Elastic, which is why it is not a surprise
   that it uses data from Elasticsearch for its analytics.

   Kibana can be integrated with Zammad, allowing for helpdesk data to be
   mapped in the reporting tool.

   .. hint:: **🤓 This does not apply to SaaS Zammad instances.**

   You can learn more on our `Kibana landing page <https://zammad.com/en/product/features/kibana-integration>`_.

Knowledge Base
   Think of a very extensive set of FAQs - that's exactly what the
   Zammad knowledge base is. It collects all important information:
   definitions, processes, how-to's, organigrams, etc.

   Knowledge base articles can be either internal or external, so you can
   either show them to the world (good for information on your product or
   service, for example) or keep them for your team
   (e.g. for internal processes or team info).

   Administrators can learn more about the Knowledge Base
   :admin-docs:`in the admin documentation </manage/knowledge-base.html>`,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/knowledge-base`.

L
-

LDAP
   A Lightweight Directory Access Protocol (LDAP) helps provide information
   about your users within Zammad. Authentication of users against the LDAP
   and LDAP role mapping to Zammad roles are also possible.

   Learn more about LDAP integration
   :admin-docs:`in the admin documentation </system/integrations/ldap/index.html>`.

M
-

Macro
   A macro is a series of actions. By starting the macro, the actions are also
   triggered (like a domino effect), so users don't have to work through each
   individual step separately.
   It saves an enormous amount of time and ensures that no step is forgotten.

   An example of this is declaring a ticket as "spam".
   The manual way here would be to assign an owner, set a status, and add the
   tag "spam". Using a macro, all this can be done in just one action.
   Macros can be used in the ticket zoom or within an overview
   (using multiple selection).

   Administrators can learn more about Macros
   :admin-docs:`in the admin documentation </manage/macros.html>`,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/advanced/macros`.

Mentions
   Mentions are a Zammad feature that allows you to tag another agent in a
   ticket. Just type ``@@`` and the name. The selected person will be notified
   and will be watching the ticket from now on.

   Learn more on this page: :ref:`mentions`.

Merging Tickets
   If you have two (or more) tickets about the same issue, you can merge one of
   them into the other. By default, Zammad performs checks if a message from
   an external party belongs to an existing ticket. However, if your customer
   for example writes a completely new email instead of answering the
   auto response, Zammad can't assign the message to the existing ticket but
   creates a new one.

   See :doc:`/advanced/ticket-actions` for further information.

Migrator / Migration Wizard
   If a company wants to switch from another helpdesk software to Zammad,
   they often have one concern: What about their existing data?
   That's why we have built our migration wizards that help with migrating all
   data at the touch of a button.

Monit
   Monit is an open-source monitoring tool that relies on a simple setup and
   a strong community. You can integrate it with Zammad - this way,
   a ticket is created every time you receive an email in Monit.

   You can learn more on our `Monit landing page <https://zammad.com/en/product/features/monit-integration>`_.

N
-

Nagios
   Nagios is another monitoring tool that alerts IT teams when, for example,
   a server is no longer accessible or a hard disk is about to be exhausted.
   Nagios can be integrated with Zammad so that a ticket is created in case of
   an alert.

   You can learn more on our `Nagios landing page <https://zammad.com/en/product/features/nagios-integration>`_.

Notifications
   To avoid overlooking new messages (e.g. from a customer) Zammad notifies you
   about every relevant change by default. You can adjust your general
   notification settings in your user profile. You can even mention other users
   or subscribe to a specific ticket if you are interested how it proceeds.

   See :doc:`/extras/profile-and-settings` for more information.

O
-

Organization
   An organization identifies a grouping of customers that operate under the
   same roof or within the same customer group.
   If a customer whose organization is "sharing" logs in to the customer
   interface, this user has access to all tickets of his organization.

Overview
   Overviews are your starting point to work on tickets. You can think of
   overviews as a kind of filter for existing tickets. Some basic overviews
   are shipped with Zammad by default. If you want to have a custom overview,
   ask your admin to create it.

   For more information please have a look in
   :doc:`/basics/find-ticket`.

Owner
   The owner of a ticket is the person responsible for it and ensures that it
   is processed in the best possible way.
   Of course, ownership can be transferred to another agent.
   In this case, it is recommended to leave a handover note on the ticket so
   that the new owner knows what is expected of them.

P
-

Parent/Child Relationship
   If one ticket results in other subtasks (or additional correspondences),
   you can split it into several tickets. The main one will then be the parent
   ticket and the tickets with related subtopics are children.
   By the way: in the same way, you can also merge two tickets into one.

   Learn more about this function on this page:
   :doc:`/advanced/ticket-actions/link`.

Placetel
   Placetel is a Cloud Telephone System that allows users to make phone calls
   via VoIP. Use your regular phone number and call someone directly on their
   mobile or landline while still having all communication in one place
   (aka Zammad).

   Integrating a Placetel account with Zammad provides users with a call log,
   making the history of their correspondences even more accurate.
   Callers are identified directly by their caller ID - a key function that
   saves agents a lot of time when assigning callers.

   Administrators can learn more on the `placetel CTI` integration page.
   Agents can learn more about this function on this page:
   :doc:`/extras/caller-log`

Priority
   Every ticket gets assigned a priority.
   By default, the priority is 2 (normal).
   But it can be changed to either 1 (low) or 3 (high).

   Priorities can even be adjusted or extended to fit your needs. Your
   administrator can find more information
   :admin-docs:`here </system/objects.html#system-attributes>`.

Q
-

.. include:: /basics/emptiness.include.rst

R
-

Release
   Every few months, we bring a new version of Zammad into the world,
   which is called a release. It all started with Zammad 1.0.

   Every release adds new features to our software.
   There are major and minor releases:
   major releases (such as Zammad 1.0, 2.0, etc.) bring major changes.
   Minor releases are installed on top of them (such as 1.1, 2.1, etc.)
   and bring smaller updates.

Reporting
   The reporting helps keeping an overview over stats and numbers (e.g. created
   tickets per month). There are two types of reporting: the reporting
   functionality integrated in Zammad and the reporting with external tools.

   Admins can find further information
   :admin-docs:`here </manage/report-profiles.html>`.

Role
   Everyone who logs into Zammad has a predefined role. There are three types:
   admin, agent, and customer.

   Admins have the most rights: they can define roles, permissions,
   and settings for the entire team and instance.

   Agents can view and edit tickets, but not change any settings other than
   those of their own profiles.

   Customers can view their tickets' processing status in their
   individual Customer Interface.

S
-

Scheduler
   The scheduler is one of Zammad's automation features. An admin can define
   specific conditions and actions which are applied to tickets with matching
   conditions in a time based manner. More information in the admin
   documentation in the
   :admin-docs:`scheduler section </manage/scheduler.html>`.

Sidebar
   The sidebar on the left side contains all relevant places and object you
   might need. Depending on the configured channels and your permissions, it
   might not include all sections which are listed below:

   - Search bar
   - Notification section
   - Dashboard
   - Overviews
   - Knowledge Base
   - Customer Chat
   - Phone
   - One or more open tickets
   - Bottom section:

      - Avatar
      - Reporting
      - Admin settings
      - Button for ticket creation

Signature
   The signature is your footer in an outgoing message.
   Your customers may find contact details and the name of your
   company/department there. It can even contain your
   :ref:`avatar image <glossary-avatar>`.

   It can be customized by your admin. Further information can be found
   :admin-docs:`here </channels/email/signatures.html>`.

Sipgate
   Sipgate is a SaaS solution for internet telephony.
   The Zammad integration for Sipgate provides users with a detailed call
   overview. If you have a customer that wants to get connected to a certain
   agent, the caller log will tell you if this colleague is currently available.

   Administrators can learn more on the `sipgate CTI` integration page.
   Agents can learn more about this function on this page:
   :doc:`/extras/caller-log`

.. _glossary-sla:

SLA
   A Service Level Agreement (SLA) is a contract between an end-user and a
   company that defines the minimum expected service requirements including
   quality, availability, and punctuality.
   They are used to set expectations and hold companies accountable for keeping
   their promises.

   You can easily set up SLAs in Zammad and define parameters such as the time
   for the first response, an update, and a solution. Once the deadline has been
   reached, the ticket will escalate.

   You can learn more on our `SLA landing page <https://zammad.com/en/product/features/sla>`_.

Splitting tickets
   In case a ticket contains more than one issue and you want to handle it
   in a separate ticket, you can split the ticket. Zammad creates a new ticket
   then based on the selected article for splitting.
   See :doc:`/advanced/ticket-actions` for more information.

SSO
   Single-sign-on (SSO) allows you to access all your systems and devices with
   just one login. There are various providers that make this process easy and
   secure. Zammad currently supports SSO via SAML and Shibboleth.

   .. hint:: 🤓 Self Hosted users can also use Kerberos authentication.

   You can learn more on our `SSO landing page <https://zammad.com/en/product/features/sso>`_.

State
   Every ticket has a state. You can change it once you've updated the ticket.
   There are four types of states, and they are all color-coded.

   Learn more about states and their color coding on this page:
   :ref:`ticket-attributes`

   The available states can be changed or extended. Your admin can find further
   information :admin-docs:`here </system/objects.html#system-attributes>`.

S/MIME
   S/MIME is the most widely-supported method for secure email communication.
   By activating it in Zammad, all messages sent from Zammad will be signed and
   encrypted.

   Administrators can learn more about S/MIME
   :admin-docs:`in the admin documentation </system/integrations/smime/index.html>`,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/secure-email`.

T
-

Tags
   Tags help you to categorize tickets. You can define them based on your use
   case. For example, if you're a retail business, your tags could be based on
   your product categories to help you organize tickets by the type of product
   they refer to.
   But they could also be based on the type of request, e.g.
   refund, delivery issue, missing…

   Administrators can learn more about tags
   :admin-docs:`here </manage/tags.html>`.
   Agents can learn more about this function on this page:
   :ref:`ticket-attributes`

Text module
   If you find that you send the same answers / text bits over and over again,
   you can save yourself a bunch of work and create a text module.
   This way, you just need to type ``::`` shortcut and the pre-defined paragraph
   will automatically appear in your article.

   For example, here at Zammad, we have a text module with the shortcut
   ``::ilff``, which turns into ``I look forward to your feedback``.

   Administrators can learn more about text modules
   :admin-docs:`here </manage/text-modules.html>`.
   Agents can learn more about this function on this page:
   :doc:`/advanced/text-modules`

(Ticket) Template
   If you create many similar tickets or write many similar texts, you can
   create a template for them. This is helpful for introductions to your
   product/service or for drawing up an offer. It's a real time-saver!

   You can learn more on this page: :doc:`/advanced/ticket-templates`.

Title
   The title of a ticket is different based on the channel it came in.
   You can find the title in the sidebar and in the top area in the ticket view.
   If the title is not very meaningful, you can change it by clicking on the
   title in a ticket view.

Ticket hook
   The ticket hook is the identifier of a ticket. By default, it is ``Ticket#``
   with an appended number (e.g. ``Ticket#904627``). It can be changed by an
   admin.
   See :admin-docs:`here </settings/ticket.html>` for further information.

Trigger
   Triggers are one of Zammad's automation features. An admin can define
   specific conditions and actions which are applied to tickets with matching
   conditions. More information in the admin
   documentation in the
   :admin-docs:`trigger section </manage/trigger.html>`.

U
-

User
   A user is any user of the ticket system. Each user is assigned certain
   permissions, which allow them to access certain areas and information.
   Users can have various roles, with the standard options being agent, admin,
   and customer.

V
-

.. include:: /basics/emptiness.include.rst

W
-

Webhooks
   In a nutshell, webhooks are an easy way for systems to communicate with each
   other and allow you to send real-time data to any other application.
   We use them to allow our users to inform a third-party system about new
   information in Zammad.

   Learn more about webhooks on
   :admin-docs:`this page </manage/webhook.html>`.

X
-

.. include:: /basics/emptiness.include.rst

Y
-

.. include:: /basics/emptiness.include.rst

Z
-

Zammad
   Zammad is the greatest helpdesk in the world. Period.
