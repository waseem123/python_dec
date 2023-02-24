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

print(engg_students.symmetric_difference(med_students))

med_students.symmetric_difference_update(engg_students)
print(med_students)