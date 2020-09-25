



function LessonSection(props) {
	return (
		<div className="ordered_option">
			<p>{ props.lesson_section.id }</p>
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>

		</div>
	) 
}

class LessonSectionList extends React.Component {
	constructor(props) {
		super(props);
		var lesson = JSON.parse(this.props.lesson_json);
		this.state = {
			lesson_sections: lesson.lesson_sections,
			lesson_id: lesson.id
		}
	}

	moveUp(i) {
		var lesson_sections = this.state.lesson_sections;
		const swap_first = lesson_sections[i-1];
		lesson_sections[i-1] = lesson_sections[i];
		lesson_sections[i] = swap_first;
		this.setState({
			lesson_sections: lesson_sections
		})
	}

	moveDown(i) {
		var lesson_sections = this.state.lesson_sections;
		const swap_first = lesson_sections[i+1];
		lesson_sections[i+1] = lesson_sections[i];
		lesson_sections[i] = swap_first;
		this.setState({
			lesson_sections: lesson_sections
		})
	}

	render() {
		const lesson_sections = this.state.lesson_sections.map( (lesson_section, index, arrayObj) => 
			<LessonSection
			 key={lesson_section.id.toString()}
			 lesson_section={lesson_section}
			 first_item={index==0}
			 last_item={index == (arrayObj.length - 1)}
			 onUpClick={i => this.moveUp(index)}
			 onDownClick={i => this.moveDown(index)}
			/>
		);

		return ( 
			<div>
				<h1>Lesson Sections</h1>
				{ lesson_sections }
			</div>
		)
	}
}

const root = document.getElementById('react_root');
const dataContainer = document.getElementById('data_container');


ReactDOM.render(<LessonSectionList lesson_json={dataContainer.getAttribute('lesson')}/>, root)