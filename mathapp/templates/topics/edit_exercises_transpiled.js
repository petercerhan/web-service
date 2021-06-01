var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function Exercise(props) {
	return React.createElement(
		'div',
		{ className: 'ordered_option' },
		React.createElement(
			'p',
			null,
			props.exercise.name
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
			var exercise_elements = this.props.exercises.map(function (exercise, index, arrayObj) {
				return React.createElement(Exercise, {
					exercise: exercise
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
			var exercises = JSON.parse(this.props.exercises_json);
			var formula_exercises = exercises.filter(function (e) {
				return e.type == 'formula_exercise';
			});
			var diagram_exercises = exercises.filter(function (e) {
				return e.type == 'diagram_exercise';
			});
			return React.createElement(
				'div',
				null,
				React.createElement(ExerciseList, { exercises: formula_exercises }),
				React.createElement('hr', null),
				React.createElement('br', null),
				React.createElement(ExerciseList, { exercises: diagram_exercises }),
				React.createElement('hr', null),
				React.createElement('br', null)
			);
		}
	}]);

	return ExerciseSectionedList;
}(React.Component);

var exerciseTableRoot = document.getElementById('react_exercise_table');
var exercisesJsonDiv = document.getElementById('exercises_json_div');

ReactDOM.render(React.createElement(ExerciseSectionedList, { exercises_json: exercisesJsonDiv.getAttribute('exercises') }), exerciseTableRoot);
