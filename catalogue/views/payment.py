#<!-- Bilal ma - Views paiement -->

from django.shortcuts import render, redirect, get_object_or_404
from catalogue.models import Cart, Order, Show
from catalogue.forms import PaymentForm
from django.contrib.auth.decorators import login_required

# @login_required
# def make_payment(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             payment_method = form.cleaned_data['payment_method']
#             cart_items = request.session.get('cart', {})
#             total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
            
#             # Créer une nouvelle commande
#             order = Order.objects.create(
#                 user=request.user,
#                 total_amount=total_price,
#                 payment_method=payment_method,
#                 payment_confirmed=False
#             )

#             # Ajouter les articles à la commande
#             for item_id, item_info in cart_items.items():
#                 show = Show.objects.get(pk=item_id)
#                 quantity = item_info['quantity']
#                 # Ajouter l'élément à la relation many-to-many
#                 order.ordered_items.add(show, through_defaults={'quantity': quantity})

#             # Vider le panier après la commande
#             request.session['cart'] = {}

#             # Rediriger l'utilisateur vers la vue de paiement réussi avec l'ID de la commande
#             return redirect('catalogue:payment_success')
#     else:
#         form = PaymentForm()

#     cart_items = request.session.get('cart', {})
#     total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
#     return render(request, 'cart/payment_information.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})

@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_method = form.cleaned_data['payment_method']
            cart_items = request.session.get('cart', {})
            
            # Calculer le prix total pour chaque article dans le panier
            total_price = 0
            for item_id, item_info in cart_items.items():
                show = Show.objects.get(pk=item_id)
                item_info['price'] = show.price  # Mettre à jour le prix de l'article avec le prix du spectacle actuel
                item_info['total_price'] = item_info['quantity'] * item_info['price']
                total_price += item_info['total_price']

            # Créer une nouvelle commande
            order = Order.objects.create(
                user=request.user,
                total_amount=total_price,
                payment_method=payment_method,
                payment_confirmed=False
            )

            # Ajouter les articles à la commande
            for item_id, item_info in cart_items.items():
                show = Show.objects.get(pk=item_id)
                quantity = item_info['quantity']
                # Ajouter l'élément à la relation many-to-many
                order.ordered_items.add(show, through_defaults={'quantity': quantity})

            # Vider le panier après la commande
            request.session['cart'] = {}

            # Rediriger l'utilisateur vers la vue de paiement réussi avec l'ID de la commande
            return redirect('catalogue:payment_success')
    else:
        form = PaymentForm()

    cart_items = request.session.get('cart', {})
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render(request, 'cart/payment_information.html', {'form': form, 'cart_items': cart_items.values(), 'total_price': total_price})


# Billy Ma - Hostirque de commande & détaille de celle ci
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'cart/order_detail.html', {'order': order})


@login_required
def order_history(request):
    # Récupérer l'historique des commandes de l'utilisateur connecté
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'cart/order_history.html', {'orders': orders})


@login_required
def payment_success(request):
    last_order = Order.objects.last()
    return render(request, 'cart/payment_success.html', {'order': last_order})

def checkout_summary(request):
    cart = Cart(request)
    cart_items = request.session.get('cart', {})
  # Utilisation de la méthode get_items() pour obtenir les articles du panier
    total_price = sum(item['quantity'] * item['price'] for item in cart_items.values())
    return render(request, 'cart/checkout_summary.html', {'cart_items': cart_items, 'total_price': total_price})