import datetime


class DateService:

	def current_datetime_utc(self):
		return datetime.datetime.utcnow()

	def format_datetime(self, datetime, format_string):
		return datetime.strftime(format_string)

	def format_datetime_as_timestamp(self, datetime):
		return datetime.strftime('%Y%m%d%H%M%S%f')
