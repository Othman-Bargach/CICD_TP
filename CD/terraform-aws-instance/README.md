# terraform-aws-instance

Ce dossier contient la configuration Terraform pour déployer une instance EC2 AWS destinée à héberger l'API Flask du projet.

---

## 📁 Contenu

- `main.tf` : Déclaration de la ressource EC2 et sortie de l'IP publique.
- `network.tf` : Création du VPC, subnet, gateway et table de routage.
- `provider.tf` : Configuration du provider AWS.
- `remote-state.tf` : Configuration du backend distant (S3) pour stocker l'état Terraform.
- `securityGroup.tf` : Définition du groupe de sécurité ouvrant les ports nécessaires (SSH et 5000 pour Flask).

## 🚀 Déploiement

1. **Initialiser le projet Terraform**
   terraform init

2. **Vérifier le plan d'exécution**
    terraform plan  

3. **Appliquer la configuration**
    terraform apply

4. **Récupérer l'adresse IP publique**
    terraform output public_ip

## 🔒 Sécurité

Le groupe de sécurité autorise :
SSH (port 22) depuis n'importe où (à restreindre si l'on était en context réel de prod en entreprise)
Le port 5000 pour accéder à l'API Flask

## 📝 Prérequis

Un compte AWS avec les droits nécessaires
Une clé SSH existante sur AWS nommée TP DevOps SSH Key
Terraform >= 1.2.0

## 📦 Backend distant

L'état Terraform est stocké dans un bucket S3 (terraform-tp-devops) pour permettre le travail collaboratif.
