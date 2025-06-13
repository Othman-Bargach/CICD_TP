# TP DevOps – Automatisation CI/CD avec GitHub Actions

Ce TP a pour objectif de vous faire découvrir et manipuler les **workflows GitHub Actions** pour automatiser le déploiement d’une application web sur AWS, en utilisant Terraform et Ansible.

---

## Objectifs pédagogiques

- Comprendre la structure d’un workflow GitHub Actions
- Automatiser le déploiement et la destruction d’infrastructure avec Terraform
- Automatiser la configuration d’une instance avec Ansible
- Enchaîner plusieurs jobs dans un pipeline CI/CD
- Appliquer les bonnes pratiques de sécurité et de documentation

---

## Prérequis

- Un compte AWS avec les droits nécessaires pour créer des ressources (EC2, VPC, etc.)
- Une clé SSH créée sur AWS (Key Pair) pour accéder à l’EC2
- Les credentials AWS (Access Key ID et Secret Access Key) ajoutés dans les **secrets GitHub** du dépôt (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- Avoir lu la structure du projet et compris le rôle de chaque dossier (voir README)
- (Optionnel) Un schéma d’architecture ou de pipeline pour visualiser le processus

---

## Déroulé du TP

### 1. Premier workflow : Hello World

- **But** : Créer un workflow `.github/workflows/hello.yml` qui affiche simplement "Hello World" dans les logs GitHub Actions.
- **Aide** : Utilisez un job avec une seule étape `run: echo "Hello World"`.

<details>
<summary>Exemple minimal</summary>

```yaml
name: Hello World

on: [push]

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Print Hello
        run: echo "Hello World"
```
</details>

- **Question** : Que se passe-t-il si vous changez le nom du job ou du workflow ?

---

### 2. Déploiement de l’infrastructure avec Terraform

- **But** : Ajouter un job qui initialise, planifie et applique la configuration Terraform pour créer une instance EC2.
- **Aide** : Inspirez-vous de la documentation officielle [setup-terraform](https://github.com/hashicorp/setup-terraform).
- **Tips** : Utilisez les secrets GitHub pour les credentials AWS.
- **Exemple de structure** :

<details>
<summary>Exemple de job Terraform</summary>

```yaml
name: Deploy Infra

on: [workflow_dispatch, push]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.6

      - name: Terraform Init
        run: terraform init
        working-directory: ./terraform-aws-instance
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: eu-west-1 # à adapter

      - name: Terraform Apply
        run: terraform apply -auto-approve
        working-directory: ./terraform-aws-instance
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: eu-west-1
```
</details>

- **Question** : Pourquoi ne faut-il jamais mettre ses credentials AWS en clair dans le workflow ?

---

### 3. Destruction de l’infrastructure

- **But** : Ajouter un job qui détruit l’infrastructure créée par Terraform (`terraform destroy`).
- **Aide** : Ce job doit être déclenché manuellement (`workflow_dispatch`).
- **Exemple** :

<details>
<summary>Exemple de job Destroy</summary>

```yaml
name: Destroy Infra

on:
  workflow_dispatch:

jobs:
  destroy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3

      - name: Terraform Init
        run: terraform init
        working-directory: ./terraform-aws-instance
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: eu-west-1

      - name: Terraform Destroy
        run: terraform destroy -auto-approve
        working-directory: ./terraform-aws-instance
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: eu-west-1
```
</details>

- **Question** : Pourquoi est-il préférable de déclencher la destruction manuellement ?

---

### 4. Configuration de l’instance avec Ansible

- **But** : Ajouter un job qui, après le déploiement Terraform, utilise Ansible pour configurer l’instance EC2 (installation de Python, Flask, etc.).
- **Aide** : Utilisez l’IP publique générée par Terraform comme cible Ansible.
- **Tips** : Récupérez l’output Terraform avec `terraform output` et passez-le à Ansible.
- **Exemple de structure** :

<details>
<summary>Exemple de job Ansible</summary>

```yaml
- name: Configure EC2 with Ansible
  run: |
    pip install ansible
    ansible-playbook -i "${IP_PUBLIC}," ansible/playbook.yml --private-key ~/.ssh/id_rsa
  env:
    IP_PUBLIC: ${{ steps.terraform_output.outputs.public_ip }}
```
</details>

- **Question** : Comment sécuriser la clé SSH utilisée par Ansible dans GitHub Actions ?

---

### 5. (Bonus) Déploiement continu

- **But** : Enchaîner les jobs pour que le pipeline complet s’exécute automatiquement à chaque push sur `main`.
- **Aide** : Utilisez les dépendances entre jobs (`needs:`) pour orchestrer le pipeline.

---

## Conseils

- Commencez simple, testez chaque étape séparément.
- Utilisez les outputs Terraform pour récupérer l’IP de l’instance.
- Pensez à bien sécuriser vos credentials AWS dans les secrets GitHub.
- Documentez chaque étape dans vos workflows (nom, description, commentaires).
- Ajoutez des badges de statut dans le README pour visualiser l’état des workflows.
- Utilisez un schéma pour visualiser le pipeline (optionnel mais recommandé).

---

## Pour aller plus loin

- Ajoutez des tests automatisés sur l’API Flask (job de test).
- Déployez le frontend sur S3 via un job supplémentaire.
- Ajoutez des notifications Slack ou Teams en fin de pipeline.
- Proposez des variantes : changer la région AWS, le type d’instance, ou ajouter d’autres ressources (RDS, S3…).

---

## Questions de réflexion

- Pourquoi séparer le déploiement et la configuration dans deux jobs différents ?
- Que se passe-t-il si le job Terraform échoue ? Comment le pipeline doit-il réagir ?
- Quels sont les risques de sécurité liés à l’automatisation du cloud via CI/CD ?

---

**À vous de jouer !**