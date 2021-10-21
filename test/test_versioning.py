import unittest
from unittest.mock import patch, ANY

from archicad.versioning import _Versioning, os, importlib


class TestVersioning(unittest.TestCase):
    @patch('archicad.versioning._Versioning.load')
    def test_init(self, mocked_load):
        self.assertRaises(AssertionError, _Versioning, -24, 2310, ANY)
        self.assertRaises(AssertionError, _Versioning, 0, 2310, ANY)
        self.assertRaises(AssertionError, _Versioning, 23, 2310, ANY)
        self.assertIsInstance(_Versioning(24, 2310, ANY), _Versioning)
        self.assertIsInstance(_Versioning(50, 2310, ANY), _Versioning)

    @patch('archicad.versioning.importlib.import_module')
    @patch('archicad.versioning._Versioning.discover')
    def test_load(self, mocked_discover, mocked_import_module):
        self.assertIs(mocked_discover, _Versioning.discover)
        self.assertIs(mocked_import_module, importlib.import_module)
        
        def types():
            return 'Imported Types' 
        def commands(request):
            return 'Imported Commands' 
        def utils(types, commands):
            return 'Imported Utilities' 
        import_module_side_effect = [
            type('obj', (object,), {'Types': types}),
            type('obj', (object,), {'Commands': commands}),
            type('obj', (object,), {'Utilities': utils})
        ]
        mocked_discover.return_value = [25, 2310]
        mocked_import_module.side_effect = import_module_side_effect

        test_version = _Versioning(25, 2320,ANY)

        self.assertEqual(test_version.types, 'Imported Types')
        self.assertEqual(test_version.commands, 'Imported Commands')
        self.assertEqual(test_version.utilities, 'Imported Utilities')

    @patch('archicad.versioning.importlib.import_module')
    @patch('archicad.versioning.os.scandir')
    def test_discover(self, mocked_os_scandir, mocked_import_module):
        self.assertIs(mocked_import_module, importlib.import_module)
        self.assertIs(mocked_os_scandir, os.scandir)

        def returnTrue():
            return True
        mocked_os_scandir.return_value = None
        mocked_import_module.return_value = type('obj', (object,), {'__path__':['random_path_string',]})
        
        os_scandir_side_effect_values = [[
                type('obj', (object,), {'name':'ac25', 'is_dir': returnTrue}),
                type('obj', (object,), {'name':'ac24', 'is_dir': returnTrue}),
                type('obj', (object,), {'name':'ac30', 'is_dir': returnTrue}),
                type('obj', (object,), {'name':'ac27', 'is_dir': returnTrue}),
                type('obj', (object,), {'name':'ac26', 'is_dir': returnTrue})
            ], [
                type('obj', (object,), {'name':'b2300commands', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2300types', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2300utilities', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2310commands', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2310types', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2310utilities', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2305commands', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2305types', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b2305utilities', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b1610commands', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b1610types', 'is_file': returnTrue}),
                type('obj', (object,), {'name':'b1610utilities', 'is_file': returnTrue}),
            ]
        ]
        
        mocked_os_scandir.side_effect = os_scandir_side_effect_values
        release, build = _Versioning.discover(53, 7000)
        self.assertEqual(release, 30)
        self.assertEqual(build, 2310)
        
        mocked_os_scandir.side_effect = os_scandir_side_effect_values
        release, build = _Versioning.discover(27, 2306)
        self.assertEqual(release, 27)
        self.assertEqual(build, 2305)
        
        mocked_os_scandir.side_effect = os_scandir_side_effect_values
        release, build = _Versioning.discover(28, 1610)
        self.assertEqual(release, 27)
        self.assertEqual(build, 2310)
        
        mocked_os_scandir.side_effect = os_scandir_side_effect_values
        self.assertRaises(StopIteration, _Versioning.discover, 23, 2300)
        
        mocked_os_scandir.side_effect = os_scandir_side_effect_values
        self.assertRaises(StopIteration, _Versioning.discover, 24, 1500)
        
