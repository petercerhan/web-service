

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
		const exercises = JSON.parse(this.props.exercises_json);
		const tags = exercises.map(x => x.tag);
		const uniqueTags = [...new Set(tags)];

		const exerciseLists = uniqueTags.map( (tag, index, arrayObj) =>
			<div>
				<p>{tag}</p>
				<ExerciseList
					exercises={exercises.filter(function(e) { return e.tag == tag })}
				/>
				<br/>
			</div>
		)

		return (exerciseLists)
	}
}

const exerciseTableRoot = document.getElementById('react_exercise_table');
const exercisesJsonDiv = document.getElementById('exercises_json_div');

ReactDOM.render(<ExerciseSectionedList exercises_json={exercisesJsonDiv.getAttribute('exercises')} />, exerciseTableRoot)