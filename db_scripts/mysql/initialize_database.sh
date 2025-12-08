#!/usr/bin/env bash

cd "$(dirname "$0")"

mysql < 99_drop_all.sql
mysql < 00_create_schema.sql
mysql < 01_create_tables.sql
mysql < 02_seed_data.sql