# 1-install_a_package.pp
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  path    => '/usr/bin/:/bin/:/usr/sbin/:/sbin/',
  unless  => '/usr/bin/python3 -c "import flask; print(flask.__version__)" | grep -q "^2.1.0$"',
}
