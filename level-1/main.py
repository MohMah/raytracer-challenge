
def read_model(file_name):
    with open(file_name) as f:
    for line in f:
        if 'VERTICES' in line:
            pass
        if 'FACES' in line:
            pass
        if 'CAMERAS' in line:
            pass

# vertex = vector =(id, (X, Y, Z, 1))
# vertices = [v1, v2, ... ]
# face = (id1, id2, id3, vector)
# camera = (vector, pitch, yaw, roll, focal_length)
# cameras = {name: camera}


# image_data = [ [(x1,y1), (x2,y2)], ... ]

# get data
# for camera in cameras:
#   image_data = render(vertices, faces, camera)
#   draw(image_data, file_name)




# def render(vertices, faces, camera):
#   tranasformed_vertices = tranasform_vertices(vertices, camera)
#   wire_lines = []
#   for face in faces:
#       wire_lines = calculate_wire_lines(face, tranasformed_vertices)
# 
#   image_data = []
#   for wire_line in wire_lines:
#       projection = project_on_camera(wire_line, camera)
#       if projection not None:
#           image_data += projection
#   return image_data



# transform_vertex(vertex, local_vertex, pitch_theta, yaw_theta, roll_theta):
#   return Mrr*Myr*Mpr*Mi*vertex


# project_on_camera(wire_line, camera):
#   return 

# calculate_wire_lines(face, tranasformed_vertices):
#   return three lines of the triangle




        # tranasform_vertices(vertices, camera):
        #   result = []
        #   for vertex in vertices:
        #       result += transform_vertex(vertex, local_vertex, pitch_theta, yaw_theta, roll_theta)
        #   return result
