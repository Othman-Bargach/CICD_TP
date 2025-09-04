# Exercice 3 - Déploiement de configuration avec Ansible

S'exercer à l'utilisation de GitHub Actions pour déployer une configuration sur une VM AWS via Ansible.

## Prérequis
Cet exercice se fait directement via l’interface GitHub.

✅ Les pré-requis de l'exercice 2,  
**Aide** : Inspirez-vous de la documentation officielle [ansible](https://docs.ansible.com/).

---

## Étape 1 : Récupération de l'IP de la VM déployée par Terraform

**Objectif** : Compléter le workflow `.github/workflows/CICD_Complète.yml` pour :

- Récupérer l'IP de la VM après son déploiement & la sauvegarder dans un fichier
- Uploader ce fichier en tant qu'Artifact GitHub

<details>
<summary>Code à compléter : remplacez les ??? dans le fichier yml CICD_Complète</summary>

```yaml
# ... étapes précédentes de déploiement ...

   # Enregistre l'adresse IP publique de l'instance EC2 créée par Terraform dans un fichier texte
   - name: Save public IP output
      run: ???
      working-directory: ./CD/terraform-aws-instance

   # Upload l'adresse IP publique dans les artifacts du workflow pour qu'elle puisse être utilisée par d'autres jobs ou workflows
   - name: Upload public IP artifact
      uses: ???
      with:
         name: ???
         path: ./CD/terraform-aws-instance/???
```

</details>

<details>

<summary>Correction</summary>

```yaml
# ... étapes précédentes de déploiement ...

   # Enregistre l'adresse IP publique de l'instance EC2 créée par Terraform dans un fichier texte
   - name: Save public IP output
      run: |
         terraform output -raw public_ip > public_ip.txt
      working-directory: ./CD/terraform-aws-instance

   # Upload l'adresse IP publique dans les artifacts du workflow pour qu'elle puisse être utilisée par d'autres jobs ou workflows
   - name: Upload public IP artifact
      uses: actions/upload-artifact@v4
      with:
         name: public-ip
         path: ./CD/terraform-aws-instance/public_ip.txt
```

</details>

**Question 1** : Pourquoi faut-il sauvegarder l'IP dans un fichier et l'uploader en tant qu'Artifact ?

---

## Étape 2 : Configuration Ansible avec l'IP de la VM

**Objectif** :  Compléter le workflow `.github/workflows/CICD_Complète.yml` pour :
- Télécharger l'Artifact contenant l'IP
- Utiliser cette IP pour configurer Ansible et déployer la configuration

<details>
<summary>Code à compléter : remplacez les ??? dans le fichier yml CICD_Complète</summary>

```yaml
# ... étapes précédentes de configuration ...

   # Télécharge l'adresse IP publique de l'instance EC2 créée par Terraform depuis les artifacts du workflow précédent
   - name: Download public IP artifact
      uses: ???
      with:
         name: public-ip

   # Ajoute l'hôte EC2 dans known_hosts pour éviter l'erreur de vérification de clé SSH
   - name: Add EC2 to known_hosts
      run: |
         ANSIBLE_HOST=$(cat ???.txt)
         mkdir -p ~/.ssh
         ssh-keyscan "$ANSIBLE_HOST" >> ~/.ssh/known_hosts

   - name: Add SSH key
      uses: webfactory/ssh-agent@v0.9.0
      with:
         ssh-private-key: ${{ secrets.ANSIBLE_SSH_PRIVATE_KEY }}

   - name: Run Ansible Playbook
      run: |
         ANSIBLE_HOST=$(cat ???.txt)
         ansible-playbook -i "$ANSIBLE_HOST," CD/ansible/playbook.yml -u ubuntu
```

</details>

<details>
<summary>Correction</summary>

```yaml
# ... étapes précédentes de configuration ...

   # Télécharge l'adresse IP publique de l'instance EC2 créée par Terraform depuis les artifacts du workflow précédent
   - name: Download public IP artifact
      uses: actions/download-artifact@v4
      with:
         name: public-ip

   # Ajoute l'hôte EC2 dans known_hosts pour éviter l'erreur de vérification de clé SSH
   - name: Add EC2 to known_hosts
      run: |
         ANSIBLE_HOST=$(cat public_ip.txt)
         mkdir -p ~/.ssh
         ssh-keyscan "$ANSIBLE_HOST" >> ~/.ssh/known_hosts

   - name: Add SSH key
      uses: webfactory/ssh-agent@v0.9.0
      with:
         ssh-private-key: ${{ secrets.ANSIBLE_SSH_PRIVATE_KEY }}

   - name: Run Ansible Playbook
      run: |
         ANSIBLE_HOST=$(cat public_ip.txt)
         ansible-playbook -i "$ANSIBLE_HOST," CD/ansible/playbook.yml -u ubuntu
```

</details>

**Question 2** : À quoi sert de récupérer l'IP via un Artifact dans ce contexte ?
