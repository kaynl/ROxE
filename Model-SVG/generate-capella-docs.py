# Code for automated generation of svg files


import capellambse
#import pandas as pd

path_to_model = "/home/runner/work/ROxE/ROxE/RegolithO2ExtractionDemonstrator/RegolithO2ExtractionDemonstrator.aird"
model = capellambse.MelodyModel(path_to_model)
model

#!pip install -q pandas openpyxl

## Creation of Operational Analysis Document

OAB = model.diagrams.by_name('[OAB] Operational Context')
open('/home/runner/work/ROxE/ROxE/Model-SVG/OA/OAB.svg', 'w').write(OAB.as_svg)

## Creation of System Analysis Documents

SAB1 = model.diagrams.by_name('[SAB] O2Extractor - SF 1st level')
SAB2 = model.diagrams.by_name('[SAB] O2Extractor - SF 2nd level')

open('/home/runner/work/ROxE/ROxE/Model-SVG/SA/SAB_HLF.svg', 'w').write(SAB1.as_svg)
open('/home/runner/work/ROxE/ROxE/Model-SVG/SA/SAB_LLF.svg', 'w').write(SAB2.as_svg)

## Creation of Logical Architecture Document

LAB = model.diagrams.by_name('[LAB] Logical System')
open('/home/runner/work/ROxE/ROxE/Model-SVG/LA/LAB-Logical System.svg', 'w').write(LAB.as_svg)
