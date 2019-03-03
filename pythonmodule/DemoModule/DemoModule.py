""" This module serves as an example as to how you can use sphinx to document a python module.

"""

from .DemoModuleError import DemoModuleError

class DemoModule(object):
	def __init__(self):
		""" This is the init function, no  arguments are needed. """
		pass


	def saySomethin(self, something=None):
		""" This is a function that says something.
			
			Args:
				something (str) : This is the thing you want to say.

			Returns:
				string (str) : This is what you said!
		"""
		if something is None:
			raise DemoModuleError("You cannot say none!")

		return f"I'm just sayin: {something}"