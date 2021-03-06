var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function Lesson(props) {
	function remove() {
		submitDeleteLessonForm(props.delete_delete_url);
	}

	function edit() {
		window.location.href = props.edit_lesson_url;
	}

	return React.createElement(
		"div",
		{ className: "ordered_option" },
		React.createElement(
			"p",
			null,
			props.lesson.name
		),
		React.createElement(
			"button",
			{ type: "button", className: props.first_item ? "hidden" : "", onClick: props.onUpClick },
			"Up"
		),
		React.createElement(
			"button",
			{ type: "button", className: props.last_item ? "hidden" : "", onClick: props.onDownClick },
			"Down"
		),
		React.createElement(
			"button",
			{ type: "button", onClick: edit },
			"Edit"
		),
		React.createElement(
			"button",
			{ type: "button", onClick: remove },
			"Delete"
		)
	);
}

function LessonInput(props) {
	var lessons = props.lessons.map(function (lesson, index) {
		lesson.position = index;
		return lesson;
	});
	var lessons_json = JSON.stringify(props.lessons);
	return React.createElement("input", { type: "hidden", name: "lessons", value: lessons_json });
}

var LessonList = function (_React$Component) {
	_inherits(LessonList, _React$Component);

	function LessonList(props) {
		_classCallCheck(this, LessonList);

		var _this = _possibleConstructorReturn(this, (LessonList.__proto__ || Object.getPrototypeOf(LessonList)).call(this, props));

		var topic = JSON.parse(_this.props.topic_json);
		_this.state = {
			lessons: topic.lessons,
			topic_id: topic.id
		};
		return _this;
	}

	_createClass(LessonList, [{
		key: "moveUp",
		value: function moveUp(i) {
			var lessons = this.state.lessons;
			var swap_first = lessons[i - 1];
			lessons[i - 1] = lessons[i];
			lessons[i] = swap_first;
			this.setState({
				lessons: lessons
			});
		}
	}, {
		key: "moveDown",
		value: function moveDown(i) {
			var lessons = this.state.lessons;
			var swap_first = lessons[i + 1];
			lessons[i + 1] = lessons[i];
			lessons[i] = swap_first;
			this.setState({
				course_topics: lessons
			});
		}
	}, {
		key: "render",
		value: function render() {
			var _this2 = this;

			var lessons = this.state.lessons.map(function (lesson, index, arrayObj) {
				return React.createElement(Lesson, {
					key: lesson.id.toString(),
					lesson: lesson,
					edit_lesson_url: _this2.props.edit_lesson_url.replace('0/edit', lesson.id).toString(),
					delete_delete_url: _this2.props.delete_lesson_url.replace('0/delete', lesson.id.toString() + '/delete'),
					first_item: index == 0,
					last_item: index == arrayObj.length - 1,
					onUpClick: function onUpClick(i) {
						return _this2.moveUp(index);
					},
					onDownClick: function onDownClick(i) {
						return _this2.moveDown(index);
					}
				});
			});

			return React.createElement(
				"div",
				null,
				React.createElement(LessonInput, { lessons: this.state.lessons }),
				lessons,
				React.createElement("hr", null)
			);
		}
	}]);

	return LessonList;
}(React.Component);

var lessonTableRoot = document.getElementById('react_lesson_table');
var topicJsonDiv = document.getElementById('topic_json_div');
var editLessonURLDiv = document.getElementById('edit_lesson_url_div');
var delete_lesson_url_div = document.getElementById('delete_lesson_url_div');

ReactDOM.render(React.createElement(LessonList, { topic_json: topicJsonDiv.getAttribute('topic'),
	edit_lesson_url: editLessonURLDiv.getAttribute('url'),
	delete_lesson_url: delete_lesson_url_div.getAttribute('url') }), lessonTableRoot);
