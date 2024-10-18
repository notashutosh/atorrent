import unittest
from atorrent.main import main
from unittest.mock import patch
import sys


class TestMain(unittest.TestCase):
    @patch('builtins.print')
    def test_start(self, mock_print):
        test_args = ['atorrent', 'start']
        with patch.object(sys, 'argv', test_args):
            main()
        mock_print.assert_called_with("Starting torrent...")

    @patch('builtins.print')
    def test_stop(self, mock_print):
        test_args = ['atorrent', 'stop']
        with patch.object(sys, 'argv', test_args):
            main()
        mock_print.assert_called_with("Stopping torrent...")

    @patch('builtins.print')
    def test_status(self, mock_print):
        test_args = ['atorrent', 'status']
        with patch.object(sys, 'argv', test_args):
            main()
        mock_print.assert_called_with("Torrent status...")


if __name__ == '__main__':
    unittest.main()
