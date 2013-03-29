# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
panic, 1

CompileOptions:
convexify: False
parser: structured
fastslow: False
decompose: False
use_region_bit_encoding: True

CurrentConfigName:
ros

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
4thfloor.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
fear, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
classroom = classroom
office = office
lab = lab
lounge = lounge
library = library
hall = hall
kitchen = kitchen

Spec: # Specification in structured English
group cool_places is office, library, lounge
do panic if and only if you are sensing fear
if you are not sensing fear then visit all cool_places

if you are sensing start of fear or end of fear then stay there

