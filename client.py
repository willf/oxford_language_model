import requests
import os
import json

class Client:

    """
    Client is a client for the Project Oxford Web Language Model API
    
    Information about the Web Language Model API can be found at 
    https://msdn.microsoft.com/en-US/library/mt628626.aspx
    
    You will need a subscription key to use this services. There are limits to 
    the number of calls one can make to this service, and rate limits. This client 
    does not concern itself with these limits.
    """

    OXFORD_LANGUAGE_MODEL_ENDPOINT = 'https://api.projectoxford.ai/text/weblm/v1.0/'
    SUBSCRIPTION_KEY_NAME = 'Ocp-Apim-Subscription-Key'
    DEFAULT_SUBSCRIPTION_KEY = os.getenv('OXFORD_LANGUAGE_MODEL_KEY')
    
    def __init__(self, subscription_key=DEFAULT_SUBSCRIPTION_KEY):
        "Constructor. Subscription is required. Defaults to os.getenv('OXFORD_LANGUAGE_MODEL_KEY')"
        self.subscription_key = subscription_key
        
    def models(self):
        "Returns a list of dictionaries of available models"
        headers = {self.SUBSCRIPTION_KEY_NAME: self.subscription_key}
        r = requests.get(self.OXFORD_LANGUAGE_MODEL_ENDPOINT + 'models', headers=headers)
        if r.status_code == 200:
            return r.json['models']
        else:
            raise Exception("Error getting models:" + r.reason)
            
    def break_into_words(self, text, model='body',order=5,max_number_of_candidates=5):
        """
        Breaks a non-segmented string into word tokens. For example, "thebeatles" => "the beatles"
        
        Returns up to *max_number_of_candidates* segmentations, each as a dictionary
        with keys 'words' and 'probability'
        
        Arguments:
        text: the text to be segmented
        model: the name of a web model (one of the names from self.models)
        order: the order of the model to use; default to 5 (probably best)
        max_number_of_candidates: Maximum number of candidates to return
        """
        headers = {
            self.SUBSCRIPTION_KEY_NAME: self.subscription_key,
            'Content-Type': 'application/json',
            'Content-Length': '0'
        }
        params = {
         'model' : model,
         'text' : text,
         'order' : order,
         'maxNumOfCandidatesReturned': max_number_of_candidates
        }
        r = requests.post(self.OXFORD_LANGUAGE_MODEL_ENDPOINT + 'breakIntoWords', headers=headers, params=params)
        if r.status_code == 200:
            return r.json['candidates']
        else:
            raise Exception("Error getting word breaks", r.reason)
        
    
        
    def generate_next_words(self, words, model='body',order=5,max_number_of_candidates=5):
        """
        Given a (lower-cased) string of (space separated) words, returns the 
        best guesses of the next word.
        
        Returns up to *max_number_of_candidates* segmentations, each as a dictionary
        with keys 'word' and 'probability'
        
        Arguments:
        words: the words string to be sent
        model: the name of a web model (one of the names from self.models)
        order: the order of the model to use; default to 5 (probably best)
        max_number_of_candidates: Maximum number of candidates to return
        """
        headers = {
            self.SUBSCRIPTION_KEY_NAME: self.subscription_key,
            'Content-Type': 'application/json',
            'Content-Length': '0'
        }
        params = {
         'model' : model,
         'words' : words,
         'order' : order,
         'maxNumOfCandidatesReturned': max_number_of_candidates
        }
        r = requests.post(self.OXFORD_LANGUAGE_MODEL_ENDPOINT + 'generateNextWords', headers=headers, params=params)
        if r.status_code == 200:
            return r.json['candidates']
        else:
            raise Exception("Error getting word breaks", r.reason)
            
    def joint_probabilities(self, queries, model='body',order=5):
        """
        Returns the joint log probabilities of space-separated word strings.
        
        Arguments:
        queries: a list of word strings
        model: the name of a web model (one of the names from self.models)
        order: the order of the model to use; default to 5 (probably best)
        """
        data = json.dumps({'queries' : queries})
        headers = {
            self.SUBSCRIPTION_KEY_NAME: self.subscription_key,
            'Content-Type': 'application/json',
            'Content-Length': str(len(data))
        }
        params = {
         'model' : model,
         'order' : order
        }
        
        r = requests.post(self.OXFORD_LANGUAGE_MODEL_ENDPOINT + 'calculateJointProbability', headers=headers, params=params, data=data)
        if r.status_code == 200:
            return r.json['results']
        else:
            raise Exception("Error getting joint probabilities", r.reason)
    
            
    def conditional_probabilities(self, prior, posts, model='body',order=5):
        """
        Returns the conditional probabilities of words conditioned on a prior
        word string
        
        Arguments:
        prior: a word string
        posts: a list of words to calculate log probability conditioned on prior
        model: the name of a web model (one of the names from self.models)
        order: the order of the model to use; default to 5 (probably best)
        """
        data = json.dumps({'queries' : [{'words': prior, 'word': word} for word in posts]})
        headers = {
            self.SUBSCRIPTION_KEY_NAME: self.subscription_key,
            'Content-Type': 'application/json',
            'Content-Length': str(len(data))
        }
        params = {
         'model' : model,
         'order' : order
        }
        
        r = requests.post(self.OXFORD_LANGUAGE_MODEL_ENDPOINT + 'calculateConditionalProbability', headers=headers, params=params, data=data)
        if r.status_code == 200:
            return r.json['results']
        else:
            raise Exception("Error getting conditional probabilities", r.reason)
    
        
        
        
        