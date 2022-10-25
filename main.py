from db.querys import Querys

query = Querys()

while(1):
    print("Sobre quem você deseja saber mais? (Digite o nome do membro da família)")
    query.getAll()
    print( )
    member = input()
    query.checkMember(member)
    print("-----------------------------------------------------")