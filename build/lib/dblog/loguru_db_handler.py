from .models import ErrorLog


class LoguruDbHandler(object):
	"""
	handler to save logs into db
	"""
	def __init__(self, endpoint: str):
		self.url = endpoint
	
	def write(self, message):
		"""
		save loguru message into db
		"""
		new_error = ErrorLog()
		new_error.url = self.url
		new_error.exception_name = message.record.get('level').name
		new_error.exception = message.record.get('message')
		new_error.referer = ''
		new_error.traceback = ''
		new_error.save()
