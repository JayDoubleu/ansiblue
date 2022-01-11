# ansiblue

#### Experimental playbook aiming to provision silverblue system using ansible.

Install ansible on silverblue without rpm-ostree
```
python3 -m ensurepip
python3 -m pip install ansible
ansible --version
```

- Edit `configs/flatpak.yaml`, `configs/toolbox.yaml` and `config/host.yaml`
- Run with `ansible-playbook ansiblue.yaml -K`

- Flatpak names are case sensitive. While flatpak is ok with it, creation of symlinks will fail.

#### Targeting:
- `ansible-playbook ansiblue.yaml --tags flatpak` <- Run only flatpak tasks
- `ansible-playbook ansiblue.yaml --tags toolbox` <- Run only toolbox tasks ( for all toolboxes )
- `ansible-playbook ansiblue.yaml --tags fedora-toolbox-35` <- Run only specific toolbox tasks
- `ansible-playbook ansiblue.yaml --tags host -K` <- Run only host tasks
