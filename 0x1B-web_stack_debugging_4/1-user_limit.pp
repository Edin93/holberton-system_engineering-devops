# Configure the OS to allow the login with the holberton user.
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
