# 2-execute_a_command.pp
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
