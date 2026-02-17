#! /bin/bash

run_tests()
{
echo "running the pytest"
cd test && python3 -m pytest -vv 
cd -
echo "Tests completed"
}

run_tests