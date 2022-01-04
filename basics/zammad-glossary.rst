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
   it doesn't work, find an admin in your organization and ask them – chances
   are, they can help.

Agent
   An agent is what we call a user in Zammad who processes tickets/inquiries.
   There are usually several or many agents who use Zammad regularly and
   sometimes even consider it their main tool. Some of them are admins,
   meaning that they can change settings, user rights, and so on (see above).

API
   An API (Application Programming Interface) is a connection that allows you
   to create or modify business objects. Zammad has a REST
   (`Representational State Transfer`_) API that allows our users,
   among other things, to connect third-party systems to their instance
   (such as social media or messengers).
   
   You can learn more on our `API landing page`_.

.. _Representational State Transfer:
   https://en.wikipedia.org/wiki/Representational_state_transfer

.. _API landing page:
   https://zammad.com/en/product/features/rest-api

Automation
   There are many processes that can be automated with Zammad.
   This means that certain steps or actions take place automatically,
   hence no further action is required from the agents.
   One example would be the weekly deletion of tickets at a pre-defined time.

Article
   Each correspondence within a ticket is called an article. Ticket articles
   can be internal (so only agents can see them) or public
   (e.g. emails to your customers, which they receive, too).

Autosave
   Autosave might be one of the coolest traits of Zammad:
   It saves all your work as you go along, so if you ever log out unexpectedly
   or your browser crashes (we’ve all been there…) none of your work gets lost!
   
   You can learn more on our `Autosave landing page`_.

.. _Autosave landing page:
   https://zammad.com/en/product/features/autosave

B
-

Branding
   Every company has a different identity, and Zammad accommodates this in
   various ways, e.g. by letting you design your signatures freely and add
   your company logo to the platform.
   
   `Learn more about branding options in the admin documentation`_.

.. _Learn more about branding options in the admin documentation:
   https://admin-docs.zammad.org/en/latest/settings/branding.html

C
-

Custom Development (CD)
   We are constantly working on improving Zammad, and we keep adding new
   features with every single release. However, sometimes our customers might
   require a very specific new feature, addition, or adjustment that is either
   very urgent or very particular to their individual use case.
   This is when a custom development can take place: We offer the customer to
   develop the desired feature at a price that we agree upon previously
   (which is based on the expected hours needed for completion).

Changelog
   With every new release comes a new changelog. It is basically a list of all
   the things that have changed, from new enhancements to bug fixes.
   
   `You can find them all on our GitHub`_!

.. _You can find them all on our GitHub:
   https://github.com/zammad/zammad/blob/stable/CHANGELOG.md

Customer
   A customer is a person that you communicate with from within Zammad.
   Every customer receives a profile page, which we call the
   `Customer Information Page`_, and it shows all the tickets of this particular
   customer.
   Various customers can be assigned to the same organization.
   Each customer can access their individual `Customer Interface`_, where they
   see all their tickets with the current status and live updates.

.. _Customer Information Page:
   https://user-docs.zammad.org/en/latest/extras/customers.html

.. _Customer Interface:
   https://zammad.com/en/product/features/customer-interface

Core Workflows
   This feature allows every organization to configure their individual dynamic
   fields and ticket masks based on their specific workflows.
   This way, certain Groups will only (or always) see certain fields.
   You can even set up dependencies, as in, if one field is filled in,
   another one opens up or becomes mandatory.
   
   `Learn more about Core Worklows in the admin documentation`_.

.. _Learn more about Core Worklows in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/core-workflows.html

CTI
   CTI stands for Computer Telephony Integration and allows you to collect
   detailed information on all your incoming and outgoing calls.
   This includes, for example, a call log, an overview of which agent is
   currently on a call, a caller ID search, and even a Do-Not-Disturb-Mode.
   
   `Learn more on our CTI landing page`_.

   Here's the fitting documentation pages:

      * `generic CTI`_
      * `placetel CTI`_
      * `sipgate CTI`_

.. _Learn more on our CTI landing page:
   https://zammad.com/en/product/features/cti-integration

.. _generic CTI:
   https://admin-docs.zammad.org/en/latest/system/integrations/generic-cti.html

.. _placetel CTI:
   https://admin-docs.zammad.org/en/latest/system/integrations/placetel-cti.html

.. _sipgate CTI:
   https://admin-docs.zammad.org/en/latest/system/integrations/sipgate.html

Checkmk
   Checkmk is a powerful IT monitoring tool that can send real-time status
   alerts to Zammad via email or REST API. Set these alerts up in Checkmk,
   and Zammad will automatically create, update, and close tickets based on
   the health of your system.
   
   `Learn more about checkmk integration in the admin documentation`_.

