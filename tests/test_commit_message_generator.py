import unittest
from unittest.mock import patch, Mock
from src import commit_message_generator 

class TestScript(unittest.TestCase):

    @patch('your_script_name.os.getenv')
    @patch('your_script_name.requests.post')
    def test_generate_commit_message(self, mock_post, mock_getenv):
        # Setup the environment variable
        mock_getenv.return_value = 'test_app_type'
        
        # Mock the API response
        mock_response = Mock()
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'Test commit message'}}]
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response
        
        # Call the function with a dummy diff
        result = commit_message_generator.generate_commit_message('dummy diff')
        
        # Assertions
        self.assertEqual(result, 'Test commit message')
        mock_post.assert_called_once()
        mock_getenv.assert_called_with('OPENAI_API_KEY')

    @patch('your_script_name.subprocess.check_output')
    def test_get_staged_diff(self, mock_check_output):
        # Mock the subprocess output
        mock_check_output.return_value = 'dummy diff output'

        # Call the function
        result = commit_message_generator.get_staged_diff()

        # Assertions
        self.assertIsInstance(result, str)
        mock_check_output.assert_called_with(['git', 'diff', '--cached'], text=True)

    @patch('your_script_name.subprocess.check_output')
    def test_commit_changes(self, mock_check_output):
        # Call the function with a dummy commit message
        commit_message_generator.commit_changes('Test commit message')

        # Assertions
        mock_check_output.assert_called_with(['git', 'commit', '-m', 'Test commit message'])


if __name__ == '__main__':
    unittest.main()