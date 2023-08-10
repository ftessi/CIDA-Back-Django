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
            for _, row in df.iterrows():
                if not pd.notnull(row.iloc[1:]).any() and (pd.notnull(row.iloc[0]) and not pd.notnull(row.iloc[1])):
                # Skip iteration if there is text only in the first column's cell
                    continue


                codigo = row.get('codigo', 'Sin Codigo')
                sku = row['SKU']
                ean = row['EAN']
                categoria = row['CATEGORIA']
                descripcion = row['DESCRIPCION DEL PRODUCTO']
                pvp = row['PVP CLASSIC']

                print(f'Processing product: {sku}')

                # Check if fields exist and handle them accordingly
                if pd.notnull(codigo):
                    # Field is present in the Excel file
                    codigo = str(codigo)  # Convert to string if needed
                else:
                    # Field is not present in the Excel file
                    codigo = 'Default Value'  # Assign a default value or handle it as needed

                if pd.notnull(ean):
                    # Field is present in the Excel file
                    ean = str(ean)  # Convert to string if needed
                else:
                    # Field is not present in the Excel file
                    ean = 'Default Value'  # Assign a default value or handle it as needed

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
                print(f'Saved product: {sku}')

            return render(request, 'microservices/upload_success.html')

    else:
        form = ExcelUploadForm()

    print('Invalid form or GET request')
    return render(request, 'microservices/upload.html', {'form': form})