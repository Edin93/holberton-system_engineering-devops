# Configure Nginx to accept a load of requests simultaneously.
exec { 'update_ulimit':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 200\"/g" /etc/default/nginx',
provider => 'shell',
}

exec { 'update_worker_processes':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sed -i "s/worker_processes 4;/worker_processes 8;/g" /etc/nginx/nginx.conf',
provider => 'shell',
}

exec { 'reload_nginx':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sudo service nginx reload',
provider => 'shell',
}

exec { 'restart_nginx':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sudo service nginx restart',
provider => 'shell',
}
