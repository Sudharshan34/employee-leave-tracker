from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LeaveRequestForm
from .models import LeaveRequest
from django.core.exceptions import PermissionDenied

@login_required
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user
            leave.save()
            return redirect('my_leaves')
    else:
        form = LeaveRequestForm()
    return render(request, 'leaves/apply_leave.html', {'form': form})

@login_required
def my_leaves(request):
    leaves = LeaveRequest.objects.filter(employee=request.user).order_by('-applied_on')
    return render(request, 'leaves/my_leaves.html', {'leaves': leaves})
def is_manager_or_admin(user):
    if user.is_authenticated and user.role in ['manager', 'admin']:
        return True
    raise PermissionDenied

@login_required
@login_required
def manage_leaves(request):
    if request.user.role not in ['manager', 'admin']:
        return render(request, '403.html', status=403)
    leaves = LeaveRequest.objects.filter(status='pending').order_by('-applied_on')
    return render(request, 'leaves/manage_leaves.html', {'leaves': leaves})
@login_required
def update_leave_status(request, leave_id, new_status):
    if request.user.role not in ['manager', 'admin']:
        return render(request, '403.html', status=403)
    leave = get_object_or_404(LeaveRequest, id=leave_id)

    if new_status == 'approved' and leave.status != 'approved':
        days = (leave.end_date - leave.start_date).days + 1
        emp = leave.employee
        if leave.leave_type == 'sick':
            emp.sick_leave_balance = max(0, emp.sick_leave_balance - days)
        elif leave.leave_type == 'casual':
            emp.casual_leave_balance = max(0, emp.casual_leave_balance - days)
        elif leave.leave_type == 'earned':
            emp.earned_leave_balance = max(0, emp.earned_leave_balance - days)
        emp.save()

    leave.status = new_status
    leave.reviewed_by = request.user
    leave.save()
    return redirect('manage_leaves')

@login_required
def dashboard(request):
    if request.user.role in ['manager', 'admin']:
        return redirect('manage_leaves')
    return redirect('my_leaves')