from re import I


# Fonction pour crypter er décpyter 
def encryptage_decryptage(mot):
    mot=mot[::-1]
    return mot
# Fonction pour creer la premiére base de donnée  
def creer_base_donnée():
    lstcomp=["Numéro_de_compt","Mot_de_passe","Montant_chèque","Montant_épargne","Montant_placement","taux_intérête"]
    client1=["1234","voiture1","100","1000","10000","1.8%"]
    client2=["3456","chat123","150","2000","25000","3%"]
    client3=["3333","1234","5","100","1000","15%"]
    client4=["0000","admin","0","0","0","0%"]
    
    f=open("bd.txt","w", encoding='utf8')
    for lst in range(len(lstcomp)):
        f.write(lstcomp[lst]+"  ")
    
    f.write("\n")
    for clt1 in range(6):
        f.write(encryptage_decryptage(client1[clt1])+" "*(17-len(client1[clt1])))
        
    f.write("\n")
    for clt2 in range(6):
        f.write(encryptage_decryptage(client2[clt2])+" "*(17-len(client2[clt2])))
    
    f.write("\n")
    for clt3 in range(6):
        f.write(encryptage_decryptage(client3[clt3])+" "*(17-len(client3[clt3])))
    
    f.write("\n")
    for clt4 in range(6):
        f.write(encryptage_decryptage(client4[clt4])+" "*(17-len(client4[clt4])))
    f.close()
   
    return lstcomp,client1,client2,client3,client4 

# Fonction pour remplir une based de donner 
def base_donnée(lstcomp,client1,client2,client3,client4):
        
    f=open("bd.txt","w", encoding='utf8')
    for lst in range(len(lstcomp)):
        f.write(lstcomp[lst]+"  ")
    
    f.write("\n")
    for clt1 in range(6):
        f.write(client1[clt1]+" "*(17-len(client1[clt1])))
        
    f.write("\n")
    for clt2 in range(6):
        f.write(client2[clt2]+" "*(17-len(client2[clt2])))
    
    f.write("\n")
    for clt3 in range(6):
        f.write(client3[clt3]+" "*(17-len(client3[clt3])))
    
    f.write("\n")
    for clt4 in range(6):
        f.write(client4[clt4]+" "*(17-len(client4[clt4])))
    f.close()
   
    return lstcomp,client1,client2,client3,client4
# Menu pour choisir le type de fichier
def menu1():
    print("*"*30)
    print("1-Compte Cheque")
    print("2-Compte Épargne")
    print("3-Compte Placements")
    print("*"*30)
    nbr=int(input("Entrer votre choix du compte :")) 
    return (nbr)

# Menu pour choisir le type d'opération a effectuer sur le compte
def menu2():
    print("---"*30)
    print("1-Faire un dépôt")
    print("2-Faire un retrait")
    print("3-Changer de compte")
    print("4-Terminer")
    print("---"*30)
    nbr=int(input("Entrer votre choix d'opération :")) 
    return (nbr)

# Menu pour l'administarteur 
def menu3():
    print("----"*10)
    print("1-Ajouter un compte")
    print("2-Enlever un compte")
    print("3-Changer le taux d'intérêt d'un compte")
    print("4-Terminer")
    print("----"*10)
    nbr=int(input("Entrer votre choix : ")) 
    return (nbr)

# Fonction pour creer la liste pour chaque clients 
def list_client(lst):
    client=[]
    for ls  in range(len(lst)-1):
        if lst[ls]!="":
            client.append(lst[ls])   
            
    return client

