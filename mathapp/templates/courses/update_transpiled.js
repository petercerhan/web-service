var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function LessonsTitle(props) {
	return React.createElement(
		"h1",
		null,
		"Lessons"
	);
}

function Lesson(props) {
	function handleClick() {
		submitDeleteLessonSequenceItemForm(props.delete_lesson_sequence_item_url);
	}

	return React.createElement(
		"div",
		{ className: "ordered_option" },
		React.createElement(
			"p",
			null,
			props.lesson_sequence_item.lesson.name
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
			{ type: "button", onClick: handleClick },
			"Remove"
		)
	);
}

function LessonInput(props) {
	var lesson_sequence_items = props.lesson_sequence_items.map(function (lesson_sequence_item, index) {
		lesson_sequence_item.position = index;
		return lesson_sequence_item;
	});
	var lesson_sequence_items_json = JSON.stringify(props.lesson_sequence_items);
	return React.createElement("input", { type: "hidden", name: "lesson_sequence_items", value: lesson_sequence_items_json });
}

var LessonSequenceList = function (_React$Component) {
	_inherits(LessonSequenceList, _React$Component);

	function LessonSequenceList(props) {
		_classCallCheck(this, LessonSequenceList);

		var _this = _possibleConstructorReturn(this, (LessonSequenceList.__proto__ || Object.getPrototypeOf(LessonSequenceList)).call(this, props));

		var course = JSON.parse(_this.props.course_json);
		_this.state = {
			lesson_sequence_items: course.lesson_sequence_items
		};
		return _this;
	}

	_createClass(LessonSequenceList, [{
		key: "moveUp",
		value: function moveUp(i) {
			var lesson_sequence_items = this.state.lesson_sequence_items;
			var swap_first = lesson_sequence_items[i - 1];
			lesson_sequence_items[i - 1] = lesson_sequence_items[i];
			lesson_sequence_items[i] = swap_first;
			this.setState({
				lesson_sequence_items: lesson_sequence_items
			});
		}
	}, {
		key: "moveDown",
		value: function moveDown(i) {
			var lesson_sequence_items = this.state.lesson_sequence_items;
			var swap_first = lesson_sequence_items[i + 1];
			lesson_sequence_items[i + 1] = lesson_sequence_items[i];
			lesson_sequence_items[i] = swap_first;
			this.setState({
				lesson_sequence_items: lesson_sequence_items
			});
		}
	}, {
		key: "render",
		value: function render() {
			var _this2 = this;

			var lessons = this.state.lesson_sequence_items.map(function (lesson_sequence_item, index, arrayObj) {
				return React.createElement(Lesson, {
					key: lesson_sequence_item.id.toString(),
					lesson_sequence_item: lesson_sequence_item,
					delete_lesson_sequence_item_url: _this2.props.delete_lesson_sequence_item_url.replace('0/delete', lesson_sequence_item.id.toString() + '/delete'),
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
				React.createElement(LessonInput, { lesson_sequence_items: this.state.lesson_sequence_items }),
				lessons,
				React.createElement("hr", null)
			);
		}
	}]);

	return LessonSequenceList;
}(React.Component);

var root = document.getElementById('react_root');
var dataContainer = document.getElementById('data_container');

ReactDOM.render(React.createElement(LessonSequenceList, { course_json: dataContainer.getAttribute('course'),
	delete_lesson_sequence_item_url: dataContainer.getAttribute('delete_lesson_sequence_item_url') }), root);
