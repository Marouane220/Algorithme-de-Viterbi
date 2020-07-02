# Viterbi algorithm
Viterbi algorithm is known as a dynamic programming algorithm for finding the most likely sequence of hidden states. It provides a Viterbi path based on five parameters: States, observations, transition_probability, emission_probability and start_probability.

Viterbi algorithm applications are a lot we give as examples:  decoding the convolutional codes used in both CDMA and GSM digital cellular, dial-up modems, satellite, deep-space communications, speech recognition, speech synthesis, diarization, keyword spotting, computational linguistics, and bioinformatics.

Consider reading the "historique" and python files to learn more about Viterbi algorithm and it's complexity.

As we aimed to create an application mixing between AI concepts and Viterbi path fiding, one of the best choices that we could work on was "Word tagging". This technique allows the machine to recognize automatically tags of every word or sign given in a sentence as an input to our program. For example given the following sentence "Jane will spot Will" the ouput will be "noun, model, verb, noun". The program here gave a number of tags corresponding to each word in the sentences provided. You can notice also that even the sentence has got a homonyms "will" & "Will" and considering that the input is lowercased you can how effective a well trained vitebi algorithm can spot the difference.

The program has already got a trained data only on the words that we worked on in the example. As if someone thought of making his own dataset and trained models he can refer to the "trainer.py" file under "viterbi tagging" directory to give a set of sentences -We suggest having a huge dataset to maximaze the accuracy- and put it in the data.txt" file. Running with a huge dataset may take a lot of time so we suggest also to work on computers with high preformances like the cloud services: AWS, GCP ...

The "training.py" file contains a libarary "nltk" - don't forget "pip install nltk"- that will help to give tags automatically instead of doing each word in each sentence, this way will take you forever :D. And then you'll have as an output the parameters needed in the viterbi algorithm as lists and json texts.
