# CI/CD TP

## Description

Le projet CiCD_TP met en place une chaîne CI/CD complète pour déployer une application web composée d’un frontend statique et d’un backend Python (API Flask), le tout automatisé avec Terraform, Ansible et GitHub Actions.

## Structure du projet

* frontend/ : Contient la page web statique (HTML/CSS/JS) qui interagit avec l’API Flask.

* terraform-aws-instance/ : Contient les fichiers Terraform pour créer l’infrastructure AWS (principalement une instance EC2, réseau, sécurité, etc.).

* ansible/ : Contient le playbook et l’inventaire Ansible pour configurer automatiquement l’instance EC2 (installation de Python, Flask, ouverture des ports, déploiement du code backend).

* .github/workflows/ : Contient les workflows GitHub Actions pour automatiser le déploiement et la destruction de l’infrastructure.

## Fonctionnement global

1. Déploiement de l’infrastructure avec Terraform
Les fichiers .tf décrivent la création d’une instance EC2 Ubuntu, d’un VPC, d’un subnet, d’un groupe de sécurité ouvrant les ports nécessaires (SSH et 5000).
Un workflow GitHub Actions (TerraformDeploy.yml) s’exécute à chaque push sur la branche main : il initialise Terraform, planifie et applique les changements sur AWS en utilisant les credentials stockés dans les secrets GitHub.
2. Configuration de l’instance avec Ansible
Une fois l’EC2 créée, Ansible se connecte en SSH à la machine, installe les dépendances (Python, pip, virtualenv, git), clone le dépôt backend, installe les requirements et lance l’API Flask.
Le playbook ouvre aussi le port 5000 pour permettre l’accès à l’API.
3. Frontend
La partie frontend est une page statique qui interroge l’API Flask déployée sur l’EC2.