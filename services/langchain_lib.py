from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import OpenAIEmbeddings
from pydantic import BaseModel
from typing import List
import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.Claim import Claim
from models.Video import Video
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the LLM
llm = ChatOpenAI( api_key=api_key, temperature=0.1) #model_name='gpt-4o',


# Define Pydantic models
class ClaimModel(BaseModel):
    claim: str
    measurable: bool
    analysis: str
    # quote: str

class ClaimList(BaseModel):
    claims: List[ClaimModel]
# Create the output parser
parser = PydanticOutputParser(pydantic_object=ClaimList)

def load_document(file_path):
    loader = TextLoader(file_path)
    return loader.load()

def extract_speaker(file_path):
    extract_speaker_template = ChatPromptTemplate.from_template(
        "Extract the speaker's name from this filename: {filename}. Only return the name, nothing else."
    )
    speaker_chain = extract_speaker_template | llm
    speaker_result = speaker_chain.invoke({"filename": os.path.basename(file_path)})
    return speaker_result.content.strip()

# Create the prompt templates for claim extraction and analysis
extract_claims_template = ChatPromptTemplate.from_template(
    "Extract claims from the following text:\n\n{text}\n\n list each claim as a separate bullet point. Claims:"
)

analyze_claims_template = ChatPromptTemplate.from_template(
    """For each claim, determine if it is measurable or not. If measurable, explain how it could be quantifiably measured or validated using real-world data. If not measurable, explain why it's too vague or subjective to measure. Consider specific metrics, data sources, or methods that could be used for validation.

    Format your response as a list of claims with their analysis, following this structure:
    {format_instructions}

    Claims to analyze:
    {claims}
    """
)

# Create the LCEL chain for claim extraction and analysis
chain = (
    {"text": lambda x: x['text']}
    | extract_claims_template
    | llm
    | {"claims": lambda x: x.content}
    | analyze_claims_template.partial(format_instructions=parser.get_format_instructions())
    | llm
    | parser
)

def get_claims(speaker,video: Video):
    document = load_document(video.captions_location)
    text=document[0].page_content
    print("loaded document into text")
    # Extract speaker
    if not speaker:
        speaker = extract_speaker(video.captions_location)
    else:
        speaker = speaker
    print("extracted speaker",speaker)

    timestamp = datetime.datetime.now().isoformat()
    try:
        result = chain.invoke({"text": text})
    except Exception as e:
        print(f"Error extracting claims: {str(e)}")

    # print("got result",result)
    claims = [
        Claim(
            speaker=speaker,
            claim=claim.claim,
            timestamp=timestamp,
            measurable=claim.measurable,
            analysis=claim.analysis,
            quote=' ',
            embedding=get_embedding(claim.claim),
        )
        for claim in result.claims
    ]
    return claims

def get_embedding(claim: Claim):
    embeddings = OpenAIEmbeddings()
    
    # Generate embedding for the single claim
    embedded_claim = embeddings.embed_query(claim.claim)
    print("got embeddings for {claim.claim}",embedded_claim[:2])
    
    return embedded_claim

# def test():
#     file_path = "../data/President_Bidens_State_of_the_Union_Address_2024-03-08T034913Z.txt"
#     loader = TextLoader(file_path)
#     document = loader.load()

#     extract_speaker_template = ChatPromptTemplate.from_template(
#         "Extract the speaker's name from this filename: {filename}. Only return the name, nothing else."
#     )

#     # Extract speaker using LLM
#     speaker_chain = extract_speaker_template | llm
#     speaker_result = speaker_chain.invoke({"filename": os.path.basename(file_path)})
#     speaker = speaker_result.content.strip()
#     print("speaker", speaker)
#     # # Create the LCEL chain for claim extraction and analysis
#     chain = (
#         {"text": lambda x: x['text']}
#         | extract_claims_template
#         | llm
#         | {"claims": lambda x: x.content}
#         | analyze_claims_template.partial(format_instructions=parser.get_format_instructions())
#         | llm
#         | parser
#     )

#     # Run the chain
#     result = chain.invoke({"text": document[0].page_content})
#     timestamp = datetime.datetime.now().isoformat()
#     # Convert the results to Claims objects
#     claims_objects = [
#         Claim(
#             speaker=speaker,
#             claim=claim.claim,
#             timestamp=timestamp,
#             measurable=claim.measurable,
#             analysis=claim.analysis
#         )
#         for claim in result.claims
#     ]
#     print("nunber of claims: ", len(claims_objects))
#     # Print the results
#     for claim in claims_objects:
#         print(f"Speaker: {claim.speaker}")
#         print(f"Claim: {claim.claim}")
#         print(f"Timestamp: {claim.timestamp}")
#         print(f"Measurable: {'Yes' if claim.measurable else 'No'}")
#         print(f"Analysis: {claim.analysis}")
#         print()
