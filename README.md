
# Adapting the logging mechanism to meet forensic requirements 
The objective of the tool is to augment Python's prevailing logging mechanism 
to facilitate **case-based** logging.

The implementation of this tool involves the creation of a distinct log file 
for each forensic case, with the option of directing this within a user-defined 
directory if needed.
This approach facilitates the establishment of a clear separation and traceability 
of log data per investigation unit. 

The implementation of this tool is contingent upon the following requirements:
<ul>
    <li> Case-based log structure: Automated creation of a dedicated log file per case</li>    
    <li> User-defined path: The possibility to define file and folder structure by case name</li>
    <li> The system must also be compatible with Python logging (Utilisation and extension of the logging module) </li>  
</ul>

The overarching objective is to facilitate the seamless integration of the logging 
functionality with the Python framework, 
thereby ensuring optimal performance and interoperability. 
The forensically traceable nature of the separate log data is conducive 
to the clean documentation of individual analysis cases.

It is imperative to exercise caution when utilising file and folder names, 
ensuring that character validation is meticulously adhered to 
(e.g. refrain from the utilisation of Windows reserved characters).

The following sources have been consulted:
<ul>
<li> The Python logging documentation can be found here: https://docs.python.org/3/library/logging.html </li>
</ul>

The translation was carried out using the DeepL.com free version.


# Installation and usage of the logging-forensic module
To illustrate, the configuration of logging can be facilitated through the utilization 
of the logging-directory named as the case-name (for example "2502214") 
and the designation of the logging file "date_casenumber.log" 
(for example "2025-04-19_2502214.log").

The implementation of the logging-forensic module necessitates its installation via pip, 
followed by its utilization, as outlined in the provided example.

## Install logging-forensic via pip
````
pip install git+https://github.com/fackelm2/logging-forensic.git
````

## Update logging-forensic via pip
````
pip install --upgrade --force-reinstall git+https://github.com/fackelm2/logging-forensic.git
````

## How to use logger-forensic in your python script
````
.. 
from logging-forensic import forensic_logger
.. 

timestring = time.strftime("%Y%m%d-%H%M%S")
logfile_path = Path(__file__).resolve().parent.parent / "log" / f"{timestring}_<case>.log"
logger = forensic_logger('<scriptname>', logfile_path, 'INFO', False)
````

### Example script named "forensic-download.py"
cat forensic-download.py
````
..
from logging_forensic import forensic_logger
..
logfile_path = Path(__file__).resolve().parent.parent / 'log' / f'forenisc-download.log'
logfile_path.parent.mkdir(parents=True, exist_ok=True)
logger = forensic_logger('forensic-download', logfile_path, console=False, level='INFO', timestamp=True)
..
````
## Logfile (with logging-forensic)
Logfile (default) will be written to: "log/forensic-download.log"

````
$> cat log/forensic-download.log
..
2025-04-09 17:48:38,712 - INFO - forensic-downlaod.py OK - downloaded file 1: https://apkid.de/test1.txt to D:\download_data\output\download_20250409174838
2025-04-09 17:48:39,081 - INFO - forensic-download.py OK - downloaded file 2: https://apkid.de/wallpaper_16487800940ff7b95bc63e4c56a8843b2c50d3b0de.jpeg to D:\download_data\output\download_20250409174838
..
````