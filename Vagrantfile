# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  	config.vm.network "forwarded_port", guest: 5000, host: 5000
	config.vm.provision :shell, path: "bootstrap.sh"
	config.vm.provision "file", source: ".vimrc", destination: ".vimrc"
  config.ssh.forward_x11 = true
end
