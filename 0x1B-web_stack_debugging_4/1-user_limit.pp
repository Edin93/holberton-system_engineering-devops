# Configure the OS to allow the login with the holberton user.
exec { 'update_holberton_hard':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 524288/" /etc/security/limits.conf',
provider => 'shell',
}

exec { 'update_holberton_soft':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 524288/" /etc/security/limits.conf',
provider => 'shell',
}

exec { 'execute_the_updates':
path     => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
command  => '/sbin/sysctl -p',
provider => 'shell',
}
