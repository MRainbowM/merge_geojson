import json

import geojson
import shapely.geometry
import shapely.ops


def merge_geojson():
    with open('file1.json') as file:
        geojson_1 = json.load(file)

    with open('file2.json') as file:
        geojson_2 = json.load(file)

    polygon_1 = shapely.geometry.shape(geojson_1['features'][0]['geometry'])
    polygon_2 = shapely.geometry.shape(geojson_2['features'][0]['geometry'])

    # Merging polygons into one
    merged_polygon = shapely.ops.unary_union([polygon_1, polygon_2])

    # Formatting in geojson
    return geojson.Feature(geometry=merged_polygon, properties={})
