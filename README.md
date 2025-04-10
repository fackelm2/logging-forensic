The tool has been developed for the purpose of facilitating the forensic aspects of logging configurations. 
<br>
It enables users to easy customize their logging environment by specifying 
parameters such as file names and directory structures.
<br>
For example you can easy configure your logging with the logging-directory <casenumber> and 
the name of the logging file <date>_<casenumber>.log
<br>
To use logging-forensic install the modul via pip and use it (see example usage)

# install logging-forensic via pip
````
pip install git+https://github.com/fackelm2/logging-forensic.git
````

# update logging-forensic via pip
````
pip install --upgrade --force-reinstall git+https://github.com/fackelm2/logging-forensic.git
````

# example usage of logger-forensic in your python script:
````
from logging-forensic import forensic_logger

timestring = time.strftime("%Y%m%d-%H%M%S")
logfile_path = Path(__file__).resolve().parent.parent / "log" / f"{timestring}_<case>.log"
logger = forensic_logger('<scriptname>', logfile_path, 'INFO', False)
````

# example logfile in log/<scriptname>.log


# example 2

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
cat log/my-script.log
````
..
2025-04-09 17:48:38,712 - INFO - my-script.py OK - downloaded file 1: https://apkid.de/test1.txt to D:\download_data\output\download_20250409174838
2025-04-09 17:48:39,081 - INFO - my-script.py OK - downloaded file 2: https://apkid.de/wallpaper_16487800940ff7b95bc63e4c56a8843b2c50d3b0de.jpeg to D:\download_data\output\download_20250409174838
..
````