# Fonction pour les opérations sur les comptes 
def opération(nbr, opera,client):
    if opera==1:
            if nbr==1:
               depot=int(input("Enter le montant à déposer : "))
               total=int(encryptage_decryptage(client[2]))+depot
               client[2]=encryptage_decryptage(str(total))
               print(f"le nouveau solde de votre compte chéque est : {total}")
            elif nbr==2:
                depot=int(input("Enter le montant à déposer : "))
                total=int(encryptage_decryptage(client[3]))+depot
                client[3]=encryptage_decryptage(str(total))
                print(f"le nouveau solde de votre compte épargne est : {total}")
    
    elif opera==2:
            if nbr==1:
                retrait=int(input("Enter le montant à retirer : "))
                condition=False
                while condition==False:
                   if retrait<=int(encryptage_decryptage(client[2])):
                       total=int(encryptage_decryptage(client[2]))-retrait
                       client[2]=encryptage_decryptage(str(total))
                       print(f"le nouveau solde de votre compte chéque est : {total}")
                       condition=True
                   else: 
                        retrait=int(input("Votre solde est inférieur Enterer de nouveau le montant à retirer  : "))
                        condition==False
            if nbr==2:
                retrait=int(input("Enter le montant à retirer : "))
                condition=False
                while condition==False:
                   if retrait<=int(encryptage_decryptage(client[3])):
                       total=int(encryptage_decryptage(client[3]))-retrait
                       client[3]=encryptage_decryptage(str(total))
                       print(f"le nouveau solde de votre compte chéque est : {total}")
                       condition=True
                   else: 
                        retrait=int(input("Votre solde est inférieur Enterer de nouveau le montant à retirer  : "))
                        condition==False            
                       
    elif opera==3:
        if nbr==1:
            print("*******************")
            print("1-Compte Épargne")
            print("2-Compte Placements")
            print("*******************")
            chx=int(input("choisir un autre compte : "))
            if chx==1:
                print(encryptage_decryptage(client[3]))
            else:
                print(encryptage_decryptage(client[4])) 
        elif nbr==2:
            print("*******************")
            print("1-Compte Cheque")
            print("2-Compte Placements")
            print("*******************")
            chx=int(input("choisir un autre compte : "))
            if chx==1:
                print(encryptage_decryptage(client[2]))
            else:
     
                print(encryptage_decryptage(client[4])) 
    elif opera==4:
                exit()


    #print(client)
    return client

# Fonction pour le retour de placement 
def  opération_palcement(client):
     
     term5=encryptage_decryptage(client[5])
     term5=term5[:-1]
     p1=int(encryptage_decryptage(client[4]))*(1+float(term5))**1
     p2=int(encryptage_decryptage(client[4]))*(1+float(term5))**2
     p3=int(encryptage_decryptage(client[4]))*(1+float(term5))**3
     p4=int(encryptage_decryptage(client[4]))*(1+float(term5))**4
     p5=int(encryptage_decryptage(client[4]))*(1+float(term5))**5
     return p1,p2,p3,p4,p5  

# Fonction pour les opérations d'administarteur  
def operation_admin(nbr,lstcomp,client1,client2,client3,client4):
    if nbr==1:
        compte=input("Entrer le numéro de nouveau compte à 4 chiffres: ")
        mot_de_passe=input("Entrer le mot de passe : ")
        montant_cheque=("0")
        montant_epargne=("0")
        montant_placement=("0")
        taux_interet=("0")
        ln=[encryptage_decryptage(compte),encryptage_decryptage(mot_de_passe),encryptage_decryptage(montant_cheque), encryptage_decryptage(montant_cheque),encryptage_decryptage(montant_epargne),encryptage_decryptage(montant_placement),encryptage_decryptage(taux_interet)]
        
        f=open("bd.txt","r", encoding='utf8')
        clt=f.readlines()
        lstcomp=list_client(clt[0].split(' '))
        client1=list_client(clt[1].split(' '))
        client2=list_client(clt[2].split(' '))
        client3=list_client(clt[3].split(' '))
        client4=list_client(clt[4].split(' '))
        admin=["0000",encryptage_decryptage("admin"),"0","0","0","0%"]
        client3=ln
        client4=admin
        base_donnée(lstcomp,client1,client2,client3,client4)

    elif nbr==2:
        compte=input("Entrer le numéro de compte à enlever: ")
        f=open("bd.txt","w", encoding='utf8')
        if compte==encryptage_decryptage(client1[0]):
            client1=["                 ","                 ","                 ","                 ","                 ","                 ","                 "]
            base_donnée(lstcomp,client2,client3,client4,client1)
        if compte==encryptage_decryptage(client2[0]):
            client2=["                 ","                 ","                 ","                 ","                 ","                 ","                 "]
            base_donnée(lstcomp,client1,client3,client4,client2) 
        if compte==encryptage_decryptage(client3[0]):
            client3=["                 ","                 ","                 ","                 ","                 ","                 ","                 "]
            base_donnée(lstcomp,client1,client2,client4,client3) 
        f.close
    
    elif nbr==3:
        compte=input("Entrer le numéro de compte dont vous voulez changer le taux d'interet: ")
        if compte==encryptage_decryptage(client1[0]):
            taux=str(input("Entrer le nouveau taux d'interet: "))+"%"
            client1[5]=encryptage_decryptage(taux)
            base_donnée(lstcomp,client1,client2,client3,client4)
        if compte==encryptage_decryptage(client2[0]):
            taux=str(input("Entrer le nouveau taux d'interet: "))+"%"
            client2[5]=encryptage_decryptage(taux)
            base_donnée(lstcomp,client1,client2,client3,client4)
        if compte==encryptage_decryptage(client3[0]):
            taux=str(input("Entrer le nouveau taux d'interet: "))+"%"
            client3[5]=encryptage_decryptage(taux)
            base_donnée(lstcomp,client1,client2,client3,client4)
            
    return None     

        
  
