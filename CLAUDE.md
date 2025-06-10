# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Ansiblue is an experimental Ansible playbook for provisioning Fedora Silverblue systems. It automates the setup of flatpaks, toolbox containers, and host configurations while respecting Silverblue's immutable design philosophy.

## Development Commands

### Run the playbook
```bash
# Full system provisioning (requires sudo password)
ansible-playbook ansiblue.yaml -K

# Target specific components
ansible-playbook ansiblue.yaml --tags flatpak        # Only flatpak tasks
ansible-playbook ansiblue.yaml --tags toolbox        # All toolbox tasks
ansible-playbook ansiblue.yaml --tags fedora-35      # Specific toolbox
ansible-playbook ansiblue.yaml --tags host -K        # Host tasks (needs sudo)
```

### Install Ansible on Silverblue
```bash
python3 -m ensurepip
python3 -m pip install ansible
```

## Architecture

### Configuration Structure
- **`ansiblue.yaml`**: Main orchestration playbook that loads configs and delegates to setup playbooks
- **`configs/`**: YAML configuration files defining what to install/configure
  - `flatpak.yaml`: Flatpak remotes and applications
  - `toolbox.yaml`: Development containers and their setup
  - `host.yaml`: Host system modifications (packages, GNOME settings)
  - `host_gnome_*.yaml`: GNOME-specific configurations

### Playbook Organization
- **`playbooks/setup/`**: High-level setup orchestration
- **`playbooks/common/`**: Shared tasks for host and containers
- **`playbooks/host/`**: Host-specific configuration tasks
- **`playbooks/toolbox/`**: Container-specific tasks

### Key Design Patterns
1. **Minimal Host Modifications**: Uses rpm-ostree only for essential packages
2. **Container-Host Integration**: Toolboxes can execute host commands via shims in `~/.local/bin`
3. **Flatpak Command Wrappers**: Creates command aliases for flatpak applications
4. **Tag-based Targeting**: All tasks are tagged for selective execution

### Important Implementation Details
- Flatpak names are case-sensitive - incorrect casing will break symlink creation
- The playbook uses `lookup('template')` to load YAML configs with Jinja2 templating support
- Host runner scripts enable containers to execute commands on the host system
- All file paths in configs support Ansible/Jinja2 variables (e.g., `{{ ansiblue_dir }}`)
