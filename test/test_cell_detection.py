import unittest
from cell_detection import *
import data_manager
import globals
import os
class TestCellDetectorThreshold(unittest.TestCase):
    def testDomain(self):
        g=globals.Globals()
        detector=CellDetectorThreshold()
        detector.threshold=2000
        dmanager=data_manager.DataManager()
        dmanager.storage=data_manager.DataStorageLocal(folder=os.path.join('data','test'))
        image=dmanager.load('testimage.jpg')
        detector.detect(image)
        pass
    def testInterface(self):
        detector = CellDetectorThreshold()
        detector.detect
    def testAcceptance(self):
        #todo
        pass

class TestCellMaskHistogramThreshold(unittest.TestCase):
    def testDomain(self):
        detector = CellDetectHistogramThreshold()
        detector.threshold = 2000
        dmanager = data_manager.DataManager()
        dmanager.storage = data_manager.DataStorageLocal(folder=os.path.join('data','test'))
        image = dmanager.load('testimage.jpg')
        detector.detect(image)
        pass
    def testInterface(self):
        detector = CellMaskCellpose()
        detector.detect
        pass
    def testAcceptance(self):
        # todo
        pass


class TestCellDetectorCellpose(unittest.TestCase):
    def testDomain(self):
        detector = CellDetectorCellpose(dims=(32,32))
        detector.threshold = 2000
        dmanager = data_manager.DataManager()
        dmanager.storage = data_manager.DataStorageLocal(folder=os.path.join('data','test'))
        image = dmanager.load('testimage.jpg')
        detector.detect(image)
        pass
    def testInterface(self):
        # todo
        detector=CellDetectorCellpose()
        detector.detect
        pass
    def testAcceptanece(self):
        # todo
        pass


class TestCellMaskCellpose(unittest.TestCase):
    def testDomain(self):
        detector = CellMaskCellpose(dims=(32,32))
        detector.threshold = 2000
        dmanager = data_manager.DataManager()
        dmanager.storage = data_manager.DataStorageLocal(folder=os.path.join('data','test'))
        image = dmanager.load('testimage.jpg')
        detector.detect(image)
        pass
    def testInterface(self):
        # todo
        detector=CellMaskCellpose()
        detector.detect
        pass
    def testAcceptanece(self):
        # todo
        pass
