import arcpy
from arcpy import env
import webbrowser
import subprocess

env.workspace = "D:\Projects\stations.gdb"
arcpy.env.overwriteOutput = True
#webbrowser.open('http://localhost/stationcopyphp.php')
subprocess.call('xml2csv-conv -l "speed" -i "status, flow, station_data" -d http://data.dot.state.mn.us/dds/station.xml D:\Projects\stationupdator2.csv', shell=True)


intable = "D:\Projects\stationupdator2.csv"
outlocation = "D:\Projects\stations.gdb"
outtable = "Thestationtable"
tabletohavejoin = "StationPoints"
roads = "HennepinRoads"
if arcpy.Exists(outtable):
    arcpy.Delete_management(outtable)

arcpy.TableToTable_conversion(intable, outlocation, outtable)

#arcpy.AddField_management(outtable, "fix_speed", "DOUBLE")

#arcpy.CalculateField_management(outtable, "fix_speed", '!speed!', "PYTHON")
#arcpy.DeleteField_management(outtable, )

#arcpy.MakeTableView_management(outtable, "id_table_view")

#arcpy.MakeFeatureLayer_management(tabletohavejoin, "id_layer")

arcpy.DeleteField_management(tabletohavejoin, ["id", "flow", "occupancy", "volume", "speed", "station", "station_status"])
arcpy.JoinField_management(tabletohavejoin, "station_id", outtable, "station",)
#arcpy.ApplySymbologyFromLayer_management(tabletohavejoin, "Style.lyr")

arcpy.DeleteField_management(roads, ["id", "flow", "occupancy", "volume", "speed", "station", "station_status"])
arcpy.JoinField_management(roads, "station_id", outtable, "station",)
#arcpy.ApplySymbologyFromLayer_management(roads, "styleroadsOccu.lyr")