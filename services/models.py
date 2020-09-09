from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):
    """ Service Form Fields """
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254,
                           null=True,
                           blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024,
                                null=True,
                                blank=True)
    image = models.ImageField(null=True,
                              blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    """
        Service Boolean Fields: instead of listing options on the database,
        the options are listed here for service customizations.
        Option box iterates in for-loops through service details page
        and bag page via a python shell command.
        Service options can be accessed by the admin panel.
     """
    # design size options
    has_sizes = models.BooleanField(default=False,
                                    null=True,
                                    blank=True)
    # design color options
    has_colors = models.BooleanField(default=False,
                                     null=True,
                                     blank=True)
    # webdev options
    has_webdev_options = models.BooleanField(default=False,
                                             null=True,
                                             blank=True)
    # project message
    has_message = models.BooleanField(default=False,
                                      null=True,
                                      blank=True)

    def __str__(self):
        return self.name
