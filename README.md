The tool has been developed for the purpose of facilitating the forensic aspects of logging configurations. 
It enables users to customize their logging environment by specifying parameters such as file names and directory structures.

To use logging-forensic install the modul via pip

# install logging-forensic via pip
````
pip install git+https://github.com/fackelm2/logging-forensic.git
````

# update logging_setup via pip
````
pip install --upgrade --force-reinstall git+https://github.com/fackelm2/logging-forensic.git
````

# example usage of logger_setup:
````
from logging-forensic import logger_setup

timestring = time.strftime("%Y%m%d-%H%M%S")
logfile_path = Path(__file__).resolve().parent.parent / "log" / f"{timestring}_pythonscript.log"
logger = logger_setup('pythonscript', logfile_path, 'INFO', False)
````

