# Analyse du caractère le plus fréquent pour la première colonne (clé de longueur 5)

# cat secret | fold -w 5 | cut -b 1 | sort | uniq -c | sort -n | tail -1

# Analyse des caractères les plus fréquents (clé de longueur 5)

for i in 1 2 3 4 5; do cat secret | fold -w 5 | cut -b $i | sort | uniq -c | sort -n | tail -1; done