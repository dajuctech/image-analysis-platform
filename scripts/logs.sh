#!/bin/bash

echo "---- Last 10 log entries ----"
tail -n 10 logs/*.log

echo "---- Count of WARNINGS and ERRORS ----"
grep -E 'WARNING|ERROR' logs/*.log | wc -l

echo "---- All ERROR messages ----"
grep 'ERROR' logs/*.log
