import arcpy
import os.path
from arcpy import env
import webbrowser
import time
import subprocess
import threading

env.workspace = "D:/Projects/DetectionUpdates.gdb"
##arcpy.env.overwriteOutput = True
##webbrowser.open('http://localhost/stationrecording.php')

input_time = int(raw_input('How many minutes to run program? '))
max_time = input_time * 60
start_time = time.time()
timeout = time.time() + 60 * input_time
while (time.time() - start_time) < max_time:
   now = time.time()
   num = time.strftime("_%b_%d_%Y_%I_%M_%S")
   subprocess.call('xml2csv-conv http://data.dot.state.mn.us/dds/station.xml D:/Projects/Temporalcreator/StationRecord' + num + '.csv', shell=True)
   print("converted")
   elapsed = time.time() - now
   time.sleep(30 - elapsed)


1


num = time.strftime("_%b_%d_%Y_%I_%M_%S")
intable = 'D:\Projects\StationRecord' + num + '.csv'
outlocation = "D:\Projects\DetectionUpdates.gdb"
outtable = 'StationRecord' + num
#tabletohavejoin = "StationPoints"
#if arcpy.Exists(outtable):
    #arcpy.Delete_management(outtable)

arcpy.TableToTable_conversion(intable, outlocation, outtable)

#arcpy.MakeTableView_management(outtable, "id_table_view")

#arcpy.MakeFeatureLayer_management(tabletohavejoin, "id_layer")

#arcpy.DeleteField_management(tabletohavejoin, ["id", "flow", "occupancy", "volume", "speed"])

#arcpy.JoinField_management( tabletohavejoin, "station_id", outtable, "id", )

#arcpy.ApplySymbologyFromLayer_management(tabletohavejoin, "Style.lyr")