import unittest
from app.models import Source


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources Class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_source=Source('123movies','123 Movies','lorem picsum','https://blahblahblah','madtings','patois','jm')


    def test_instance(self):

        self.assertTrue(isinstance(self.new_source,Source))


         
