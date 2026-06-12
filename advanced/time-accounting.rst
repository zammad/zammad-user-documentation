Time Accounting
===============

Zammad supports detailed time accounting to help administrators keep track of
how much time you spend on any given ticket, customer or client organization.
If the time accounting is enabled, a dialog appears each time you update
a ticket. There you can enter how much time you spent on it.

This feature is optional. If you don't see it whenever you update a
ticket, either your administrator hasn't enabled it yet or the tickets aren't
considered as relevant for time accounting.
Administrators can find additional information in the
:admin-docs:`time accounting section of the admin documentation </manage/time-accounting.html>`.

Units
-----

The Accounted time is always recorded as unitless numbers. However, your
administrator may decide to show an optional label next to the field to hint
you and your colleagues which unit is assumed.

.. figure:: /images/advanced/time-accounting/time-accounting-unit-recording.png
   :alt: Time Accounting Unit
   :align: center

Activity Types
--------------

**Activity Types** are used for grouping accounted time entries together.
This is an optional feature which shows a list of activities as a
selectable list.

.. figure:: /images/advanced/time-accounting/time-accounting-select-activity-type.png
   :alt: Time Accounting Activity Type
   :align: center

Simply choose the closest type of the activity you are recording the time
for, noting that one of the choices may be pre-selected. You can always
remove the selection for general accounted time that is not supposed to be
grouped together.

Accounted Time in Ticket
------------------------

If a ticket already has accounted time(s), you can see it in the ticket sidebar
at the bottom. You can find the calculated sums of each activity type as well
as the total sum of accounted times for all activity types.

.. figure:: /images/advanced/time-accounting/ticket-pane-accounted-time.png
   :alt: Screenshot showing accounted times in ticket sidebar
   :align: center

   Accounted times in the ticket view