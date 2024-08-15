# Anti-Profanity
 A FastText Classifier for Profanity, for filtering games, forums, and any other user-based text input.
 Built using Facebook's FastText vectorizer and text classifier, and using Swastik Gupta's tutorial on ["Profanity Detection with FastText"](https://towardsdatascience.com/profanity-detection-with-fasttext-ab2b3d63264f).
### What's in the Repo
**preprocess.py** - This file is used to format test.csv into processed-train.txt using a csv reader, and NLTK's Lemmatizer and Stop Word library
**train.py** - Used to Train the FastText Classifier on processed-train.txt, and then quantize, save, and test the model
**test.py** - Used to simply load the model and test with words
**train.csv** - Just the training data from [Kaggle's Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data?select=train.csv.zip)
### Usage? 
Just install:
`pip install fasttext nltk`
And then run:
`python preprocess.py`
to process the original training data. (Although I provided the output, cause it took a while to process. Last time I grabbed the training data was August 14, 2024)
Finally run:
`python train.py`
to train the data and quantize it. It should take 5 to 10 mintues to complete, depending on hardware.
You should now have a model! Congrats!

### Credits
Facebook - Thanks for your amazing Fast Text AI, highly appreciated
Kaggle - Thanks for your work on putting all toxic comments in one place
NLTK - Thanks for your library to remove useless noise in the English Language
Swastik Gupta - For putting the idea together, you really should be the one to release this 
My savior, Jesus Christ - The sole reason my life has a purpose. If you want to see his work, just look at everything that is good. 

This was created by PonderForge, if you use this code, give credit where credit is due.
Pslam 111:2 "Great are the works of the LORD; they are pondered by all who delight in them."