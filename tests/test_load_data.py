import unittest
import pandas as pd
from unittest.mock import patch, mock_open
from io import StringIO
from scripts.load_data import Load_Data  # Replace 'your_module' with the actual module name

class TestLoadData(unittest.TestCase):
    
    @patch('pandas.read_excel')
    def test_load_data_success(self, mock_read_excel):
        # Mock the read_excel function to return a DataFrame
        mock_read_excel.return_value = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        
        loader = Load_Data('test.xlsx')
        loader.load_data()
        
        self.assertIsNotNone(loader.data)
        self.assertEqual(loader.data.shape, (2, 2))
        print("test_load_data_success passed")
    
    @patch('pandas.read_excel')
    def test_load_data_file_not_found(self, mock_read_excel):
        # Mock the read_excel function to raise FileNotFoundError
        mock_read_excel.side_effect = FileNotFoundError
        
        loader = Load_Data('non_existent_file.xlsx')
        loader.load_data()
        
        self.assertIsNone(loader.data)
        print("test_load_data_file_not_found passed")
    
    @patch('pandas.read_excel')
    def test_load_data_empty_data_error(self, mock_read_excel):
        # Mock the read_excel function to raise EmptyDataError
        mock_read_excel.side_effect = pd.errors.EmptyDataError
        
        loader = Load_Data('empty_file.xlsx')
        loader.load_data()
        
        self.assertIsNone(loader.data)
        print("test_load_data_empty_data_error passed")
    
    @patch('pandas.read_excel')
    def test_load_data_parser_error(self, mock_read_excel):
        # Mock the read_excel function to raise ParserError
        mock_read_excel.side_effect = pd.errors.ParserError
        
        loader = Load_Data('corrupt_file.xlsx')
        loader.load_data()
        
        self.assertIsNone(loader.data)
        print("test_load_data_parser_error passed")
    
    @patch('pandas.read_excel')
    def test_load_data_unicode_decode_error(self, mock_read_excel):
        # Mock the read_excel function to raise UnicodeDecodeError
        mock_read_excel.side_effect = UnicodeDecodeError('utf-8', b"", 0, 1, 'reason')
        
        loader = Load_Data('unicode_error_file.xlsx')
        loader.load_data()
        
        self.assertIsNone(loader.data)
        print("test_load_data_unicode_decode_error passed")

if __name__ == '__main__':
    unittest.main()
