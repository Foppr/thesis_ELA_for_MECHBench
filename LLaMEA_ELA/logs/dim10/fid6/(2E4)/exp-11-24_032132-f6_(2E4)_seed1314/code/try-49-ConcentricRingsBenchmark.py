import numpy as np

class ConcentricRingsBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.center = np.zeros(dim)
        self.ring_radii = [1.0, 2.0, 3.0, 4.0]
        self.num_minima_per_ring = 8
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Quadratic basin term
        basin = np.sum((x - self.center)**2)
        
        # Central global minimum
        central_term = np.sum((x - self.center)**2)
        
        # Ring local minima
        ring_terms = []
        for radius in self.ring_radii:
            for i in range(self.num_minima_per_ring):
                angle = 2 * np.pi * i / self.num_minima_per_ring
                min_pos = self.center + radius * np.array([np.cos(angle), np.sin(angle)] + [0.0] * (self.dim - 2))
                distance = np.sum((x - min_pos)**2)
                ring_terms.append(distance)
        
        # Find the minimum distance to any ring minimum
        min_ring_distance = min(ring_terms) if ring_terms else float('inf')
        
        # Deceptive term that increases with distance from center
        deceptive_term = 0.1 * np.sum(x**2)
        
        return central_term + min_ring_distance + deceptive_term