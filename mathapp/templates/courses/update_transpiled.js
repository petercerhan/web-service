var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function CourseTopic(props) {
	function remove() {
		submitDeleteCourseTopicForm(props.delete_course_topic_url);
	}

	function edit() {
		window.location.href = props.edit_topic_url;
	}

	return React.createElement(
		"div",
		{ className: "ordered_option" },
		React.createElement(
			"p",
			null,
			props.course_topic.topic.display_name
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
			"Remove"
		)
	);
}

function CourseTopicInput(props) {
	var course_topics = props.course_topics.map(function (course_topic, index) {
		course_topic.position = index;
		return course_topic;
	});
	var course_topics_json = JSON.stringify(props.course_topics);
	return React.createElement("input", { type: "hidden", name: "course_topics", value: course_topics_json });
}

var CourseTopicList = function (_React$Component) {
	_inherits(CourseTopicList, _React$Component);

	function CourseTopicList(props) {
		_classCallCheck(this, CourseTopicList);

		var _this = _possibleConstructorReturn(this, (CourseTopicList.__proto__ || Object.getPrototypeOf(CourseTopicList)).call(this, props));

		var course = JSON.parse(_this.props.course_json);
		_this.state = {
			course_topics: course.course_topics,
			course_id: course.id
		};
		return _this;
	}

	_createClass(CourseTopicList, [{
		key: "moveUp",
		value: function moveUp(i) {
			var course_topics = this.state.course_topics;
			var swap_first = course_topics[i - 1];
			course_topics[i - 1] = course_topics[i];
			course_topics[i] = swap_first;
			this.setState({
				course_topics: course_topics
			});
		}
	}, {
		key: "moveDown",
		value: function moveDown(i) {
			var course_topics = this.state.course_topics;
			var swap_first = course_topics[i + 1];
			course_topics[i + 1] = course_topics[i];
			course_topics[i] = swap_first;
			this.setState({
				course_topics: course_topics
			});
		}
	}, {
		key: "render",
		value: function render() {
			var _this2 = this;

			var course_topics = this.state.course_topics.map(function (course_topic, index, arrayObj) {
				return React.createElement(CourseTopic, {
					key: course_topic.id.toString(),
					course_topic: course_topic,
					delete_course_topic_url: _this2.props.delete_course_topic_url.replace('0/delete', course_topic.id.toString() + '/delete'),
					edit_topic_url: _this2.props.edit_topic_url.replace('0/edit', course_topic.topic.id).toString(),
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
				React.createElement(CourseTopicInput, { course_topics: this.state.course_topics }),
				course_topics,
				React.createElement("hr", null)
			);
		}
	}]);

	return CourseTopicList;
}(React.Component);

var dataContainer = document.getElementById('data_container');
var rootTwo = document.getElementById('react_root_2');
var edit_topic_url_div = document.getElementById('edit_topic_url_div');
var delete_course_topic_url_div = document.getElementById('delete_course_topic_url_div');

ReactDOM.render(React.createElement(CourseTopicList, { course_json: dataContainer.getAttribute('course'),
	edit_topic_url: edit_topic_url_div.getAttribute('url'),
	delete_course_topic_url: delete_course_topic_url_div.getAttribute('url') }), rootTwo);
