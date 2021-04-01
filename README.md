# PI_4SEM

## Gerar chave SSH
$ cd .ssh
$ ssh-keygen -trsa
$ cat id_rsa.pub

## Definir numero de threads usadas para compactar para o push (economizar ram)
$ git config --global pack.threads

## Resolver problemas de merge (em caso de commitar arquivos grandes por exemplo)
$ git filter-branch --tree-filter 'rm -rf path/file' HEAD
$ grep -ril "<<<<<<< HEAD" ./*

## Problemas de conexão no git
.ssh/confg > 
Host github.com
	Hostname ssh.github.com
	Port 443
