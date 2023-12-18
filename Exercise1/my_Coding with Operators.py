income = 12000
Single_person_tax_allowance = 1150
Taxable_20_percent = income - Single_person_tax_allowance
Taxable_40_percent = income - Taxable_20_percent
Percent_taxable_20 = Taxable_20_percent * .2
Percent_taxable_40 = Taxable_40_percent * .4
Total_tax = Percent_taxable_20 + Percent_taxable_40
print(Total_tax)