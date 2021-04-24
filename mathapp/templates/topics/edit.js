

function Lesson(props) {
	function remove() {
		submitDeleteLessonForm(props.delete_delete_url);
	}

	function edit() {
		window.location.href = props.edit_lesson_url;
	}
	
	return (
		<div className="ordered_option">
			<p>{ props.lesson.name }</p>
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
			<button type="button" onClick={edit}>Edit</button>
			<button type="button" onClick={remove}>Delete</button>
		</div>
	) 
}

function LessonInput(props) {
	const lessons = props.lessons.map(function (lesson, index) {
		lesson.position = index;
		return lesson;
	});
	const lessons_json = JSON.stringify(props.lessons);
	return <input type="hidden" name="lessons" value={lessons_json} />
}

class LessonList extends React.Component {
	constructor(props) {
		super(props);
		var topic = JSON.parse(this.props.topic_json);
		this.state = {
			lessons: topic.lessons,
			topic_id: topic.id
		};
	}

	moveUp(i) {
		var lessons = this.state.lessons;
		const swap_first = lessons[i-1];
		lessons[i-1] = lessons[i];
		lessons[i] = swap_first;
		this.setState({
			lessons: lessons
		})
	}

	moveDown(i) {
		var lessons = this.state.lessons;
		const swap_first = lessons[i+1];
		lessons[i+1] = lessons[i];
		lessons[i] = swap_first;
		this.setState({
			course_topics: lessons
		})
	}

	render() {
		const lessons = this.state.lessons.map( (lesson, index, arrayObj) => 
			<Lesson 
			 key={lesson.id.toString()}
			 lesson={lesson}
			 edit_lesson_url={ (this.props.edit_lesson_url).replace('0/edit', lesson.id).toString() }
			 delete_delete_url={ (this.props.delete_lesson_url).replace('0/delete', lesson.id.toString() + '/delete') }
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)}
			 onUpClick={i => this.moveUp(index)}
			 onDownClick={i => this.moveDown(index)}
			/>
		);

		return ( 
			<div>
				<LessonInput lessons={this.state.lessons} />
				{ lessons }
				<hr/>
			</div>
		)
	}
}

const lessonTableRoot = document.getElementById('react_lesson_table');
const topicJsonDiv = document.getElementById('topic_json_div');
const editLessonURLDiv = document.getElementById('edit_lesson_url_div')
const delete_lesson_url_div = document.getElementById('delete_lesson_url_div');

ReactDOM.render(<LessonList topic_json={topicJsonDiv.getAttribute('topic')} 
							edit_lesson_url={editLessonURLDiv.getAttribute('url')}
							delete_lesson_url={delete_lesson_url_div.getAttribute('url')} />, lessonTableRoot)




