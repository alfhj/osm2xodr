from math import floor, pi
import numpy as np
from OSMParser.testing import TestEntity, _test_nodes, testSimpleRoad, test_3WayTCrossing2
from OSMParser.osmParsing import parseAll,rNode, OSMWay,JunctionRoad, OSMWayEndcap, createOSMJunctionRoadLine, createOSMWayNodeList2XODRRoadLine
from OSMParser.xodrWriting import startBasicXODRFile,fillNormalRoads,fillJunctionRoads

osmPfad = '/mnt/chromeos/GoogleDrive/MyDrive/AI/Masteroppgave/Kode/Notebooks/gloshaugen.osm'
topographieKartenPfad = '/mnt/chromeos/GoogleDrive/MyDrive/AI/Masteroppgave/Kode/Notebooks/hoyde.png'
xodrPfad = '/mnt/chromeos/GoogleDrive/MyDrive/AI/Masteroppgave/Kode/Notebooks/gloshaugen.xodr'

parseAll(osmPfad, bildpfad=topographieKartenPfad, minimumHeight = 0.0, maximumHeight= 80.07621, curveRadius=12)
startBasicXODRFile(xodrPfad)
fillNormalRoads(xodrPfad)
fillJunctionRoads(xodrPfad)

