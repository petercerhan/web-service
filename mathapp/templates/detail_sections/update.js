



function DetailGlyph(props) {
	var display_name = props.detail_glyph.type;
	if(props.detail_glyph.type == 'text_glyph') {
		display_name = props.detail_glyph.text;
	} else if (props.detail_glyph.type == 'formula_glyph') {
		display_name = props.detail_glyph.formula;
	}

	return (
		<div className="ordered_option">
			<p>{ display_name }</p>
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
		</div>
	)
}

function DetailGlyphsInput(props) {
	const detail_glyphs = props.detail_glyphs.map(function (detail_glyph, index) {
		detail_glyph.position = index;
		return detail_glyph;
	});
	const detail_glyphs_json = JSON.stringify(props.detail_glyphs);
	return <input type="hidden" name="detail_glyphs" value={detail_glyphs_json} />
}

class DetailGlyphList extends React.Component {
	constructor(props) {
		super(props);
		var detail_section = JSON.parse(this.props.detail_section_json);
		this.state = {
			detail_glyphs: detail_section.detail_glyphs
		}
	}

	moveUp(i) {
		var detail_glyphs = this.state.detail_glyphs;
		const swap_first = detail_glyphs[i-1];
		detail_glyphs[i-1] = detail_glyphs[i];
		detail_glyphs[i] = swap_first;
		this.setState({
			detail_glyphs: detail_glyphs
		})
	}

	moveDown(i) {
		var detail_glyphs = this.state.detail_glyphs;
		const swap_first = detail_glyphs[i+1];
		detail_glyphs[i+1] = detail_glyphs[i];
		detail_glyphs[i] = swap_first;
		this.setState({
			detail_glyphs: detail_glyphs
		})
	}

	render() {
		const detail_glyphs = this.state.detail_glyphs.map ( (detail_glyph, index, arrayObj) =>
			<DetailGlyph
			    key={detail_glyph.id.toString()}
			 	detail_glyph={detail_glyph}
			 	first_item={index==0}
			 	last_item={index == (arrayObj.length - 1)}
				onUpClick={i => this.moveUp(index)}
				onDownClick={i => this.moveDown(index)}
			/>
		)

		return (
			<div>
				<DetailGlyphsInput detail_glyphs={this.state.detail_glyphs} />
				{ detail_glyphs }
			</div>
		)
	}
}	




	


const root = document.getElementById('react_root');
const detailSectionContainer = document.getElementById('detail_section_container');

ReactDOM.render(<DetailGlyphList detail_section_json={detailSectionContainer.getAttribute('detail_section')}/>, root)

