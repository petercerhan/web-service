

function TutorialStep(props) {
	
	return (
		<div className="ordered_option">
			<p>{ props.tutorial_step.type }</p>
		</div>
	) 
}

function TutorialStepInput(props) {
	const tutorial_steps = props.tutorial_steps.map(function (tutorial_step, index) {
		tutorial_step.position = index;
		return tutorial_step;
	});
	const tutorial_steps_json = JSON.stringify(props.tutorial_steps);
	return <input type="hidden" name="tutorial_steps" value={tutorial_steps_json} />
}

class TutorialStepList extends React.Component {
	constructor(props) {
		super(props);
		var tutorial = JSON.parse(this.props.tutorial_json);
		this.state = {
			tutorial_steps: tutorial.tutorial_steps,
			tutorial_id: tutorial.id
		};
	}

	render() {
		const tutorial_steps = this.state.tutorial_steps.map( (tutorial_step, index, arrayObj) => 
			<TutorialStep 
			 key={tutorial_step.id.toString()}
			 tutorial_step={tutorial_step}
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)}
			/>
		);

		return ( 
			<div>
				<TutorialStepInput tutorial_steps={this.state.tutorial_steps} />
				{ tutorial_steps }
				<hr/>
			</div>
		)
	}
}






const tutorialStepTableRoot = document.getElementById('react_tutorial_step_table');
const tutorialJsonDiv = document.getElementById('tutorial_json_div');

ReactDOM.render(<TutorialStepList tutorial_json={tutorialJsonDiv.getAttribute('tutorial')} />, tutorialStepTableRoot)





