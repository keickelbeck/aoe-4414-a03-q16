# sez_to_ecef.py
#
# Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km 
#  Converts SEZ vector to ECEF vector

# Parameters:
#  o_lat_deg: observatory/origin latitude in degrees
#  o_lon_deg: observatory/origin longitude in degrees
#  o_hae_km: observatory/origin height above the ellipsoid in km 
#  s_km: SEZ s-component (South) in km
#  e_km: SEZ e-component (East) in km
#  z_km: SEZ z-component in km
#  ...
# Output:
#  Prints the ECEF x-component (km), ECEF y-component (km), and ECEF z-component (km)
#
# Written by Kristin Eickelbeck
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## calculated denominator
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
o_lat_deg = float('nan') # observatory/origin latitude in degrees
o_lon_deg = float('nan') # observatory/origin longitude in degrees
o_hae_km = float('nan') # observatory/origin height above the ellipsoid in km 
s_km = float('nan') # SEZ s-component (South) in km
e_km = float('nan') # SEZ e-component (East) in km
z_km = float('nan') # SEZ z-component in km

# parse script arguments
if len(sys.argv)==7:
   o_lat_deg = float(sys.argv[1])
   o_lon_deg = float(sys.argv[2])
   o_hae_km = float(sys.argv[3])
   s_km = float(sys.argv[4])
   e_km = float(sys.argv[5])
   z_km = float(sys.argv[6])

else:
    print(\
     'Usage: '\
     'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
    )
    exit()

# write script below this line
lon_rad = o_lon_deg*math.pi/180
lat_rad = o_lat_deg*math.pi/180

r_x_ecef = math.cos(lon_rad)*math.sin(lat_rad)*s_km + math.cos(lon_rad)*math.cos(lat_rad)*z_km - math.sin(lon_rad)*e_km
r_y_ecef = math.sin(lon_rad)*math.sin(lat_rad)*s_km + math.sin(lon_rad)*math.cos(lat_rad)*z_km + math.cos(lon_rad)*e_km
r_z_ecef = -math.cos(lat_rad)*s_km + math.sin(lat_rad)*z_km

denom = calc_denom(E_E,lat_rad)
c_E = R_E_KM/denom
s_E = (R_E_KM*(1-E_E**2))/denom

r_x_km = (c_E + o_hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E + o_hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E + o_hae_km)*math.sin(lat_rad)

ecef_x_km = r_x_ecef + r_x_km
ecef_y_km = r_y_ecef + r_y_km
ecef_z_km = r_z_ecef + r_z_km

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)

