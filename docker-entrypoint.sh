#!/bin/bash

# Intenta cambiar permisos del socket (no fallar si no puede)
if [ -S /var/run/docker.sock ]; then
  chown root:docker /var/run/docker.sock 2>/dev/null || true
  chmod 660 /var/run/docker.sock 2>/dev/null || true
fi

# Ejecutar Jenkins
exec /usr/bin/tini -- /usr/local/bin/jenkins.sh "$@"