# SSH

## Mandatory

### 0-use_a_private_key
- Bash script that connects to server via ssh
    - Private key: ~/.ssh/holberton
    - User: ubuntu

### 1-create_ssh_key_pair
- Bash script that creates RSA key pair
    - Private key: holberton
    - Number of bits: 4096
    - Passphrase: betty

### 2-ssh_config
- Configured SSH configuration file without password
    - Private key: ~/.ssh/holberton
    - Refuse authentification using password

### 3 (no file, just in server)
- SSH public key entered into server

## Learning Objectives
- What is a server
- Where do servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash
