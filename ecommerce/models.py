from django.db import models


class Basket(models.Model):
    basket_id = models.TextField(db_column='BasketId')
    product_id = models.TextField(db_column='ProductId',
                                  primary_key=True)
    user_id = models.TextField(db_column='UserId')
    is_checked_out = models.BooleanField(db_column='IsCheckedOut')

    class Meta:
        managed = False
        db_table = 'Baskets'
        unique_together = (('product_id', 'user_id', 'basket_id'),)


class Invoice(models.Model):
    basket_id = models.TextField(db_column='BasketId')
    userid = models.TextField(db_column='UserId',
                              primary_key=True)
    items = models.TextField(db_column='Items')

    class Meta:
        managed = False
        db_table = 'Invoices'
        unique_together = (('userid', 'basket_id'),)


class ProductCount(models.Model):
    asin = models.TextField(db_column='Asin', primary_key=True)
    count = models.IntegerField(db_column='Count')

    class Meta:
        managed = False
        db_table = 'ProductCounts'


class Product(models.Model):
    asin = models.CharField(max_length=200, blank=True, null=True, db_comment='TRIAL')
    title = models.CharField(max_length=1500, blank=True, null=True, db_comment='TRIAL')
    img_url = models.CharField(db_column='imgUrl', max_length=200, blank=True, null=True,
                               db_comment='TRIAL')
    product_url = models.CharField(db_column='productUrl', max_length=200, blank=True, null=True,
                                   db_comment='TRIAL')
    stars = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True, db_comment='TRIAL')
    reviews = models.BigIntegerField(blank=True, null=True, db_comment='TRIAL')
    price = models.DecimalField(max_digits=28, decimal_places=6, blank=True, null=True, db_comment='TRIAL')
    is_best_seller = models.BooleanField(db_column='isBestSeller', blank=True, null=True,
                                         db_comment='TRIAL')
    bought_in_last_month = models.BigIntegerField(db_column='boughtInLastMonth', blank=True, null=True,
                                                  db_comment='TRIAL')
    category_name = models.CharField(db_column='categoryName', max_length=200, blank=True, null=True,
                                     db_comment='TRIAL')

    class Meta:
        managed = False
        db_table = 'Products'
        db_table_comment = 'TRIAL'
