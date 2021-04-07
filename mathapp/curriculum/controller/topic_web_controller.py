from flask import (
    request, flash, redirect, url_for, render_template, abort
)

import json

class TopicWebController:

	def __init__(self,
				request,
				topic_interactor,
				topic_presenter):
		self._request = request
		self._topic_interactor = topic_interactor
		self._topic_presenter = topic_presenter

	def get_index(self):
		topics = self._topic_interactor.list()
		# return json.dumps(topics)
		return self._topic_presenter.index(topics)