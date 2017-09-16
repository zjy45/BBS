#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.app

"""
建立一个软连接
ln -s /var/www/BBS/BBS/BBS.conf /etc/supervisor/conf.d/BBS.conf

ln -s /var/www/BBS/BBS/BBS.nginx /etc/nginx/sites-enabled/BBS



➜  ~ cat /etc/supervisor/conf.d/BBS.conf

[program:BBS]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/root/var/www/BBS/BBS
autostart=true
autorestart=true




/usr/local/bin/gunicorn wsgi --bind 0.0.0.0:2001 --pid /tmp/blog.pid
"""
