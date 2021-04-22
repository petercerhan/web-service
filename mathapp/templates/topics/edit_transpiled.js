var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function Lesson(props) {
	return React.createElement(
		"div",
		{ className: "ordered_option" },
		React.createElement(
			"p",
			null,
			props.lesson.name
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
		key: "render",
		value: function render() {
			var lessons = this.state.lessons.map(function (lesson, index, arrayObj) {
				return React.createElement(Lesson, {
					key: lesson.id.toString(),
					lesson: lesson,
					first_item: index == 0,
					last_item: index == arrayObj.length - 1
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

ReactDOM.render(React.createElement(LessonList, { topic_json: topicJsonDiv.getAttribute('topic') }), lessonTableRoot);
