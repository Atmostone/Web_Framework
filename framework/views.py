def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 PAGE Not Found']
