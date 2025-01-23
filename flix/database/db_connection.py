from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from FlagEmbedding import BGEM3FlagModel

DATABASE_URI = "postgresql://postgres.ikezyblrkiyajmdgpkzz:Open!ProjectFlix@aws-0-us-west-1.pooler.supabase.com:6543/postgres"
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)

model = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)

def get_session():
    return SessionLocal()
