#!/usr/bin/env bash
# Configure Nginx so that its HTTP response contains a custom header
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server
# Nginx is running on
# ALL THIS MUST BE AUTOMATED BY DOING IT WITH PUPPT.
exec { 'update_packages':
path     => ['/usr/bin/', '/usr/sbin'],
command  => 'sudo apt-get -y update',
provider => 'shell',
}

exec { 'install_nginx':
path     => ['/usr/bin/', '/usr/sbin'],
command  => 'sudo apt-get -y install nginx',
provider => 'shell',
}

exec { 'start_nginx':
path     => ['/usr/bin/', '/usr/sbin'],
command  => 'sudo service nginx start',
provider => 'shell',
}

exec { 'modify_nginx_config':
path     => ['/usr/bin/', '/usr/sbin'],
command  => 'sed -i -e "/sendfile/i \\\tadd_header X-Served-By \$hostname;" /etc/nginx/nginx.conf',
provider => 'shell',
}

exec { 'restart_nginx':
path     => ['/usr/bin', '/usr/sbin'],
command  => 'sudo service nginx restart',
provided => 'shell',
}
