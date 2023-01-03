from tkinter import Label,Tk,SUNKEN
import tkinter as tk
from tkinter import ttk #pour le Treeview
from tkinter import Canvas
from PIL import Image, ImageTk #pour le bg
from calendar import month_name #pour le combobox
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
from itertools import combinations
from collections import Counter   


def traitmenMois(chemin):
    #lire les donnees csv ppour le mois
    MData = pd.read_csv('C:/Users/ANIS/Desktop/Sales_Data/'+chemin)
    #dataframe 
    dataM=pd.DataFrame(MData)
    #supp des donnees nan
    dataM.dropna(inplace=True)
    #supp des ligne non chiffre
    dataM=dataM.drop(dataM.loc[dataM['Order Date'] == "Order Date", :].index)
    #changement de type
    dataM['Quantity Ordered'] = dataM['Quantity Ordered'].astype('int')
    dataM['Price Each'] = pd.to_numeric(dataM['Price Each'])
    dataM['Order Date'] = pd.to_datetime(dataM['Order Date'])
    #par ordre de date
    dataM= dataM.sort_values('Order Date',ascending=False)
    return dataM
def month_changed(event):
    
       
       # handle the month changed event    
    if selected_month.get()=="January":
         dataM=dataJanuary
    else:
        if selected_month.get()=="February":
            dataM=dataFebruary          
        else:
            if selected_month.get()=="March":
                dataM=dataMars               
            else:
                if selected_month.get()=="April":
                    dataM=dataApril
                else:
                    if selected_month.get()=="May":
                        dataM=dataMay                        
                    else:
                        if selected_month.get()=="June":
                            dataM=dataJune                            
                        else:
                            if selected_month.get()=="July":
                                dataM=dataJuly                           
                            else:
                                if selected_month.get()=="August":
                                    dataM=dataAugust                               
                                else:
                                    if selected_month.get()=="September":
                                        dataM=dataSeptember
                                    else:
                                        if selected_month.get()=="October":
                                            dataM=dataOctober
                                        else:
                                            if selected_month.get()=="November":
                                                dataM=dataNovember
                                            else:
                                                if selected_month.get()=="December":
                                                    dataM=dataDecember
                       
    l1=list(dataM)
    rset=dataM.to_numpy().tolist()
    table=ttk.Treeview(fenetre,selectmode='browse') #mode navigation
    table.place(x =600, y = 150, width=700,height=400)
    table['height']=5
    table['show']='headings'
    #d'ou les colomn viendrant
    table['columns']=l1
    #deffenir la longeur de colomn
    for i in l1:
        table.column(i, width=100,anchor='c')
        table.heading(i, text=i)
    sl=0
    for j in rset:  #ajout des donnees
        v=[r for r in j] #il cree une liste dans j
        table.insert('', 'end', iid=sl,values=v)
        sl+=1   
    table.column(5, width=200)
    
def nom_ville(addresse):
  return addresse.split(',')[1].strip() #avoire la premiere valeur apres la, sans espace
 
