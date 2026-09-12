from sqlalchemy import create_engine,Column,Integer,String,Text,DateTime
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime,timezone
engine=create_engine('sqlite:///./documents.db',connect_args={'check_same_thread':False}); SessionLocal=sessionmaker(bind=engine); Base=declarative_base()
class Job(Base):
 __tablename__='jobs'; id=Column(Integer,primary_key=True); filename=Column(String); status=Column(String); extracted_json=Column(Text); error=Column(Text); created_at=Column(DateTime,default=lambda:datetime.now(timezone.utc))
Base.metadata.create_all(engine)
def db():
 s=SessionLocal();
 try: yield s
 finally: s.close()
