# Puppet manifest to fix WP settings issue.
exec { 'fix WP settings error':
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  provider => 'shell',
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
