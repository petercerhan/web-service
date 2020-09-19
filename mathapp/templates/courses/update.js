

function LessonsTitle(props) {
	return <h1>Lessons</h1>
}

function Lesson(props) {
	function remove() {
		submitDeleteLessonSequenceItemForm(props.delete_lesson_sequence_item_url);
	}

	function edit() {
		window.location.href = props.update_lesson_url;
	}

	return (
		<div className="ordered_option">
			<p>{ props.lesson_sequence_item.lesson.name }</p>
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
			<button type="button" onClick={edit}>Edit</button>
			<button type="button" onClick={remove}>Remove</button>
		</div>
	) 
}

function LessonInput(props) {
	const lesson_sequence_items = props.lesson_sequence_items.map(function (lesson_sequence_item, index) {
		lesson_sequence_item.position = index;
		return lesson_sequence_item;
	});
	const lesson_sequence_items_json = JSON.stringify(props.lesson_sequence_items);
	return <input type="hidden" name="lesson_sequence_items" value={lesson_sequence_items_json} />
}

class LessonSequenceList extends React.Component {
	constructor(props) {
		super(props);
		var course = JSON.parse(this.props.course_json);
	    this.state = {
	      lesson_sequence_items: course.lesson_sequence_items,
	      course_id: course.id
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
			 delete_lesson_sequence_item_url={ (this.props.delete_lesson_sequence_item_url).replace('0/delete', lesson_sequence_item.id.toString() + '/delete') }
			 update_lesson_url={ (this.props.update_lesson_url).replace('0/update', lesson_sequence_item.lesson.id).toString() + '?return_to_course_id=' + this.state.course_id }
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)} 
			 onUpClick={i => this.moveUp(index)}
			 onDownClick={i => this.moveDown(index)}
			/>
		);

		return ( 
			<div>
				<LessonInput lesson_sequence_items={this.state.lesson_sequence_items} />
				{ lessons }
				<hr/>
			</div>
		)
	}
}

const root = document.getElementById('react_root');
const dataContainer = document.getElementById('data_container');

ReactDOM.render(<LessonSequenceList course_json={dataContainer.getAttribute('course')} 
									delete_lesson_sequence_item_url={dataContainer.getAttribute('delete_lesson_sequence_item_url')} 
									update_lesson_url={dataContainer.getAttribute('update_lesson_url')}/>, root)



