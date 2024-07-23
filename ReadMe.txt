PilotLogic.py

## Table of Contents
1. Introduction
2. Features
3. Installation/Usage
4. Author


1. Introduction: This is a prototype for Iowa State University that uses drone pilot's information (certification, flight hours
and simulation hours) to create a safety case to determine whether it is safe for them to start their mission. There are many
safety cases related to weather, drone history, mission, and airspace, but this program just focuses on the pilot. The output
argument files are named based on the pilot's ID, and is read through NASA's program called advoCATE. An example of a fully
filled argument file ran through advoCATE can be seen under 'PilotSafetyCase_Argument.jpg'.

2. Features:
    - "Config File Mode": If a pilot configuration file, 'pilotConfig.YAML' is found, it will automatically run and create the corresponding
    argument files.
    - "Manual Mode": If 'pilotConfig.YAML' is not found in the project directory, it will enter manual mode where you can
    manually enter each pilot's information

3. Installation/Usage: This program is run through a Windows terminal. In the directory of the 'pilotLogic.py', simply type
"python pilotLogic.py" and it will run in the mode based if it can find 'pilotConfig.YAML'.

4. Author: Written by Piper Ideker
