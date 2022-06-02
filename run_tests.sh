#!/bin/bash

#Activate the project virtual environment.
source venv/bin/activate

#Execute the test suite.
python -m pytest tests/task5.py

# collect exit code from pytest
# exit code is 0 if all tests pass
PYTEST_EXIT_CODE=$?

#Return exit code 0 if all tests passed, or 1 if something went wrong.
# [[ NUM -eq NUM ]]	Equal
# We have also assigned exit value 1 as opposed to 0 meaning that the script exited with an error.
if [[ $PYTEST_EXIT_CODE -eq 0 ]]; then
  exit 0
else
  exit 1
fi