# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2017 replay file
# Internal Version: 2016_09_27-17.54.59 126836
# Run by djj5138 on Fri Apr  3 13:49:30 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=201.214889526367, 
    height=194.867599487305)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName='/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/model.cae')
#: The model database "/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/model.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].loads['Load-1'].resume()
mdb.models['Model-1'].boundaryConditions['BC-2'].resume()
mdb.models['Model-1'].boundaryConditions['BC-3'].resume()
mdb.models['Model-1'].loads['Load-1'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
import sys
sys.path.insert(13, 
    r'/opt/aci/sw/abaqus/2017/CAE/linux_a64/code/python2.7/lib/abaqus_plugins/amplitudePlotter')
import amplitudeTools
amplitudeTools.plotAmplitudes(amplitudeNameList=(('Amp-1', ), ), needXmin=0, 
    needXmax=0, needSaveXYPlot=0, displayLegend=1, applySmoothingFactor=0)
session.viewports['Viewport: 1'].makeCurrent()
del session.viewports['Viewport: Amplitude Plotter']
del session.xyPlots['Amplitude Plotter-1']
del session.xyDataObjects['_temp_ap_Amp-1']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb')
#: Model: /storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.animationOptions.setValues(frameRate=53)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=SHADED)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=FEATURE)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=EXTERIOR)
session.animationController.stop()
session.animationController.showLastFrame()
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.animationController.play(duration=UNLIMITED)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.animationController.stop()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=0.0125, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.save()
#: The model database has been saved to "/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/model.cae".
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb')
#: Model: /storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.stop()
session.animationController.showLastFrame()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=0.0025, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb')
#: Model: /storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
session.animationController.setValues(animationType=NONE)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = mdb.models['Model-1'].parts['Part-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Part-1']
p.deleteSeeds()
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=0.025, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
f = p.faces
p.assignStackDirection(referenceRegion=f[4], cells=pickedCells)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
p = mdb.models['Model-1'].parts['Part-1']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Part-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=0.025, deviationFactor=0.1, 
    minSizeFactor=0.1, constraint=FINER)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
odb = session.odbs['/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Explicit Packager completed successfully.
#: Job Job-1: Abaqus/Explicit completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb')
#: Model: /storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          5
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
    'Viewport: 1', ))
session.animationController.play(duration=UNLIMITED)
mdb.save()
#: The model database has been saved to "/storage/work/d/djj5138/classes/me563/flagshyp/job_folder/explicit_100elt_3D/abaqus/model.cae".
