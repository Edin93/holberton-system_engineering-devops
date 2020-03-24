# Use puppet to make changes to our configuration file.
file_line { 'ssh config IdentityFile':
name =>   'AUTH_PWD',
path =>   '/etc/ssh/ssh_config',
line =>   'IdentityFile ~/.ssh/holberton',
}
file_line {'ssh remove password authentication':
name =>   'IDENTITY_FILE',
path =>   '/etc/ssh/ssh_config',
line =>   'PasswordAuthentication no',
}
