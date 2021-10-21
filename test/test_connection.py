import unittest
from unittest.mock import patch, ANY

from archicad.commands import UnsucceededCommandCall
from archicad.connection import ACConnection


class TestACConnection(unittest.TestCase):
    def setUp(self):
        self.prod_info_patcher = patch('archicad.connection.BasicCommands.GetProductInfo')
        self.versioning_patcher = patch('archicad.connection._Versioning')
        self.mocked_prod_info = self.prod_info_patcher.start()
        self.mocked_versioning = self.versioning_patcher.start()
        self.mocked_prod_info.return_value = [24, 2310, 'INT']
        self.mocked_versioning.return_value = type('obj', (object,), {'commands':1, 'types':2, 'utilities':3})
        
    def tearDown(self):
        self.prod_info_patcher.stop()
        self.versioning_patcher.stop()

    def test_connect_on_port(self):
        self.assertRaises(AssertionError, ACConnection.connect, 1500)
        self.assertEqual(self.mocked_prod_info.called, False)
        self.assertEqual(self.mocked_versioning.called, False)

        self.assertRaises(AssertionError, ACConnection.connect, 19722)
        self.assertEqual(self.mocked_prod_info.called, False)
        self.assertEqual(self.mocked_versioning.called, False)

        self.assertIsInstance(ACConnection.connect(19723), ACConnection)
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

        self.assertIsInstance(ACConnection.connect(19728), ACConnection)
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

        self.assertIsInstance(ACConnection.connect(19743), ACConnection)
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

        self.assertRaises(AssertionError, ACConnection.connect, 19744)

    @patch('archicad.connection.ACConnection.port_from_args')
    def test_connect_with_port_from_args(self, mocked_port_from_args):
        mocked_port_from_args.return_value = 2140
        self.assertRaises(AssertionError, ACConnection.connect)
        self.assertEqual(self.mocked_prod_info.called, False)
        self.assertEqual(self.mocked_versioning.called, False)

        mocked_port_from_args.return_value = 19722
        self.assertRaises(AssertionError, ACConnection.connect)
        self.assertEqual(self.mocked_prod_info.called, False)
        self.assertEqual(self.mocked_versioning.called, False)

        mocked_port_from_args.return_value = 19723
        self.assertIsInstance(ACConnection.connect(), ACConnection)
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

        mocked_port_from_args.return_value = 19728
        self.assertIsInstance(ACConnection.connect(), ACConnection)
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

        mocked_port_from_args.return_value = 19742
        self.assertIsInstance(ACConnection.connect(), ACConnection)
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

        
    @patch('archicad.connection.ACConnection.port_from_args')
    def test_connect_on_default_port(self, mocked_port_from_args):
        self.assertIs(mocked_port_from_args, ACConnection.port_from_args)
        mocked_port_from_args.return_value = None

        conn = ACConnection.connect()
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)
        self.assertIsInstance(conn, ACConnection)
        self.assertEqual(conn.port, 19723)

        self.mocked_prod_info.side_effect = [
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            [24, 2310, 'INT'],
            [24, 2310, 'INT']
        ]
        conn = ACConnection.connect()
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)
        self.assertIsInstance(conn, ACConnection)
        self.assertEqual(conn.port, 19727)


        self.mocked_prod_info.side_effect = [
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            [24, 2310, 'INT'],
            [24, 2310, 'INT']
        ]
        conn = ACConnection.connect()
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)
        self.assertIsInstance(conn, ACConnection)
        self.assertEqual(conn.port, 19743)
        
        self.mocked_prod_info.side_effect = [
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall(),
            UnsucceededCommandCall()
        ]
        self.assertIsNone(ACConnection.connect())
        self.mocked_prod_info.assert_called_with()
        self.mocked_versioning.assert_called_with(24, 2310, ANY)

