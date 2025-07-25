# Exercice 1 - Hello World !

## Prérequis
Cet exercice se fait directement via l’interface GitHub.

✅ Avoir un compte GitHub actif  
✅ Avoir forké le dépôt du TP dans son propre compte  
✅ Être capable de modifier un fichier .yml dans le dossier .github/workflows/  
✅ Savoir où trouver les logs GitHub Actions (onglet "Actions")  

## Objectif
Prendre en main la syntaxe d’un workflow GitHub Actions.

---

## Déroulé de l'exercice 1

### 1. Premier workflow : Hello World

- **Objectif** : Copier et compléter le workflow `.github/workflows/HelloWorld.yml` pour qu'il affiche simplement "Hello World !" dans les logs GitHub Actions.

<details>
<summary>Code à copier et compléter</summary>

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

- **Question 1** : Que se passe-t-il si vous changez le nom du job ou du workflow ?
- **Question 2** : Le job s’exécute-t-il même avec un nom différent ?
