import unittest
import spacy
from EntityLinker import EntityLinker

nlp =  spacy.load('en_core_web_trf')
nlp.add_pipe("entityLinker", last=True)

data = "And the very fact that he accomplished all this very quickly without even breaking a sweat PROVES TO ALL WHO WOULD OPEN THEIR EYES that the last 4 previous presidents (and this current coup-installed one) were working nonstop to purposefully weaken and destroy the United States of America."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()
        
data = " see Zombies crawling down the street. Is that the Plague that they've been talking about? Honey, That's the Soros Plague. It's Everywhere !!! Quick. How many grenades do we have?Let me count. Five. Give them to me. You can snipe the leftovers. Roger that, Babe! Let's Roll !!!"
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "McCarthy and the House Republicans should adopt bold new Rules to withhold funds from radical Democrats. House Rules can't be challenged by courts, the Senate, or the President! McCarthy can stop the radical Democrat agenda by controlling the money! That's what we elected the Republican House to do! Stop the FBI and DOJ from working for the Democrat party!"
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "President Trump decided to NOT go along with the globalists’ plans, and since he is not one of them and is an ACTUAL American President working for our NATION and the American people according to the U.S. constitution, he is ENEMY NUMBER ONE to the New World Order. That’s all it takes to become their enemy; be an actual American who doesn’t want to destroy our national sovereignty for Claus Schwab and the entire globalist cabal."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "In the first two years of his first term (prior to the False Flag Covid lock-down and take-down of the entire economies of the west), Trump had the economy in the best condition in 80 years. He had the lowest unemployment for blacks, Latinos, and women by simply doing what any ACTUAL U.S. president should be doing."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()





data = "It is the west's history and culture that has to “go away” in order for the globalists’ Grrrreat Reset to take place. National sovereignty has to give way to a global dystopian nightmare dictatorship run by bankers and corporations who dictate and “provide” for the serfs they allow to exist (who will own nothing and live in pods and eat bugs while twerking, while thinking themselves to be the most intelligent and free people to have ever lived) if the globalists’ plans are carried out (that President Trump was trying to reverse)."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()
        
data = "The U.S. constitution and a global government CANNOT exist under the same roof. They are OPPOSITES that are diametrically opposed to each other."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "All actual history (especially western CHRISTIAN history) must be erased. That's why Star Wars and Lord of the Rings now SUCKS. New and SCRIPTED culture is being created to REPLACE actual culture."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "There is no more left vs right. There is now only national sovereignty (and the rights and freedoms enumerated in the U.S. constitution vs the Grrreat Reset! global dystopian nightmare post-sovereignty plan of no borders and a sort of global E.U.-style government of elite banks and corporations and child-like serfs who are allowed to service them. Everything else is just SCRIPTED WINDOW DRESSING AND DIVIDE AND CONQUER TACTICS."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "If we ever want to see any possibility for ACTUAL fair and honest elections again (or even to be able to PRETEND that we still live in the United States of America under the U.S. constitution and the rule of law), then we must get rid of the CIA, FBI, DHS, and all the other post-sovereignty, globalist shill organizations perpetrating the controlled demolition of the United States and the entire western world (along with their corporate owned enemy media and social media censoring platforms that they also own and/or control)."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()



data = "The globalists have been using the “good cop / bad cop” routine on the American people for quite some time."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()
        
data = "President Trump is not a RINO. Trump is unique and he is, shall we say, very Trumpian. But he actually has a desire for America to be great again, and to NOT relinquish national sovereignty to the Great Reset global government dystopian nightmare."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "They need a new wokified generation to helm the post-sovereignty global province that the U.S. (and every western nation) is to become."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()



data = "He got rid of many restrictive regulations and freed up our industrial base again, and so Trump had actually (in this same short two year period) made the U.S. ENERGY INDEPENDENT who didn’t need to rely on foreign nations for our energy production. And Trump had made the borders the most secure in 50 years, and illegal invaders were being kept in Mexico (by agreement) instead of being released into the American heartland."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()
        
data = "President Trump accomplished all of this because he DIDN’T act like the previous four presidents (Bush, Clinton, Bush, Obama) or the current coup-installed occupier of the White House, Biden, who all had been (or are) working nonstop AGAINST the American people and FOR the managed decline of our country and the end of the independent middle class and the sovereignty of our nation."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "And the very fact that he accomplished all this very quickly without even breaking a sweat PROVES TO ALL WHO WOULD OPEN THEIR EYES that the last 4 previous presidents (and this current coup-installed one) were working nonstop to purposefully weaken and destroy the United States of America."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "And President Trump accomplished all of this while the entire Democrat party, 90% of the RINO Republican party, the entire corporate owned enemy media, all of academia and the teachers unions and university staff, the entire Deep State entrenched and unelected government agencies, and most of the politicians in the nations of most of our so-called “allies” were actively doing everything they could possibly come up with to coordinate and thwart and destroy him and his supporters."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()

data = "The ruling tribe actively taking down the United States in a controlled demolition do not in any way adhere to the U.S. constitution, or even the notion of a sovereign United States. And the American people better not be waiting for the DOJ, intelligence agencies, or the Feds (like the FBI) to step in to investigate or arrest anybody who has been violating the U.S. constitution against the American people, as these are the VERY PERPETRATORS OF THE VERY CRIMES that we’re talking about. The ones who should be doing the arresting would have to arrest themselves."
doc = nlp(data)
print(data)
doc._.linkedEntities.pretty_print()
nlp.remove_pipe("entityLinker")