.. _Learn more about checkmk integration in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/checkmk/index.html

Clearbit
   Clearbit is a marketing data engine designed to collect information on your
   contacts. Thus, new queries from unknown users in Zammad can be automatically
   enriched with information such as company, number of employees,
   annual turnover, industry, and much more.
   
   `Learn more about clearbit integration in the admin documentation`_.

.. _Learn more about clearbit integration in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/clearbit.html

Conflict Warning
   When two agents edit the same ticket at the same time, a lot can go wrong -
   from duplicate replies to overwritten messages. Zammad helps you to avoid
   this with its integrated conflict warning. So if you see another agents
   avatar and a little pen at the bottom of your ticket, it means they are
   currently editing it.
   
   :ref:`Learn more on our following up page <caution-im-working-here>`.

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
   If this Glossary isn’t enough already (just kidding, it won’t be),
   our Documentation is the place to head to for all information on Zammad,
   especially when it comes to the more technical aspects,
   such as settings or installations.

   We have three different ones:
   `Zammad for Agents`_, `Zammad for Admins`_, and the
   `general Zammad Documentation`_ (System Administrators, API).

.. _Zammad for Agents:
   https://user-docs.zammad.org/en/latest/

.. _Zammad for Admins:
   https://admin-docs.zammad.org/en/latest/

.. _general Zammad Documentation:
   https://docs.zammad.org/en/latest/

E
-

Escalation
   An escalation is what happens after the deadline for a ticket has passed and,
   for example, no update to the customer has been created. The ticket is marked
   in red in your taskbar and the overviews and everyone else who is involved in
   its process gets very sad. So don't let tickets escalate! Also, in order to
   prevent escalations, you can use our SLAs
   (see :ref:`SLAs <glossary-sla>`).

External Authentication
   External authentication is an easy, one-click option for your users to log
   into Zammad. It has various benefits: not only is it faster but it also
   means that your users will have to remember fewer passwords.
   Zammad currently supports more than ten login providers, such as Facebook,
   GitHub, GitLab, Google, or Microsoft / Office365.

   `See our admin documentation for all third party authenticators`_.

.. _See our admin documentation for all third party authenticators:
   https://admin-docs.zammad.org/en/latest/settings/security/third-party.html

Exchange Integration
   The Exchange integration allows users to sync their contacts from their
   Exchange address book with Zammad. This way, every time a contact is updated
   in Exchange, the iteration will be reflected in Zammad, giving you direct
   access to all your Exchange contacts from within your helpdesk.

   `Learn more about the exchange integration in our admin documentation`_.

.. _Learn more about the exchange integration in our admin documentation:
   https://admin-docs.zammad.org/de/latest/system/integrations/exchange.html

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

F
-

Feature
   A feature is what we call the different functionalities of Zammad,
   such as our integrations, productivity tools, or time-saving aspects.
   We keep adding new features with every release.

Feature request
   Users can let us know if they are missing a particular feature in Zammad.
   We collect all of their wishes 
   `in our Community in the Feature Request category`_. 
   If a request comes in regularly and we feel that it would be a
   great addition, we'll put it on our roadmap and start working on it.

.. _in our Community in the Feature Request category:
   https://community.zammad.org/c/stuff-you-like-zammad-to-have-feel-free-to-discuss-and-add-proposals/6

Feature sponsoring
   If an organization urgently requires one of the features on the list,
   they can fast-forward the development and put it on top of the list by
   sponsoring it, which means that they cover the costs for the development.

G
-

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

   `Learn more on our group landing page`_.

.. _Learn more on our group landing page:
   https://zammad.com/en/product/features/groups

Grafana
   Grafana is an open-source reporting tool.
   Zammad users on the Plus plan can integrate it into their instance and
   receive detailed analytics on their performance.

   .. hint:: **🤓 Self Hosted users**

      Hooking up Grafana to Elasticsearch is an possibility you can do on your
      own as well.

   `Learn more on how to add Grafana dashboards for Zammad on our documentation`_.

.. _Learn more on how to add Grafana dashboards for Zammad on our documentation:
   https://docs.zammad.org/en/latest/appendix/reporting-tools-thirdparty/grafana.html

