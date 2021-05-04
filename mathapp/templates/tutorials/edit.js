

function TutorialStepContent(props) {
	if(props.tutorial_step.type == 'text_tutorial_step') {
		return (<p>{ props.tutorial_step.text }</p>)
	} else if (props.tutorial_step.type == 'formula_tutorial_step') {
		return (<p>{ props.tutorial_step.formula_latex }</p>)
	}
}

function TutorialStep(props) {	
	return (
		<div className="ordered_option">
			<TutorialStepContent tutorial_step={props.tutorial_step} />
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
			<button>(group {props.tutorial_step.display_group})</button>
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

	moveUp(i) {
		var tutorial_steps = this.state.tutorial_steps;
		const swap_first = tutorial_steps[i-1];
		tutorial_steps[i-1] = tutorial_steps[i];
		tutorial_steps[i] = swap_first;
		this.setState({
			tutorial_steps: tutorial_steps
		})
	}

	moveDown(i) {
		var tutorial_steps = this.state.tutorial_steps;
		const swap_first = tutorial_steps[i+1];
		tutorial_steps[i+1] = tutorial_steps[i];
		tutorial_steps[i] = swap_first;
		this.setState({
			tutorial_steps: tutorial_steps
		})
	}

	render() {
		const tutorial_steps = this.state.tutorial_steps.map( (tutorial_step, index, arrayObj) => 
			<TutorialStep 
			 key={tutorial_step.id.toString()}
			 tutorial_step={tutorial_step}
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)} 
			 onUpClick={i => this.moveUp(index)}
			 onDownClick={i => this.moveDown(index)}
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






