def point_in_polygon(poly, pts):
    def is_point_on_edge(px, py, x1, y1, x2, y2):
        if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
            return (x2 - x1) * (py - y1) == (y2 - y1) * (px - x1)
        return False
    def is_inside(p):
        x, y = p
        n = len(poly)
        inside = False
        for i in range(n):
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % n]
            if is_point_on_edge(x, y, x1, y1, x2, y2):
                return True
            if ((y1 > y) != (y2 > y)):
                x_cross = (x2 - x1) * (y - y1) / (y2 - y1 + 1e-12) + x1
                if x < x_cross:
                    inside = not inside
        return inside
    return [is_inside(pt) for pt in pts]
# Take polygon input
n = int(input("Enter number of vertices in polygon: "))
poly = []
for i in range(n):
    x, y = map(float, input(f"Enter vertex {i+1} (x y): ").split())
    poly.append((x, y))
# Take points input
m = int(input("Enter number of points to check: "))
pts = []
for i in range(m):
    x, y = map(float, input(f"Enter point {i+1} (x y): ").split())
    pts.append((x, y))
result = point_in_polygon(poly, pts)
print(result)