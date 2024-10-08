import math

# Définition des fonctions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erreur : Division par zéro."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Erreur : Racine carrée d'un nombre négatif."
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0:
        return "Erreur : Logarithme d'un nombre non positif."
    return math.log(x, base)

# Fonction principale
def calculator():
    print("Sélectionnez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Racine carrée")
    print("7. Logarithme")

    # Remplacer les inputs par des valeurs fixes pour le test
    test_choices = ['1', '2', '3', '4', '5', '6', '7', 'q']
    for choice in test_choices:
        print(f"Test avec le choix : {choice}")
        
        if choice == 'q':
            print("Au revoir!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = 5  # Valeur fixe pour le test
            num2 = 3  # Valeur fixe pour le test

            if choice == '1':
                print("Résultat :", add(num1, num2))
            elif choice == '2':
                print("Résultat :", subtract(num1, num2))
            elif choice == '3':
                print("Résultat :", multiply(num1, num2))
            elif choice == '4':
                print("Résultat :", divide(num1, num2))
            elif choice == '5':
                print("Résultat :", power(num1, num2))

        elif choice == '6':
            num = 16  # Valeur fixe pour le test
            print("Résultat :", square_root(num))

        elif choice == '7':
            num = 10  # Valeur fixe pour le test
            base = 10  # Valeur fixe pour le test
            print("Résultat :", logarithm(num, base))

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    calculator()
