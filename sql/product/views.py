from django.db import connection
from django.shortcuts import render
from .models import Product
from django.shortcuts import render
from .models import Product

def search_products(request):
    query = request.GET.get('query', '').lower()
    products = []

    if query:
        sql = f"SELECT * FROM product WHERE lower(category) LIKE '%%{query}%%';"
        for p in Product.objects.raw(sql):
            products.append(p)
    else:
        products = Product.objects.all()

    return render(request, 'search_products.html', {'products': products})

# '; DELETE FROM product; --











# # parameterized query
# def search_products(request):
#     query = request.GET.get('query', '').lower()
#     products = []

#     if query:
#         # Using a parameterized query to avoid SQL injection
#         sql = "SELECT * FROM product WHERE lower(category) LIKE %s;"
#         with connection.cursor() as cursor:
#             cursor.execute(sql, [f"%{query}%"])
#             rows = cursor.fetchall()
#             print(rows,'\n')
           
            
#             for row in rows:
#                 products.append({
#                     'id': row[0],         
#                     'name': row[1],       
#                     'price': row[2],
#                     'description': row[3],
#                     'stock': row[4],
#                     'category': row[5],
#                     'created_at': row[6],
#                 })
#     else:
#         # Use ORM for all results if no query
#         products = Product.objects.all()

#     return render(request, 'search_products.html', {'products': products})











# # django orm
# def search_products(request):
#     query = request.GET.get('query', '')
#     products = []

#     if query:
#         # Securely filter using Django ORM with case-insensitive matching
#         products = Product.objects.filter(category__icontains=query)
#     else:
#         products = Product.objects.all()

#     return render(request, 'search_products.html', {'products': products})

