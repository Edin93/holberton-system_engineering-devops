# Create a manifesto that kills a process named killmenow.
exec { 'kill_process_killmenow':
path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
provider => 'shell',
onlyif   => 'ps -ef | grep -i "killmenow"',
command  => 'pkill killmenow',
}