import arcpy


#----------------------------------------------------------------------
def are_collinear(p1, p2, p3, tolerance=0.5):
    """return True if 3 points are collinear.
    tolerance value will decide whether lines are collinear; may need
    to adjust it based on the XY tolerance value used for feature class"""
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    res = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if -tolerance <= res <= tolerance:
        return True


#----------------------------------------------------------------------
def get_redundant_vertices(vertices):
    """get redundant vertices from a line shape vertices"""
    indexes_of_vertices_to_remove = []
    start_idx, middle_index, end_index = 0, 1, 2
    for i in range(len(vertices)):
        p1, p2, p3 = vertices[start_idx:end_index + 1]
        if are_collinear(p1, p2, p3):
            indexes_of_vertices_to_remove.append(middle_index)

        start_idx += 1
        middle_index += 1
        end_index += 1
        if end_index == len(vertices):
            break
    return indexes_of_vertices_to_remove


#----------------------------------------------------------------------
def clean_geometries(fc, densify_curves=False):
    """clean polyline features in the fc removing redundant vertices"""
    in_sr = arcpy.Describe(fc).spatialReference.factoryCode

    with arcpy.da.UpdateCursor(fc, ['SHAPE@', 'OID@']) as ucur:
        for row in ucur:
            print "OBJECTID", row[1]
            cleaned_parts = []
            shape = row[0]

            if 'curvePaths' in shape.JSON:
                if densify_curves:
                    shape = shape.densify('DISTANCE', 1, 1)
                else:
                    continue

            for part in range(shape.partCount):
                vertices = [(p.X, p.Y) for p in shape.getPart(part)]
                if len(vertices) < 3:  #polyline's part consists of 2 vertices
                    continue
                vertices_to_remove = get_redundant_vertices(vertices)
                vertices_to_keep = [
                    val for idx, val in enumerate(vertices)
                    if idx not in vertices_to_remove
                ]
                cleaned_part_as_array = arcpy.Array(
                    [arcpy.Point(*coords) for coords in vertices_to_keep])
                cleaned_parts.append(cleaned_part_as_array)

            if cleaned_parts:
                cleaned_shape = arcpy.Polyline(
                    arcpy.Array(cleaned_parts), in_sr)
                row[0] = cleaned_shape
                ucur.updateRow(row)


if __name__ == '__main__':
    fc = r'C:\GIS\Temp\ArcGISHomeFolder\Default.gdb\_SimpleRoads'    
    clean_geometries(fc, densify_curves=False)
