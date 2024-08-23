# Increases the capacity of an Nginx server to handle higher traffic volumes.

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} ->

# Restart Nginx with the correct command
exec { 'nginx-restart':
  command => 'systemctl restart nginx',
  path    => ['/usr/sbin', '/sbin', '/usr/bin', '/bin'],
}
