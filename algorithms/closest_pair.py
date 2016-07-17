import algorithm
import mergesort


class Algorithm(algorithm.Algorithm):
    '''
    Find the closes pair of points in R2, O(nlogn) complexity.

    Assumptions:
    - no repeated x- or y-coordinates
    '''

    def run(self, pts):
        px = mergesort.Algorithm().run(pts, key=0)
        py = mergesort.Algorithm().run(pts, key=1)
        return self.closest_pair(px, py)

    def closest_pair(self, px, py):
        if len(px) > 3:
            qx, qy, rx, ry = self.split(px, py)
            p1, q1, d1 = self.closest_pair(qx, qy)
            p2, q2, d2 = self.closest_pair(rx, ry)

            delta = min(d1, d2)
            pairs = [(p1, q1, d1), (p2, q2, d2)]

            p3, q3, d3 = self.closest_split_pair(px, py, delta)
            if d3:
                pairs.append((p3, q3, d3))
            return mergesort.Algorithm().run(pairs, key=2)[0]

        return self.simple_closest_pair(px)

    def split(self, px, py):
        i_half = len(px) / 2
        x_half = px[i_half][0]

        qx = px[:i_half]
        rx = px[i_half:]
        qy = []
        ry = []

        for p in py:
            if p[0] >= x_half:
                ry.append(p)
            else:
                qy.append(p)

        return qx, qy, rx, ry

    def closest_split_pair(self, px, py, delta):
        i_half = len(px) / 2
        x_half = px[i_half][0]
        min_pts = ((), ())
        sy = []

        for p in py:
            if p[0] >= x_half - delta and p[0] <= x_half + delta:
                sy.append(p)

        if len(sy) < 2:
            return min_pts + (None,)

        d_min = None
        for i, p in enumerate(sy[:-1]):
            for j in range(1, min(7, len(sy) - i)):
                d = self.euclidean(p, sy[i + j])
                if d < d_min or (d_min is None and d < delta):
                    d_min = d
                    min_pts = (p, sy[i + j])

        return min_pts + (d_min,)

    def simple_closest_pair(self, pts):
        d_min = None
        for i1, p1 in enumerate(pts):
            _pts = pts[i1 + 1:]
            if not _pts:
                break
            for p2 in _pts:
                d = self.euclidean(p1, p2)
                if d < d_min or d_min is None:
                    d_min = d
                    min_pts = (p1, p2)

        return min_pts + (d_min,)

    def create_input(self, n):
        x = self.make_random_ints(n)
        y = self.make_random_ints(n)
        return zip(x, y)
