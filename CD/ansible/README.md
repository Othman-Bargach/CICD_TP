# 🚀 Déploiement d'une API Flask avec Ansible

Ce projet utilise **Ansible** pour configurer une machine virtuelle qui fera office de backend (API Flask)
Dans le cadre du TP, cette machine virtuelle est un serveur EC2 AWS sous Ubuntu server

---

## 📁 Structure

```bash
.
├── playbook.yml              # Playbook Ansible
├── inventory.ini             # Inventaire des hôtes (modifiable dynamiquement)
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

## 📄 Description des tâches du Playbook

* Installe Python, pip, git, virtualenv
* Copie le dossier de l'application dans /home/ubuntu/flask_app
* Crée un venv et installe les dépendances
* Ouvre le port 5000 via UFW
* Lance Flask en tâche de fond avec nohup

## Execution

ansible-playbook -i inventory.ini playbook.yml

## ✅ Vérification

Test via navigateur ou curl :

```bash
curl http://<IP_PUBLIC_EC2>:5000/call_results```