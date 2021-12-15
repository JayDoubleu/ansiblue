# ansiblue

#### Experimental playbook aiming to provision silverblue system using ansible.

Install ansible on silverblue without rpm-ostree
```
python3 -m ensurepip
python3 -m pip install ansible
ansible --version
```

Edit `configs/flatpak.yaml`
Run with `ansible-playbook ansiblue.yaml`

- Flatpak names are case sensitive. While flatpak is ok with it, creation of symlinks will fail.
