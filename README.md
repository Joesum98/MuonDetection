# MuonDetection
Take in data from TASD and create 3 different kinds of plots:
1.) Average energy deposited vs incident energy
2.) # of triggers vs Energy Deposited (for a specific energy bin)
3.) Energy deposit distribution

Instructions:

1.) Average energy deposit VS incident energy
        Put all simulation data of energy bins in a single folder.
        Each data file should be named simply the incident energy (e.g. a file with data from a -ke 10 simulation should be         named 10MeV or a -ke 10000 could be named 10GeV as code ignores any non-numeric characteres).
        Set the "folderPath" equal to the folders path followed by /*.txt.
        Change plt.title to the appropriate title, as well as the units on the x and y axes (MeV or GeV)
        If the point (0,0) is needed, it can be uncommented
        
        
2.) Bar graphs for # of triggers VS Energy Deposited
        Must be run on a single energy bin file.
        Set "filePath" equal to the path of the file.
        Set title and x/y axis units.
          Can also change units of average displayed on graph on lines 101 & 102
          
          
3.) Energy Distribuition Plots
        Must be run on a single energy bin file.
        Set "filePath" equal to the path of the file.
        Set title and x/y axis units.
        
        
Notes:
    For the "listAverage(ent, tob)" function, 'ent' should be a string of the energy value and 'tob' is for the "Top Or Bottom" scinitlator; either a 0, for top, or a 1, for bottom.


IMPORTANT:
    In order for the DataFile objects to be created properly, I had to ignore the numerical digits that were present in my path string (had to ignore 6 digits present in string so [6:] present at the end of line 6). Line 6 of dataFile.py should be changed according to your specific path file string.
