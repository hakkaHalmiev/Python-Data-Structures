import drawsvg
def graph_to_svg(graph):
    d = drawsvg.Drawing(800, 800, (0,0), "d", True)  # coordinates: (0,0) -> left lower corner
    for edge in graph.get_edges():
        d.append(drawsvg.Line( edge.get_left_vertex().get_x(), edge.get_left_vertex().get_y(), edge.get_right_vertex().get_x(), edge.get_right_vertex().get_y(), stroke='blue', stroke_width=3, fill='none', marker_end=''))
    for vertex in graph.get_vertices():
        d.append(drawsvg.Circle(vertex.get_x(), vertex.get_y(), 20, fill='red', stroke_width=2, stroke='black'))
    for vertex in graph.get_vertices():
        d.append(drawsvg.Text( vertex.get_name(), 18, vertex.get_x() - 7, vertex.get_y() - 5, fill='black'))  # Text with font size 85
    f = open('icon.svg', 'w')
    f.write(d.as_svg())
    f.close()
