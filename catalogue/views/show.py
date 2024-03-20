# Bilal Ma - reservations\catalogue\views\show.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseBadRequest
from catalogue.models import Show, Cart
from django.contrib import messages

def index(request):
     # Récupérer uniquement les spectacles réservables + fltre
    shows = Show.objects.filter(bookable=True)
    title = 'Liste des spectacles réservables'
    
    return render(request, 'show/index.html', {
        'shows': shows,
        'title': title
    })

#Bilal Maayoud - Show/show.html

def show(request, show_id=None):
    if show_id:
        try:
            show = Show.objects.get(id=show_id)
        except Show.DoesNotExist:
            raise Http404('Spectacle inexistant')
        title = "Fiche d'un spectacle"
        return render(request, 'show/show.html', {'show': show, 'title': title})
    else:
        # Si aucun show_id n'est fourni, affichez la liste de tous les spectacles
        shows = Show.objects.filter(bookable=True)
        title = 'Liste des spectacles'
        return render(request, 'show/index.html', {'shows': shows, 'title': title})

#Bm - add au pannier un spectacle/ add,delet,remove,ect...

def add_to_cart(request, pk):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        try:
            show = Show.objects.get(pk=pk)
        except Show.DoesNotExist:
            raise Http404('Spectacle inexistant')
        cart = Cart(request)
        cart.add(show, quantity)
        messages.success(request, f"{quantity} {show.title}(s) added to your cart.")
        return redirect('catalogue:show_index')
    else:
        return HttpResponseBadRequest("Méthode non autorisée")

def view_cart(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

def remove_from_cart(request, pk):
    if request.method == 'POST':
        show = get_object_or_404(Show, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        cart = Cart(request)
        cart.remove(show, quantity)
        messages.success(request, f"{quantity} {show.title}(s) removed from your cart.")
        return redirect('catalogue:view_cart')
    else:
        return HttpResponseBadRequest("Méthode non autorisée")

# Bm - add au pannier un spectacle/ add,delet,remove,ect...
class Cart:
    def __init__(self, request):
        """
        Initialise un nouveau panier.
        
        :param request: L'objet requête Django.
        """
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, show, quantity):
        """
        Ajoute un spectacle au panier ou met à jour la quantité si le spectacle est déjà présent.
        
        :param show: L'objet Show à ajouter au panier.
        :param quantity: La quantité du spectacle à ajouter.
        """
        show_id = str(show.id)
        if show_id not in self.cart:
            self.cart[show_id] = {'quantity': quantity, 'title': show.title, 'price': float(show.price)}
        else:
            self.cart[show_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Enregistre le panier en marquant la session comme modifiée.
        """
        self.session.modified = True

    def __iter__(self):
        """
        Itère sur les éléments du panier.
        """
        show_ids = self.cart.keys()
        shows = Show.objects.filter(id__in=show_ids)
        for show in shows:
            self.cart[str(show.id)]['show'] = show

        for item in self.cart.values():
            item['total_price'] = item['quantity'] * item['price']
            yield item

    def __len__(self):
        """
        Renvoie le nombre total d'articles dans le panier.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Renvoie le prix total du panier.
        """
        return sum(item['quantity'] * item['price'] for item in self.cart.values())

    def clear(self):
        """
        Supprime tous les éléments du panier.
        """
        del self.session['cart']
        self.save()

    def remove(self, show, quantity):
        """
        Supprime une quantité donnée du spectacle du panier.

        :param show: L'objet Show à supprimer du panier.
        :param quantity: La quantité du spectacle à supprimer.
        """
        show_id = str(show.id)
        if show_id in self.cart:
            if quantity >= self.cart[show_id]['quantity']:
                del self.cart[show_id]
            else:
                self.cart[show_id]['quantity'] -= quantity
            self.save()

