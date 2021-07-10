# nom, prix, ingredients, végétarirenne


# Classe PIZZAS
class Pizza:
    def __init__(self, nom, prix, ingredients, vegetarienne= False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne



# Affichage
    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = " - Végétarienne"
        print(f"PIZZA {self.nom} : {self.prix} €" + veg_str)
        print(", ".join(self.ingredients))
        print("==================================================================================")
        print()


# Classe de la pizza personalisée
class pizzaPersonnalisee(Pizza):
    PRIX_DE_BASE = 6
    PRIX_PAR_INGREDIENT = 2
    dernier_numero = 0


    def __init__(self):
        # le numero des pizza ajoutés
        pizzaPersonnalisee.dernier_numero += 1
        self.numero = pizzaPersonnalisee.dernier_numero

        # appel du constructeur parrent avec super
        super().__init__("Personaliser " + str(self.numero), 0, [])

        # demander a l'utilisateur d'ajouter des ingredients
        self.demander_ingredients_utilissateur()

        # ic j'appelle ma foction calculer le prix
        self.calculer_le_prix()




        # ici je demande à l'utilisateur d'ajouter les ingredients
    def demander_ingredients_utilissateur(self):
        print()

        # ingrédient de la pizza personalisée
        print(f"Ingrédients pour la pizza personnalisée N°{self.numero}")

        # ici je fait toujour boucler
        while True:
            ingredient = input("Ajoutez un ingrédient ( ou ENTER pour terminer) : ")

            # ici c'est ma condition de sortie
            if ingredient == "":
                return
            self.ingredients.append(ingredient)

        # ici j'affiche le nombre d'ingrédient ajouter
            print(f"Vous avez {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")



    def calculer_le_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients) * self.PRIX_PAR_INGREDIENT




# triage de pizza par odre alphabetique avec sort
pizzas = [
    Pizza("4 fromages", 9.5, ("brie", "emmental", "compté", "parmesan"),True),
    Pizza("végétarienne", 8.5, ("melanzana", "peperoni", "zucchina","mozzarella"), True),
    Pizza("hawai", 10.5, ("mozzarella", "peperoni", "salame", "pomodore")),
    Pizza("calzone", 11, ("mozzarella", "fungi", "zucchine", "parmesan")),
    Pizza("4 saisons", 8, ("mozzarella", "olive", "zucchine", "parmesan", "cipolla")),
    pizzaPersonnalisee(),
    pizzaPersonnalisee()
]



# ici je cré mon élement
def tri(e):
    #return e.nom
    # return e.prix
    return len(e.ingredients)


# fonction sort
# pizzas.sort(key=tri)
# pizzas.sort(key=tri, reverse=True)



# Boucle
for i in pizzas:
    i.Afficher()



