# Illumina Run Parameters Grabber
This tool is a script used to extract the consumable information for an Illumina Sequencing run from its RunParameters.xml file. This tool is comprised of three parts; the metrics extraction script, a consumable checklist file, and a Microsoft batch file. This tool is meant for Windows computers only. Once all files are in place, you can right click on the RunParameters.xml in the run folder, select the 'Send to' option, then RPGv2.bat. This will open a command prompt window while running. Once completed, the data is saved directly to the clipboard for immediate pasting.


https://github.com/dmatica/run-parameters-grabber/assets/4794041/eba6110c-c989-4fb9-9efc-f2a42ad36a9a


The extraction script (rpg_v2.py) reads the RunParameters.xml file to grab the Run ID, the consumables used, and for each consumable grabs the serial and lot numbers, and tells whether the consumable was expired at the time the run was started. For MiniSeq, NextSeq 500/550, and NovaSeq 6000 runs, it will tell whether custom primers were used, and will indicate whether a NovaSeq 6000 run was in Standard or XP mode.

This python script was also compiled into an executable as an alternative for those without python installed on their computer.

## Installation instructions
First, download the following files:
1. Extraction script: RPG_v2.py or RPG_v2.exe
2. Batch file: RPG_v2.bat
3. Consumable reference file: RPG_bom.csv

Next, save the extraction script and comsumable reference files to C:\Illumina_Resources. We'll then want to open a File Explorer window, and in the address bar, type in 'shell:sendto'. We're going to place the RPG_v2.bat file there. Once we do this, we should be able to access this script by right clicking on a RunParameters.xml file and then navigating down to the 'Send to' option.
