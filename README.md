# TestOpus
## Automated Test Execution and Reporting

This script performs automated unit test discovery and execution in a specified directory, 
providing a detailed report in JSON format.

## Prerequisites

- Python 3.x

## Usage

You can run a tool with default configuration:
````bash
python main.py
````

or with your own configuration file: 

````bash
python main.py --config /path/to/file
````

## Configuration Details

### Search Path

The `search_path` parameter specifies the directory where the unit tests are located. In this configuration, 
the unit tests are expected to be present in the "unit_tests/" directory.

````json
"search_path": "unit_tests/"
````

### Test Case Name Rules
The `test_case_name_rules` parameter is an array of rules used to identify test case files. Test case files are expected 
to follow the naming patterns specified in this array.
In this configuration, test case files should match either the pattern `*_tests.py` or start with the prefix `test_`.

````json
"test_case_name_rules": ["*_tests.py", "test_"]
````

### Unit Test Name Rules
The `unit_test_name_rules` parameter is an array of rules used to identify individual unit tests within test case files. 
Unit tests are expected to follow the naming patterns specified in this array. 
In this configuration, unit tests should start with the prefix `test`.

````json
"unit_test_name_rules": ["test"]
````

### Reporting Configuration

- `should_report`: A boolean parameter indicating whether the testing framework should generate a report. Set to true in
this configuration.

- `report_format`: Specifies the format of the generated report. In this configuration, the report format is set to 
"json". Note, that for now only json format is supported.

- `should_save_report`: A boolean parameter indicating whether the generated report should be saved. Set to true in
this configuration.

- `report_path`: Specifies the directory where the generated reports should be saved. In this configuration, reports 
are expected to be saved in the "reports/json" directory.

````json
"should_report": true,
"report_format": "json",
"should_save_report": true,
"report_path": "reports/json"
````