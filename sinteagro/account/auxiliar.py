from localidades.models import Cidade

# Brazilian States
select_estados = (("AC", "Acre"),
                  ("AL", "Alagoas"),
                  ("AP", "Amapá"),
                  ("AM", "Amazonas"),
                  ("BA", "Bahia"),
                  ("CE", "Ceará"),
                  ("DF", "Distrito Federal"),
                  ("ES", "Espírito Santo"),
                  ("GO", "Goiás"),
                  ("MA", "Maranhão"),
                  ("MT", "Mato Grosso"),
                  ("MS", "Mato Grosso do Sul"),
                  ("MG", "Minas Gerais"),
                  ("PA", "Pará"),
                  ("PB", "Paraíba"),
                  ("PR", "Paraná"),
                  ("PE", "Pernambuco"),
                  ("PI", "Piauí"),
                  ("RJ", "Rio de Janeiro"),
                  ("RN", "Rio Grande do Norte"),
                  ("RS", "Rio Grande do Sul"),
                  ("RO", "Rondônia"),
                  ("RR", "Roraima"),
                  ("SC", "Santa Catarina"),
                  ("SP", "São Paulo"),
                  ("SE", "Sergipe"),
                  ("TO", "Tocantins"),
                  ("ST", "Estrangeiro"),)

#Gender
genero = ( ("m", "Masculino"),
           ("f", "Feminino"))

def get_cities(state):
    cities = Cidade.objects.filter(uf=state).values()
    return cities

def get_city(id):
    city = Cidade.objects.get(id=id)
    return city.nome