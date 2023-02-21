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

print(engg_students.intersection(med_students))

engg_students.intersection_update(med_students)
print(engg_students)