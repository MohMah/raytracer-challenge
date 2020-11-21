
import pprint
import numpy as np
from math import radians, sin, cos
from functools import reduce
from matplotlib import pyplot as plt
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

def transform_vertex(p_vertex, c_vertex, pitch_theta, yaw_theta, roll_theta):
    Mrr = [[cos(roll_theta), sin(roll_theta), 0, 0],
           [-sin(roll_theta), cos(roll_theta), 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
    Myr = [[cos(yaw_theta), 0, -sin(yaw_theta), 0],
           [0, 1, 0, 0],
           [sin(yaw_theta), 0, cos(yaw_theta), 0],
           [0, 0, 0, 1]]
    Mpr = [[1, 0, 0, 0],
           [0, cos(pitch_theta), sin(pitch_theta), 0],
           [0, -sin(pitch_theta), cos(pitch_theta), 0],
           [0, 0, 0, 1]]
    Mt = [[1, 0, 0, -c_vertex[0]],
           [0, 1, 0, -c_vertex[1]],
           [0, 0, 1,  -c_vertex[2]],
           [0, 0, 0, 1]]
    return reduce(np.dot, [Mrr, Myr, Mpr, Mt, [*p_vertex]])

def transform_vertices(vertices, camera):
  result = []
  for vertex in vertices:
      result.append(transform_vertex(vertex, camera[0], radians(camera[1]), radians(camera[2]), radians(camera[3])))
  return result

def calculate_wire_lines(faces, vertices):
    wire_lines = []
    for face in faces:
        wire_lines.append((vertices[face[0]-1], vertices[face[1]-1]))
        wire_lines.append((vertices[face[1]-1], vertices[face[2]-1]))
        wire_lines.append((vertices[face[2]-1], vertices[face[0]-1]))
    return wire_lines

def project_on_camera(wire_line, camera):
    p1 = wire_line[0]
    p2 = wire_line[1]
    if p1[2] < 1 and p2[2] < 1:
        return None
    # TODO
    focal_length = camera[4]
    return [(focal_length * p1[0] / p1[2], focal_length * p1[1] / p1[2]), (focal_length * p2[0] / p2[2], focal_length * p2[1] / p2[2])]

def render(vertices, faces, camera):
  transformed_vertices = transform_vertices(vertices, camera)
  wire_lines = calculate_wire_lines(faces, transformed_vertices)

  image_data = []
  for wire_line in wire_lines:
      projection = project_on_camera(wire_line, camera)
      if projection is not None:
          image_data.append(projection)
  return image_data

def draw(image_data, image_name):
    plt.clf()
    plt.xlim(-0.5,0.5)
    plt.ylim(-0.5,0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    for line_data in image_data:
        line = plt.Line2D((line_data[0][0], line_data[1][0]), (line_data[0][1], line_data[1][1]), lw=1)
        plt.gca().add_line(line)
    plt.title('Camera: ' + image_name)
    plt.axis('off')
    plt.savefig(image_name)
    # plt.show()


def main():
    vertices, faces, cameras = read_model('model.txt')
    for camera_name, camera in cameras.items():
        image_data = render(vertices, faces, camera)
        draw(image_data, camera_name)

if __name__ == "__main__":
    main()



