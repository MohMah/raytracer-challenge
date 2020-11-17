
def read_model(file_name):
    with open(file_name) as f:
    for line in f:
        if 'VERTICES' in line:
            pass
        if 'FACES' in line:
            pass
        if 'CAMERAS' in line:
            pass

# vertex = vector =(X, Y, Z, 1)
# vertices = [v1, v2, ... ]
# face = (v1, v2, v3, vector)
# camera = (vector, pitch, yaw, roll, focal_length)
# cameras = {name: camera}


# image_data = [ [(x1,y1), (x2,y2)], ... ]

# get data
# for camera in cameras:
#   image_data = render(vertices, faces, camera)
#   draw(image_data, file_name)




# def render(vertices, faces, camera):
#   transorm_vertices(vertices, camera)
#   project vertices on camera on yz plane
#   project vertices on camera on xz plane
#   draw projected vertices on a square canvas
#   connect vertices using FACES data


# tranasform_vertices(vertices, camera):
#   result = []
#   for vertex in vertices:
#       result += transform_vertex(vertex, local_vertex, pitch_theta, yaw_theta, roll_theta)
#   return result

# transform_vertex(vertex, local_vertex, pitch_theta, yaw_theta, roll_theta):
#   return Mrr*Myr*Mpr*Mi*vertex