#Fonction principale         
def principal():
    
    f=open("bd.txt","r", encoding='utf8')
    
    clt=f.readlines()
    lstcomp=list_client(clt[0].split(' '))
    client1=list_client(clt[1].split(' '))
    client2=list_client(clt[2].split(' '))
    client3=list_client(clt[3].split(' '))
    client4=list_client(clt[4].split(' '))
    

    cmpt=input("Entrer votre numéro de copmte à 4 chiffres: ")
    mot_pas=input("Entrer votre mot de passe  : ")
   
    controle=False       
    while controle==False:
        if  cmpt+mot_pas==encryptage_decryptage(client1[0])+encryptage_decryptage(client1[1]):
            controle==True
            nbr=menu1()
            if nbr==1:
                opera=menu2()
                client1=opération(nbr, opera,client1)
                base_donnée(lstcomp,client1,client2,client3,client4)
            elif nbr==2:
                opera=menu2()
                client1=opération(nbr, opera,client1)
                base_donnée(lstcomp,client1,client2,client3,client4)     
            elif nbr==3:       
                p1,p2,p3,p4,p5=opération_palcement(client1)    
                print(f"votre retour de placement en 1 année est : {p1}")
                print(f"votre retour de placement en 2 année est : {p2}")
                print(f"votre retour de placement en 3 année est : {p3}")
                print(f"votre retour de placement en 4 année est : {p4}")
                print(f"votre retour de placement en 5 année est : {p5}")
        
        elif cmpt+mot_pas==encryptage_decryptage(client2[0])+encryptage_decryptage(client2[1]):
            controle==True
            nbr=menu1()
            if nbr==1:
                opera=menu2()
                client2=opération(nbr, opera,client2)
                base_donnée(lstcomp,client1,client2,client3,client4)
            elif nbr==2:
                opera=menu2()
                client2=opération(nbr, opera,client2)
                base_donnée(lstcomp,client1,client2,client3,client4)     
            elif nbr==3:       
                p1,p2,p3,p4,p5=opération_palcement(client2)    
                print(f"votre retour de placement en 1 année est : {p1}")
                print(f"votre retour de placement en 2 année est : {p2}")
                print(f"votre retour de placement en 3 année est : {p3}")
                print(f"votre retour de placement en 4 année est : {p4}")
                print(f"votre retour de placement en 5 année est : {p5}")


        elif cmpt+mot_pas==encryptage_decryptage(client3[0])+encryptage_decryptage(client3[1]):
            controle==True
            nbr=menu1()
            if nbr==1:
                opera=menu2()
                client3=opération(nbr, opera,client3)
                base_donnée(lstcomp,client1,client2,client3,client4)
            elif nbr==2:
                opera=menu2()
                client3=opération(nbr, opera,client3)
                base_donnée(lstcomp,client1,client2,client3,client4)     
            elif nbr==3:       
                p1,p2,p3,p4,p5=opération_palcement(client3)    
                print(f"votre retour de placement en 1 année est : {p1}")
                print(f"votre retour de placement en 2 année est : {p2}")
                print(f"votre retour de placement en 3 année est : {p3}")
                print(f"votre retour de placement en 4 année est : {p4}")
                print(f"votre retour de placement en 5 année est : {p5}")

            
            
        elif cmpt+mot_pas==encryptage_decryptage(client4[0])+encryptage_decryptage(client4[1]):
            controle==True
            nbr=menu3()
            condition=False
            while condition==False:
                operation_admin(nbr,lstcomp,client1,client2,client3,client4)
                nbr=menu3()
                if nbr==4:
                    exit()
                    

        else:     
                cmpt=input("Erreur!! Entrer votre numéro de copmte à 4 chiffres: ")
                mot_pas=input("Entrer votre mot de passe  : ")
            
    return

principal()
#creer_base_donnée()
