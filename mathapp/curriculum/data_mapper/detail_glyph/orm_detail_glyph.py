from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from mathapp.sqlalchemy.base import Base

from mathapp.curriculum.domain_model.detail_glyph import DetailGlyph

from mathapp.sqlalchemy.domain_model_unit_of_work import DomainModelUnitOfWork

class ORMDetailGlyph(Base):
    __tablename__ = 'detail_glyph'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    position = Column(Integer)
    detail_section_id = Column(Integer, ForeignKey('detail_section.id'))

    __mapper_args__ = {
        'polymorphic_identity': 'detail_glyph',
        'polymorphic_on': type
    }

    def __init__(self, position):
        self.position = position
        self._detail_glyph = None

    @orm.reconstructor
    def init_on_load(self):
        self._detail_glyph = None

    def _set_model(self, model):
        self._detail_glyph = model

    def get_model(self, unit_of_work):
        if self._detail_glyph is not None:
            return self._detail_glyph

        domain_model_unit_of_work = DomainModelUnitOfWork(unit_of_work=unit_of_work, orm_model=self)

        detail_glyph = DetailGlyph(position=self.position, 
                                   unit_of_work=domain_model_unit_of_work)
        detail_glyph.id = self.id
        self._detail_glyph = detail_glyph
        return detail_glyph

    def sync_id(self):
        self._detail_glyph._id = self.id

    def sync_fields(self):
        self.position = self._detail_glyph._position

    def __repr__(self):
        return f'<ORMDetailGlyph(id={self.id}, type={self.type})>'