---

## 📌 Normes per actualitzar els diagrames UML

- Cada vegada que es modifica el codi, s’ha d’actualitzar el diagrama `.puml` corresponent.
- Els fitxers UML es guarden dins la carpeta `diagrames/`.
- El nom del fitxer `.puml` ha de coincidir amb el del fitxer `.py` (per exemple: `AC2_PY.py` → `ACT2.puml`).
- Si el canvi afecta l'estructura (afegir classes, relacions, atributs...), el diagrama s’ha de modificar immediatament abans de fer el commit.

---

## ✅ Bones pràctiques per fer commits

- Fer commits **freqüents** i **clars**.
- Incloure tant el fitxer de codi com el diagrama UML relacionat.
- Fer servir missatges descriptius, com per exemple:
  ```bash
  git commit -m "Afegida classe Camio i modificat diagrama ACT3.puml"