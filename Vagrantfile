# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|

  config.vm.box = "generic/ubuntu2204"

  config.vm.network "forwarded_port", guest: 3001, host: 8080
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provision "shell", path: "bootstrap.sh"
end
