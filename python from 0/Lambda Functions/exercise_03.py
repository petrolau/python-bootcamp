#zip com dictionary comprehension

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

#final_grades = {
#                'dan': 98,
#                'ang' : 91,
#                'kate' : 78
#                }

#aqui eu vou pegar uma lista com as notas mais altas das duas listas, comparando por índice.
#também vou zipar com o nome dos estudantes, que estão organizados por ind.
grades = zip(
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)
print (dict(grades))