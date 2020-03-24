# Use puppet to make changes to our configuration file.
file_line { 'ssh config IdentityFile':
path =>   '/etc/ssh/ssh_config',
line =>   'IdentityFile ~/.ssh/holberton',
}
file_line {'ssh remove password authentication':
path =>   '/etc/ssh/ssh_config',
line =>   'PasswordAuthentication no',
}
