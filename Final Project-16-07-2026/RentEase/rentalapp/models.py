from django.db import models


# ==========================
# COUNTRY MODEL
# ==========================

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['country_name']
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country_name


# ==========================
# STATE MODEL
# ==========================

class State(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='states'
    )

    state_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['state_name']

    def __str__(self):
        return self.state_name


# ==========================
# CITY MODEL
# ==========================

class City(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cities'
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='cities'
    )

    city_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['city_name']

    def __str__(self):
        return self.city_name


# ==========================
# OWNER MODEL
# ==========================

class Owner(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='owners'
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='owners'
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='owners'
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    profile_image = models.ImageField(upload_to='owners/')
    id_proof = models.ImageField(upload_to='owner_documents/')

    experience = models.PositiveIntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


# ==========================
# TENANT MODEL
# ==========================

class Tenant(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='tenants'
    )

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='tenants'
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='tenants'
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)

    profile_image = models.ImageField(upload_to='tenants/')

    occupation = models.CharField(max_length=100)
    family_members = models.PositiveIntegerField(default=1)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

# ==========================
# PROPERTY CATEGORY MODEL
# ==========================

class PropertyCategory(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.category_name


# ==========================
# AMENITY MODEL
# ==========================

class Amenity(models.Model):
    amenity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.amenity_name


# ==========================
# PROPERTY MODEL
# ==========================

class Property(models.Model):

    PROPERTY_TYPE = (
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('PG', 'PG'),
        ('Room', 'Room'),
        ('Office', 'Office'),
    )

    STATUS = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
        ('Unavailable', 'Unavailable'),
    )

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE)

    address = models.TextField()

    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)

    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()

    furnishing = models.CharField(max_length=100)

    area_sqft = models.PositiveIntegerField()

    available_from = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Available'
    )

    property_image = models.ImageField(upload_to='properties/')

    amenities = models.ManyToManyField(Amenity)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# ==========================
# BOOKING MODEL
# ==========================

class Booking(models.Model):

    BOOKING_STATUS = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    )

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    booking_status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS,
        default='Pending'
    )

    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant} - {self.property}"


# ==========================
# PAYMENT MODEL
# ==========================

class Payment(models.Model):

    PAYMENT_METHOD = (
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('Net Banking', 'Net Banking'),
        ('Cash', 'Cash'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True
    )

    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id


# ==========================
# REVIEW MODEL
# ==========================

class Review(models.Model):

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField()

    review = models.TextField()

    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property} ({self.rating}★)"

# ==========================
# PROPERTY IMAGE MODEL
# ==========================

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to='property_gallery/')

    def __str__(self):
        return f"Image - {self.property.title}"


# ==========================
# WISHLIST MODEL
# ==========================

class Wishlist(models.Model):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant} - {self.property}"


# ==========================
# CONTACT MESSAGE MODEL
# ==========================

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject