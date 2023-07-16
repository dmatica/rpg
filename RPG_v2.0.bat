rem : name = Run Parameters Grabber
rem : version = 2.0
rem : author = Davinder Sandhu
rem : date = 30-JUN-2023
@echo off
cls
ECHO Running Run Parameters Grabber v2.0
ECHO by Davinder Sandhu
ECHO Please do not close.
rem : Edit this line below with the correct location of the RPG_v2.0.exe and RPG_bom.csv files
C:\Illumina_Resources\RPG_v2.0.exe %1 C:\Illumina_Resources\RPG_bom.csv
rem : Remove 'rem' from the line below to debug if you encounter an error
rem pause