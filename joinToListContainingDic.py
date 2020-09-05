A = [{'air_temperature_celcius': '7', 'date' : '2010-08-20', 'relative_humidity' : '37.9', 'station': '2002-022A', 'wind_speed_knots': '5.5'}] 

B = [{'latitude': '-37.591', 'longitude': '148.111', 'datetime':'2019-10-02T03:52:12', 'surface_temp':'57', 'confidence': '83', 'power' : '26.7'}]

print(A.extend(B))
print(A)