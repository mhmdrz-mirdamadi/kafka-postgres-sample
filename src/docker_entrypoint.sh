#!/bin/bash

exec python3 get_data.py &
exec python3 add_ts.py &
exec python3 add_label.py &
exec python3 write_db.py