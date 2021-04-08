from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '20210101 00:00:00'
c.events.add(e)
c.events
# {<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>}kshop Git' started 2 years ago"