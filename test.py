import os, subprocess
import arcpy
from arcpy import env
# Set csv_directory as C:\..\..\mndot2arcmap.csv
# os.path.join joins the mndot2arcmap.csv argument to the current path that the script is ran from
csv_dir = os.path.join(os.getcwd(), "mndot2arcmap.csv")
# the current path the script is ran from is given the variable 'path'
path = os.getcwd()
# os.path.join with \stations is assigned to variable gdb_name
gdb_name = os.path.join("\stations")
# the current path, with the gdb name of stations plus .gdb is set as gdb_path variable
gdb_path = path + gdb_name + '.gdb'
#enviornment is setup
env.workspace = gdb_path
# more variables are set for feature classes
# inputtable = mndot2arcmap.csv
intable = csv_dir
# output location = station.gdb
outlocation = gdb_path
# the output table variable is "thestationtable"
outtable = "thestationtable"
# the Table to have the join, which is the point file, is named StationPoints
tabletohavejoin = "StationPoints"
#still trying to work on the road feature
#roads = "motorways_new"
# ----- creates gdb if it does not exist yet ---- #
if arcpy.Exists(outlocation):
    pass
else:
    gdb = arcpy.CreateFileGDB_management(path, gdb_name)
#DEMO#
#subprocess.call('SET %PATH%=' + path, shell=True)

# Subprocess.call() passes argument to computer's terminal terminal
subprocess.call('xml2csv-conv -l "speed" -i "status, flow, station_data" -d http://data.dot.state.mn.us/dds/station.xml ' + csv_dir, shell=True)
# if "thestationtable" already exists, delete it for updated table to be imported
if arcpy.Exists(outtable):
    arcpy.Delete_management(outtable)
# Makes the csv file into a table in our station.gdb with the name "thestationstable"
arcpy.TableToTable_conversion(intable, outlocation, outtable)
# Deletes any existing fields in the station point file before making the join.
arcpy.DeleteField_management(tabletohavejoin, ["station_id_", "flow", "occupancy", "volume", "speed", "station", "station__status_"])
# Joins the traffic flow data to the stations in the point file
arcpy.JoinField_management(tabletohavejoin, "station_id", outtable, "station__id_",)
# Symbolizes the points based on occupancy within sections of the highway
arcpy.ApplySymbologyFromLayer_management(tabletohavejoin, "Style.lyr")
#arcpy.ApplySymbologyFromLayer_management(roads, "Styleroad.lyr")
