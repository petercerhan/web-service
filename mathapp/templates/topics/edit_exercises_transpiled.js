var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _toConsumableArray(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } else { return Array.from(arr); } }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function Exercise(props) {
	function edit() {
		if (props.exercise.type == 'formula_exercise') {
			window.location.href = props.edit_formula_exercise_url;
		} else if (props.exercise.type == 'diagram_exercise') {
			window.location.href = props.edit_diagram_exercise_url;
		}
	}

	return React.createElement(
		'div',
		{ className: 'ordered_option' },
		React.createElement(
			'p',
			null,
			props.exercise.name
		),
		React.createElement(
			'button',
			{ type: 'button', onClick: edit },
			'Edit'
		)
	);
}

var ExerciseList = function (_React$Component) {
	_inherits(ExerciseList, _React$Component);

	function ExerciseList() {
		_classCallCheck(this, ExerciseList);

		return _possibleConstructorReturn(this, (ExerciseList.__proto__ || Object.getPrototypeOf(ExerciseList)).apply(this, arguments));
	}

	_createClass(ExerciseList, [{
		key: 'render',
		value: function render() {
			var _this2 = this;

			var exercise_elements = this.props.exercises.map(function (exercise, index, arrayObj) {
				return React.createElement(Exercise, {
					exercise: exercise,
					edit_formula_exercise_url: _this2.props.edit_formula_exercise_url.replace('/0', '/' + exercise.id.toString()),
					edit_diagram_exercise_url: _this2.props.edit_diagram_exercise_url.replace('/0', '/' + exercise.id.toString())
				});
			});

			return exercise_elements;
		}
	}]);

	return ExerciseList;
}(React.Component);

var ExerciseSectionedList = function (_React$Component2) {
	_inherits(ExerciseSectionedList, _React$Component2);

	function ExerciseSectionedList() {
		_classCallCheck(this, ExerciseSectionedList);

		return _possibleConstructorReturn(this, (ExerciseSectionedList.__proto__ || Object.getPrototypeOf(ExerciseSectionedList)).apply(this, arguments));
	}

	_createClass(ExerciseSectionedList, [{
		key: 'render',
		value: function render() {
			var _this4 = this;

			var exercises = JSON.parse(this.props.exercises_json);
			var tags = exercises.map(function (x) {
				return x.tag;
			});
			var uniqueTags = [].concat(_toConsumableArray(new Set(tags)));

			var exerciseLists = uniqueTags.map(function (tag, index, arrayObj) {
				return React.createElement(
					'div',
					null,
					React.createElement(
						'p',
						null,
						tag
					),
					React.createElement(ExerciseList, {
						exercises: exercises.filter(function (e) {
							return e.tag == tag;
						}),
						edit_formula_exercise_url: _this4.props.edit_formula_exercise_url,
						edit_diagram_exercise_url: _this4.props.edit_diagram_exercise_url
					}),
					React.createElement('br', null)
				);
			});

			return exerciseLists;
		}
	}]);

	return ExerciseSectionedList;
}(React.Component);

var exerciseTableRoot = document.getElementById('react_exercise_table');
var exercisesJsonDiv = document.getElementById('exercises_json_div');
var editFormulaURLDiv = document.getElementById('edit_formula_exercise_url_div');
var editDiagramURLDiv = document.getElementById('edit_diagram_exercise_url_div');

ReactDOM.render(React.createElement(ExerciseSectionedList, { exercises_json: exercisesJsonDiv.getAttribute('exercises'),
	edit_formula_exercise_url: editFormulaURLDiv.getAttribute('url'),
	edit_diagram_exercise_url: editDiagramURLDiv.getAttribute('url') }), exerciseTableRoot);
