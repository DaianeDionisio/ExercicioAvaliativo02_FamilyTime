from db.database import Graph

class Querys:

    parent = ["Edson","Angela","Maria","Antonio","Luiza","Joao","Luciete","Laercio","Carlos"];
    sons = ["Edson","Angela","Danilo","Daiane","Luciete","Leonardo","Carlos","Geovana"]
    married = ["Edson","Angela","Luciete","Laercio","Maria","Antonio","Luiza","Joao"]
    dating = ["Danilo","Daiane","Mariana","Joao Pedro"]
    brother = ["Danilo","Daiane","Edson","Angela","Luciete","Carlos"]
    pet = ["Mike","Bob","Sirius","Gigi"]
    petOwner = ["Joao Pedro"]

    def __init__(self):
        self.db = Graph("bolt://34.232.50.158:7687", "neo4j", "glances-colds-ceramics")

    def getAll(self):
        self.db.execute_query("MATCH(n) RETURN n.nome")

    def checkMember(self,member):
        i=1
        options = []
        print("O que deseja saber sobre " + member + "?")
        if member in self.parent:
            print(i,"- Saber de quem",member,"é pai/mae")
            option = [i,"parent"]
            options.append(option)
            i += 1
        if member in self.sons:
            print(i, "- Saber quem são os pais de", member)
            option = [i, "sons"]
            options.append(option)
            i += 1
        if(member in self.married):
            print(i,"- Saber com quem",member,"é casado(a)")
            option = [i, "married"]
            options.append(option)
            i += 1
        if (member in self.dating):
            print(i, "- Saber com quem", member, "namora")
            option = [i, "dating"]
            options.append(option)
            i += 1
        if (member in self.brother):
            print(i, "- Saber quem são os irmãos/irmãs de", member)
            option = [i, "brother"]
            options.append(option)
            i += 1
        if (member in self.pet):
            print(i, "- Saber quem é o dono de", member)
            option = [i, "pet"]
            options.append(option)
            i += 1
        if (member in self.petOwner):
            print(i, "- Saber quais os pets de", member)
            option = [i, "petOwner"]
            options.append(option)
            i += 1
        if(len(options) == 0):
            print("Ops...este membro não pertence a familia")

        else:
            decision = int(input())
            query = 0
            for i in options:
                if(decision == i[0]):
                    query = i[1]

            if(query == "parent"):
                self.getSons(member)
            elif(query == "sons"):
                self.getParents(member)
            elif(query == "married"):
                self.getMarried(member)
            elif(query == "dating"):
                self.getDating(member)
            elif (query == "brother"):
                self.getBrother(member)
            elif (query == "pet"):
                self.getPet(member)
            elif (query == "petOwner"):
                self.getPetOwner(member)
            elif(query == 0):
                print("Opção inválida")

    def getSons(self,member):
        query = "MATCH (p:Pessoa)-[r:PAI_DE]->(q:Pessoa) WHERE p.nome = '"+member+"' RETURN q.nome"
        print(member+" é pai/mae de:")
        self.db.execute_query(query)

    def getParents(self,member):
        query = "MATCH (p:Pessoa)-[r:PAI_DE]->(q:Pessoa) WHERE q.nome = '"+member+"' RETURN p.nome"
        print("Os pais de "+member+" são:")
        self.db.execute_query(query)

    def getMarried(self,member):
        query = "MATCH (p:Pessoa)-[r:CASADO_COM]->(q:Pessoa) WHERE p.nome = '" + member + "' RETURN q.nome"
        print(member + " é casado(a) com: ")
        self.db.execute_query(query)

        print("Deseja saber:")
        print("1 - Desde quando eles são casados")
        print("2 - Quantos anos de casamento eles tem")
        print("3 - Voltar ao menu")
        decision = input()

        if(int(decision) == 1):
            query = "MATCH (p:Pessoa)-[r:CASADO_COM]->(q:Pessoa) WHERE p.nome = '" + member + "' RETURN r.desde"
            print("Desde: ")
            self.db.execute_query(query)
        elif(int(decision) == 2):
            query = "MATCH (p:Pessoa)-[r:CASADO_COM]->(q:Pessoa) WHERE p.nome = '" + member + "' RETURN r.tempoCasamento"
            print("Tempo de casamento:")
            self.db.execute_query(query)
            print("anos")

    def getDating(self,member):
        query = "MATCH (p:Pessoa)-[r:NAMORA_COM]->(q:Pessoa) WHERE p.nome = '" + member + "' RETURN q.nome"
        print(member + " namora com: ")
        self.db.execute_query(query)

        print("Deseja saber:")
        print("1 - Desde quando eles namoram")
        print("2 - Quantos anos de namoro eles tem")
        print("3 - Voltar ao menu")
        decision = input()

        if(int(decision) == 1):
            query = "MATCH (p:Pessoa)-[r:NAMORA_COM]->(q:Pessoa) WHERE p.nome = '" + member + "' RETURN r.desde"
            print("Desde: ")
            self.db.execute_query(query)
        elif(int(decision) == 2):
            query = "MATCH (p:Pessoa)-[r:NAMORA_COM]->(q:Pessoa) WHERE p.nome = '" + member + "' RETURN r.tempoNamoro"
            print("Tempo de namoro:")
            self.db.execute_query(query)
            print("anos")

    def getBrother(self,member):
        query = "MATCH (p:Pessoa)-[r:IRMAO_DE]->(q:Pessoa) WHERE q.nome = '"+member+"' RETURN p.nome"
        print(member+" é irmão/irmã de:")
        self.db.execute_query(query)

    def getPet(self,member):
        query = "MATCH (p:Pessoa)-[r:DONO_DE]->(q:Pet) WHERE q.nome = '"+member+"' RETURN p.nome"
        print(member+" é de:")
        self.db.execute_query(query)

    def getPetOwner(self,member):
        query = "MATCH (p:Pessoa)-[r:DONO_DE]->(q:Pet) WHERE p.nome = '"+member+"' RETURN q.nome"
        print(member+" é dono de:")
        self.db.execute_query(query)