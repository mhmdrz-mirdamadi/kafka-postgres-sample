#!/bin/bash

set -e

exec python3 get_data.py &
exec python3 add_label.py