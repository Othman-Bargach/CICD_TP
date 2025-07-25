# Exercice 1 - Hello World !

## Prérequis
- Comprendre la logique et la syntaxe de Github Actions
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

- **Question** : Que se passe-t-il si vous changez le nom du job ou du workflow ?
