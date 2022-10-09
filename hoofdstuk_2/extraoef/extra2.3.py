PI = 3.14
INCH_IN_CM = 0.0254

diameter_wiel = float(input("Diameter fietswiel (in inch): "))
af_te_leggen_m = float(input("Afstand die de wiel moet afleggen: "))

afgelegde_weg_in_m = diameter_wiel * PI * INCH_IN_CM

aantal_omwentelingen = af_te_leggen_m / afgelegde_weg_in_m

print("De wiel moet " + str(aantal_omwentelingen) + " keer omwentelen om "
      + str(af_te_leggen_m) + " meter af te leggen")
