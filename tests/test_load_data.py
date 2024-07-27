import unittest
import pandas as pd
from data.load_data import load_data

class TestLoadData(unittest.TestCase):

    def test_load_data(self):
        file_path = '/Users/jagatchaitanya/Desktop/vishruti/bidding-simulation/data/FPSBA_merged.xlsx'
        data = load_data(file_path)
        
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIn('auction_id', data.columns)
        self.assertIn('optimal_bid', data.columns)

if __name__ == '__main__':
    unittest.main()