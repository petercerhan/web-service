



function Exercise(props) {
	return (
		<div className="ordered_option">
			<p>{ props.exercise.name }</p>			
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
			/>
		);

		return(exercise_elements)
	}
}


const exerciseTableRoot = document.getElementById('react_exercise_table');
const exercisesJsonDiv = document.getElementById('exercises_json_div');

ReactDOM.render(<ExerciseList exercises_json={exercisesJsonDiv.getAttribute('exercises')}/>, exerciseTableRoot)

