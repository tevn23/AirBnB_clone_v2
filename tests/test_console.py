#!/usr/bin/python3
""""""
import unittest
import sys
import os
import cmd
from models import storage
from io import StringIO
from unittest.mock import patch, create_autospec
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User

class test_Console(unittest.TestCase):

	def setUp(self):
		self.console = HBNBCommand()
		self.mock_stdout = StringIO()

	def tearDown(self):
		try:
			os.remove("file.json")
		except FileNotFoundError:
			pass

	def test_do_create(self):
		#Test case for invalid input passed
		with patch("sys.stdout", self.mock_stdout):
			self.console.onecmd("create User =invalid_input= name=\"tevn23\"")
			self.console.onecmd("show User {}".format(self.mock_stdout.getvalue().strip()))
			self.assertIn("'name': 'tevn23'", self.mock_stdout.getvalue().strip())
			self.assertNotIn("=invalid_input=", self.mock_stdout.getvalue().strip())
		self.mock_stdout.truncate(0)
		self.mock_stdout.seek(0)

		# Test case for string input
		with patch("sys.stdout", self.mock_stdout):
			self.console.onecmd('create User name="tevn23_and_frank"')
			output = self.mock_stdout.getvalue().strip()
			self.assertTrue(len(output) > 0)
			self.assertTrue(isinstance(output, str))
		key = "User.{}".format(output)
		result = storage.all()[key]
		self.assertIn("tevn23 and frank", result.name)
		self.mock_stdout.truncate(0)
		self.mock_stdout.seek(0)

		# Test case for float parameter
		with patch("sys.stdout", self.mock_stdout):
			self.console.onecmd('create BaseModel price=123.45')
			output = self.mock_stdout.getvalue().strip()
			self.assertTrue(len(output) > 0)
			self.assertTrue(isinstance(output, str)) # output should be an instance of a float class (do this also for int and multiple input)
		new_instance = storage.all()["BaseModel.{}".format(output)]
		self.assertEqual(new_instance.price, 123.45) # new_instance.price is a string (do this also for int and multiple input)
		self.mock_stdout.truncate(0)
		self.mock_stdout.seek(0)

		# Test case for integer parameter
		with patch("sys.stdout", self.mock_stdout):
			self.console.onecmd('create BaseModel number=10')
			output = self.mock_stdout.getvalue().strip()
			self.assertTrue(len(output) > 0)
			self.assertTrue(isinstance(output, str))
		new_instance = storage.all()["BaseModel.{}".format(output)]
		self.assertEqual(new_instance.number, '10')
		self.mock_stdout.truncate(0)
		self.mock_stdout.seek(0)

		# Test case for string parameter containing escaped quotes
		with patch("sys.stdout", self.mock_stdout):
			self.console.onecmd('create BaseModel description="My_\\"house"')
			output = self.mock_stdout.getvalue().strip()
			self.assertTrue(len(output) > 0)
			self.assertTrue(isinstance(output, str))
		new_instance = storage.all()["BaseModel.{}".format(output)]
		self.assertEqual(new_instance.description, 'My "house')
		self.mock_stdout.truncate(0)
		self.mock_stdout.seek(0)

		# Test case for multiple parameters
		with patch("sys.stdout", self.mock_stdout):
			self.console.onecmd('create BaseModel name="My_house" price=99.99 number=2')
			output = self.mock_stdout.getvalue().strip()
			self.assertTrue(len(output) > 0)
			self.assertTrue(isinstance(output, str))
		new_instance = storage.all()["BaseModel.{}".format(output)]
		self.assertEqual(new_instance.name, "My house")
		self.assertEqual(new_instance.price, '99.99')
		self.assertEqual(new_instance.number, '2')
		self.mock_stdout.truncate(0)
		self.mock_stdout.seek(0)

if __name__ == "__main__":
    unittest.main()
