# Exercice 1 - Hello World !
Prendre en main la syntaxe d’un workflow GitHub Actions.

## Prérequis
Cet exercice se fait directement via l’interface GitHub.

✅ Avoir un compte GitHub actif  
✅ Avoir forké le dépôt du TP dans son propre compte  
✅ Être capable de modifier un fichier .yml dans le dossier .github/workflows/  
✅ Savoir où trouver les logs GitHub Actions (onglet "Actions")  

---

## Étape 1 : Déclenchement manuel (workflow_dispatch)
**Objectif** : Compléter le workflow `.github/workflows/HelloWorld.yml`. 
- Le workflow doit être déclenché par un bouton depuis l'onglet "Actions" du repo GitHub,
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
#Le nom qui apparaîtra dans l'onglet "Actions" du repo GitHub
name: Hello world !

# Contrôle quand le workflow sera exécuté
on:
  # Workflow_dispatch permet de lancer manuellement un workflow depuis l'onglet "Actions" — idéal pour les tests.
  workflow_dispatch:

# Un workflow est composé d'un ou plusieurs jobs qui peuvent s'exécuter de manière séquentielle ou en parallèle
jobs:
  hello:
    runs-on: ubuntu-latest
    # Les étapes représentent une séquence de tâches qui seront exécutées dans le cadre du job
    steps:
      # Exécute une seule commande en utilisant le shell du runner
      - name: Print Hello
        run: echo "Hello World !"
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

