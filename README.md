# Viterbi algorithm

Viterbi algorithm is known as a dynamic programming algorithm for finding the most likely sequence of hidden states. It provides a Viterbi path based on five parameters: States, observations, transition_probability, emission_probability and start_probability.

Viterbi algorithm applications are a lot we give as examples:  decoding the convolutional codes used in both CDMA and GSM digital cellular, dial-up modems, satellite, deep-space communications, speech recognition, speech synthesis, diarization, keyword spotting, computational linguistics, and bioinformatics.

Consider reading the "historique" and python files to learn more about Viterbi algorithm and it's complexity.

As we aimed to create an application mixing between AI concepts and Viterbi path fiding, one of the best choices that we could work on was "Word tagging". This technique allows the machine to recognize automatically tags of every word or sign given in a sentence as an input to our program. For example given the following sentence "Jane will spot Will" the ouput will be "noun, model, verb, noun". 

![alt input](https://user-images.githubusercontent.com/31079981/86388838-5c1c7180-bc8d-11ea-9bca-f7f046cf0d56.png)

The program here gave a number of tags corresponding to each word in the sentences provided.

![alt params](https://user-images.githubusercontent.com/31079981/86390304-bd454480-bc8f-11ea-8196-4cb9ccbdc9ef.png)

![alt output](https://user-images.githubusercontent.com/31079981/86389025-a30a6700-bc8d-11ea-9d69-46e1fd1906f0.png)

You can notice also that even the sentence has got a homonyms "will" & "Will" and considering that the input is lowercased you can how effective a well trained a viterbi algorithm can spot the difference.

![alt output](https://user-images.githubusercontent.com/31079981/86391419-ad2e6480-bc91-11ea-8540-5c4ba5f00c2f.png)

The program has already got a trained data only on the words that we worked on in the example. As if someone thought of making his own dataset and trained models he can refer to the "trainer.py" file under "viterbi tagging" directory to give a set of sentences -We suggest having a huge dataset to maximize the accuracy- and put it in the "data.txt" file. Running with a huge dataset may take a lot of time so we suggest also to work on computers with high preformances like the cloud services: AWS, GCP ...

The "trainer.py" file contains a libarary "nltk" - don't forget "pip install nltk"- that will help to give tags automatically instead of doing each word in each sentence, this way will take you forever :D. And then you'll have as an output the parameters needed in the viterbi algorithm as lists and json texts.

You'll find the list of english tags possible in the following link:
https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

You may think why looking for retagging words if already nltk can do it. The viterbi algorithm is more optimized, consider scaling projects in the future and having the data structured as the viterbi can process it, it will improve your word tagging framework's speed and efficiency.

Finally this work couldn't be done without the collaboration of this beautiful team: Aya Sebti, Marouane Maaou and Mohammed Rhaouti
