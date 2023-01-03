from tkinter import Label,Tk,SUNKEN
import tkinter as tk
from tkinter import ttk #pour le Treeview
from tkinter import Canvas
from calendar import month_name #pour le combobox
import pandas as pd


def btn1(button,datamois):
    fenetre.geometry("700x550+300+100")
    button.place_forget()
    
    lbdetails = Label(fenetre, text='♦Voici la liste des mois ainsi que leurs chiffre daffaire: ',font=("Arial",10), 
                    background="black",foreground="white")
    lbdetails.place(x=100,y=190)
     
    l1=list(datamois)
    rset=datamois.to_numpy().tolist()
    table=ttk.Treeview(fenetre,selectmode='browse') #mode navigation
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
    
    
    
def nom_ville(addresse):
  return addresse.split(',')[1].strip() #avoire la premiere valeur apres la, sans espace

def traitmenMois(chemin):
    #lire les donnees csv ppour le mois de Février
    MData = pd.read_csv('C:/Users/ANIS/Desktop/Sales_Data/'+chemin)
    #dataframe de Février
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
fenetre = Tk()
fenetre.title(" info meilleur mois de vente")
fenetre.geometry("700x250+300+100")
fenetre.resizable(False,False)
fenetre.config(bg="black")
can= Canvas(fenetre,width=700,height=300,highlightthickness=0,background="black")
can.place(x=0,y=0)

can.create_text(120, 10,font=("Sans Serif",25),fill="#FF4500" ,anchor = "nw",text="Analyse des données par ventes ")#x y
can.create_line(200 ,55,500,55,fill="white")
selection = str(moismax) +'est le meilleur mois de vente, avec un chiffre daffaires de \n\n'+str(maxchif)
lbtitre = Label(fenetre, text=selection ,font=("Arial",16), 
                background="black",foreground="white")
lbtitre.place(x=25,y=100)
maxchif
bt= tk.Button(fenetre, text= "Afficher plus de détails", font= ("Arial",12),
                background ="#FF4500", foreground="white",  command=lambda: btn1(bt,datamois))
bt.place(x=260,y=200) 
bt.grid_forget()
fenetre.mainloop()
