from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from apps.estampado.models import Estampado
from apps.estampado.serializers import EstampadoSerializer
from apps.category.models import Category

from django.db.models import Q

class EstampadoDetailView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, estampadoid, format=None):
        try:
            estampado_id=int(estampadoid)
        except:
            return Response(
                {'error': 'El producto no existe'},
                status = status.HTTP_404_NOT_FOUND)
        if Estampado.objects.filter(id=estampado_id).exists():
            estampado = Estampado.objects.get(id=estampado_id)
            
            estampado = EstampadoSerializer(estampado)
            
            return Response({'product': estampado.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'El producto no existe'},
                status=status.HTTP_404_NOT_FOUND)

            
class ListEstampadoView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        sortBy = request.query_params.get('sortBy')
        
        if not (sortBy == 'artista' or sortBy == 'fecha_creacion' or sortBy == 'precio' or sortBy == 'ventas' or sortBy == 'nombre'):
            sortBy = 'fecha_creacion'
            
        order = request.query_params.get('order')
        limit = request.query_params.get('limit')

        if not limit:
            limit = 6
        
        try:
            limit = int(limit)
        except:
            return Response(
                {'error': 'Limit must be an integer'},
                status=status.HTTP_404_NOT_FOUND)
        
        if limit <= 0:
            limit = 6
            
        if order == 'desc':
            sortBy = '-' + sortBy
            estampados = Estampado.objects.order_by(sortBy).all()[:int(limit)]
        elif order == 'asc':
            estampados = Estampado.objects.order_by(sortBy).all()[:int(limit)]
        else:
            estampados = Estampado.objects.order_by(sortBy).all()
            
        estampados = EstampadoSerializer(estampados, many = True)
        
        if estampados:
            return Response ({'estampados': estampados.data}, status=status.HTTP_200_OK)
        else:
            return Response ({'error': 'No hay estampas registradas'},
                             status=status.HTTP_404_NOT_FOUND)
            
class ListSearchView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            category_id = int(data['category_id'])
        except:
            return Response(
                {'error': 'Category ID must be an integer'},
                status=status.HTTP_404_BAD_REQUEST)

        search = data['search']
        # Chequear si algo input ocurrio en la busqueda
        if len(search) == 0:
            # mostrar todos los productos si no hay input en la busqueda
            search_results = Estampado.objects.order_by('-fecha_creacion').all()
        else:
            # Si hay criterio de busqueda, filtramos con dicho criterio usando Q
            search_results = Estampado.objects.filter(
                Q(descripcion__icontains=search) | Q(nombre__icontains=search)
            )
        if category_id == 0:
                search_results = EstampadoSerializer(search_results, many=True)
                return Response(
                    {'search_products': search_results.data},
                    status=status.HTTP_200_OK)
                
        # revisar si existe categoria
        if not Category.objects.filter(id=category_id).exists():
            return Response(
                {'error': 'Category not found'},
                status=status.HTTP_404_NOT_FOUND)

        category = Category.objects.get(id=category_id)
        
        # si la categoria tiene apdre, fitlrar solo por la categoria y no el padre tambien
        if category.parent:
            search_results = search_results.order_by(
                '-fecha_creacion'
            ).filter(category=category)
        
        else:
            # si esta categoria padre no tiene hijjos, filtrar solo la categoria
            if not Category.objects.filter(parent=category).exists():
                search_results = search_results.order_by(
                    '-fecha_creacion'
                ).filter(category=category)
                
            else:
                categories = Category.objects.filter(parent=category)
                filtered_categories = [category]

                for cat in categories:
                    filtered_categories.append(cat)
                
                filtered_categories = tuple(filtered_categories)

                search_results = search_results.order_by(
                    '-fecha_creacion'
                ).filter(category__in=filtered_categories)
        
        search_results = EstampadoSerializer(search_results, many=True)
        return Response({'search_products': search_results.data}, status=status.HTTP_200_OK)
    
