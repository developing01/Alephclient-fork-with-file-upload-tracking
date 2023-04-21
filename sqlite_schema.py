from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class UploadedFile(Base):
    __tablename__ = 'uploaded_file'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_identification = Column(String)
