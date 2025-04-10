The tool has been developed for the purpose of facilitating the forensic aspects of logging configurations. 
<br>
It enables users to easy customize their logging environment by specifying 
parameters such as file names and directory names.
As the process of developing the tool progressed, it became evident that the directory 
constitutes the optimal definition within the program, given its utilization of 
logging-forensic capabilities.
<br>
To illustrate, the configuration of logging can be facilitated through the utilization of the 
logging-directory named as the casenumber (for example "2502214") 
and the designation of the logging file "date_casenumber.log" (for example "2025-04-19_2502214.log").
<br>
The implementation of the logging-forensic module necessitates its installation via pip, 
followed by its utilization, as outlined in the provided example.

# install logging-forensic via pip
````
pip install git+https://github.com/fackelm2/logging-forensic.git
````

# update logging-forensic via pip
````
pip install --upgrade --force-reinstall git+https://github.com/fackelm2/logging-forensic.git
````

# example: Use logger-forensic in your python script
````
from logging-forensic import forensic_logger

timestring = time.strftime("%Y%m%d-%H%M%S")
logfile_path = Path(__file__).resolve().parent.parent / "log" / f"{timestring}_<case>.log"
logger = forensic_logger('<scriptname>', logfile_path, 'INFO', False)
````

# example: how to write logfile in file "log/my-script.log"
cat my-script.py
````
..
from logging_forensic import forensic_logger
..
logfile_path = Path(__file__).resolve().parent.parent / 'log' / f'my-script.log'
logfile_path.parent.mkdir(parents=True, exist_ok=True)
logger = forensic_logger('my-script', logfile_path, console=False, level='INFO', timestamp=True)
..
````
# see output in logfile:
cat log/my-script.log
````
..
2025-04-09 17:48:38,712 - INFO - my-script.py OK - downloaded file 1: https://apkid.de/test1.txt to D:\download_data\output\download_20250409174838
2025-04-09 17:48:39,081 - INFO - my-script.py OK - downloaded file 2: https://apkid.de/wallpaper_16487800940ff7b95bc63e4c56a8843b2c50d3b0de.jpeg to D:\download_data\output\download_20250409174838
..
````
