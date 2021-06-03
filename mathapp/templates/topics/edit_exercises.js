



function Exercise(props) {
	function edit() {
		if(props.exercise.type == 'formula_exercise') {
			window.location.href = props.edit_formula_exercise_url;
		}
	}

	return (
		<div className="ordered_option">
			<p>{ props.exercise.name }</p>			
			<button type="button" onClick={edit}>Edit</button>
		</div>
	) 
}

class ExerciseList extends React.Component {
	render() {

		const exercise_elements = this.props.exercises.map( (exercise, index, arrayObj) =>
			<Exercise
				exercise={exercise}
				edit_formula_exercise_url={ (this.props.edit_formula_exercise_url.replace('/0', '/' + exercise.id.toString() ))  }
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
					edit_formula_exercise_url={this.props.edit_formula_exercise_url}
				/>
				<br/>
			</div>
		)

		return (exerciseLists)
	}
}

const exerciseTableRoot = document.getElementById('react_exercise_table');
const exercisesJsonDiv = document.getElementById('exercises_json_div');
const editFormulaURLDiv = document.getElementById('edit_formula_exercise_url_div')

ReactDOM.render(<ExerciseSectionedList exercises_json={exercisesJsonDiv.getAttribute('exercises')} 
									   edit_formula_exercise_url={editFormulaURLDiv.getAttribute('url')}/>, exerciseTableRoot)