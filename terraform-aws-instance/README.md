# terraform-aws-instance

Ce dossier contient la configuration Terraform pour déployer une instance EC2 AWS destinée à héberger l'API Flask du projet.

## 📁 Contenu

- `main.tf` : Déclaration de la ressource EC2 et sortie de l'IP publique.
- `network.tf` : Création du VPC, subnet, gateway et table de routage.
- `provider.tf` : Configuration du provider AWS.
- `remote-state.tf` : Configuration du backend distant (S3) pour stocker l'état Terraform.
- `securityGroup.tf` : Définition du groupe de sécurité ouvrant les ports nécessaires (SSH et 5000 pour Flask).

## 🚀 Déploiement

1. **Initialiser le projet Terraform**
   terraform init

terraform plan  

## 🔒 Sécurité

Le groupe de sécurité autorise :
SSH (port 22) depuis n'importe où (à restreindre en production)
Le port 5000 pour accéder à l'API Flask
