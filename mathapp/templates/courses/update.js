

function CourseTopic(props) {
	function remove() {
		submitDeleteCourseTopicForm(props.delete_course_topic_url);
	}

	function edit() {
		window.location.href = props.edit_topic_url;
	}

	return (
		<div className="ordered_option">
			<p>{ props.course_topic.topic.display_name }</p>
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
			<button type="button" onClick={edit}>Edit</button>
			<button type="button" onClick={remove}>Remove</button>
		</div>
	) 
}

function CourseTopicInput(props) {
	const course_topics = props.course_topics.map(function (course_topic, index) {
		course_topic.position = index;
		return course_topic;
	});
	const course_topics_json = JSON.stringify(props.course_topics);
	return <input type="hidden" name="course_topics" value={course_topics_json} />
}

class CourseTopicList extends React.Component {
	constructor(props) {
		super(props);
		var course = JSON.parse(this.props.course_json);
	    this.state = {
	      course_topics: course.course_topics,
	      course_id: course.id
	    };
	}

	moveUp(i) {
		var course_topics = this.state.course_topics;
		const swap_first = course_topics[i-1];
		course_topics[i-1] = course_topics[i];
		course_topics[i] = swap_first;
		this.setState({
			course_topics: course_topics
		})
	}

	moveDown(i) {
		var course_topics = this.state.course_topics;
		const swap_first = course_topics[i+1];
		course_topics[i+1] = course_topics[i];
		course_topics[i] = swap_first;
		this.setState({
			course_topics: course_topics
		})
	}

	render() {
		const course_topics = this.state.course_topics.map( (course_topic, index, arrayObj) => 
			<CourseTopic 
			 key={course_topic.id.toString()}
			 course_topic={course_topic}
			 delete_course_topic_url={ (this.props.delete_course_topic_url).replace('0/delete', course_topic.id.toString() + '/delete') }
			 edit_topic_url={ (this.props.edit_topic_url).replace('0/edit', course_topic.topic.id).toString() }
			 first_item={index==0} 
			 last_item={index == (arrayObj.length - 1)} 
			 onUpClick={i => this.moveUp(index)}
			 onDownClick={i => this.moveDown(index)}
			/>
		);

		return ( 
			<div>
				<CourseTopicInput course_topics={this.state.course_topics} />
				{ course_topics }
				<hr/>
			</div>
		)
	}
}



const dataContainer = document.getElementById('data_container');
const rootTwo = document.getElementById('react_root_2');
const edit_topic_url_div = document.getElementById('edit_topic_url_div');
const delete_course_topic_url_div = document.getElementById('delete_course_topic_url_div');

ReactDOM.render(<CourseTopicList course_json={dataContainer.getAttribute('course')}
								 edit_topic_url={edit_topic_url_div.getAttribute('url')}
								 delete_course_topic_url={delete_course_topic_url_div.getAttribute('url')} />, rootTwo)




