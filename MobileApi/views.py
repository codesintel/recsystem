from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import RecommendedItems
from rest_framework.views import APIView
from .serializers import RecommendedItemsSerializer
#from mysite import settings as stcd
import smtplib
import turicreate as tc
from RecSystem import settings as st
import os
# Create your views here.


class ItemsUserApi(APIView):
    def get(self,request):
        x=RecommendedItems()
        ProductsId=[]
        x.id=123
        x.ItemID="111"
        filepath=os.path.join(st.PROJECT_ROOT, 'my_model.model')
        model=tc.load_model(filepath)
        recommendations = model.recommend()
        ids=recommendations['movieId']
        i=1
        for k in ids:
            x=RecommendedItems()
            x.id=i
            x.ProductId=str(k)            
            ProductsId.append(x)
            i+=1
            if i==100:
                break
        #model.save(st.STATIC_ROOT+"/" +"hello1.model")
        serializer=RecommendedItemsSerializer(ProductsId,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class ItemsUserSpecificApi(APIView):
    def post(self,request):
        userId=request.data['user_id']
        x=RecommendedItems()
        ProductsId=[]
        x.id=123
        x.ItemID="111"
        filepath=os.path.join(st.STATIC_ROOT, 'my_model.model')
        model=tc.load_model(filepath)
        recommendations = model.recommend(users=[int(userId)])
        ids=recommendations['movieId']
        i=1
        for k in ids:
            x=RecommendedItems()
            x.id=i
            x.ProductId=str(k)            
            ProductsId.append(x)
            i+=1
            if i==100:
                break
        #model.save(st.STATIC_ROOT+"/" +"hello1.model")
        serializer=RecommendedItemsSerializer(ProductsId,many=True)
        return Response(serializer.data)





