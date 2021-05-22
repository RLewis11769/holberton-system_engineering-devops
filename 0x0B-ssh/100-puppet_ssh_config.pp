# Use Puppet to set up configuration file to connect to server without password

file { '/etc/ssh/ssh_config':
  ensure => 'present',
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/holberton'
}
