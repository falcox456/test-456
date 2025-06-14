from django.db import models
from django.contrib.auth.models import User

# # class ContactMessage(models.Model):
# #     name = models.CharField(max_length=100)
# #     email = models.EmailField()
# #     password1 = models.IntegerField()
# #     password2 = models.IntegerField()
#
#     def __str__(self):
#         return f'Message from {self.name}'

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.title} — {self.date}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=500)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'portfolio')

    def __str__(self):
        return f"{self.user.username} о {self.ticket.title}: {self.rating}★"

