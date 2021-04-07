from flask import (
    flash, redirect, url_for, render_template, abort
)

import json

class TopicPresenter:

	def index(self, topics):
		return render_template('topics/index.html', topics = topics)