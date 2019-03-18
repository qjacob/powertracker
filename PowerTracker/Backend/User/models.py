from django.db import models
from django.contrib.auth.models import User

class PowerUser(User):
	"""
	Models that define a regular user of PowerTracker
	"""
	weight = models.IntegerField(default=0)
	max_squat = models.IntegerField(default=0)
	max_bench = models.IntegerField(default=0)
	max_deadlift = models.IntegerField(default=0)

	def __str__(self):
		return self.email

	def __repr__(self):
		return (
			"<{class_name}("
			"id={self.id}, "
			"username={self.username}, "
			"email={self.email}, "
			"first_name={self.first_name}, "
			"last_name={self.last_name}, "
			"weight={self.weight}, "
			"max_squat={self.max_squat}, "
			"max_bench={self.max_bench}, "
			"max_deadlift={self.max_deadlift})>".format(
				class_name=self.__class__.__name__,
				self=self
			)
		)