from sqlalchemy import select

# Create and insert test data
# test_data = [
#     TestModel(name="Item 1", embedding=[1.0, 2.0, 3.0]),
#     TestModel(name="Item 2", embedding=[4.0, 5.0, 6.0]),
#     TestModel(name="Item 3", embedding=[7.0, 8.0, 9.0])
# ]
# session.add_all(test_data)
# session.commit()

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

