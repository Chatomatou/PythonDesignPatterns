# PythonDesignPatterns
_Ce dépôt regroupe les **patrons de conception** (design patterns) principaux, mis en application avec le [langage Python](https://www.python.org/)._

_Un patron de conception est un modèle permettant de résoudre un problème récurrent en informatique. Attention, il ne s'agit pas d'un algorithme qui peut être implémenté directement dans un langage de programmation divers. Voyez cela comme une représentation d'un modèle qui sera reproductible._

|NOM|DESCRIPTION|EXEMPLE D'APPLICATION|
|---|---|---|
|**Composite**|Permet de manipuler de la même manière une structure complète, une partie ou un élément unique|Dans un jeu vidéo, un inventaire (sac) est un item, qui contient lui-même d'autres items. Le sac est donc géré comme un item (récursivité)|
|**État**||Lecteur audio qui peut avoir plusieurs états (lecture, pause, arrêt, ...) et peut changer de comportement en fonction de son état|
|**Façade**|Cache la conception de systèmes complexes, souvent difficiles à comprendre en les regroupant dans un système unique et accessible|Utilisation simplifiée d'un agenda (façade) utilisant plusieurs sous-systèmes pour sa gestion (date, prise de rendez-vous, etc.)|
|**Prototype**|Définit une instance originale qui permet de créer de nouveaux objets en copiant le prototype original|Création facilitée et rendue plus rapide pour des entités similaires|
|**Singleton**|Garantit qu'une classe n'a qu'une seule instance et fournit un point d'accès depuis cette dernière, en bloquant la création d'instance supplémentaires|Instance de connexion à une base de données, pour éviter de surcharger le serveur|
