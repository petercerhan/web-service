import datetime


class DateService:

	def current_datetime_utc(self):
		return datetime.datetime.utcnow()