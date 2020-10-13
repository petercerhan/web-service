var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function InstructionSection(props) {
	return React.createElement(
		"div",
		{ className: "ordered_option" },
		React.createElement(
			"p",
			null,
			props.instruction_section.display_name
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
		)
	);
}

function InstructionSectionsInput(props) {
	var instruction_sections = props.instruction_sections.map(function (instruction_section, index) {
		instruction_section.position = index;
		return instruction_section;
	});
	var instruction_sections_json = JSON.stringify(props.instruction_sections);
	return React.createElement("input", { type: "hidden", name: "instruction_sections", value: instruction_sections_json });
}

var InstructionSectionList = function (_React$Component) {
	_inherits(InstructionSectionList, _React$Component);

	function InstructionSectionList(props) {
		_classCallCheck(this, InstructionSectionList);

		var _this = _possibleConstructorReturn(this, (InstructionSectionList.__proto__ || Object.getPrototypeOf(InstructionSectionList)).call(this, props));

		var lesson_intro = JSON.parse(_this.props.lesson_intro_json);
		_this.state = {
			instruction_sections: lesson_intro.instruction_sections
		};
		return _this;
	}

	_createClass(InstructionSectionList, [{
		key: "moveUp",
		value: function moveUp(i) {
			var instruction_sections = this.state.instruction_sections;
			var swap_first = instruction_sections[i - 1];
			instruction_sections[i - 1] = instruction_sections[i];
			instruction_sections[i] = swap_first;
			this.setState({
				instruction_sections: instruction_sections
			});
		}
	}, {
		key: "moveDown",
		value: function moveDown(i) {
			var instruction_sections = this.state.instruction_sections;
			var swap_first = instruction_sections[i + 1];
			instruction_sections[i + 1] = instruction_sections[i];
			instruction_sections[i] = swap_first;
			this.setState({
				instruction_sections: instruction_sections
			});
		}
	}, {
		key: "render",
		value: function render() {
			var _this2 = this;

			var instruction_sections = this.state.instruction_sections.map(function (instruction_section, index, arrayObj) {
				return React.createElement(InstructionSection, {
					key: instruction_section.id.toString(),
					instruction_section: instruction_section,
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
				React.createElement(InstructionSectionsInput, { instruction_sections: this.state.instruction_sections }),
				instruction_sections
			);
		}
	}]);

	return InstructionSectionList;
}(React.Component);

var root = document.getElementById('react_root');
var dataContainer = document.getElementById('data_container');

ReactDOM.render(React.createElement(InstructionSectionList, { lesson_intro_json: dataContainer.getAttribute('lesson_intro') }), root);