GitHub
   GitHub is a service for the version management of software development
   projects. It uses Git, a software that tracks changes in file sets.
   Here at Zammad, we use it to maintain our repository.

   As Zammad in an open-source project, many developers and tech-lovers from all
   over the world contribute to it. GitHub is where we coordinate all of this.

   `You can find the repository here`_.

   Besides our own repo, Zammad also has an integration for GitHub.
   It creates a data exchange that shows you all relevant information about your
   issues directly in the helpdesk, such as status or assignees.

   `Administrators can learn more about GitHub in the admin documentation`_,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/github-gitlab-integration`.

.. _You can find the repository here:
   https://github.com/zammad/zammad

.. _Administrators can learn more about GitHub in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/github.html

GitLab
   GitLab is similar to GitHub.
   Here at Zammad, we use it for our internal development.

   There is also an integration that allows users to connect GitLab to Zammad
   so that all their issues and their corresponding changes are reflected in
   both systems.

   `Administrators can learn more about GitLab in the admin documentation`_,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/github-gitlab-integration`.

.. _Administrators can learn more about GitLab in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/gitlab.html

H
-

.. include:: /basics/emptiness.include.rst

I
-

i-doit
   i-doit is a CMDB (Configuration Management Data Base).
   It helps you to keep an eye on every piece of the physical and digital
   infrastructure. A corresponding integration makes it possible to connect
   it to Zammad, where it adds a new tab to Zammad's ticket sidebar so
   you can link to existing i-doit objects for easy reference.
   It also allows you to create Zammad tickets in i-doit.

   `Administrators can learn more about i-doit in the admin documentation`_,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/i-doit-track-company-property`.

.. _Administrators can learn more about i-doit in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/i-doit.html

Icinga
   Icinga is a monitoring system that supervises the availability of an
   organization's entire system infrastructure.
   It can be integrated into Zammad so that it triggers a ticket in case
   of a warning situation.

   `Learn more about Icinga on our landing page`_.

.. _Learn more about Icinga on our landing page:
   https://zammad.com/en/product/features/icinga-integration

Issue-tracking system
   Issue trackers are usually systems that track processes on a technical level.
   Two of the best-known examples are GitHub and GitLab.

   Zammad is also often referred to as an issue-tracking system.
   However, as a helpdesk, it focuses on communication at the customer
   level rather than the technical level.

J
-

.. include:: /basics/emptiness.include.rst

K
-

Knowledge Base
   Think of a very extensive set of FAQs – that’s exactly what the
   Zammad knowledge base is. It collects all important information:
   definitions, processes, how-to’s, organigrams, etc.

   Knowledge base articles can be either internal or external, so you can
   either show them to the world (good for information on your product or
   service, for example) or keep them for your team
   (e.g. for internal processes or team info).

   `Administrators can learn more about the Knowledge Base in the admin documentation`_,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/knowledge-base`.

.. _Administrators can learn more about the Knowledge Base in the admin documentation:
   https://admin-docs.zammad.org/en/latest/manage/knowledge-base.html

Kibana
   Kibana is a browser-based, open-source reporting tool that focuses on data
   evaluation. It was developed by Elastic, which is why it is not a surprise
   that it uses data from Elasticsearch for its analytics.

   Kibana can be integrated with Zammad, allowing for helpdesk data to be
   mapped in the reporting tool.

   .. hint:: **🤓 This does not apply to SaaS Zammad instances.**

   `Learn more about Kibana on our landing page`_.

.. _Learn more about Kibana on our landing page:
   https://zammad.com/en/product/features/kibana-integration

L
-

LDAP
   A Lightweight Directory Access Protocol (LDAP) helps provide information
   about your users within Zammad. Authentication of users against the LDAP
   and LDAP role mapping to Zammad roles are also possible.

   `Learn more about LDAP integration in the admin documentation`_.

