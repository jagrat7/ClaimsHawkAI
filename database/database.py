from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://admin:passadmin@localhost:5432/ch"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)

# class TestModel(Base):
#     from sqlalchemy import  Column, Integer, String
#     from pgvector.sqlalchemy import Vector
#     from sqlalchemy.orm import mapped_column

#     __tablename__ = "test"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     embedding = mapped_column(Vector(3))

# def test():
#     from sqlalchemy import select
#     engine = create_engine(SQLALCHEMY_DATABASE_URL)
#     Base.metadata.create_all(engine)
#     SessionLocal = sessionmaker(bind=engine)
#     session = SessionLocal()

#     # Create and insert test data
#     test_data = [
#         TestModel(name="Item 1", embedding=[1.0, 2.0, 3.0]),
#         TestModel(name="Item 2", embedding=[4.0, 5.0, 6.0]),
#         TestModel(name="Item 3", embedding=[7.0, 8.0, 9.0])
#     ]
#     session.add_all(test_data)
#     session.commit()

#     # Test vector search
#     from sqlalchemy import select

#     result = session.execute(select(TestModel.id, TestModel.name))
#     print(result)
#     for item in result:
#         print(f"ID: {item}")
#     from sqlalchemy import select

#     # Query to get all rows and their cosine distances
#     query = select(TestModel, TestModel.embedding.cosine_distance([188.0, 82.0, 113.0]).label('distance'))

#     # Execute the query
#     result = session.execute(query)

#     # Print the results
#     for row in result:
#         item = row.TestModel
#         distance = row.distance
#         similarity = 1 - distance
#         print(f"Name: {item.name}, Embedding: {item.embedding}, Similarity: {similarity:.4f}")


#     # distances = session.scalars(select(TestModel.id, TestModel.embedding.cosine_distance([1, 2, 3]).label('distance'))).all()
#     # for item in result:
#     #     distance = distance_dict[item.id]
#     #     similarity = 1 - distance
#     #     print(f"Name: {item.name}, Embedding: {item.embedding}, Similarity: {similarity:.4f}")


# if __name__ == "__main__":
#     test()

