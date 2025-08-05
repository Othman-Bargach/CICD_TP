# TP DevOps – Automatisation CI/CD avec GitHub Actions 🚀

Ce TP a pour objectif de vous faire découvrir et manipuler les **workflows GitHub Actions** pour automatiser le déploiement d’une application web sur AWS, en utilisant Terraform et Ansible.

`Commencez par Fork ce repo en décochant "copy main branch only" et continuez la lecture de ce README 📖`

---

## Objectifs pédagogiques 🎯

- Comprendre la structure d’un workflow GitHub Actions  
- Automatiser le déploiement et la destruction d’infrastructure avec Terraform  
- Automatiser la configuration d’une instance avec Ansible  
- Enchaîner plusieurs jobs dans un pipeline CI/CD  
- Appliquer les bonnes pratiques de sécurité et de documentation 

Pour suivre le TP, il faut naviguer parmi les différentes branches du repository

- **La branche main contient le projet complet fonctionnel** 
- **Les branches d'exercices permettent de le reconstruire avec un niveau de difficulté progressif**

## Structure du projet 🗂️

- **.github/workflows/** : Contient les workflows GitHub Actions pour automatiser le déploiement et la destruction de l’infrastructure.

- **app/frontend** : Contient la page web statique (HTML/CSS/JS) qui interagit avec l’API Flask.

- **app/backend-flask** : Contient le code source de l’API Flask qui sera déployée sur l’instance EC2.

- **CD/terraform-aws-instance/** : Contient les fichiers Terraform pour créer l’infrastructure AWS (principalement une instance EC2, réseau, sécurité, etc.).

- **CD/ansible/** : Contient le playbook et l’inventaire Ansible pour configurer automatiquement l’instance EC2 (installation de Python, Flask, ouverture des ports, déploiement du code backend).

## Fonctionnement global 🌐

1. **Déploiement de l’infrastructure avec Terraform 🏗️**  
   Les fichiers `.tf` décrivent la création d’une instance EC2 Ubuntu, d’un VPC, d’un subnet, et d’un groupe de sécurité ouvrant les ports nécessaires (SSH et 5000).  
   Un workflow GitHub Actions (`TerraformDeploy.yml` ou intégré dans le pipeline complet) s’exécute automatiquement à chaque push sur la branche `main` : il initialise Terraform, planifie et applique les changements sur AWS en utilisant les credentials stockés dans les secrets GitHub.  
   À la fin, l’adresse IP publique de l’EC2 est récupérée et partagée avec les jobs suivants.

2. **Configuration de l’instance avec Ansible 🔧**  
   Une fois l’EC2 créée, Ansible se connecte en SSH à la machine, installe les dépendances nécessaires (Python, pip, virtualenv), puis **copie le code du backend Flask** (présent dans le dossier `app/backend-flask` du repo) sur la VM.  
   Le playbook crée un environnement virtuel Python, installe les requirements, ouvre le port 5000 via UFW et lance l’API Flask en tâche de fond.  

3. **Backend (API Flask) 🐍**  
   L’application backend est une API Flask (dans `app/backend-flask`) qui interroge l’API publique PokéAPI pour retourner un Pokémon aléatoire au format JSON.  
   À chaque modification du code Python sur la branche `main`, le pipeline CI/CD redéploie automatiquement la nouvelle version sur l’EC2, garantissant que la dernière version de l’API est toujours en ligne.

4. **Frontend 🌐**  
   La partie frontend est une page statique (HTML/CSS/JS dans `app/frontend`) qui interroge l’API Flask déployée sur l’EC2 via son adresse IP publique et le port 5000.

**Grâce à cette chaîne CI/CD, toute modification poussée sur la branche `main` (par exemple une évolution de l’application Python) déclenche automatiquement le déploiement complet de l’infrastructure et de l’application, sans intervention manuelle.**

---
🏁Rendez-vous dans la branche de l'exercice 1🏁  
**À vous de jouer !** 🎮
