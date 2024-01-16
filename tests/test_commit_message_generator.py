import unittest
from unittest.mock import patch, MagicMock
from src import generate_commit_message  

class TestCommitMessageGenerator(unittest.TestCase):

    def setUp(self):
        # Set up any initial variables or configurations you need
        self.diff = 'diff --git a/file.txt b/file.txt\nnew file mode 100644\nindex 0000000..e69de29'
        self.app_type = 'Python'
        self.api_key = 'test_api_key'

    @patch('requests.post')
    def test_generate_commit_message(self, mock_post):
        # Mocking the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': 'Add a new Python file to improve XYZ feature.'
                }
            }]
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        # Call the function you are testing
        commit_message = generate_commit_message(self.diff)

        # Assertions to check if the results are as expected
        self.assertIsNotNone(commit_message)
        self.assertEqual(commit_message, 'Add a new Python file to improve XYZ feature.')

        # Check if API was called correctly
        mock_post.assert_called_once()
        _, kwargs = mock_post.call_args
        self.assertIn('json', kwargs)
        self.assertEqual(kwargs['json']['model'], 'gpt-3.5-turbo')
        self.assertIn('Authorization', kwargs['headers'])
        self.assertTrue(kwargs['headers']['Authorization'].startswith('Bearer'))


if __name__ == '__main__':
    unittest.main()