# A - B : All elements of Set A which are not present in Set B
# B - A : All elements of Set B which are not present in Set A

engg_students = {
			"Akhila",
			"Miran",
			"Navid",
			"Waseem",}

med_students = {
			"Swamini",
			"Miran",
			"Prerna",
			"Asmita",
			"Prem",}


print(engg_students - med_students)
print(med_students.difference(engg_students)) #med_students-engg_students

engg_students.difference_update(med_students)
# engg_students = engg_students - med_students
print(engg_students)