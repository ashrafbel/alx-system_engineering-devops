# 7-puppet_install_nginx_web_server.pp

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-available/default.erb':
  ensure => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location = /index.html {
        return 200 'Hello World!';
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}
  command     => '/usr/sbin/nginx -t && /usr/sbin/service nginx reload',
  path        => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
