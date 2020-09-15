import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Jack Healy, Jack Nicas and Mike Baker','Firefighters continued to battle blazes along the West Coast that have now charred nearly five million acres. At least 17 people are dead, with dozens still missing','2020-09-12T00:32:15.000Z','https://www.nytimes.com/2020/09/11/us/fires-oregon-california-washington.html?action=click&module=Spotlight&pgtype=Homepage','https://static01.nyt.com/images/2020/09/11/us/11wildfires-oregon02/11wildfires-oregon02-facebookJumbo.jpg','A Line of Fire South of Portland and a Yearslong Recovery Ahead')

    def test_instance(self):
        '''
        Test to check creation of new article instance
        '''
        self.assertTrue(isinstance(self.new_article,Article))
    
