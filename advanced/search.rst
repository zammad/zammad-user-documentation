Advanced Search
===============

With Zammad, you can limit your search to specific attributes.
This allows you to find e.g. tickets with specific key words and states.
Below information will help you to improve your search results.

For instance, you can search for a ticket of a specific customer::

   customer.firstname: John

or::

   customer.lastname: Doe

If you want to run a more complex search, you can use conditions
with ``()`` and ``AND``/``OR`` options::

   state.name: open AND (article.from:me OR article.from:somebody)

Available Attributes
--------------------

.. hint::

   For a more detailed list of available attributes please take a look into our
   :docs:`Zammad System Documentation </install/elasticsearch/indexed-attributes.html>`.

.. |br| raw:: html

   <br />

.. csv-table:: Attributes and their usuage
   :header: "Attribute", "possible Values", "Example", "Description"
   :widths: 10, 10, 10, 20

   "number", "1118566", "number:1118566 |br|\ number:11185*", "Search for a Ticketnumber"
   "title", "some title", "title:""some title"" |br|\ title:Printer |br|\ title: ""some ti*""", "If you need to use spacings in the search phrase, use quotes. Zammad will do a AND-Search over the given words. You can also use a single keyword without quotation."
   "created_at", "2018-11-18", "created_at:2018-11-18 |br|\ created_at:[2018-11-15 TO 2018-11-18] |br|\ created_at:>now-1h", "You can either use a simple date, a date-range or >now-xh. Please note that the date format needs to be YYYY-MM-DD"
   "state.name", "new |br|\ open |br|\ closed", "state.name: new |br|\ state.name:new OR open", "You can filter for specific ticket states (and even combine them with an OR). Please note that you need to use the english namings for states, unless you have custom ticket states defined in your instance."
   "article_count", "5 |br|\ [5 TO 10] |br|\ [5 TO \*] |br|\ [\* TO 5]", "article_count:5 |br|\ article_count: [5 TO 10] |br|\ article_count:[5 TO \*] |br|\ article_count:[\* TO 5]", "You can search for Tickets with a specific number of articles (you can even search for everything with 5 or more articles or even up to 5 articles, if needed)."
   "article.from", "\*bob\*", "article.from:\*bob\*", "Show all tickets that contain articles from ""Bob"""
   "article.body", "heat |br|\ heat~ |br|\ /joh?n(ath[oa]n)/", "article.body:heat |br|\ article.body:heat~ |br|\ articlebody:/joh?n(ath[oa]n)/", "First example shows every ticket containing the word ""heat"" - you can also use the fuzzy operator ""~"" to search for similar words like e.g. like ""head"". Zammad will also allow you to use regular expressions, where ever the attributes allows it."

Combining Search Phrases
------------------------

You can combine search phrases by using ``AND``, ``OR`` and ``TO``,
depending on the situation and phrases you use. If needed, you can parts of
your search phrase for complex searches with ``()``. This allows you to
combine several phrases with different dependencies (AND/OR). In case you
receive search results that you want to exclude, you can use negation ``!``.
Below are some examples that you could use with this:

.. csv-table:: Examples for search phrase combinations
   :header: "Search phrase", "Description"
   :widths: 10, 20

   "state.name:(closed OR open) AND (priority.name:""2 normal"" OR tags:feedback)", "Show every ticket that state is either closed or open and has priority normal or the tag feedback."
   "state.name:(closed OR open) AND (priority.name:""2 normal"" OR tags:feedback) AND !(*Zammad*)", "This gets the same result as above, expect that we don't want the ticket to contain anything matching to ""Zammad"""
   "owner.email:bob@example.net AND state.name:(open OR new)", "Show Tickets from bob@example.net that are either open or new"
   "state.name:pending* AND article_count:[1 TO 5]", "Show everything with any pending state and an article count of 1 to 5."

Some Ticket Attributes and Their Type
-------------------------------------

Below you can find the most important attributes sorted by ticket and article.

Ticket Attributes
^^^^^^^^^^^^^^^^^

   * number: string
   * title: string
   * group: object (group.name, ...)
   * priority: object (priority.name, ...)
   * state: object (state.name, ...)
   * organization: object (organization.name, ...)
   * owner: object (owner.firstname, owner.lastname, owner.email, ...)
   * customer: object
     (customer.firstname, customer.lastname, customer.email, ...)
   * first_response_at: timestamp
   * first_response_in_min: integer (business min till first response)
   * close_at: timestamp
   * close_in_min: integer (business min till close)
   * last_contact_at: timestamp (last contact by customer or agent)
   * last_contact_agent_at: timestamp (last contact by agent)
   * last_contact_customer_at: timestamp (last contact by customer)
   * create_article_type.name: string (email|phone|web|...)
   * create_article_sender: string (Customer|Agent|System)
   * article_count: integer
   * escalation_at: timestamp
   * pending_time: timestamp

Article Attributes
^^^^^^^^^^^^^^^^^^

   * article.from: string
   * article.to: string
   * article.cc: string
   * article.subject: string
   * article.body: string
   * article.attachment.title: string (filename of attachment)
   * article.attachment.content: string (content of attachment)
   * article.attachment.content_type: string (File type e.g. PDF)
