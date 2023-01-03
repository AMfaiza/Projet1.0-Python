from tkinter import Label,Tk,SUNKEN
import tkinter as tk
from tkinter import ttk #pour le Treeview
from tkinter import Canvas
from calendar import month_name #pour le combobox
import pandas as pd


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

def btn2():
    def btn22(button):
        def table_ville_vente2(df):
            
            bt2= tk.Button(fenetre2, text= "graphe associ", font= ("Arial",12),
                           background ="#FF4500", foreground="white",  command=lambda: btn2(bt))
            
            
            if var.get()==1:
                montreeveiw2(fenetre2, df)
                bt2.place(x=270,y=500)
                
            else:
                montreeveiw2(fenetre2, df)
                bt2.place_forget()

        fenetre2.geometry("700x550+300+100")
        button.place_forget()
        
        lbdetails = Label(fenetre2, text='♦Voici la liste des mois ainsi que leurs chiffre daffaire: ',font=("Arial",10), 
                        background="black",foreground="white")
        lbdetails.place()     
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


btn2()


