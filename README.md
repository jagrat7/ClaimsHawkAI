# ClaimsHawkAI
**Work In Progress** - alot of things still need to be completed and tidied up. <br>
A app the takes transcripts from politicians and world leader speechs and use ai model(from hugging face) to get the claims made by them i.e a politicians says "I will reduce the unemployment rate" or "I will reduce the waste produced by the company". It also provides ways to validate claim with data i.e "employment rate after election" , "waste volume after claim"

## Tech Stack
- [Next.js](https://nextjs.org/docs) - Fullstack framework for React. Used with App Router.
- [Prisma](https://www.prisma.io/) with SQLite for database ORM, there is dockerfile for postgresql.
- [FastAPI](https://fastapi.tiangolo.com/) for AI python microservice
- [Langchain](https://python.langchain.com/v0.2/docs/introduction/) for AI dev.
## How to run

### Setup the environment
`python -m venv venv`

On Windows: <br>
`.\venv\Scripts\activate`
<br>
On Linux: <br>
`source venv/bin/activate`

`pip install -r requirements.txt`

## MVPs
- Get claims from transcripts of youtube made by the politicians/world leader and get Vector Embeddings for the transcript
- Store the Vector Embeddings so we can group similar claims as one claim - We want to make sure that the same/similar claim does not get added as a new claim. Example "I will clean river X when I am elected" and " I will improve the the quality of the rivers in my town" should be the same claim
- Differentiate between vague and specific non vague claims, display ratio of non-vague claims



## Future features
- add timestamp to extracted captions so we can extract at the timestamp in the youtube video
- Provide metrics that can validate a non-vague claim 
- If data is available show whether claim made is being satisfied and to what degree
- Metrics to evaluate person success based on the type(vague/non-vague) of claims and successfully achieved claims, endorsements given by people or companies for the world leader
- Scraps posts made on social media and other outlets and extract the claims made from this sources 
- Target different industries and their heads/leaders i.e. FDA and how they are allowing so many banned substances in our foods, sports e.t.c ClaimsHawkAI/Food ClaimsHawkAI/Climate
