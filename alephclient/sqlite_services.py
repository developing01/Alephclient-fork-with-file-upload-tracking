from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alephclient.sqlite_schema import Base, UploadedFile


class SqliteConnection:
    database_name = 'aleph_client.db'

    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.engine = self.create_tables()
        super().__init__(*args, **kwargs)

    def create_tables(self):
        engine = create_engine(f'sqlite:///{self.path}/{self.database_name}', echo=False)
        Base.metadata.create_all(engine)
        return engine

    def add_uploaded_file(self, file_identification):
        session = sessionmaker(bind=self.engine)()
        session.add(UploadedFile(file_identification=file_identification))
        session.commit()

    def check_file_exist(self, file_identification):
        session = sessionmaker(bind=self.engine)()
        exists_file = session.query(UploadedFile).filter(
            UploadedFile.file_identification==file_identification
        ).all()
        session.close()
        return True if exists_file else False
