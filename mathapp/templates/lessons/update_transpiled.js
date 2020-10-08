var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function LessonSection(props) {
	function remove() {
		submitDeleteLessonSectionForm(props.delete_lesson_section_url);
	}

	return React.createElement(
		"div",
		{ className: "ordered_option" },
		React.createElement(
			"p",
			null,
			props.lesson_section.display_name
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
			{ type: "button", onClick: remove },
			"Remove"
		)
	);
}

function LessonSectionsInput(props) {
	var lesson_sections = props.lesson_sections.map(function (lesson_section, index) {
		lesson_section.position = index;
		return lesson_section;
	});
	var lesson_sections_json = JSON.stringify(props.lesson_sections);
	return React.createElement("input", { type: "hidden", name: "lesson_sections", value: lesson_sections_json });
}

var LessonSectionList = function (_React$Component) {
	_inherits(LessonSectionList, _React$Component);

	function LessonSectionList(props) {
		_classCallCheck(this, LessonSectionList);

		var _this = _possibleConstructorReturn(this, (LessonSectionList.__proto__ || Object.getPrototypeOf(LessonSectionList)).call(this, props));

		var lesson = JSON.parse(_this.props.lesson_json);
		_this.state = {
			lesson_sections: lesson.lesson_sections,
			lesson_id: lesson.id
		};
		return _this;
	}

	_createClass(LessonSectionList, [{
		key: "moveUp",
		value: function moveUp(i) {
			var lesson_sections = this.state.lesson_sections;
			var swap_first = lesson_sections[i - 1];
			lesson_sections[i - 1] = lesson_sections[i];
			lesson_sections[i] = swap_first;
			this.setState({
				lesson_sections: lesson_sections
			});
		}
	}, {
		key: "moveDown",
		value: function moveDown(i) {
			var lesson_sections = this.state.lesson_sections;
			var swap_first = lesson_sections[i + 1];
			lesson_sections[i + 1] = lesson_sections[i];
			lesson_sections[i] = swap_first;
			this.setState({
				lesson_sections: lesson_sections
			});
		}
	}, {
		key: "render",
		value: function render() {
			var _this2 = this;

			var lesson_sections = this.state.lesson_sections.map(function (lesson_section, index, arrayObj) {
				return React.createElement(LessonSection, {
					key: lesson_section.id.toString(),
					lesson_section: lesson_section,
					delete_lesson_section_url: _this2.props.delete_lesson_section_url.replace('0/delete', lesson_section.id.toString() + '/delete'),
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
				React.createElement(LessonSectionsInput, { lesson_sections: this.state.lesson_sections }),
				lesson_sections
			);
		}
	}]);

	return LessonSectionList;
}(React.Component);

var root = document.getElementById('react_root');
var dataContainer = document.getElementById('data_container');

ReactDOM.render(React.createElement(LessonSectionList, { lesson_json: dataContainer.getAttribute('lesson'),
	delete_lesson_section_url: dataContainer.getAttribute('delete_lesson_section_url') }), root);
