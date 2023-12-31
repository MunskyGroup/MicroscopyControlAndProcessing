from source.apd import *
from source.image_emulator import TestImageEmulator, ImageEmulator2Channel,ImageEmulatorWrapper
from source.calibration import  MatrixCalibration
apd=APDSystem()
lib=APDFunctionLibrary()
numROIXYSteps=4
imagePixSizeXY = [512*numROIXYSteps, 512*numROIXYSteps]
numCellsSimulated = numROIXYSteps*numROIXYSteps*2
ROIImSize=[512,512]
emulator=ImageEmulator2Channel()
emulator.loadImageFilePath('data/core/cell_library')
emulator.setXYImageSize(ROIImSize)
emulator.setAlpha([0.,0.,0.])
emulator.simulatePositions(imagePixSizeXY, numCellsSimulated)
emulator=ImageEmulatorWrapper(system=emulator,isCached=False)
#emulator.tryLoadCache()
calibration=MatrixCalibration()
calibration.setMatrix([[512,0],[0,512]])
calibration.setZero([0,0])
xROIRange=range(numROIXYSteps-1)
yROIRange=range(numROIXYSteps-1)
xyROIOrigin=[0,0]
apdFunction=lib.findTranscriptionSitesInGrid(xROIRange,yROIRange,xyROIOrigin,ROIImSize,threshold=200,channels=['Channel',['Cy5', 'DAPI'],[100.,100.]],
laserIntensityRGBV=[6.,1.,5.,0.],zRange=None,timeRange=[2,1.],emulator=emulator,calibration=calibration)
apd.runFunction(apdFunction)
#emulator.saveCache()