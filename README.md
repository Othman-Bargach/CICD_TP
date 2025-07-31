# TP DevOps – Automatisation CI/CD avec GitHub Actions

Ce TP a pour objectif de vous faire découvrir et manipuler les **workflows GitHub Actions** pour automatiser le déploiement d’une application web sur AWS, en utilisant Terraform et Ansible.

---

## Objectifs pédagogiques

- Comprendre la structure d’un workflow GitHub Actions
- Automatiser le déploiement et la destruction d’infrastructure avec Terraform
- Automatiser la configuration d’une instance avec Ansible
- Enchaîner plusieurs jobs dans un pipeline CI/CD
- Appliquer les bonnes pratiques de sécurité et de documentation

Pour suivre le TP, il faut naviguer parmi les différentes branches du repository

- **La branche main contient le projet complet fonctionnel**
- **Les branches d'exercices permettent de le reconstruire avec un niveau de difficulté progressif**

---

## Prérequis

- Un compte AWS avec les droits nécessaires pour créer des ressources (EC2, VPC, etc.)
- Une clé SSH créée sur AWS (Key Pair) pour accéder à l’EC2
- Les credentials AWS (Access Key ID et Secret Access Key) ajoutés dans les **secrets GitHub** du dépôt (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- Avoir lu la structure du projet et compris le rôle de chaque dossier

## Structure du projet

- .github/workflows/ : Contient les workflows GitHub Actions pour automatiser le déploiement et la destruction de l’infrastructure.

- app/frontend : Contient la page web statique (HTML/CSS/JS) qui interagit avec l’API Flask.

- app/backend-flask : Contient le code source de l’API Flask qui sera déployée sur l’instance EC2.

- CD/terraform-aws-instance/ : Contient les fichiers Terraform pour créer l’infrastructure AWS (principalement une instance EC2, réseau, sécurité, etc.).

- CD/ansible/ : Contient le playbook et l’inventaire Ansible pour configurer automatiquement l’instance EC2 (installation de Python, Flask, ouverture des ports, déploiement du code backend).

## Fonctionnement global

1. Déploiement de l’infrastructure avec Terraform
Les fichiers .tf décrivent la création d’une instance EC2 Ubuntu, d’un VPC, d’un subnet, d’un groupe de sécurité ouvrant les ports nécessaires (SSH et 5000).
Un workflow GitHub Actions (TerraformDeploy.yml) s’exécute à chaque push sur la branche main : il initialise Terraform, planifie et applique les changements sur AWS en utilisant les credentials stockés dans les secrets GitHub.
2. Configuration de l’instance avec Ansible
Une fois l’EC2 créée, Ansible se connecte en SSH à la machine, installe les dépendances (Python, pip, virtualenv, git), clone le dépôt backend, installe les requirements et lance l’API Flask.
Le playbook ouvre aussi le port 5000 pour permettre l’accès à l’API.
3. Frontend
La partie frontend est une page statique qui interroge l’API Flask déployée sur l’EC2.

---

**À vous de jouer !**
