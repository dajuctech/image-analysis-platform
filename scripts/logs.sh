#!/bin/bash

LOG_DIR="logs"

echo " Showing last 10 log entries:"
tail -n 10 $LOG_DIR/*.log

echo -e "\n Counting WARNINGS and ERRORS:"
grep -E "WARNING|ERROR" $LOG_DIR/*.log | wc -l

echo -e "\n Showing all ERROR lines:"
grep "ERROR" $LOG_DIR/*.log
