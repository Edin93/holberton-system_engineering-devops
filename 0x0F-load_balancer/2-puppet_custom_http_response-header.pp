# Configure Nginx so that its HTTP response contains a custom header
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server
# Nginx is running on
# ALL THIS MUST BE AUTOMATED BY DOING IT WITH PUPPET.
exec { 'update_packages':
path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command => 'sudo apt-get -y update',
}

exec { 'start_nginx':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sudo service nginx start',
provider => 'shell',
unless   => 'sudo apt-get -y install nginx',
}

exec { 'restart_nginx':
path     => ['/bin/', '/sbin/', '/usr/bin', '/usr/sbin'],
command  => 'sudo service nginx restart',
provider => 'shell',
unless   => 'sed -i -e "/sendfile/i \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
}
