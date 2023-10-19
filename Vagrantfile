# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|

  config.vm.box = "debian/buster64"

  config.vm.network "forwarded_port", guest: 3000, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"


config.vm.provision "shell",
  path: "bootstrap.sh",
  env: {"PORT" => "3001"}

end
