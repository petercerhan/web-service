var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

function DetailGlyph(props) {
	var display_name = props.detail_glyph.type;
	if (props.detail_glyph.type == 'text_glyph') {
		display_name = props.detail_glyph.text;
	} else if (props.detail_glyph.type == 'formula_glyph') {
		display_name = props.detail_glyph.formula;
	}

	return React.createElement(
		'div',
		{ className: 'ordered_option' },
		React.createElement(
			'p',
			null,
			display_name
		),
		React.createElement(
			'button',
			{ type: 'button', className: props.first_item ? "hidden" : "", onClick: props.onUpClick },
			'Up'
		),
		React.createElement(
			'button',
			{ type: 'button', className: props.last_item ? "hidden" : "", onClick: props.onDownClick },
			'Down'
		)
	);
}

function DetailGlyphsInput(props) {
	var detail_glyphs = props.detail_glyphs.map(function (detail_glyph, index) {
		detail_glyph.position = index;
		return detail_glyph;
	});
	var detail_glyphs_json = JSON.stringify(props.detail_glyphs);
	return React.createElement('input', { type: 'hidden', name: 'detail_glyphs', value: detail_glyphs_json });
}

var DetailGlyphList = function (_React$Component) {
	_inherits(DetailGlyphList, _React$Component);

	function DetailGlyphList(props) {
		_classCallCheck(this, DetailGlyphList);

		var _this = _possibleConstructorReturn(this, (DetailGlyphList.__proto__ || Object.getPrototypeOf(DetailGlyphList)).call(this, props));

		var detail_section = JSON.parse(_this.props.detail_section_json);
		_this.state = {
			detail_glyphs: detail_section.detail_glyphs
		};
		return _this;
	}

	_createClass(DetailGlyphList, [{
		key: 'moveUp',
		value: function moveUp(i) {
			var detail_glyphs = this.state.detail_glyphs;
			var swap_first = detail_glyphs[i - 1];
			detail_glyphs[i - 1] = detail_glyphs[i];
			detail_glyphs[i] = swap_first;
			this.setState({
				detail_glyphs: detail_glyphs
			});
		}
	}, {
		key: 'moveDown',
		value: function moveDown(i) {
			var detail_glyphs = this.state.detail_glyphs;
			var swap_first = detail_glyphs[i + 1];
			detail_glyphs[i + 1] = detail_glyphs[i];
			detail_glyphs[i] = swap_first;
			this.setState({
				detail_glyphs: detail_glyphs
			});
		}
	}, {
		key: 'render',
		value: function render() {
			var _this2 = this;

			var detail_glyphs = this.state.detail_glyphs.map(function (detail_glyph, index, arrayObj) {
				return React.createElement(DetailGlyph, {
					key: detail_glyph.id.toString(),
					detail_glyph: detail_glyph,
					first_item: index == 0,
					last_item: index == arrayObj.length - 1,
					onUpClick: function onUpClick(i) {
						return _this2.moveUp(index);
					},
					onDownClick: function onDownClick(i) {
						return _this2.moveDown(index);
					}
				});
			});

			return React.createElement(
				'div',
				null,
				React.createElement(DetailGlyphsInput, { detail_glyphs: this.state.detail_glyphs }),
				detail_glyphs
			);
		}
	}]);

	return DetailGlyphList;
}(React.Component);

var root = document.getElementById('react_root');
var detailSectionContainer = document.getElementById('detail_section_container');

ReactDOM.render(React.createElement(DetailGlyphList, { detail_section_json: detailSectionContainer.getAttribute('detail_section') }), root);