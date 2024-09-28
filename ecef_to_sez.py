# ecef_to_sez
# Written by William Sosnowski
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.1363
R_E_KM = 6378.1363
E_E=0.081819221456

# helper functions

def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

# initialize script arguments
oxkm=float('nan')
oykm=float('nan')
ozkm=float('nan')
xkm=float('nan')
ykm=float('nan')
zkm=float('nan')

# parse script arguments
if len(sys.argv)==7:
  oxkm = float(sys.argv[1])
  oykm = float(sys.argv[2])
  ozkm = float(sys.argv[3])
  xkm = float(sys.argv[4])
  ykm = float(sys.argv[5])
  zkm = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ecef_to_llh.py oxkm oykm ozkm xkm ykm zkm'\
  )
  exit()

#relitive position to observer
dx=xkm-oxkm
dy=ykm-oykm
dz=zkm-ozkm

#lat long calculation w/ projection
project = math.sqrt(oxkm**2 + oykm**2)  
sezo_lat = math.atan2(ozkm, project)  
sezo_lon = math.atan2(oykm, oxkm)

R = [
        [-math.sin(sezo_lat) * math.cos(sezo_lon), -math.sin(sezo_lon), math.cos(sezo_lat) * math.cos(sezo_lon)],
        [-math.sin(sezo_lat) * math.sin(sezo_lon),  math.cos(sezo_lon), math.cos(sezo_lat) * math.sin(sezo_lon)],
        [ math.cos(sezo_lat),                    0,                  math.sin(sezo_lat)]
    ]

s_km = R[0][0] * dx + R[0][1] * dy + R[0][2] * dz
e_km = R[1][0] * dx + R[1][1] * dy + R[1][2] * dz
z_km = R[2][0] * dx + R[2][1] * dy + R[2][2] * dz

print(s_km)
print(e_km)
print(z_km)