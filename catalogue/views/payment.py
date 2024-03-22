#<!-- Bilal ma - Views paiement -->

from django.shortcuts import render, redirect
from catalogue.models import Cart, Order
from catalogue.forms import PaymentForm
from django.contrib.auth.decorators import login_required

# def make_payment(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             payment_method = form.cleaned_data['payment_method']
#             # Récupérer les données du panier depuis la session
#             cart_items = request.session.get('cart', {})
#             total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
#             # Créer une commande avec les détails du paiement
#             order = Order.objects.create(
#                 user=request.user,
#                 total_amount=total_price,
#                 payment_method=payment_method,
#                 payment_confirmed=False
#             )
#             # Sauvegarder la commande dans la base de données
#             order.save()

#             # Réinitialiser le panier après le paiement
#             request.session['cart'] = {}

#             # Rediriger vers la page de succès de paiement
#             return redirect('payment_success')
#     else:
#         form = PaymentForm()

#     # Afficher le formulaire de paiement avec les données du panier
#     cart_items = request.session.get('cart', {})
#     total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
#     return render(request, 'cart/payment_information.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})

# def payment_success(request):
#     # Afficher la page de succès de paiement avec un récapitulatif des informations de la commande
#     last_order = Order.objects.last()
#     return render(request, 'payment_success.html', {'order': last_order})


# def checkout_summary(request):
#     cart = Cart(request)  # Initialise le panier
#     total_price = cart.get_total_price()  # Récupère le prix total
#     cart_items = cart.cart.values()  # Récupère les articles du panier

#     return render(request, 'cart/checkout_summary.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            cart_items = request.session.get('cart', {})
            total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
            order = Order.objects.create(
                user=request.user,
                total_amount=total_price,
                payment_method=payment_method,
                payment_confirmed=False
            )
            order.save()
            request.session['cart'] = {}
            return redirect('payment_success')
    else:
        form = PaymentForm()

    cart_items = request.session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render(request, 'cart/payment_information.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})

@login_required
def payment_success(request):
    last_order = Order.objects.last()
    return render(request, 'payment_success.html', {'order': last_order})

from catalogue.models import Cart

def checkout_summary(request):
    cart = Cart(request)
    cart_items = request.session.get('cart', {})
  # Utilisation de la méthode get_items() pour obtenir les articles du panier
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render(request, 'cart/checkout_summary.html', {'cart_items': cart_items, 'total_price': total_price})