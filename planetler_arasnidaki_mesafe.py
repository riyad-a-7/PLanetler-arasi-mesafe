from math import pi, sin, cos, atan2, sqrt
# planetlerin adlari ve kordinatlari
solar_system_planets = [
    {
        "name": "Merkuri",
        "mean_distance_from_sun_au": 0.39,
        "orbital_position_deg": 48.3
    },
    {
        "name": "Venera",
        "mean_distance_from_sun_au": 0.72,
        "orbital_position_deg": 76.5
    },
    {
        "name": "Yer",
        "mean_distance_from_sun_au": 1.0,
        "orbital_position_deg": 0.0
    },
    {
        "name": "Mars",
        "mean_distance_from_sun_au": 1.52,
        "orbital_position_deg": 49.6
    },
    {
        "name": "Yupiter",
        "mean_distance_from_sun_au": 5.2,
        "orbital_position_deg": 100.0
    },
    {
        "name": "Saturn",
        "mean_distance_from_sun_au": 9.58,
        "orbital_position_deg": 150.0
    },
    {
        "name": "Uran",
        "mean_distance_from_sun_au": 19.22,
        "orbital_position_deg": 200.0
    },
    {
        "name": "Neptun",
        "mean_distance_from_sun_au": 30.05,
        "orbital_position_deg": 250.0
    }
]


# planetlerin adlarina gore muqaisesi
def kordinator(user_plt):
    for i in solar_system_planets:
        if i["name"] == user_plt:
            merkez_km = i["mean_distance_from_sun_au"]
            derece = i["orbital_position_deg"]
    return merkez_km, derece


user_plnt_1 = input("Xahis olunur 1- planetin adini qeyd edin: ").capitalize()
user_plnt_2 = input("Xahis olunur 2- planetin adini qeyd edin: ").capitalize()
print("````````````````````````````````````````````````````````")

# user_plnt_1 üçün kartesian koordinatlar:
def user_plnt_1_1(user_plnt_1):
    r = kordinator(user_plnt_1)
    alpha = kordinator(user_plnt_1)
    x = r[0]*cos(alpha[1])
    y = r[0]*sin(alpha[1])
    return x, y
x_y = user_plnt_1_1(user_plnt_1)


# user_plnt_2 üçün kartesian koordinatlar:
def user_plnt_2_1(user_plnt_2):
    r = kordinator(user_plnt_2)
    alpha = kordinator(user_plnt_2)
    x = r[0]*cos(alpha[1])
    y = r[0]*sin(alpha[1])
    return x, y
x_y_2 = user_plnt_1_1(user_plnt_2)


# son isiq ilinin hesablanmasi
d = sqrt((x_y_2[0]-x_y[0])**2+(x_y_2[1]-x_y[1])**2)
isiq_ili = d/63.241

print(f"{user_plnt_1} ilə {user_plnt_2} arasindaki məsafə işiq ili ilə : {isiq_ili:.2f} edir . . . ")
print("end")