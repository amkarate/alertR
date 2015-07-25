#!/usr/bin/python2

# written by sqall
# twitter: https://twitter.com/sqall01
# blog: http://blog.h4des.org
# github: https://github.com/sqall01
#
# Licensed under the GNU Public License, version 2.


class Event:

	def __init__(self, timeOccurred):
		self.timeOccurred = timeOccurred


class EventSensorAlert(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.description = None
		self.state = None
		self.alertLevels = list()


class EventStateChange(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.hostname = None
		self.description = None
		self.state = None


class EventConnectedChange(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.hostname = None
		self.nodeType = None
		self.instance = None
		self.connected = None


class EventNewVersion(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.usedVersion = None
		self.usedRev = None
		self.newVersion = None
		self.newRev = None
		self.instance = None
		self.hostname = None


class EventNewOption(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.type = None
		self.value = None


class EventNewNode(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.hostname = None
		self.nodeType = None
		self.instance = None


class EventNewSensor(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.hostname = None
		self.description = None
		self.state = None


class EventNewAlert(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.hostname = None
		self.description = None


class EventNewManager(Event):

	def __init__(self, timeOccurred):
		Event.__init__(self, timeOccurred)
		self.hostname = None
		self.description = None





# TODO
# perhaps add event for changes for sensors, nodes etc in storage backend
# (it already has a copy of existing elements)
# BETTER: do it in the client.py => outsource sensor value update to other file to have client.py still compatible with other manager clients







# TODO
# events needed: new option, new node, new sensor, new alert, new manager, deleted option, deleted node, deleted node, deleted sensor, deleted alert, deleted manager
# perhaps: option change, node change, sensor change, alert change, manager change
#USEFUL EVENT: node goes offline, sensor timed out


'''
 option 				DONE
new node 				DONE
new sensor 				DONE
new alert 				DONE
new manager 			DONE
deleted option
deleted node
deleted sensor
deleted alert
deleted manager
option change
node change
sensor change
alert change
manager change
node goes offline
sensor timed out
'''