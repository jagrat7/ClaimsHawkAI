from pgvector.sqlalchemy import Vector

def find_similar_claims(query_embedding, top_k=5):
    """Finds the most similar claims to a given query embedding.

    Args:
        query_embedding: The embedding vector of the query claim.
        top_k: The number of similar claims to return.

    Returns:
        A list of similar Claim objects.
    """
    similar_claims = session.query(Claim).order_by(
        Claim.embedding.cosine_distance(query_embedding)
    ).limit(top_k).all()
    return similar_claims

# Example usage:
query_claim = "I will reduce taxes for the middle class."
query_embedding = get_embedding(query_claim) 
similar_claims = find_similar_claims(Vector(query_embedding), top_k=3)

for claim in similar_claims:
    print(f"Claim: {claim.claim}, Similarity: {1 - claim.embedding.cosine_distance(query_embedding):.4f}") 
