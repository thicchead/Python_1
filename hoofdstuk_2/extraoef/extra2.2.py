PI = 3.14
INCH_IN_CM = 0.0254
diameter_wiel = float(input("Diameter fietswiel (in inch): "))

afgelegde_weg_in_inch = diameter_wiel * PI
afgelegde_weg_in_m = afgelegde_weg_in_inch * INCH_IN_CM

print(str(afgelegde_weg_in_inch) + " inch")
print(str(afgelegde_weg_in_m) + " meter")
