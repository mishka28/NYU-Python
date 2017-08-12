#!/usr/bin/env python3

import unittest
from shapes import Triangle




class TestTriangle(unittest.TestCase):
	def setUp(self):
		self.test_shapes = Triangle(2 / (3**0.25))
	def testarea(self):
		self.assertAlmostEqual(self.test_shapes.area(),1)
		return "area tested fine"
	def testperimeter(self):
		self.assertAlmostEqual(self.test_shapes.perimeter(),(6 / (3**0.25)))
	def testupdateEL(self):
		self.assertNotAlmostEqual(self.test_shapes.update_edge_length(3),(6 / (3**0.25)))
	def testadd_ally(self):
		self.assertAlmostEqual(self.test_shapes.add_ally("Circle"),self.test_shapes.allies)
	def testadd_enemies(self):
		self.assertAlmostEqual(self.test_shapes.add_enemies("Square"),self.test_shapes.enemies)	
	def testshape_type(self):
		self.assertAlmostEqual(type(self.test_shapes.shape_type),str)
#	def teststr(self):
#		self.assertAlmostEqual(type(self.test_shapes),"instance")	



if __name__ == '__main__':
	unittest.main()
