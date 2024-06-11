from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)

def trigger_500(request):
        # 500エラーを強制的に発生させる
    raise Exception("This is a test exception to trigger a 500 error")