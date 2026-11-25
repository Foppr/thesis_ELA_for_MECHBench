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
        
        # Enhanced chaotic saddle points with adaptive coupling
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//4) % self.dim
            freq = 2.5 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            saddle_term += np.cos(x[i] * freq) * np.sin(x[i] * freq) * np.cos(x[delay_idx] * 0.7)
        
        # Adaptive fractional Brownian motion inspired coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Add adaptive scaling factor based on dimensionality
                scale_factor = 0.6 + 0.4 * np.sin(np.log(dist + 1) * (self.dim / 10.0))
                coupling_term += (x[i]**3 + x[j]**3) * np.exp(-0.3 * dist) * scale_factor
        
        # Enhanced chaotic local minima with adaptive centers and depths
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 4))
            depth = 1.2 + 0.3 * np.sin(i * np.pi / (self.dim + 3))
            weight = np.exp(-0.25 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2)**2
        
        # Multi-scale chaotic symmetry with enhanced delayed feedback
        symmetry_term = 0.0
        for scale in [0.15, 0.6, 1.3, 2.2]:
            # Add enhanced time-delayed component
            delayed_r = np.sum(np.roll(x, self.dim//3)**2)
            symmetry_term += np.sin(r_squared / scale) * np.cos(delayed_r / (scale + 1.5))
        
        # Enhanced chaotic noise component with adaptive frequency
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1.5)) * np.cos(x[i] * (i + 2.5)) * np.tan(x[i] / (i + 2.0))
        
        # Enhanced dimensionality-dependent scaling with adaptive factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * np.pi / 5)
        
        return dim_factor * (0.3 * radial_term + 0.2 * saddle_term + 
                            0.25 * coupling_term + 0.15 * local_minima + 
                            0.05 * symmetry_term + 0.05 * noise)