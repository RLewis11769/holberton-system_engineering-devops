file { '/etc/ssh/ssh_config':
  ensure => 'present',
  content => 'PasswordAuthentication no',
  content => 'IdentityFile ~/.ssh/holberton'
}
