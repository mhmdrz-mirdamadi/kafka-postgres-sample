#!/bin/bash

echo "* * * * * /usr/bin/python3 /home/src/get_data.py" | crontab -

exec python3 get_data.py &
exec python3 add_ts.py &
exec python3 add_label.py &
exec python3 write_db.py