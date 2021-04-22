

function Lesson(props) {
	return (
		<div className="ordered_option">
			<p>{ props.lesson.name }</p>
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

	render() {
		const lessons = this.state.lessons.map( (lesson, index, arrayObj) => 
			<Lesson 
			 key={lesson.id.toString()}
			 lesson={lesson}
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)}
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

ReactDOM.render(<LessonList topic_json={topicJsonDiv.getAttribute('topic')} />, lessonTableRoot)