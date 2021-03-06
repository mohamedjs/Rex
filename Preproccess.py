import pandas as pd
import re                                  # library for regular expression operations
import string                              # for string operations
import nltk
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

def removeSomeString(our_word):
	# remove old style restring text "RT"
	our_word = re.sub(r'^RT[\s]+', '', our_word)

	# remove hyperlinks
	our_word = re.sub(r'https?:\/\/.*[\r\n]*', '', our_word)

	# remove hashtags
	# only removing the hash # sign from the word
	our_word = re.sub(r'#', '', our_word)

	return our_word

def tokenizer(our_word):
	# instantiate tokenizer class
	tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
	                               reduce_len=True)

	# tokenize tweets
	string_tokens = tokenizer.tokenize(our_word)

	return string_tokens

def cleanString(our_word):
	string_clean = []
	stopwords_english = stopwords.words('english') 
	for word in our_word: # Go through every word in your tokens list
	    if (word not in stopwords_english and  # remove stopwords
	        word not in string.punctuation):  # remove punctuation
	        string_clean.append(word)
	return string_clean

def preproccess(our_word):
	new_str       = removeSomeString(our_word)
	tokenize_str  = tokenizer(new_str) 
	clean_str     = cleanString(tokenize_str)
	return clean_str

df = pd.read_csv("Reviews-Dataset.csv")
print(preproccess(df['text'][0]))
# preproccess_list = []
# for our_word in df['text']:
# 	preproccess_list.append(preproccess(our_word))
