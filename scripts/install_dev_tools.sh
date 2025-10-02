#!/bin/bash
set -euo pipefail

log() {
  printf '[install_dev_tools] %s\n' "$1"
}

ensure_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    log "Installing $1"
    sudo apt-get update -y
    sudo apt-get install -y "$2"
  else
    log "$1 already installed"
  fi
}

install_python_dependencies() {
  log "Installing Python dependencies"
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
}

configure_pre_commit() {
  log "Configuring pre-commit hooks"
  if [ ! -f .pre-commit-config.yaml ]; then
    cat <<'HOOK' > .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
        language_version: python3
HOOK
  fi
  pre-commit install
}

verify_docker() {
  if ! command -v docker >/dev/null 2>&1; then
    log "Docker not found; installing Docker Engine"
    curl -fsSL https://get.docker.com | sh
  else
    log "Docker detected; running version check"
    docker --version
  fi
  if ! command -v docker-compose >/dev/null 2>&1; then
    log "Installing docker-compose plugin"
    sudo apt-get install -y docker-compose-plugin
  fi
}

install_node_tools() {
  if ! command -v npm >/dev/null 2>&1; then
    log "Installing Node.js"
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
  else
    log "Node.js already installed"
  fi
  npm install --global yarn@1.22.22
}

main() {
  log "Starting development tooling installation"
  ensure_command git git
  ensure_command curl curl
  ensure_command make make
  verify_docker
  install_python_dependencies
  configure_pre_commit
  install_node_tools
  log "Development tooling installation complete"
}

main "$@"
