# Exercice 2 - Déploiement Infra Terraform
S'exercer à l'utilisation de GitHub Actions pour déployer une VM AWS sur la base d'un code Terraform. 

## Prérequis
Cet exercice se fait directement via l’interface GitHub.

✅ Les pré-requis de l'exercice 1  
✅   

---

## Étape 1 : Terraform Deploy
**Objectif** : Compléter le workflow `.github/workflows/TerraformDeploy.yml`. 
- Le workflow doit être déclenché par un bouton depuis l'onglet "Actions du repo GitHub,
- Il doit afficher "Hello World !" depuis l'onglet Actions.

<details>
<summary>Code à compléter : remplacez les ??? dans le fichier yml</summary>

```yaml
name: Hello World !

on: ???

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Print Hello
        run: ???
```
</details>

<details>
<summary>Correction</summary>

```yaml
name: Deploy with Terraform

on:
  workflow_dispatch:     # Permet le déclenchement manuel dans GitHub

jobs:
  terraform:
    name: Terraform Apply
    runs-on: ubuntu-latest

    env:
      TF_INPUT: false
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

    steps:
      # Clone le dépôt sur le runner Ubuntu de Github Actions pour accéder aux fichiers Terraform
      - name: Checkout code
        uses: actions/checkout@v4

      # Installe Terraform sur le runner Ubuntu de Github Actions
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.6

      - name: Terraform Init
        run: terraform init
        working-directory: ./terraform-aws-instance

      - name: Terraform Plan
        run: terraform plan
        working-directory: ./terraform-aws-instance

      - name: Terraform Apply
        run: terraform apply -auto-approve
        working-directory: ./terraform-aws-instance

      # Enregistre l'adresse IP publique de l'instance EC2 créée par Terraform dans un fichier texte
      - name: Save public IP output
        run: |
          terraform output -raw public_ip > public_ip.txt
        working-directory: ./terraform-aws-instance

      # Upload l'adresse IP publique dans les artifacts du workflow pour qu'elle puisse être utilisée par d'autres jobs ou workflows
      - name: Upload public IP artifact
        uses: actions/upload-artifact@v4
        with:
          name: public-ip
          path: ./terraform-aws-instance/public_ip.txt

```
</details>

  
**Question 1** : Que se passe-t-il si vous changez le nom du job ou du workflow ?  

## Étape 2 : Déclenchement automatique (push)
**Objectif** : Modifier le workflow `.github/workflows/HelloWorld.yml`.
- Le workflow doit être déclenché à chaque push sur la branche "Exercice-1-HelloWorld!".

<details>
<summary>Correction</summary>

```yaml
name: Hello world !

on:
  # Le déclencheur push exécute le workflow à chaque commit sur la branche spécifiée.
    push:
      branches: [ "Exercice-1-HelloWorld!" ]

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Print Hello
        run: echo "Hello World !"
```
</details>

**Question 2** : Que se passe-t-il si vous poussez sur une autre branche que "Exercice-1-HelloWorld!" ? Le workflow est-il déclenché ?
