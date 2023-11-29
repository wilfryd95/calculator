def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Erreur: " + str(e)

expression = input("Entrez l'opération : ")
resultat = calculator(expression)
print("Résultat:", resultat)
