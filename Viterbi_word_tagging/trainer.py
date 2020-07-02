import nltk
from nltk import word_tokenize
import json

states = []
observations = []
transition_probability = {'<S>' : {"<E>" : 0}}
emission_probability = {}

previousObservations = []
previousTags = []

def train(data="data.txt"):
    file = open("data.txt", "r")
    for line in file:
        
        text = word_tokenize(line.lower())
        tags = nltk.pos_tag(text)
        
        for idx, tag in enumerate(tags):
            try:
                previousTag = tags[idx - 1][1]
                nextTag = tags[idx + 1][1]           
            except:
                previousTag = "<S>"
                nextTag = "<E>"


                                 
            if tag[0] not in states:
                states.append(tag[0])
                
            if tag[1] not in observations:
                observations.append(tag[1])
                
            if tag[1] not in previousTags:
                emission_probability[tag[1]] = {}
                transition_probability[tag[1]] = {}
                transition_probability["<S>"][tag[1]] = 0
                transition_probability[tag[1]]["<E>"] = 0
                
                for observation in previousObservations:
                    emission_probability[tag[1]][observation] = 0

                previousTags.append(tag[1])
                
                for ptag in previousTags:
                    transition_probability[ptag][tag[1]] = 0
                    transition_probability[tag[1]][ptag] = 0
                
            if tag[0] not in previousObservations:
                for ptag in previousTags:
                    emission_probability[ptag][tag[0]] = 0
                    
                previousObservations.append(tag[0])

            # filling emission_probability
            if tag[0] not in emission_probability[tag[1]]:
                emission_probability[tag[1]][tag[0]] = 1
            else:
                emission_probability[tag[1]][tag[0]] += 1
                
            # filling transition_probability
            if previousTag == "<S>":
                if tag[1] not in transition_probability["<S>"]:
                    transition_probability["<S>"][tag[1]] = 1
                else:
                    transition_probability["<S>"][tag[1]] += 1    
                    
            else:
                if nextTag not in transition_probability[tag[1]]:
                     transition_probability[tag[1]][nextTag] = 1
                else:
                    transition_probability[tag[1]][nextTag] += 1
                    
    print("Training succeeded")        
    file.close()       
    return(states, observations, transition_probability, emission_probability)

if __name__ == "__main__":
    train()


