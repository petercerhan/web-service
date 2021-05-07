var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function TutorialStepContent(props) {
	if (props.tutorial_step.type == 'text_tutorial_step') {
		return React.createElement(
			'p',
			null,
			props.tutorial_step.text
		);
	} else if (props.tutorial_step.type == 'formula_tutorial_step') {
		return React.createElement(
			'p',
			null,
			props.tutorial_step.formula_latex
		);
	}
}

function TutorialStep(props) {
	function edit() {
		if (props.tutorial_step.type == 'text_tutorial_step') {
			window.location.href = props.edit_text_step_url;
		} else if (props.tutorial_step.type == 'formula_tutorial_step') {
			window.location.href = props.edit_formula_step_url;
		}
	}

	return React.createElement(
		'div',
		{ className: 'ordered_option' },
		React.createElement(TutorialStepContent, { tutorial_step: props.tutorial_step }),
		React.createElement(
			'button',
			{ type: 'button', className: props.first_item ? "hidden" : "", onClick: props.onUpClick },
			'Up'
		),
		React.createElement(
			'button',
			{ type: 'button', className: props.last_item ? "hidden" : "", onClick: props.onDownClick },
			'Down'
		),
		React.createElement(
			'button',
			{ type: 'button', onClick: edit },
			'Edit'
		),
		React.createElement(
			'button',
			null,
			'(group ',
			props.tutorial_step.display_group,
			')'
		)
	);
}

function TutorialStepInput(props) {
	var tutorial_steps = props.tutorial_steps.map(function (tutorial_step, index) {
		tutorial_step.position = index;
		return tutorial_step;
	});
	var tutorial_steps_json = JSON.stringify(props.tutorial_steps);
	return React.createElement('input', { type: 'hidden', name: 'tutorial_steps', value: tutorial_steps_json });
}

var TutorialStepList = function (_React$Component) {
	_inherits(TutorialStepList, _React$Component);

	function TutorialStepList(props) {
		_classCallCheck(this, TutorialStepList);

		var _this = _possibleConstructorReturn(this, (TutorialStepList.__proto__ || Object.getPrototypeOf(TutorialStepList)).call(this, props));

		var tutorial = JSON.parse(_this.props.tutorial_json);
		_this.state = {
			tutorial_steps: tutorial.tutorial_steps,
			tutorial_id: tutorial.id
		};
		return _this;
	}

	_createClass(TutorialStepList, [{
		key: 'moveUp',
		value: function moveUp(i) {
			var tutorial_steps = this.state.tutorial_steps;
			var swap_first = tutorial_steps[i - 1];
			tutorial_steps[i - 1] = tutorial_steps[i];
			tutorial_steps[i] = swap_first;
			this.setState({
				tutorial_steps: tutorial_steps
			});
		}
	}, {
		key: 'moveDown',
		value: function moveDown(i) {
			var tutorial_steps = this.state.tutorial_steps;
			var swap_first = tutorial_steps[i + 1];
			tutorial_steps[i + 1] = tutorial_steps[i];
			tutorial_steps[i] = swap_first;
			this.setState({
				tutorial_steps: tutorial_steps
			});
		}
	}, {
		key: 'render',
		value: function render() {
			var _this2 = this;

			var tutorial_steps = this.state.tutorial_steps.map(function (tutorial_step, index, arrayObj) {
				return React.createElement(TutorialStep, {
					key: tutorial_step.id.toString(),
					tutorial_step: tutorial_step,
					edit_text_step_url: _this2.props.edit_text_step_url.replace('0/edit', '/' + tutorial_step.id.toString()),
					edit_formula_step_url: _this2.props.edit_formula_step_url.replace('0/edit', '/' + tutorial_step.id.toString()),
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
				'div',
				null,
				React.createElement(TutorialStepInput, { tutorial_steps: this.state.tutorial_steps }),
				tutorial_steps,
				React.createElement('hr', null)
			);
		}
	}]);

	return TutorialStepList;
}(React.Component);

var tutorialStepTableRoot = document.getElementById('react_tutorial_step_table');
var tutorialJsonDiv = document.getElementById('tutorial_json_div');
var editTextUrlDiv = document.getElementById('edit_text_tutorial_step_url_div');
var editFormulaUrlDiv = document.getElementById('edit_formula_tutorial_step_url_div');

ReactDOM.render(React.createElement(TutorialStepList, { tutorial_json: tutorialJsonDiv.getAttribute('tutorial'),
	edit_text_step_url: editTextUrlDiv.getAttribute('url'),
	edit_formula_step_url: editFormulaUrlDiv.getAttribute('url') }), tutorialStepTableRoot);
