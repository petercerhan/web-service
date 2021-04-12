



function InstructionSection(props) {
	return (
		<div className="ordered_option">
			<p>{props.instruction_section.display_name}</p>
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
		</div>
	)
}


function InstructionSectionsInput(props) {
	const instruction_sections = props.instruction_sections.map(function (instruction_section, index) {
		instruction_section.position = index;
		return instruction_section;
	});
	const instruction_sections_json = JSON.stringify(props.instruction_sections);
	return <input type="hidden" name="instruction_sections" value={instruction_sections_json} />
}

class InstructionSectionList extends React.Component {
	constructor(props) {
		super(props);
		var concept_tutorial = JSON.parse(this.props.concept_tutorial_json);
		this.state = {
			instruction_sections: concept_tutorial.instruction_sections
		}
	}

	moveUp(i) {
		var instruction_sections = this.state.instruction_sections;
		const swap_first = instruction_sections[i-1];
		instruction_sections[i-1] = instruction_sections[i];
		instruction_sections[i] = swap_first;
		this.setState({
			instruction_sections: instruction_sections
		})
	}

	moveDown(i) {
		var instruction_sections = this.state.instruction_sections;
		const swap_first = instruction_sections[i+1];
		instruction_sections[i+1] = instruction_sections[i];
		instruction_sections[i] = swap_first;
		this.setState({
			instruction_sections: instruction_sections
		})
	}

	render() {
		const instruction_sections = this.state.instruction_sections.map( (instruction_section, index, arrayObj) =>
			<InstructionSection
			    key={instruction_section.id.toString()}
			 	instruction_section={instruction_section}
			 	first_item={index==0}
			 	last_item={index == (arrayObj.length - 1)}
				onUpClick={i => this.moveUp(index)}
				onDownClick={i => this.moveDown(index)}
		 	/>
		);

		return (
			<div>
				<InstructionSectionsInput instruction_sections={this.state.instruction_sections} />
				{ instruction_sections }
			</div>
		)
	}
}





const root = document.getElementById('react_root');
const dataContainer = document.getElementById('concept_tutorial_json');

ReactDOM.render(<InstructionSectionList concept_tutorial_json={dataContainer.getAttribute('concept_tutorial_json')} />, root)







