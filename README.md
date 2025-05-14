## 📌 Normes per actualitzar els diagrames UML

- Cada vegada que es modifica el codi, s'ha d'actualitzar el diagrama.
- Els fitxers UML es guarden dins la carpeta `diagrames/`.
- El nom del fitxer `.puml` ha de coincidir amb el del fitxer `.py`.
- Si el canvi afecta l'estructura (afegir classes, relacions...), s'ha d'actualitzar immediatament abans de fer `commit`.

## ✅ Bones pràctiques per fer commits

- Fer commits **freqüents i clars**.
- Incloure tant el fitxer de codi com el `.puml` relacionat.
- Exemple:
  ```bash
  git commit -m "Afegida classe Camio i modificat ACT3.puml"
