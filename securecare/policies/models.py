from django.db import models

# Create your models here.
#Policies
class Policy(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=[
            ('Active', 'Active'),
            ('Under Review', 'Under_Review'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#Quizzes
class Quiz(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='quizzes')
    question = models.CharField(max_length=300)
    option_a = models.CharField(max_length=150)
    option_b = models.CharField(max_length=150)
    option_c = models.CharField(max_length=150)
    option_d = models.CharField(max_length=150)
    correct_option = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
    )

    def __str__(self):
        return f"{self.policy.title} - {self.question[:50]}"

