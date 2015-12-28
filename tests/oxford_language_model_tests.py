import sys
sys.path.append("..")
import oxford_language_model
import unittest

class TestOxfordLanguageModel(unittest.TestCase):

    def test_client(self):
        c = oxford_language_model.Client()
        assert c.subscription_key is not ""
        
    def test_get_models(self):
        c = oxford_language_model.Client()
        models = c.models()
        assert len(models) > 0
    
    def test_get_word_break(self):
        tobreak = 'thebeatles'
        guesses = oxford_language_model.Client().break_into_words(tobreak)
        assert len(guesses) > 0
        assert guesses[0]['words'] == 'the beatles'
    
    def test_generate_next_words(self):
        words = 'the world wide'
        guesses = oxford_language_model.Client().generate_next_words(words)
        assert len(guesses) > 0
        assert guesses[0]['word'] == 'web'
        assert guesses[0]['probability'] < 0.0
    
    def test_joint_probabilities(self):
        phrases = ["this","this is"]
        guesses = oxford_language_model.Client().joint_probabilities(phrases)
        assert len(guesses) == 2
        assert guesses[0]['words'] == 'this'
        assert guesses[0]['probability'] > guesses[1]['probability']
    
    def test_conditional_probabilities(self):
        prior = "the world wide"
        posts = ["web", "wizard"]
        guesses = oxford_language_model.Client().conditional_probabilities(prior, posts)
        assert len(guesses) == 2
        assert guesses[0]['probability'] > guesses[1]['probability']
        assert guesses[0]['words'] == 'the world wide'
        assert guesses[0]['word'] == 'web'
    
if __name__ == '__main__':
    unittest.main()
    