# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# model1.py
# Created on: 2018-04-26 09:53:32.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
Precip2008Readings = arcpy.GetParameterAsText(0)
Nebraska__2_= arcpy.GetParameterAsText(1)
clipout = arcpy.GetParameterAsText(2)
# Local variables:
#Precip2008Readings = r"C:\Users\Yaryna\Downloads\gitstart\Lesson1education\Lesson1\Precip2008Readings.shp"
IDWout = "C:\\Users\\Yaryna\\Desktop\\progadom\\New Personal Geodatabase.mdb\\IDWout2"
reclassout = "C:\\Users\\Yaryna\\Desktop\\progadom\\New Personal Geodatabase.mdb\\reclassou2"
rasterout = "C:\\Users\\Yaryna\\Desktop\\progadom\\New Personal Geodatabase.mdb\\rasterout2"
#Nebraska__2_ = r"C:\Users\Yaryna\Downloads\gitstart\Lesson1education\Lesson1\Nebraska.shp"
#clipout = "C:\\Users\\Yaryna\\Desktop\\progadom\\New Personal Geodatabase.mdb\\clipout2"

# Process: IDW
arcpy.Idw_3d(Precip2008Readings, "RASTERVALU", IDWout, "1850,46466995651", "2", "VARIABLE 12", "")

# Process: Reclassify
arcpy.gp.Reclassify_sa(IDWout, "VALUE", "27715,960938 46615,086060 1;46615,086060 64536,670227 2;64536,670227 82132,407410 3;82132,407410 111132,789063 4", reclassout, "DATA")

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(reclassout, rasterout, "SIMPLIFY", "VALUE")

# Process: Clip
arcpy.Clip_analysis(rasterout, Nebraska__2_, clipout, "")
arcpy.env.overwriteOutput = True
