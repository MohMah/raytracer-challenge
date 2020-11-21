
import pprint
# vertex = vector =(X, Y, Z, 1)
# vertices = [v1, v2, ... ]
# face = (id1, id2, id3, #vector#)
# camera = (vector, pitch, yaw, roll, focal_length)
# cameras = {name: camera}


# image_data = [ [(x1,y1), (x2,y2)], ... ]

def read_model(file_name):
    vertices = []
    faces = []
    cameras = {}
    with open(file_name) as input_file:
        now_reading = ''
        for line in input_file:
            command = line.strip()
            if not command.strip():
                continue
            if 'VERTICES' in command or 'FACES' in command or 'CAMERAS' in command:
                now_reading = command
                continue
            # reading data lines
            if now_reading == 'VERTICES':
                vertices.append(tuple(map(float, command.split())))
            if now_reading == 'FACES':
                faces.append(tuple(map(int, command.split()[:3])))
            if now_reading == 'CAMERAS':
                split_list = command.split()
                cameras[split_list[-1]] = (tuple(map(float, split_list[:4])), *(map(float, split_list[4:8])))
    return vertices, faces, cameras

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


def main():
    # vertices, faces, cameras = read_model('model.txt')
    pprint.pprint(read_model('model.txt'))
    # for camera_name, camera in cameras.items():
    #     image_data = render(vertices, faces, camera)
    #     draw(image_data, camera_name)



if __name__ == "__main__":
    main()



