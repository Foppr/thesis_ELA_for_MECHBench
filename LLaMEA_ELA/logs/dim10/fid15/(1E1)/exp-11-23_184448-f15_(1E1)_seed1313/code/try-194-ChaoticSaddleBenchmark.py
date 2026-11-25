import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with enhanced fractional scaling
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Enhanced chaotic saddle points with adaptive frequency modulation
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//3) % self.dim
            freq = 2.5 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            saddle_term += np.cos(x[i] * freq) * np.sin(x[i] * freq) * np.cos(x[delay_idx] * 0.7)
        
        # Adaptive coupling with dimensionality-aware scaling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Add adaptive scaling factor based on dimensionality
                scale_factor = 0.6 + 0.4 * np.sin(np.log(dist + 1)) * (1.0 + 0.1 * np.log(self.dim + 1))
                coupling_term += (x[i]**3 + x[j]**3) * np.exp(-0.5 * dist) * scale_factor
        
        # Refined local minima with more uniform distribution and varying depths
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 4))
            depth = 1.2 + 0.3 * np.sin(i * np.pi / (self.dim + 3))
            weight = np.exp(-0.4 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2)**2
        
        # Improved multi-scale chaotic symmetry with reduced bias
        symmetry_term = 0.0
        scales = [0.15, 0.5, 1.2, 2.0]
        for scale in scales:
            delayed_r = np.sum(np.roll(x, self.dim//5)**2)
            symmetry_term += np.sin(r_squared / scale) * np.cos(delayed_r / (scale + 0.8))
        
        # Enhanced noise component with better distribution properties
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1.5)) * np.cos(x[i] * (i + 2.5)) * np.tan(x[i] / (i + 2.0))
        
        # Dimensionality-dependent scaling with improved balance
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * np.pi / 5)
        
        return dim_factor * (0.3 * radial_term + 0.2 * saddle_term + 
                            0.25 * coupling_term + 0.15 * local_minima + 
                            0.05 * symmetry_term + 0.05 * noise)