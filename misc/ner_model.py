from transformers import pipeline

# Load a pre-trained NER model
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")

# Example transcript
transcript = """
As your leader, I promise to reduce unemployment rates by 5% within the next year.
We will also increase the budget for healthcare by 20%.
"""
transcript = 'thank you very much thank you thank you very much and I'm delighted to be here at the faith and Freedom coalition's Road to majority what a big deal that is road to the majority conference it's a big uh event and there's a lot of people outside wanting to get in if anyone would like to give up their location please raise your hand immediately this is my ninth time speaking at this event and I would not miss it for anything you know we have a big rally tonight in Philadelphia and so somebody said they got a little bit confused and they had me speaking here and there so somebody foolishly cancelled here and when I heard about it I said wait a minute what are you doing we cancelled faith and freedom I said I don't have the courage to do that I'll do it during the day which is actually even better if you want to know the truth and we'll do the rally later I don't have the courage to do that not to you and not to Ral Reed but I want to thank Ralph Reed for his extraordinary leadership along with executive director Tim head great people thanks also to Congressman he's fantastic Barry Loudermilk he's here someplace he here some place he's doing a fantastic job with all of the things I said he walked through with Russian spies or something like that you turn out to be constituents young children oh these people are sick former congressman and a man who's heading up New York for us Lee Elden he's fantastic LEE Elden South Dakota governor Christy gnome Christie thank you chrisy great thank you Dary RNC chairman Micha wattley he's doing a great job although I'll tell you about that right after the fifth I'll tell you about the sixth but I think he will be incredible he comes from uh good stock comes from North Carolina and they didn't have they didn't have any vote stolen in North Carolina that's why I said he's the guy he watched that voter fraud more than anybody a friend of mine a man who got me involved in this whole deal not this one I mean like eight years ago he thought uh we could do something and we played around with it and I said one day let's go Corey let's go let's do it Corey lowski thank you Corey thank you he's a good man Dr alv King who's a friend of mine for a long time I can't see where his lights these lights are blinding I can't see anybody I just know there are a lot of people in this room but but they happened to have they happen to have the lights in a nice angle it's just perfect I can't see a person here nobody's going to be watching the debate on Thursday night right nobody will anybody be  watching a friend of mine and a great businessman and developer from New York and various other places including Florida Steve witkoff Steve is here here thanks Steve look at that hand you get Steve you got to run for politics and moms for Liberty co-founder Tiffany Justice I love that name Tiffany that's the greatest name I love it and thank you for your endorsement and your help and everything moms for just I'll tell you they have moms for Liberty have been great have been great and Tiffany's been so incredible so I appreciate it very much Tiffany Justice one of the best names I've heard in a long time most importantly let me say a special thanks to the gigantic Grassroots movement of volunteers who will power the faith and freedom Coalition and I know they're going to be very much involved during the election period it used to be one day now it's you know two months it used to start like election day meant election day now it means you know two and a half months before the election begins it starts but it starts actually uh pretty much on September 6th that's North Carolina Pennsylvania's think of that so September 6 and Pennsylvania's uh September 22nd and we have to get out there we have to vote we have to make sure everything's honest and you keep your eyes open you know you're you're the police in a way you can be you can police your vote a lot of people don't know that just make sure that vote counts we have to make sure it counts because if I knew that there was not going to be corruption if I knew that everything would be on hble and honest as it should be I'd stop campaigning right now we have this thing won I would immediately stop campaigning I'd go and relax I'd call up the big rally we have in Philadelphia tonight and say it's not necessary don't worry about everyone go home and relax no organization does more you are truly and I mean this indispensable this is a great group of people and and you're Warriors in the truest sense and you know what we have to do because we're not going to have a country left if we don't do it it's for sure this year you will knock on 10 million doors reach 18 million Christian voters and register 1 million new voters across 130,000 churches and I hope you can put the lock boxes in the churches because that's what you should be doing you should have lock boxes you know these boxes that they cheat with so badly uh you should put them in in your churches because you know the evangelicals and the Christians they don't vote as much as they should I don't know if you know that you know they go to church every Sunday but they don't vote and we have to make sure they vote just this time because all you have to do is this time you don't have to worry about it because we're going to straighten it out very fast just this time go vote but you know they have a uh it's very interesting the NRA gave me a very big endorsement and uh we were talking about it and gun owners don't vote very much I mean I'm saying this is just statistically we have to get people that own guns have to go and vote you own a rifle you want to keep your rifle you better go vote because the the Second Amendment is under siege and you have to vote and who would have known that I think it's sort of a protest you're so angry about what's happening but this is over years gun owners don't vote much meaning you know some vote but not relatively speaking not that much and uh Christians go to church but they don't vote that much do you know the power you have if you would vote it wouldn't even be so you got to get out of vote just this time I don't care in four years you don't have to vote okay in four years don't vote I don't care but that time but we'll have it all straighten out so it'll be much different of course then they'll come in again and they'll ruin it we'll have to do this all over again then we'll come back say you have to go vote working side by side we're going to defeat crooked Joe Biden we're going to defend our values and we're going to make America great again and this will be the most important election in the history of our country I believe that I used to say it 2016 we had a border that was bad but the Border was bad but it was like I call it peanuts peanuts compared to what we have now that was like a great border if we had that border now it would be like great it was uh it was really bad but it was is a just a tiny fraction of what it is now now it's the worst it's ever been I I would say it's the worst border anywhere of any country anywhere in the world at any time in less than four years Joe Biden has obliterated the borders of the United States we don't have borders we don't have borders we don't have elections that are proper we don't have anything and you know what we want with elections we want paper ballots same day voting voter ID and we want to ensure that people are citizens little thing a little thing like let's make sure you're a citizen right you know they're bringing these people in they're trying to get these people registered to vote they don't speak a word of English most of them and they come from all over the world that's what they're doing I said there was only a few things it could could it be they're stupid well they're not stupid nobody could cheat that well if they were stupid they're not stupid then the other is they hate our country that could be that could be but the third thing is they want to register people to vote that's I think what they really have in mind so we have to be very careful and that's where Michael wattley will do the job that's where Susie WS who's here right now she's fantastic and she'll do the job and Lara will do the job Lara chump who's fantastic she's fantastic but crooked Jill wrecked our economy with brutal inflation and2 trillion doll deficits did you hear our deficit is going to be $2 trillion doll this year two trillion his weakness failure and incompetence have set the world on fire he is a threat to democracy by the way just by being so incompetent he's a threat to democracy his Marxist Administration is pushing radical gender ideology into every school and I'm sure this group is not particularly happy with that and crooked Joe has demonstrated an amazing ability to you know he's just to demolish the rule of law by arresting political opponents diss Christians pro-life activists like a third world dictator would do it's a disgrace what's happened to our country in such a short period of time three and a half years what's happened to our country it's not even believable our one chance to save America from these leftwing fascists is less than it's now four months can you believe it I've been saying seven six five it's now we're in between four and five months from now November 5th going to go down as the most important day in the history history of our country I'm telling you because we're not going to have I hope we can get there without ending in a world war you know Russia Russia's got submarines now very nicely in Cuba you know where Cuba is is about two feet away from Florida no they've got chips there and they're talking about you know going after Russia in Ukraine and giving them authorization to go after Russia you know where's this thing going to and I've said it I will get that war s if there's anything left if there's anything left I'll get it Sol as President elect before I ever get into the White House but we need Christian voters to turn out in the largest numbers ever to tell crooked Joe Biden Joe The Apprentice Joe you're fired you're fired Joe get out of here Joe you're no good you've been the worst president ever you fired Joe get  out no worst president in the history of our country as you know the radical left is trying to shame Christians Silence You demoralize you and they want to keep you out of politics they don't want you to vote that's why you have to vote they're counting on you not because if you vote no we cannot lose they don't want you to vote but Christians cannot afford to sit on the sidelines if Joe Biden gets back in Christianity will not be safe in a nation with no borders no laws no Freedom no future they're not going to be safe you're not going to be safe as a person and your religion certainly will be I think in tatters you want to know the truth I think in tatters you see what they're doing and and I don't know it's less a little bit less to do with this room but we all care what's going on with Catholics they are being persecuted Catholics what is that all about by this guy this guy this man that has no idea what the hell is happening and by the way I don't believe it is him I think it's the people that surround him the fascist communist the young very smart vicious people because I don't think he knows he's alive if you want to know the truth Okay the reason the radical left will always come after religious Believers is simple because they know that our Allegiance is not to them our Allegiance is not to them our Allegiance is to our country and our Allegiance is to our creator and we do not not answer to the bureaucrats i'
# Extract claims
claims = ner_pipeline(transcript)

# Filter and process claims
extracted_claims = [entity['word'] for entity in claims if entity['entity_group'] == 'CLAIM']

print(claims)