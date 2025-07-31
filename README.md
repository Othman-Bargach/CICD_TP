# Exercice 2 - Déploiement Infra Terraform
S'exercer à l'utilisation de GitHub Actions pour déployer une VM AWS sur la base d'un code Terraform. 

## Prérequis
Cet exercice se fait directement via l’interface GitHub.

✅ Les pré-requis de l'exercice 1  
✅    
**Aide** : Inspirez-vous de la documentation officielle [setup-terraform](https://github.com/hashicorp/setup-terraform).

---

## Étape 1 : Terraform Deploy
**Objectif** : Compléter le workflow `.github/workflows/TerraformDeploy.yml`. 
- Le workflow doit être déclenché par un bouton depuis l'onglet "Actions du repo GitHub,
- Il doit lancer les commandes : "Terraform Init", "Terraform Plan" et "Terraform Apply"

<details>
<summary>Code à compléter : remplacez les ??? dans le fichier yml TerraformDeploy</summary>

```yaml
name: Deploy with Terraform

on:
  workflow_dispatch: 

jobs:
  Terraform_deploy:
    runs-on: ubuntu-latest

    env:
      TF_INPUT: false
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.6

      - ???
        working-directory: ./terraform-aws-instance

      - ???
        working-directory: ./terraform-aws-instance

      - ???
        working-directory: ./terraform-aws-instance
```
</details>

<details>
<summary>Correction</summary>

```yaml
name: Deploy with Terraform

on:
  workflow_dispatch:     # Permet le déclenchement manuel dans GitHub

jobs:
  Terraform_deploy :
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
```
</details>

  
**Question 1** : Pourquoi ne faut-il jamais mettre ses credentials AWS en clair dans le workflow ?

## Étape 2 : Terraform Destroy
**Objectif** : Modifier le workflow `.github/workflows/TerraformDestroy.yml`.
- Le workflow doit être déclenché par un bouton depuis l'onglet "Actions du repo GitHub,
- Il doit permettre de détruire l'instance avec la commande "Terraform destroy"

<details>
<summary>Code à compléter : remplacez les ??? dans le fichier yml TerraformDestroy</summary>

```yaml
name: Destroy with Terraform

on:
  workflow_dispatch:

jobs:
  Terraform_destroy :
    runs-on: ubuntu-latest

    env :
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

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

      - ???
        working-directory: ./terraform-aws-instance
```
</details>


<details>
<summary>Correction</summary>

```yaml
name: Destroy with Terraform

on:
  workflow_dispatch:

jobs:
  Terraform_destroy :
    runs-on: ubuntu-latest

    env :
      AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
      AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

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

      - name: Terraform Destroy
        run: terraform destroy -auto-approve
        working-directory: ./terraform-aws-instance
```
</details>

**Question 2** : ?