class ListRelatedView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, estampaId, format=None):
        try:
            estampa_id = int(estampaId)
        except:
            return Response(
                {'error': 'Product ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)
        
        # Existe estampa id
        if not Estampado.objects.filter(id=estampa_id).exists():
            return Response(
                {'error': 'Product with this product ID does not exist'},
                status=status.HTTP_404_NOT_FOUND)
            
        category = Estampado.objects.get(id=estampa_id).category

        if Estampado.objects.filter(category=category).exists():
            # Si la categoria tiene padre filtrar solo por la categoria y no el padre tambien
            if category.parent:
                related_products = Estampado.objects.order_by(
                    '-ventas'
                ).filter(category=category)
            else:
                if not Category.objects.filter(parent=category).exists():
                    related_products = Estampado.objects.order_by(
                        '-ventas'
                    ).filter(category=category)
                    
                else:
                    categories = Category.objects.filter(parent=category)
                    filtered_categories = [category]

                    for cat in categories:
                        filtered_categories.append(cat)

                    filtered_categories = tuple(filtered_categories)
                    related_products = Estampado.objects.order_by(
                        '-ventas'
                    ).filter(category__in=filtered_categories)
                
            #Excluir producto que estamos viendo
            related_products = related_products.exclude(id=estampa_id)
            related_products = EstampadoSerializer(related_products, many=True)
            
            if len(related_products.data) > 3:
                return Response(
                    {'related_products': related_products.data[:3]},
                    status=status.HTTP_200_OK)
            elif len(related_products.data) > 0:
                return Response(
                    {'related_products': related_products.data},
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'No related products found'},
                    status=status.HTTP_200_OK)
            
        else:
            return Response(
                {'error': 'No related products found'},
                status=status.HTTP_200_OK)
            
class ListBySearchView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        try:
            category_id = int(data['category_id'])
        except:
            return Response(
                {'error': 'Category ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)
        
        rango_precio = data['rango_precio']
        sort_by = data['sort_by']
        
        if not (sort_by == 'artista' or sort_by == 'fecha_creacion' or sort_by == 'precio' or sort_by == 'ventas' or sort_by == 'nombre'):
            sort_by = 'fecha_creacion'
        
        order = data['order']

        ## Si categoryID es = 0, filtrar todas las categorias
        if category_id == 0:
            product_results = Estampado.objects.all()
        elif not Category.objects.filter(id=category_id).exists():
            return Response(
                {'error': 'This category does not exist'},
                status=status.HTTP_404_NOT_FOUND)
        else:
            category = Category.objects.get(id=category_id)
            if category.parent:
                # Si la categoria tiene padrem filtrar solo por la categoria y no el padre tambien
                product_results = Estampado.objects.filter(category=category)
            else:
                if not Category.objects.filter(parent=category).exists():
                    product_results = Estampado.objects.filter(category=category)
                else:
                    categories = Category.objects.filter(parent=category)
                    filtered_categories = [category]

                    for cat in categories:
                        filtered_categories.append(cat)

                    filtered_categories = tuple(filtered_categories)
                    product_results = Estampado.objects.filter(
                        category__in=filtered_categories)

        # Filtrar por precio
        if rango_precio == '20000 - 29000':
            product_results = product_results.filter(precio__gte=20000)
            product_results = product_results.filter(precio__lt=30000)
        elif rango_precio == '30000 - 39000':
            product_results = product_results.filter(precio__gte=30000)
            product_results = product_results.filter(precio__lt=40000)
        elif rango_precio == '40000 - 59000':
            product_results = product_results.filter(precio__gte=40000)
            product_results = product_results.filter(precio__lt=60000)
        elif rango_precio == '60000 - 79000':
            product_results = product_results.filter(precio__gte=60000)
            product_results = product_results.filter(precio__lt=80000)
        elif rango_precio == 'Mas 80000':
            product_results = product_results.filter(precio__gte=80000)
        
        #Filtrar producto por sort_by
        if order == 'desc':
            sort_by = '-' + sort_by
            product_results = product_results.order_by(sort_by)
        elif order == 'asc':
            product_results = product_results.order_by(sort_by)
        else:
            product_results = product_results.order_by(sort_by)
        
        product_results = EstampadoSerializer(product_results, many=True)

        if len(product_results.data) > 0:
            return Response(
                {'filtered_products': product_results.data},
                status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'No products found'},
                status=status.HTTP_200_OK)
                
    