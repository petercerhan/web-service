

function DetailGlyphContent(props) {
	if(props.detail_glyph.type == 'text_glyph') {
		return (<p>{ props.detail_glyph.text }</p>)
	} else if (props.detail_glyph.type == 'formula_glyph') {
		return (<p>{ props.detail_glyph.formula }</p>)
	} else if (props.detail_glyph.type == 'image_glyph') {
		return (<img src={"data:image/png;base64," + props.detail_glyph.image_data} height="200" width="200"/>)
	} else {
		return (<p>Unknown Glyph Type</p>)
	}
}

function DetailGlyph(props) {
	var display_name = props.detail_glyph.type;
	if(props.detail_glyph.type == 'text_glyph') {
		display_name = props.detail_glyph.text;
	} else if (props.detail_glyph.type == 'formula_glyph') {
		display_name = props.detail_glyph.formula;
	} else if (props.detail_glyph.type == 'image_glyph') {
		display_name = props.detail_glyph.source_code_filename
	}

	function edit() {
		if(props.detail_glyph.type == 'text_glyph') {
			window.location.href = props.update_text_glyph_url;
		} else if(props.detail_glyph.type == 'formula_glyph') {
			window.location.href = props.update_formula_glyph_url;
		} else if(props.detail_glyph.type == 'image_glyph') {
			window.location.href = props.update_image_glyph_url;
		}
	}

	return (
		<div className="ordered_option">
			<DetailGlyphContent detail_glyph={props.detail_glyph} />
			<button type="button" className={props.first_item ? "hidden" : ""} onClick={props.onUpClick}>Up</button>
			<button type="button" className={props.last_item ? "hidden" : ""} onClick={props.onDownClick}>Down</button>
			<button type="button" onClick={edit}>Edit</button>
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
			 	update_text_glyph_url={ (this.props.update_text_glyph_url.replace('text_glyphs/0', 'text_glyphs/' + detail_glyph.id.toString() ) ) }
			 	update_formula_glyph_url={ (this.props.update_formula_glyph_url.replace('formula_glyphs/0', 'formula_glyphs/' + detail_glyph.id.toString() ) ) }
			 	update_image_glyph_url={ (this.props.update_image_glyph_url.replace('image_glyphs/0', 'image_glyphs/' + detail_glyph.id.toString() ) ) }
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
const updateTextGlyphURLContainer = document.getElementById('update_text_glyph_url');
const updateFormulaGlyphURLContainer = document.getElementById('update_formula_glyph_url');
const updateImageGlyphURLContainer = document.getElementById('update_image_glyph_url');

ReactDOM.render(<DetailGlyphList detail_section_json={detailSectionContainer.getAttribute('detail_section')} 
								 update_text_glyph_url={updateTextGlyphURLContainer.getAttribute('url')} 
								 update_formula_glyph_url={updateFormulaGlyphURLContainer.getAttribute('url')} 
								 update_image_glyph_url={updateImageGlyphURLContainer.getAttribute('url')}/>, root)