def btn1():
    def btn11(button,datamois):
        fenetre1.geometry("700x550+300+100")
        button.place_forget()
        
        lbdetails = Label(fenetre1, text='♦Voici la liste des mois ainsi que leurs chiffre daffaire: ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place(x=100,y=190)
        
        fenetre1.resizable(False,False)
        fenetre1.config(bg="black")
         
        l1=list(datamois)
        rset=datamois.to_numpy().tolist()
        table=ttk.Treeview(fenetre1,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        #d'ou les colomn viendrant
        table['columns']=l1
        #deffenir la longeur de colomn
        for i in l1:
            table.column(i, width=100,anchor='c')
            table.heading(i, text=i)
            sl=0
            table.tag_configure('orange', background="#FFFAFA")
        for j in rset:  #ajout des donnees 
            v=[r for r in j] #il cree une liste dans j
            table.insert('', 'end', iid=sl,values=v,)
            sl+=1
    #ma fenetre
    fenetre1 = Tk()
    fenetre1.title(" info meilleur mois de vente")
    fenetre1.geometry("700x250+300+100")
    fenetre1.resizable(False,False)
    fenetre1.config(bg="black")
    can= Canvas(fenetre1,width=700,height=300,highlightthickness=0,background="black")
    can.place(x=0,y=0)

    can.create_text(120, 10,font=("Sans Serif",25),fill="#FF4500" ,anchor = "nw",text="Analyse des données par ventes ")#x y
    can.create_line(200 ,55,500,55,fill="white")
    selection = str(moismax) +' est le meilleur mois de vente, avec un chiffre daffaires de \n\n'+str(maxchif)
    lbtitre = Label(fenetre1, text=selection ,font=("Arial",16), 
                    background="black",foreground="white")
    lbtitre.place(x=25,y=100)

    bt= tk.Button(fenetre1, text= "Afficher plus de détails", font= ("Arial",12),
                    background ="#FF4500", foreground="white",  command=lambda: btn11(bt,datamois))
    bt.place(x=260,y=200) 
    
    fenetre1.mainloop()
    

    



def chiffredaff_parville(liste,listville):
    
    dchiffreparville=pd.DataFrame(columns = ['Mois' ,'ville', 'chiffre daffaire'])
    
    loc=0
    for i in range(0,12):
        for j in range(0,9):
            dm=liste[i].loc[liste[i]['ville']==listville[j]]
            dchiffreparville.loc[loc]=[month_name[i+1],listville[j],
                                       sum(dm['chiffre daffaire'])]
            loc+=1
    
    return dchiffreparville

def chiffredaff_global(dchiffreparville,listville):#df c'est dchiffreparville
    dchiffrevilleglobal=pd.DataFrame(columns = ['ville', 'chiffre daffaire'])
    loc=0
    for j in range(0,9):
        dg=dchiffreparville.loc[dchiffreparville['ville']==listville[j]]
        dchiffrevilleglobal.loc[loc]=[listville[j],sum(dg['chiffre daffaire'])]
        loc+=1
    return dchiffrevilleglobal

def btn2():
    def btn22(button):
        def table_ville_vente2(df):
            
            bt2= tk.Button(fenetre2, text= "graphe associ", font= ("Arial",12),
                           background ="#FF4500", foreground="white",  command=lambda: btn2(bt))
            bt2.place(x=270,y=500)
            
            if var.get()==1:
                montreeveiw2(fenetre2, df)
                
                
            else:
                montreeveiw2(fenetre2, df)
                bt2.place_forget()

        fenetre2.geometry("700x550+300+100")
        button.place_forget()     
        table=ttk.Treeview(fenetre2,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        
        lbdetails = Label(fenetre2, text='♦Sélectionner la façon dont vous voulez visualiser vos données: ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place(x=100,y=190)
         
        
        var=tk.IntVar()
        case_cocher1 =  tk.Radiobutton(fenetre2 ,text = "global",background='white',indicatoron=0,selectcolor='#FF4500',
                                       variable=var,value=1, command=lambda:table_ville_vente2(dg2))
        case_cocher1.place(x=470,y=190)
        case_cocher2 =  tk.Radiobutton(fenetre2, text = "par mois",background='white',indicatoron=0,selectcolor='#FF4500',
                                    variable=var ,value=2, command=lambda:table_ville_vente2(dm2))
        case_cocher2.place(x=520,y=190)
        
    def montreeveiw2(fenetre,df):
        
        
        l1=list(df)
        rset=df.to_numpy().tolist()
        table=ttk.Treeview(fenetre2,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        #d'ou les colomn viendrant
        table['columns']=l1
        #deffenir la longeur de colomn
        for i in l1:
            table.column(i, width=100,anchor='c')
            table.heading(i, text=i)
        sl=0
        table.tag_configure('orange', background="#FFFAFA")
        for j in rset:  #ajout des donnees
            v=[r for r in j] #il cree une liste dans j
            table.insert('', 'end', iid=sl,values=v)
            sl+=1
    
    dm2=chiffredaff_parville(liste,listville)
    dg2=chiffredaff_global(dm2,listville)
    
    
    maxchif=dg2['chiffre daffaire'].max()
    for i in range(0,9) :
        if dg2.loc[i]['chiffre daffaire']==maxchif :
            moismax = dg2.loc[i]['ville']
            
    fenetre2 = Tk()
    fenetre2.title(" info meilleur mois de vente")
    fenetre2.geometry("700x250+300+100")
    fenetre2.resizable(False,False)
    fenetre2.config(bg="black")
    can= Canvas(fenetre2,width=700,height=300,highlightthickness=0,background="black")
    can.place(x=0,y=0)

    can.create_text(120, 10,font=("Sans Serif",25),fill="#FF4500" ,anchor = "nw",text="Analyse des données par ventes ")#x y
    can.create_line(200 ,55,500,55,fill="white")
    
    selection = str(moismax) +'est le meilleur mois de vente, avec un chiffre daffaires de \n\n'+str(maxchif)

    lbtitre = Label(fenetre2, text=selection ,font=("Arial",16), 
                    background="black",foreground="white")
    lbtitre.place(x=10,y=100)

    bt= tk.Button(fenetre2, text= "Afficher plus de détails", font= ("Arial",12),
                  background ="#FF4500", foreground="white",  command=lambda: btn22(bt))
    bt.place(x=260,y=200) 
    bt.grid_forget()
    fenetre2.mainloop()
    

def btn3():
    def btn33(button):
        def table_ville_vente3(df):
            
            
            bt2= tk.Button(fenetre3, text= "graphe associ", font= ("Arial",12),
                          background ="#FF4500", foreground="white")
            
            
            if var.get()==1:
                montreeveiw3(fenetre3, df)
                bt2.place(x=270,y=500)
                
            else:
                montreeveiw3(fenetre3, df)
                bt2.place_forget()

        fenetre3.geometry("700x550+300+100")
        button.place_forget()
        
        lbdetails = Label(fenetre3, text='♦Voici la liste des mois ainsi que leurs chiffre daffaire: ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place()     
        table=ttk.Treeview(fenetre3,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        
        lbdetails = Label(fenetre3, text='♦Sélectionner la façon dont vous voulez visualiser vos données: ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place(x=100,y=190)
         
        
        var=tk.IntVar()
        case_cocher1 =  tk.Radiobutton(fenetre3 ,text = "global",background='white',indicatoron=0,selectcolor='#FF4500',
                                       variable=var,value=1, command=lambda:table_ville_vente3(dg2))
        case_cocher1.place(x=470,y=190)
        case_cocher2 =  tk.Radiobutton(fenetre3, text = "par mois",background='white',indicatoron=0,selectcolor='#FF4500',
                                    variable=var ,value=2, command=lambda:table_ville_vente3(dm2))
        case_cocher2.place(x=520,y=190)
        
    def montreeveiw3(fenetre,df):
        
        
        l1=list(df)
        rset=df.to_numpy().tolist()
        table=ttk.Treeview(fenetre3,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        #d'ou les colomn viendrant
        table['columns']=l1
        #deffenir la longeur de colomn
        for i in l1:
            table.column(i, width=100,anchor='c')
            table.heading(i, text=i)
        sl=0
        table.tag_configure('orange', background="#FFFAFA")
        for j in rset:  #ajout des donnees
            v=[r for r in j] #il cree une liste dans j
            table.insert('', 'end', iid=sl,values=v)
            sl+=1
            
    dm2=chiffre_hourparmois(liste)
    dg2=chiffre_hourglobal(dm2)
    
    maxchif=dg2['chiffre daffaire'].max()
    for i in range(0,24) :
        if dg2.loc[i]['chiffre daffaire']==maxchif :
            hourmax = dg2.loc[i]['heure']
            
    fenetre3 = Tk()
    fenetre3.title(" info meilleur mois de vente")
    fenetre3.geometry("700x250+300+100")
    fenetre3.resizable(False,False)
    fenetre3.config(bg="black")
    can= Canvas(fenetre3,width=700,height=300,highlightthickness=0,background="black")
    can.place(x=0,y=0)

    can.create_text(120, 10,font=("Sans Serif",25),fill="#FF4500" ,anchor = "nw",text="Analyse des données par ventes ")#x y
    can.create_line(200 ,55,500,55,fill="white")
    
#    selection = str(hourmax) +'est la meilleur heure de pub, avec un chiffre daffaires de \n\n'+str(maxchif)
    selection = 'On devrait afficher la publicité entre 10 et 11 et entre 18 et 19\n le nombre de vente augmente dans ces laps de temps' 
    lbtitre = Label(fenetre3, text=selection ,font=("Arial",16), 
                    background="black",foreground="white")
    lbtitre.place(x=40,y=100)

    bt= tk.Button(fenetre3, text= "Afficher plus de détails", font= ("Arial",12),
                  background ="#FF4500", foreground="white",  command=lambda: btn33(bt))
    bt.place(x=260,y=200) 
    bt.grid_forget()
    fenetre3.mainloop()


def chiffre_hourparmois(liste):
    dchiffreparheure=pd.DataFrame(columns = ['Mois','heure' ,'la quantité de produit vendu', 'chiffre daffaire'])
    loc=0
    for i in range(0,12):
        for j in range(0,24):
            dh=liste[i].loc[liste[i]['heure']==j]
            dchiffreparheure.loc[loc]=[month_name[i+1] ,j,sum(dh['Quantity Ordered']),sum(dh['chiffre daffaire'])]
            loc+=1
    return dchiffreparheure

def chiffre_hourglobal(dchiffreparheure):
    dchiffreheureglobal=pd.DataFrame(columns = ['heure','la quantité de produit vendu', 'chiffre daffaire'])
    loc=0
    for j in range(0,24):
        dg=dchiffreparheure.loc[dchiffreparheure['heure']==j]
        dchiffreheureglobal.loc[loc]=[int(j),sum(dg['la quantité de produit vendu']),sum(dg['chiffre daffaire'])]
        loc+=1
    return dchiffreheureglobal

def btn4():
    def btn44(button,dfproduitplusvendu):
        fenetre4.geometry("700x550+300+100")
        button.place_forget()
        
        lbdetails = Label(fenetre4, text='♦Voici la liste des produits les plus vendu ensemble pour chaque mois : ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place(x=100,y=190)
         
        l1=list(dfproduitplusvendu)
        rset=dfproduitplusvendu.to_numpy().tolist()
        table=ttk.Treeview(fenetre4,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        #d'ou les colomn viendrant
        table['columns']=l1
        #deffenir la longeur de colomn
        for i in l1:
            table.column(i, width=100,anchor='c')
            table.heading(i, text=i)
        sl=0
        table.tag_configure('orange', background="#FFFAFA")
        for j in rset:  #ajout des donnees
            v=[r for r in j] #il cree une liste dans j
            table.insert('', 'end', iid=sl,values=v)
     
            sl+=1
    count = Counter()
    dfproduitplusvendu=produit_pasmois(liste)
    count = Counter()

    for i in range(0,12):
        for achat in dfproduitplusvendu.loc[i]['Liste dees produits souvent achetés ensemble']:
            products = achat.split(';')
            count.update(Counter(combinations(products, 2)))
            dfproduitplusvendu.loc[i]['Liste dees produits souvent achetés ensemble']=count.most_common(1)
    
    fenetre4 = Tk()
    fenetre4.title(" info meilleur mois de vente")
    fenetre4.geometry("700x250+300+100")
    fenetre4.resizable(False,False)
    fenetre4.config(bg="black")
    can= Canvas(fenetre4,width=700,height=300,highlightthickness=0,background="black")
    can.place(x=0,y=0)

    can.create_text(120, 10,font=("Sans Serif",25),fill="#FF4500" ,anchor = "nw",text="Analyse des données par ventes ")#x y
    can.create_line(200 ,55,500,55,fill="white")

    selection = 'Les produits qui sont souvent achetés ensemble sont\n USB-C Charging Cable et Google Phone'
    lbtitre = Label(fenetre4, text=selection ,font=("Arial",16), 
                    background="black",foreground="white")
    lbtitre.place(x=70,y=100)

    bt= tk.Button(fenetre4, text= "Afficher plus de détails", font= ("Arial",12),
                  background ="#FF4500", foreground="white",  command=lambda: btn44(bt,dfproduitplusvendu))
    bt.place(x=260,y=200) 
    bt.grid_forget()
    fenetre4.mainloop()
    
def concat_produit_par_order_id(p: list): #♣prend tous les produit de la meme id i les concat en str
  return ";".join(p)

def produit_pasmois(liste):
    
    produitparmois=pd.DataFrame(columns = ['Mois','Liste dees produits souvent achetés ensemble'])
    loc=0
    for i in range(0,12):        
        dp=liste[i][liste[i]['Order ID'].duplicated(keep=False)].copy()      
        did=dp.groupby('Order ID')['Product'].apply(concat_produit_par_order_id)
        produitparmois.loc[loc]=[month_name[i+1],did]
        loc+=1
    return produitparmois 
   
def btn5():
    def btn55(button,df):
        fenetre5.geometry("700x550+300+100")
        button.place_forget()
        
        lbdetails = Label(fenetre5, text='♦Voici la liste des produits ainsi que leurs quantité vendues: ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place(x=100,y=190)
         
        l1=list(df)
        rset=df.to_numpy().tolist()
        table=ttk.Treeview(fenetre5,selectmode='browse') #mode navigation
        table.place(x =100, y = 220, width=500,height=280)
        table['height']=5
        table['show']='headings'
        #d'ou les colomn viendrant
        table['columns']=l1
        #deffenir la longeur de colomn
        for i in l1:
            table.column(i, width=100,anchor='c')
            table.heading(i, text=i)
        sl=0
        table.tag_configure('orange', background="#FFFAFA")
        for j in rset:  #ajout des donnees
            v=[r for r in j] #il cree une liste dans j
            table.insert('', 'end', iid=sl,values=v)
            sl+=1
    
    fenetre5 = Tk()
    fenetre5.title(" info meilleur mois de vente")
    fenetre5.geometry("700x250+300+100")
    fenetre5.resizable(False,False)
    fenetre5.config(bg="black")
    can= Canvas(fenetre5,width=700,height=300,highlightthickness=0,background="black")
    can.place(x=0,y=0)

    can.create_text(120, 10,font=("Sans Serif",25),fill="#FF4500" ,anchor = "nw",text="Analyse des données par ventes ")#x y
    can.create_line(200 ,55,500,55,fill="white")
    dfproduit=produitplusvendu_global(liste)
    maxvente=dfproduit.loc[0]['La quantité vendue']
    maxproduit=dfproduit.loc[0]['Produit']
    selection = 'Le produit le plus vendu est '+str(maxproduit) +' avec une quantité\n de '+ str(maxvente)
    lbtitre = Label(fenetre5, text=selection ,font=("Arial",16), 
                    background="black",foreground="white")
    lbtitre.place(x=25,y=100)

    bt= tk.Button(fenetre5, text= "Afficher plus de détails", font= ("Arial",12),
                    background ="#FF4500", foreground="white",  command=lambda: btn55(bt,dfproduit))
    bt.place(x=260,y=200) 
    bt.grid_forget()
    fenetre5.mainloop()
    
def produitplusvendu_global(liste):
    df = pd.concat(liste)
    l=['AAA Batteries (4-pack)','AA Batteries (4-pack)', 'USB-C Charging Cable',
      'Lightning Charging Cable','Wired Headphones', 'Apple Airpods Headphones','Bose SoundSport Headphones',
      '27in FHD Monitor','iPhone','27in 4K Gaming Monitor','34in Ultrawide Monitor ',
      'Google Phone','Flatscreen TV','Macbook Pro Laptop','ThinkPad Laptop','20in Monitor',
      'Vareebadd Phone','LG Washing Machine','LG Dryer']
    quantite=df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False)
    quantite.to_list()
    produit=pd.DataFrame(columns=['Produit','La quantité vendue'])
    for i in range(0,19) :
        produit.loc[i]=[l[i],quantite[i]]
    return produit

    
    
#ma fenetre 
fenetre = Tk()

fenetre.title("SalesAnalysis")
fenetre.geometry("1380x700+-10+0")
fenetre.resizable(False,False)
fenetre.config(bg="#091821")

#bg image
image = Image.open("C:\\Users\\ANIS\\Desktop\\M1 SDAD\\Python\\TP\\bb.jpg") 
photo = ImageTk.PhotoImage(image) 
cnv = Canvas(fenetre, width=1400, height=620, bg='orange')
cnv.create_image(0,0, anchor = tk.NW, image=photo)
cnv.place(x=-2,y=80)
#canvas
cnv.create_rectangle(10,140,560,80,outline="white")
cnv.create_rectangle(10,220,560,160,outline="white")
cnv.create_rectangle(10,320,560,250,outline="white")
cnv.create_rectangle(10,400,560,340,outline="white")
cnv.create_rectangle(10,480,560,420,outline="white")

#TitelTop de la fenetre
lbtitre = Label(fenetre, borderwidth=3, relief= SUNKEN, text="            Analyse des données de ventes 2019",font=("Sans Serif",25), 
                background="#FF4500",foreground="#FFFAFA")
lbtitre.place(x=0,y=0,width=1380,height=80)
  
#traitment de chaque dossier csv

#Janvier : January
dataJanuary=datajanuary=traitmenMois('Sales_January_2019.csv')
#Février : February
dataFebruary=datafebruary=traitmenMois('Sales_February_2019.csv')
#Mars : March
dataMars=datamars=traitmenMois('Sales_March_2019.csv')
#Avril : April
dataApril=dataapril=traitmenMois('Sales_April_2019.csv')
#Mai : May
dataMay=datamay=traitmenMois('Sales_May_2019.csv')
#Juin : June
dataJune=datajune=traitmenMois('Sales_June_2019.csv')
#Juillet : July
dataJuly=datajuly=traitmenMois('Sales_July_2019.csv')
#Aout : August
dataAugust=dataaugust=traitmenMois('Sales_August_2019.csv')
#Septembre : September
dataSeptember=dataseptember=traitmenMois('Sales_September_2019.csv')
#Octobre : October
dataOctober=dataoctober=traitmenMois('Sales_October_2019.csv')
#Novembre : November
dataNovember=datanovember=traitmenMois('Sales_November_2019.csv')
#Décembre : December
dataDecember=datadecember=traitmenMois('Sales_December_2019.csv')


#Creation de la Treeview                                   
l1=list(dataJanuary)
rset=dataJanuary.to_numpy().tolist()
table=ttk.Treeview(fenetre,selectmode='browse') #mode navigation
table.place(x =600, y = 150, width=700,height=400)
table['height']=5
table['show']='headings'
#d'ou les colomn viendrant
table['columns']=l1
#deffenir la longeur de colomn
for i in l1:
    table.column(i, width=100,anchor='c')
    table.heading(i, text=i)  
table.column(5, width=200)

# creer combobox
#tyle= ttk.Style()
#tyle.theme_use('clam')
#tyle.configure("month_cb", fieldbackground= "orange", background= "white")
selected_month = tk.StringVar()
month_cb = ttk.Combobox(fenetre, textvariable=selected_month)
month_cb.insert(0, ' sélectionner un mois pour visualiser ses données')

#get month name
month_cb['values'] = [month_name[m] for m in range(1, 13)]

#mode lecteur
month_cb['state'] = 'readonly'

# place the widget
month_cb.place(x=600, y=120,width=700)


# bind the selected value changes
                                                             
month_cb.bind('<<ComboboxSelected>>', month_changed)

#Quel est le meilleur mois de vente ? et Quel est le chiffre d'affaires de ce mois ?
#frontend
lbmv=Label(fenetre,text="Le meilleur mois de vente ains que son chiffre d'affaires",
           font=("Arial",14),background="#222222",foreground="white")                      
lbmv.place(x=35,y=150,width=500)
btnmv= tk.Button(fenetre, text= "Afficher", font= ("Arial",12),
                background ="#FF4500", foreground="white",  command=btn1) #
btnmv.place(x=170,y=180,width=200)

#○backend
listville=['San Francisco','Los Angeles','New York City','Boston','Atlanta',
            'Dallas','Seattle','Portland','Austin']   


liste=[datajanuary,datafebruary,datamars ,dataapril,datamay,datajune,datajuly,dataaugust,dataseptember,dataoctober,datanovember,datadecember]    


for i in range(0,12):
    liste[i]['ville']=liste[i]['Purchase Address'].apply(nom_ville)
    liste[i]['chiffre daffaire']=liste[i]['Quantity Ordered']*liste[i]['Price Each']
    
datamois = pd.DataFrame( columns = ['Mois' , 'la quantité de produit vendu', 'chiffre daffaire'])

for i in range (0,12):
    
    datamois.loc[i]=[ month_name[i+1],sum( liste[i]['Quantity Ordered']),
                     sum( liste[i]['Quantity Ordered'] *liste[i]['Price Each']) ]      
maxchif=datamois['chiffre daffaire'].max()
for i in range(0,12) :
    if datamois.loc[i]['chiffre daffaire']==maxchif :
        moismax = datamois.loc[i]['Mois']
               
#Dans quelle ville a-t-on le plus vendu de produits ?
#frontend
#backend


lbmv=Label(fenetre,text="La ville dont la vente des produits est la plus élevée",
           font=("Arial",14),background="#222222",foreground="white")
lbmv.place(x=35,y=230,width=500)#80
btnmv= tk.Button(fenetre, text= "Afficher", font= ("Arial",12),
                background ="#FF4500", foreground="white",command=btn2)#
btnmv.place(x=170,y=260,width=200) #30

#A quelle heure devons-nous passer de la publicité pour augmenter nos ventes ?

#backend
for i in range(0,12):
    liste[i]['heure'] = liste[i]['Order Date'].dt.hour
for i in range(0,12):
    liste[i].groupby('heure')['chiffre daffaire'].sum().sort_values(ascending=False) 
    
lbmv=Label(fenetre,text="l'heur idéal pour mettre de la publicité afin de maximiser\n nos vente",
           font=("Arial",14),background="#222222",foreground="white")
lbmv.place(x=35,y=310,width=500)#80
btnmv= tk.Button(fenetre, text= "Afficher", font= ("Arial",12),
                background ="#FF4500", foreground="white",  command= btn3)#
btnmv.place(x=170,y=360,width=200) #30
  


#Quels sont les produits qui sont souvent achetés ensemble ?
lbmv=Label(fenetre,text="Les produits qui sont souvent achetés ensemble",
           font=("Arial",14),background="#222222",foreground="white")
lbmv.place(x=35,y=410,width=500)#80
btnmv= tk.Button(fenetre, text= "Afficher", font= ("Arial",12),
                background ="#FF4500", foreground="white",  command= btn4)#
btnmv.place(x=170,y=440,width=200) #30

#Quel produit a-t-on le plus vendu et pourquoi ?
lbmv=Label(fenetre,text="Le prodduit le plus vendu",
           font=("Arial",14),background="#222222",foreground="white")
lbmv.place(x=35,y=490,width=500)#80
btnmv= tk.Button(fenetre, text= "Afficher", font= ("Arial",12),
                background ="#FF4500", foreground="white",  command= btn5)#
btnmv.place(x=170,y=520,width=200) #30



fenetre.mainloop()
