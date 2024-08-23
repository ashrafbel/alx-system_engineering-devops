# Increases the capacity of an Nginx server to handle higher traffic volumes

exec { 'nginx fix':
  onlyif   => 'test -e /etc/default/nginx',
  command  => "sed -i s/'-n 15'/'-n 4096'/g /etc/default/nginx;  service nginx restart",
  provider => 'shell'
}
