import unittest
from unittest.mock import patch
from datetime import datetime, time, timezone
from backend.market import Market


class TestMarket(unittest.TestCase):
    def setUp(self):
        # Create a market that is open from 9:00 to 17:00 UTC
        self.market = Market()
        self.market._timeOpen = time(9, 0, 0)
        self.market._timeClose = time(17, 0, 0)

    @patch('backend.market.datetime')
    def test_isOpen_open(self, mock_datetime):
        # Mock datetime to return 12:00 UTC
        mock_datetime.now.return_value = datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        self.assertTrue(self.market.isOpen())

    @patch('backend.market.datetime')
    def test_isOpen_closed(self, mock_datetime):
        # Mock datetime to return 20:00 UTC
        mock_datetime.now.return_value = datetime(2023, 1, 1, 20, 0, 0, tzinfo=timezone.utc)
        self.assertFalse(self.market.isOpen())