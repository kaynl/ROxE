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
## Physical Architecture Blanks
PAB = model.diagrams.by_name('[PAB] ROLEX')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB.svg', 'w').write(PAB.as_svg)
PABVCS = model.diagrams.by_name('[PAB] VCS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-VCS.svg', 'w').write(PABVCS.as_svg)
PABOSS = model.diagrams.by_name('[PAB] OSS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-OSS.svg', 'w').write(PABOSS.as_svg)
PABRIS = model.diagrams.by_name('[PAB] RIS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-RIS.svg', 'w').write(PABRIS.as_svg)
PABPCM = model.diagrams.by_name('[PAB] PCM')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/PAB-PCM.svg', 'w').write(PABPCM.as_svg)

## Component Breakdown
CBD_RIS = model.diagrams.by_name('[PCBD] RIS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/CBD_RIS.svg', 'w').write(CBD_RIS.as_svg)
CBD_VCS = model.diagrams.by_name('[PCBD] VCS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/CBD_VCS.svg', 'w').write(CBD_VCS.as_svg)
CBD_ORSS = model.diagrams.by_name('[PCBD] ORSS')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/CBD_ORSS.svg', 'w').write(CBD_ORSS.as_svg)
CBD_PMC = model.diagrams.by_name('[PCBD] PMC')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/CBD_PMC.svg', 'w').write(CBD_PMC.as_svg)

## Root Physical Functions
FBD_F1 = model.diagrams.by_name('[PFBD] F1 - Produce Oxygen from Regolith')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/FBD_F1.svg', 'w').write(FBD_F1.as_svg)
FBD_F2 = model.diagrams.by_name('[PFBD] F2 - Support Oxygen Production and Storage')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/FBD_F2.svg', 'w').write(FBD_F2.as_svg)
FBD_F3 = model.diagrams.by_name('[PFBD] F3 - Control Process')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/FBD_F3.svg', 'w').write(FBD_F3.as_svg)
FBD_F4 = model.diagrams.by_name('[PFBD] F4 - Monitor Process')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/FBD_F4.svg', 'w').write(FBD_F4.as_svg)
FBD_F5 = model.diagrams.by_name('[PFBD] F5 - Handle Electrical Power')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/FBD_F5.svg', 'w').write(FBD_F5.as_svg)
FBD_F6 = model.diagrams.by_name('[PFBD] F6 - Survive Environmental Conditions')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/FBD_F6.svg', 'w').write(FBD_F6.as_svg)

## State Machines
MSM = model.diagrams.by_name('[MSM] Operational State')
open('/home/runner/work/ROxE/ROxE/Model-SVG/PA/MSM.svg', 'w').write(MSM.as_svg)
