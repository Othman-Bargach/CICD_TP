# 🚀 Déploiement d'une API Flask avec Ansible

Ce projet utilise **Ansible** pour configurer une machine virtuelle qui fera office de backend (API Flask)
Dans le cadre du TP, cette machine virtuelle est un serveur EC2 AWS sous Ubuntu server

---

## 📁 Structure

```bash
.
├── deploy.yml                # Playbook Ansible
├── inventory.ini             # Inventaire des hôtes (modifiable dynamiquement)
├── files/
│   └── id_ansible_deploy     # Clé privée SSH pour cloner le dépôt GitHub
```

## ⚙️ Prérequis

* Ansible installé localement (`ansible --version`)

* Machine virutelle
  * Un serveur distant qui tourne (EC2 Ubuntu) avec le port 5000 ouvert
  * Son adresse IP publique
  * Utilisateur SSH (`ubuntu`)
  * Une clé privée SSH d'accès à l'EC2 (bien configuré sur AWS)

* Dépot GitHub :
  * Le dépot Github Flask (ex. : [Othman-Bargach/backend-flask](https://github.com/Othman-Bargach/backend-flask))
  * Une clé privée SSH Ansible (non chiffrée) dans `files/id_ansible_deploy` ayant **accès au dépôt GitHub**

## 📄 Description des tâches du Playbook

* Installe Python, pip, git, virtualenv
* Configure GitHub comme hôte de confiance
* Clone le dépôt dans /home/ubuntu/flask_app
* Crée un venv et installe les dépendances
* Ouvre le port 5000 via UFW
* Lance Flask en tâche de fond avec nohup

## ✅ Vérification

Test via navigateur ou curl :

```bash
curl http://<IP_PUBLIC_EC2>:5000/call_results```
