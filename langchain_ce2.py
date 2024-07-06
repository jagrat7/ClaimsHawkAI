from langchain.chains import LLMCheckerChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the LLM
llm = OpenAI(api_key=api_key, temperature=0.7)

# Define custom prompts for claim extraction
create_draft_answer_prompt = PromptTemplate(
    input_variables=['question'],
    template='Extract claims from the following text:\n\n{question}\n\nClaims:'
)

list_assertions_prompt = PromptTemplate(
    input_variables=['statement'],
    template='Here are some claims:\n{statement}\nList each claim as a separate bullet point.'
)

check_assertions_prompt = PromptTemplate(
    input_variables=['assertions'],
    template='Here is a list of claims:\n{assertions}\nFor each claim, determine if it is measurable or not. If it is measurable, explain how it could be measured.'
)

revised_answer_prompt = PromptTemplate(
    input_variables=['checked_assertions', 'question'],
    template="Based on the analysis of the claims:\n{checked_assertions}\n\nProvide a final list of measurable claims from the original text:\n{question}\n\nMeasurable Claims:"
)

# Create the LLMCheckerChain
checker_chain = LLMCheckerChain.from_llm(
    llm,
    create_draft_answer_prompt=create_draft_answer_prompt,
    list_assertions_prompt=list_assertions_prompt,
    check_assertions_prompt=check_assertions_prompt,
    revised_answer_prompt=revised_answer_prompt
)

def extract_claims(text):
    try:
        result = checker_chain.invoke({"question": text})
    except ValueError:
        result = checker_chain.invoke({"query": text})
    
    print("Full result:", result)  # This will help us see the structure of the result
    
    # Assuming the result contains the final answer, let's try to extract it
    if isinstance(result, dict):
        # If it's a dictionary, look for keys that might contain our answer
        for key in ['text', 'answer', 'output', 'result']:
            if key in result:
                return result[key]
    
    # If we couldn't find a suitable key, return the entire result
    return str(result)

# Use the function
speech = """ thank you very much thank you thank you very much and I'm delighted to be here at the faith and Freedom coalition's Road to majority what a big deal that is road to the majority conference it's a big uh event and there's a lot of people outside wanting to get in if anyone would like to give up their location please raise your hand immediately this is my ninth time speaking at this event and I would not miss it for anything you know we have a big rally tonight in Philadelphia and so somebody said they got a little bit confused and they had me speaking here and there so somebody foolishly cancelled here and when I heard about it I said wait a minute what are you doing we cancelled faith and freedom I said I don't have the courage to do that I'll do it during the day which is actually even better if you want to know the truth and we'll do the rally later I don't have the courage to do that not to you and not to Ral Reed but I want to thank Ralph Reed for his extraordinary leadership along with executive director Tim head great people thanks also to Congressman he's fantastic Barry Loudermilk he's here someplace he here some place he's doing a fantastic job with all of the things I said he walked through with Russian spies or something like that you turn out to be constituents young children oh these people are sick former congressman and a man who's heading up New York for us Lee Elden he's fantastic LEE Elden South Dakota governor Christy gnome Christie thank you chrisy great thank you Dary RNC chairman Micha wattley he's doing a great job although I'll tell you about that right after the fifth I'll tell you about the sixth but I think he will be incredible he comes from uh good stock comes from North Carolina and they didn't have they didn't have any vote stolen in North Carolina that's why I said he's the guy he watched that voter fraud more than anybody a friend of mine a man who got me involved in this whole deal not this one I mean like eight years ago he thought uh we could do something and we played around with it and I said one day let's go Corey let's go let's do it Corey lowski thank you Corey thank you he's a good man Dr alv King who's a friend of mine for a long time I can't see where his lights these lights are blinding I can't see anybody I just know there are a lot of people in this room but but they happened to have they happen to have the lights in a nice angle it's just perfect I can't see a person here nobody's going to be watching the debate on Thursday night right nobody will anybody be  watching a friend of mine and a great businessman and developer from New York and various other places including Florida Steve witkoff Steve is here here thanks Steve look at that hand you get Steve you got to run for politics and moms for Liberty co-founder Tiffany Justice I love that name Tiffany that's the greatest name I love it and thank you for your endorsement and your help and everything moms for just I'll tell you they have moms for Liberty have been great have been great and Tiffany's been so incredible so I appreciate it very much Tiffany Justice one of the best names I've heard in a long time most importantly let me say a special thanks to the gigantic Grassroots movement of volunteers who will power the faith and freedom Coalition and I know they're going to be very much involved during the election period it used to be one day now it's you know two months it used to start like election day meant election day now it means you know two and a half months before the election begins it starts but it starts actually uh pretty much on September 6th that's North Carolina Pennsylvania's think of that so September 6 and Pennsylvania's uh September 22nd and we have to get out there we have to vote we have to make sure everything's honest and you keep your eyes open you know you're you're the police in a way you can be you can police your vote a lot of people don't know that just make sure that vote counts we have to make sure it counts because if I knew that there was not going to be corruption if I knew that everything would be on hble and honest as it should be I'd stop campaigning right now we have this thing won I would immediately stop campaigning I'd go and relax I'd call up the big rally we have in Philadelphia tonight and say it's not necessary don't worry about everyone go home and relax no organization does more you are truly and I mean this indispensable this is a great group of people and and you're Warriors in the truest sense and you know what we have to do because we're not going to have a country left if we don't do it it's for sure this year you will knock on 10 million doors reach 18 million Christian voters and register 1 million new voters across 130,000 churches and I hope you can put the lock boxes in the churches because that's what you should be doing you should have lock boxes you know these boxes that they cheat with so badly uh you should put them in in your churches because you know the evangelicals and the Christians they don't vote as much as they should I don't know if you know that you know they go to church every Sunday but they don't vote and we have to make sure they vote just this time because all you have to do is this time you don't have to worry about it because we're going to straighten it out very fast just this time go vote but you know they have a uh it's very interesting the NRA gave me a very big endorsement and uh we were talking about it and gun owners don't vote very much I mean I'm saying this is just statistically we have to get people that own guns have to go and vote you own a rifle you want to keep your rifle you better go vote because the the Second Amendment """
claims = extract_claims(speech)
print(claims)
