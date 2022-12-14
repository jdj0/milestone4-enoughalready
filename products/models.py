from django.conf import settings
from django.db import models


CATEGORY_CHOICES = (
    ('SS', 'Sweatshirt'),
    ('JP', 'Jumper'),
    ('TS', 'T-shirt'),
)


SIZE_CHOICES = (
    ('XS', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
    ('6', 'Six'),
    ('8', 'Eight'),
    ('10', 'Ten'),
    ('12', 'Twelve'),
    ('14', 'Fourteen'),
    ('16', 'Sixteen'),
    ('18', 'Eighteen'),
    ('20', 'Twenty'),
)


class Item(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    size = models.CharField(choices=SIZE_CHOICES, max_length=4)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username
