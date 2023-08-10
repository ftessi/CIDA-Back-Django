import pandas as pd
from django.shortcuts import render
from .forms import ExcelUploadForm
from .models import User, Product

def upload_excel(request):
    if request.method == 'POST':
        print('POST request received')
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('Form is valid')
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            # Process the parsed data and save it to the database
            for _, row in df.iterrows():
                username = row['username']
                password = row['password']
                privileges = row['privileges']
                email = row['email']
                refreshtoken = row['refreshtoken']

                print(f'Processing user: {username}')

                # Create a new User object and save it to the database
                user = User(
                    username=username,
                    password=password,
                    privileges=privileges,
                    email=email,
                    refreshtoken=refreshtoken
                )
                user.save()
                print(f'Saved user: {username}')

            return render(request, 'microservices/upload_success.html')

    else:
        form = ExcelUploadForm()

    print('Invalid form or GET request')
    return render(request, 'microservices/upload.html', {'form': form})



def upload_excel_products(request):
    if request.method == 'POST':
        print('POST request received')
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('Form is valid')
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)

            # Assign hardcoded values for proveedor and marca
            proveedor = 'Truper'
            marca = 'Truper'

            # Process the parsed data and save it to the database
            column = 1  # Counter to track the position of rows in the Excel file
            for _, row in df.iterrows():
                # Check if the row has only a single cell and skip it
                if row.count() == 1:
                    print(f'Skipping single-cell row at position: {column}')
                    column += 1
                    continue

                codigo = row.get('codigo', 'Sin Codigo')
                sku = row.get('SKU')
                ean = row.get('EAN ')
                categoria = row.get('CATEGORIA ')
                descripcion = row.get('DESCRIPCION DEL PRODUCTO ')
                pvp = row.get('PVP CLASSIC ')

                # print(f'Processing product: {sku}')

                # Check if any required field is empty and skip the row
                if any(
                    field is None or (isinstance(field, str) and field.strip() == '')
                    for field in (sku, ean, categoria, descripcion, pvp)
                ):
                    print(f'Skipping row with empty fields at position: {column}')
                    column += 1
                    continue

                # Create a new Product object and save it to the database
                product = Product(
                    codigo=codigo,
                    sku=sku,
                    ean=ean,
                    proveedor=proveedor,
                    categoria=categoria,
                    marca=marca,
                    descripcion=descripcion,
                    pvp=pvp
                )
                product.save()
                # print(f'Saved product: {sku}')

                column += 1

            return render(request, 'microservices/upload_success.html')

    else:
        form = ExcelUploadForm()

    print('Invalid form or GET request')
    return render(request, 'microservices/upload.html', {'form': form})