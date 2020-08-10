

function LessonsTitle(props) {
	return <h1>Lessons</h1>
}

function Lesson(props) {
	return (
		<div className="ordered_option">
			<p>{ props.lesson_sequence_item.lesson.name } and { props.last_item.toString() }</p>
			<button className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
		</div>
	) 
}


class LessonSequenceList extends React.Component {
	constructor(props) {
		super(props);
		var course = JSON.parse(this.props.course_json);
	    this.state = {
	      lesson_sequence_items: course.lesson_sequence_items
	    };
	}

	moveUp(i) {
		var lesson_sequence_items = this.state.lesson_sequence_items;
		const swap_first = lesson_sequence_items[i-1];
		lesson_sequence_items[i-1] = lesson_sequence_items[i];
		lesson_sequence_items[i] = swap_first;
		this.setState({
			lesson_sequence_items: lesson_sequence_items
		})
	}

	moveDown(i) {
		var lesson_sequence_items = this.state.lesson_sequence_items;
		const swap_first = lesson_sequence_items[i+1];
		lesson_sequence_items[i+1] = lesson_sequence_items[i];
		lesson_sequence_items[i] = swap_first;
		this.setState({
			lesson_sequence_items: lesson_sequence_items
		})
	}

	render() {
		const lessons = this.state.lesson_sequence_items.map( (lesson_sequence_item, index, arrayObj) => 
			<Lesson 
			 key={lesson_sequence_item.id.toString()}
			 lesson_sequence_item={lesson_sequence_item} 
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)} 
			 onUpClick={i => this.moveUp(index)}
			 onDownClick={i => this.moveDown(index)}
			/>
		);

		return ( 
			<div>
				<LessonsTitle />
				<hr/>
				{ lessons }
				<hr/>
			</div>
		)
	}
}

const root = document.getElementById('react_root');
const dataContainer = document.getElementById('data_container');

ReactDOM.render(<LessonSequenceList course_json={dataContainer.getAttribute('course')}/>, root)
