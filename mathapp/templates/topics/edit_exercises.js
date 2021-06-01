

function Exercise(props) {
	return (
		<div className="ordered_option">
			<p>{ props.exercise.name }</p>
		</div>
	) 
}

class ExerciseList extends React.Component {
	render() {
		const exercise_elements = this.props.exercises.map( (exercise, index, arrayObj) =>
			<Exercise
				exercise={exercise}
			/>
		);

		return(exercise_elements)
	}
}

class ExerciseSectionedList extends React.Component {
	render() {
		let exercises = JSON.parse(this.props.exercises_json);
		let formula_exercises = exercises.filter(function(e) { return e.type == 'formula_exercise'} );
		let diagram_exercises = exercises.filter(function(e) { return e.type == 'diagram_exercise'} );
		return (
			<div>
				<ExerciseList exercises={formula_exercises} />
				<hr/>
				<br/>
				<ExerciseList exercises={diagram_exercises} />
				<hr/>
				<br/>
			</div>
		)
	}
}

const exerciseTableRoot = document.getElementById('react_exercise_table');
const exercisesJsonDiv = document.getElementById('exercises_json_div');

ReactDOM.render(<ExerciseSectionedList exercises_json={exercisesJsonDiv.getAttribute('exercises')} />, exerciseTableRoot)