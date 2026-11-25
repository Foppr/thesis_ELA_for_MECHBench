import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with enhanced fractional scaling
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.15 * r_squared) * (r_squared + 1e-8)
        
        # Chaotic saddle points with modified time-delayed interactions
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//4) % self.dim
            freq = 2.5 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            saddle_term += np.cos(x[i] * freq) * np.sin(x[i] * freq) * np.cos(x[delay_idx] * 0.7)
        
        # Fractional Brownian motion inspired coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                scale_factor = 0.4 + 0.6 * np.sin(np.log(dist + 1))
                coupling_term += (x[i]**2 + x[j]**2) * np.exp(-0.3 * dist) * scale_factor
        
        # Enhanced local minima with multi-scale chaotic centers
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 6))
            depth = 1.2 + 0.3 * np.sin(i * np.pi / (self.dim + 3))
            weight = np.exp(-0.25 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**4 - 2*x[i]**2)**2
        
        # Multi-scale chaotic symmetry with improved delayed feedback
        symmetry_term = 0.0
        scales = [0.1, 0.5, 1.0, 2.0]
        for scale in scales:
            delayed_r = np.sum(np.roll(x, self.dim//5)**2)
            symmetry_term += np.sin(r_squared / scale) * np.cos(delayed_r / (scale + 0.5))
        
        # Chaotic noise component with modified frequency spectrum
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1.5)) * np.cos(x[i] * (i + 2.5)) * np.tan(x[i] / (i + 4))
        
        # Adaptive dimensionality scaling with improved conditioning
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * np.pi / 5)
        
        return dim_factor * (0.3 * radial_term + 0.2 * saddle_term + 
                            0.25 * coupling_term + 0.15 * local_minima + 
                            0.05 * symmetry_term + 0.05 * noise)