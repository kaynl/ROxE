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
LFBD = model.diagrams.by_name('[LFBD] Root Logical Function')
open('/home/runner/work/ROxE/ROxE/Model-SVG/LA/LFBD-Logical System.svg', 'w').write(LFBD.as_svg)
LCBD = model.diagrams.by_name('[LCBD] Logical System')
open('/home/runner/work/ROxE/ROxE/Model-SVG/LA/LCBD-Logical System.svg', 'w').write(LCBD.as_svg)

## Creation of Physical Architecture Document

PAB = model.diagrams.by_name('[PAB] Physical System')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB.svg', 'w').write(PAB.as_svg)
PABRPORS = model.diagrams.by_name('[PAB] RPORS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-RPORS.svg', 'w').write(PABRPORS.as_svg)
PABOSS = model.diagrams.by_name('[PAB] OSS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-OSS.svg', 'w').write(PABOSS.as_svg)
PABRIS = model.diagrams.by_name('[PAB] RIS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-RIS.svg', 'w').write(PABRIS.as_svg)
PABPCM = model.diagrams.by_name('[PAB] PCM')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-PCM.svg', 'w').write(PABPCM.as_svg)