.. _Learn more about LDAP integration in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/ldap.html

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

   `Administrators can learn more about Macros in the admin documentation`_,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/advanced/macros`.

.. _Administrators can learn more about Macros in the admin documentation:
   https://admin-docs.zammad.org/en/latest/manage/macros.html

Migrator / Migration Wizard
   If a company wants to switch from another helpdesk software to Zammad,
   they often have one concern: What about their existing data?
   That's why we have built our migration wizards that help with migrating all
   data at the touch of a button.

Monit
   Monit is an open-source monitoring tool that relies on a simple setup and
   a strong community. You can integrate it with Zammad – this way,
   a ticket is created every time you receive an email in Monit.

   `Learn more about Monit on our landing page`_.

.. _Learn more about Monit on our landing page:
   https://zammad.com/en/product/features/monit-integration

Mentions
   Mentions are a Zammad feature that allows you to tag another agent in a
   ticket. Just type ``@@`` and the name. The selected person will be notified
   and will be watching the ticket from now on.

   Learn more on this page: :ref:`mentions`.

N
-

Nagios
   Nagios is another monitoring tool that alerts IT teams when, for example,
   a server is no longer accessible or a hard disk is about to be exhausted.
   Nagios can be integrated with Zammad so that a ticket is created in case of
   an alert.

   `Learn more about Nagios on our landing page`_.

.. _Learn more about Nagios on our landing page:
   https://zammad.com/en/product/features/nagios-integration

O
-

Owner
   The owner of a ticket is the person responsible for it and ensures that it
   is processed in the best possible way.
   Of course, ownership can be transferred to another agent.
   In this case, it is recommended to leave a handover note on the ticket so
   that the new owner knows what is expected of them.

   Learn more about ticket owners on this page:
   :doc:`/basics/service-ticket/settings`

Organization
   An organization identifies a grouping of customers that operate under the
   same roof or within the same customer group.
   If a customer whose organization is "sharing" logs in to the customer
   interface, this user has access to all tickets of his organization.

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

Q
-

.. include:: /basics/emptiness.include.rst

R
-

Role
   Everyone who logs into Zammad has a predefined role. There are three types:
   admin, agent, and customer.

   Admins have the most rights: they can define roles, permissions,
   and settings for the entire team and instance.

   Agents can view and edit tickets, but not change any settings other than
   those of their own profiles.

   Customers can view their tickets’ processing status in their
   individual Customer Interface.

Release
   Every few months, we bring a new version of Zammad into the world,
   which is called a release. It all started with Zammad 1.0.

   Every release adds new features to our software.
   There are major and minor releases:
   major releases (such as Zammad 1.0, 2.0, etc.) bring major changes.
   Minor releases are installed on top of them (such as 1.1, 2.1, etc.)
   and bring smaller updates.

S
-

SSO
   Single-sign-on (SSO) allows you to access all your systems and devices with
   just one login. There are various providers that make this process easy and
   secure. Zammad currently supports SSO via SAML and Shibboleth.

   .. hint:: 🤓 Self Hosted users can also use Kerberos authentication.

   `You can learn more about SSO on our landing page`_.

.. _You can learn more about SSO on our landing page:
   https://zammad.com/en/product/features/sso

S/MIME
   S/MIME is the most widely-supported method for secure email communication.
   By activating it in Zammad, all messages sent from Zammad will be signed and
   encrypted.

   `Administrators can learn more about S/MIME in the admin documentation`_,
   if you're an agent you can learn more about the functionality on this page:
   :doc:`/extras/secure-email`.

.. _Administrators can learn more about S/MIME in the admin documentation:
   https://admin-docs.zammad.org/en/latest/system/integrations/smime/index.html

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

   `Learn more about SLAs on our landing page`_.

.. _Learn more about SLAs on our landing page:
   https://zammad.com/en/product/features/sla

Status
   Every ticket has a status. You can change it once you've updated the ticket.
   There are four types of status, and they are all color-coded.

   Learn more about states and they color coding on this page:
   :doc:`/basics/service-ticket/settings/state`

T
-

Text module
   If you find that you send the same answers / text bits over and over again,
   you can save yourself a bunch of work and create a text module.
   This way, you just need to type ``::`` shortcut and the pre-defined paragraph
   will automatically appear in your article.

   For example, here at Zammad, we have a text module with the shortcut
   ``::ilff``, which turns into ``I look forward to your feedback``.

   `Administrators can learn more about text modules here`_.
   Agents can learn more about this function on this page:
   :doc:`/advanced/text-modules`

.. _Administrators can learn more about text modules here:
   https://admin-docs.zammad.org/en/latest/manage/text-modules.html

(Ticket) Template
   If you create many similar tickets or write many similar texts, you can
   create a template for them. This is helpful for introductions to your
   product/service or for drawing up an offer. It's a real time-saver!

   You can learn more on this page: :doc:`/advanced/ticket-templates`.

Tags
   Tags help you to categorize tickets. You can define them based on your use
   case. For example, if you're a retail business, your tags could be based on
   your product categories to help you organize tickets by the type of product
   they refer to.
   But they could also be based on the type of request, e.g.
   refund, delivery issue, missing…

   `Administrators can learn more about tags here`_.
   Agents can learn more about this function on this page:
   :doc:`/basics/service-ticket/settings/tags`

.. _Administrators can learn more about tags here:
   https://admin-docs.zammad.org/en/latest/manage/tags.html

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

   `Learn more about webhooks on this page`_.

.. _Learn more about webhooks on this page:
   https://admin-docs.zammad.org/en/latest/manage/webhook.html


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
