# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:03:28 2021

@author: erekz
"""

# #soru1

# string1 = 'CalculatE the nuMBer of Upper Case and Lower Case LeTTerRs in This String'

# def harf_hesapla(string):
#     b_sayac = 0
#     k_sayac = 0
#     for i in string:
#         if i.isupper():
#             b_sayac = b_sayac + 1
#         elif i.islower():
#             k_sayac = k_sayac + 1
#     print('String ifadedeki küçük harf sayısı: ' , k_sayac)
#     print('String ifadedeki büyük harf sayısı: ' , b_sayac)    
    
# harf_hesapla(string1)



# #soru2
# import numpy as np

# def Sutun_Ort_Hesapla(matris):
#     print("Matrisin sütunlarının ortalamasının listesi :",[sum(i)/5 for i in zip(*matris)])

# matris = np.random.uniform(low=0,high=1,size=(5,5))
# print("0 ve 1 arasında random olarak oluşturulmuş 5x5 Matris: \n",matris)
# Sutun_Ort_Hesapla(matris)





# #soru3

# def ekle(list1,list2):
#     for i  in list1:
#         if i not in list2:
#             list2.append(i)
#     return list2 , sum(list2)

# def main():
#     liste1=[9,6,4,3,5,8,7,12]
#     liste2=[9,5,2,6]
#     sonliste , topl_liste = ekle(liste1, liste2) 
#     print('2. Listenin son hali: ' , sonliste)
#     print('2. Listedeki değerlerin toplamı: ' , topl_liste)

# main()





#soru4

#string1 = 'termodinamik'
#string2='mukavemet'
#
#def ortakharf(str1,str2):
#    ort_lst = []
#    for i in str1:
#        if i in str2:
#            ort_lst.append(i)
#    ort_lst = set(ort_lst)
#    print('İfadeler içinde ortak bulunan karakterler: ' , ort_lst)
#    
#ortakharf(string1, string2)



# Deneme

# def sutun_ort_hesapla(a):
#     sut1 = [a[0][0] , a[1][0] , a[2][0] , a[3][0] , a[4][0]]
#     sut2 = [a[0][1] , a[1][1] , a[2][1] , a[3][1] , a[4][1]]
#     sut3 = [a[0][2] , a[1][2] , a[2][2] , a[3][2] , a[4][2]]
#     sut4 = [a[0][3] , a[1][3] , a[2][3] , a[3][3] , a[4][3]]
#     sut5 = [a[0][4] , a[1][4] , a[2][4] , a[3][4] , a[4][4]]
#     ortlist = [sum(sut1)/5 , sum(sut2)/5 , sum(sut3)/5 , sum(sut4)/5 , sum(sut5)/5]
#     return ortlist

# def main():
#     import random
    
#     b2_matris = [[] , [] , [] , [] , []]
#     for i in range(5):
#         sayi1 = random.random()
#         sayi2 = random.random()
#         sayi3 = random.random()
#         sayi4 = random.random()
#         sayi5 = random.random()
#         b2_matris[0].append(sayi1)
#         b2_matris[1].append(sayi2)
#         b2_matris[2].append(sayi3)
#         b2_matris[3].append(sayi4)
#         b2_matris[4].append(sayi5)
#     sonuc = sutun_ort_hesapla(b2_matris)
#     print('Sütunların ortalama değerleri: ' , sonuc)
    
# main()



# import random
    
# b2_matris = [[] , [] , [] , [] , []]
# for i in range(5):
#     sayi1 = random.random()
#     sayi2 = random.random()
#     sayi3 = random.random()
#     sayi4 = random.random()
#     sayi5 = random.random()
#     b2_matris[0].append(sayi1)
#     b2_matris[1].append(sayi2)
#     b2_matris[2].append(sayi3)
#     b2_matris[3].append(sayi4)
#     b2_matris[4].append(sayi5)
# print(b2_matris)

