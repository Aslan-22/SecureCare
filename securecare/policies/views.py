from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PolicyForm
from .models import Policy, Quiz
from django.db.models import Count

# Home Page
def home(request):
    policies = Policy.objects.filter(status='Active')
    return render(request, 'policies/index.html', {'policies': policies})

# Admin Panel
@login_required
def admin_panel(request):
    policies = Policy.objects.all()
    return render(request, 'policies/admin_panel.html', {'policies': policies})

# Add Policy
@login_required
def add_policy(request):
    form = PolicyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_panel')  # Use URL name, not template path
    return render(request, 'policies/policy_form.html', {'form': form, 'title': 'Add Policy'})

# Edit Policy
@login_required
def edit_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    form = PolicyForm(request.POST or None, instance=policy)
    if form.is_valid():
        form.save()
        return redirect('admin_panel')
    return render(request, 'policies/policy_form.html', {'form': form, 'title': 'Edit Policy'})

# Delete Policy
@login_required
def delete_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    if request.method == 'POST':
        policy.delete()
        return redirect('admin_panel')
    return render(request, 'policies/confirm_delete.html', {'policy': policy})

# Dashboard
@login_required
def dashboard(request):
    total_policies = Policy.objects.count()
    active_policies = Policy.objects.filter(status='Active').count()
    review_policies = Policy.objects.filter(status='Under Review').count()

    context = {
        'total': total_policies,
        'active': active_policies,
        'review': review_policies,
    }

    return render(request, 'policies/dashboard.html', context)

# Take Quiz
@login_required
def take_quiz(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    quizzes = policy.quizzes.all()

    if request.method == 'POST':
        score = 0
        for quiz in quizzes:
            # Ensure form input names match quiz.id
            answer = request.POST.get(str(quiz.id))
            if answer == quiz.correct_option:
                score += 1

        return render(request, 'policies/quiz_result.html', {
            'score': score,
            'total': quizzes.count(),
            'policy': policy
        })

    return render(request, 'policies/take_quiz.html', {
        'policy': policy,
        'quizzes': quizzes
    })
