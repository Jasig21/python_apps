## Manipulation API Vélib 

Télécharger via le code les données de l'API Vélib pour faire une carte (folium) des stations (flux de localisation) en associant à chaque station le nombre de vélib disponibles lors de l'appel de l'API (flux sur le nombre de vélo disponibles). Il faut donc faire une "jointure" entre ces 2 sources.

Chaque Marker Cartographique doit permettre d'afficher une popup avec le détail des vélos disponibles.
le script doit produire un fichier HTML dont le nom contiendra la date, l'heure, les minutes et secondes de l'appel aux API (pour garder une trace de la fraicheur des données présentes dans la carte).

Les URL de l'API doivent être configurables dans un fichier de configuration.
Le fichier de configuration doit être passé au script par un argument obligatoire.

Le script doit pouvoir prendre un argument facultatif "nbmin" de type int qui sera utilisé pour filtrer les éléments de la carte et ne garder que les stations avec au moins le nombre de vélos passé en argument (vélos éléctriques ou non).

Libre à vous d'utiliser pandas ou de traiter ca avec des objets python de base (list et dic).

Documentation de l'API Vélib : 

https://www.velib-metropole.fr/donnees-open-data-gbfs-du-service-velib-metropole

