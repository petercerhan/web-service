



function Exercise(props) {
	function remove() {
		submitRemoveExerciseForm(props.remove_url);
	}

	return (
		<div className="ordered_option">
			<p>{ props.exercise.name }</p>	
			<button type="button" onClick={remove}>Remove</button>		
		</div>
	) 
}

class ExerciseList extends React.Component {
	render() {
		const exercises = JSON.parse(this.props.exercises_json);

		const exercise_elements = exercises.map( (exercise, index, arrayObj) =>
			<Exercise
				exercise={exercise}
				key={index}
				remove_url={ (this.props.remove_exercise_url).replace('0/remove', exercise.id.toString() + '/remove') }
			/>
		);

		return(exercise_elements)
	}
}


const exerciseTableRoot = document.getElementById('react_exercise_table');
const exercisesJsonDiv = document.getElementById('exercises_json_div');
const removeExerciseURLDiv = document.getElementById('remove_exercise_url_div')

ReactDOM.render(<ExerciseList exercises_json={exercisesJsonDiv.getAttribute('exercises')}
							  remove_exercise_url={removeExerciseURLDiv.getAttribute('url')}/>, exerciseTableRoot)

