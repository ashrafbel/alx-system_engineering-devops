# 2-execute_a_command.pp

exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f killmenow || /bin/true',
  path        => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
}
