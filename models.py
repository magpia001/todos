# models.py

from sqlalchemy import Column, Integer, Boolean, Text
from database import Base

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False)

    # __repr__ 메서드는 객체를 문자열로 표현하기 위해 사용
    # 여기서는 <Todo id> 형식의 문자열을 반환하도록 정의되
    # repr() 함수를 호출하면 <Todo 1>과 같은 문자열이 반환
    # 주로 개발 및 디버깅 목적으로 사용
    def __repr__(self):
        return '<Todo %r>' % (self.id)