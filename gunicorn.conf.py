import os

workers = 1
worker_class = 'gevent'
worker_connections = 1000
timeout = 120
bind = '0.0.0.0:' + os.environ.get('PORT', '10000')
threads = 0 # Ensure threads are disabled for gevent
