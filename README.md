
# Adapting the logging mechanism to meet forensic requirements 
A lightweight Python helper library for creating structured file-based loggers 
for forensic, analysis, and automation workflows.

logging-forensic provides a simple wrapper around Python's built-in logging module. 
It helps create consistent log files with optional timestamps, 
console output, configurable log levels, and minimal setup.

The package is designed for scripts, forensic utilities, analysis tools, 
and small applications where predictable logging behavior is required.

Features:
- Simple logger creation with one function call
- File-based logging by default
- Optional console output
- Optional timestamped log filenames
- Supports Python logging levels as strings or constants
- Automatic log directory creation
- Uses Python's standard logging module
- No external dependencies

## Details
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
functionality with the Python framework, thereby ensuring optimal performance and 
interoperability. 

If a logger with the same name already has handlers configured, the existing configuration is reused.
The forensically traceable nature of the separate log data is conducive 
to the clean documentation of individual analysis cases.
Log files are written using UTF-8 encoding and is tested with Python 3.12.

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
of the logging-directory named as the case-name (for example "0001") 
and the designation of the logging file "date_casename.log"
(for example "2026-11-01_0001.log").

The implementation of the logging-forensic module necessitates its installation via pip, 
followed by its utilization, as outlined in the provided example.

## Install logging-forensic via pip
````
pip install logging-forensic
````

## Update logging-forensic via pip
````
pip install --upgrade logging-forensic
````

## How to use logger-forensic in your python script
````
from logging_forensic import forensic_logger

logger = forensic_logger("analysis")

logger.info("Forensic analysis started")
logger.error("File hash msimatch")

````

### Logging Directory Structure - Default
project/
│
├── main.py
└── log/
    └── analyze.log

### Logging Directory Structure - Option --log-file analyselogfile.log
project/
│
├── main.py
└── log/
    └── analyselogfile.log

### Logging Directory Structure - Option --log-dir case   
project/
│
├── main.py
└── case/
    └── analyze.log

### Logging Directory Structure - Option --log-dir case26 --log-file logfile.log
project/
│
├── main.py
└── case26/
    └── logfile.log

### Example - using logging-forensic in "forensic-download.py"
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
### Logfile (with logging-forensic)
Logfile (default) will be written to: "log/forensic-download.log"

````
$> cat log/forensic-download.log
..
2026-11-01 17:48:38,712 - INFO - forensic-downlaod.py OK - downloaded file 1: https://apkid.de/test1.txt to D:\download_data\output\download_20250409174838
2026-11-01 17:48:39,081 - INFO - forensic-download.py OK - downloaded file 2: https://apkid.de/wallpaper_16487800940ff7b95bc63e4c56a8843b2c50d3b0de.jpeg to D:\download_data\output\download_20250409174838
..
````


### Basic Logger

````
from logging_forensic import forensic_logger 

logger = forensic_logger( name="case001" ) 

logger.info("Case opened")

````

### Enable Console Logging

````
logger = forensic_logger( name="case001", console=True )

````

Output

2026-01-01 13:10:15 INFO download_urls.py [download] - URL https://example.de/example.txt downloaded

### Set Logging Level
The logging level can be provided as a string:

````
logger = forensic_logger(
    name="debug_analysis",
    level="DEBUG"
)
````
or using Python logging constants:

````
import logging

logger = forensic_logger(
    name="debug_analysis",
    level=logging.DEBUG
)
````
Supported levels:
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

### Verbose Setup Output

For debugging logger configuration:
````
logger = forensic_logger(
    name="test",
    verbose=True
)
````

Example output:
````
forensic-logger: logfile_path set to: log/test.log
forensic-logger: logfile path: log/test.log; level: 20; console: False
forensic-logger: creating logger test
````


### Logger Reuse Behavior

Python loggers are managed by name.

If a logger with the same name already exists and has handlers configured, the existing configuration is reused.

Example:
````
logger1 = forensic_logger("case001")
logger2 = forensic_logger("case001")
````

The second call does not create duplicate handlers.

### Log Format

The default format is:
````
%(asctime)s %(levelname)-6s %(filename)s [%(funcName)s] - %(message)s
````

Example:
````
2026-11-01 13:20:44 INFO download_urls.py [download] - URL downloaded
````

## Forensic Considerations

````logging-forensic```` provides convenient logging configuration, but it is not an audit log system.

The package does not provide:

- Cryptographic log signing 
- Tamper detection 
- Hash chaining 
- Secure log transport 
- Write-once storage

For evidentiary logging requirements, additional controls should be implemented.

### Requirements
- Python 3.8+
The package uses only Python's standard library.

### Development

Clone the repository:
````
git clone https://github.com/fackelm2/logging-forensic.git
````

Install development requirements:
````
pip install -e .
````

### License

MIT License

