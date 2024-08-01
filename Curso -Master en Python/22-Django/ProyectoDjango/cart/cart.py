from django.conf import settings
from fonluz.models import Article
from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, article, quantity=1, override_quantity=False):
        article_id = str(article.id)
        if article_id not in self.cart:
            self.cart[article_id] = {
                'quantity':0,
                'price':str(article.price)
            }
        if override_quantity:
            self.cart[article_id]['quantity'] = quantity
        else:
            self.cart[article_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, article):
        article_id = str(article.id)
        if article_id in self.cart:
            del self.cart[article_id]
            self.save()

    def __iter__(self):
        articles_ids = self.cart.keys()
        articles = Article.objects.filter(id__in=articles_ids)
        cart = self.cart.copy()
        for article in articles:
            cart[str(article.id)]['article'] = article.toJSON()
        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = (item['price'] * item['quantity']).__round__(2)
            item['quantity'] = str(item['quantity'])
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * int(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __str__(self):
        return f'{self.cart}'
