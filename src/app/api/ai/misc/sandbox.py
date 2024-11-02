from sqlalchemy.orm import Session
from sqlalchemy import select
from models.Claim import Claim
from database.database import SessionLocal
import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Claim import Claim
from models.Video import Video
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

# Load environment variables
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
def get_embedding(claim: Claim):
    embeddings = OpenAIEmbeddings()
    
    # Generate embedding for the single claim
    embedded_claim = embeddings.embed_query(claim.claim)
    print("got embeddings for {claim.claim}",embedded_claim)
    
    return embedded_claim
def update_claim_embeddings():
    db = SessionLocal()
    try:
        claims = db.scalars(select(Claim)).all()
        for claim in claims:
            embedding = get_embedding(claim)
            claim.embedding = embedding
            db.add(claim)
        db.commit()
        print(f"Updated embeddings for {len(claims)} claims")
    finally:
        db.close()

def is_repeated(claim: Claim):
    from sqlalchemy import select
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    # Test vector search
    from sqlalchemy import select

    result = session.execute(select(TestModel.id, TestModel.name))
    print(result)
    for item in result:
        print(f"ID: {item}")
    from sqlalchemy import select

    # Query to get all rows and their cosine distances
    query = select(TestModel, TestModel.embedding.cosine_distance([188.0, 82.0, 113.0]).label('distance'))

    # Execute the query
    result = session.execute(query)

    # Print the results
    for row in result:
        item = row.TestModel
        distance = row.distance
        similarity = 1 - distance
        print(f"Name: {item.name}, Embedding: {item.embedding}, Similarity: {similarity:.4f}")




if __name__ == "__main__":
    # update_claim_embeddings()
    db = SessionLocal()
    try:
        claims = db.scalars(select(Claim.embedding).limit(5)).all()
        for claim in claims:
            print(claim[:5])
    finally:
        db.close()  