import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with fractional-like scaling
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Chaotic saddle points with time-delayed interactions
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//3) % self.dim
            freq = 3.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            saddle_term += np.cos(x[i] * freq) * np.sin(x[i] * freq) * np.cos(x[delay_idx] * 0.5)
        
        # Fractional Brownian motion inspired coupling (mutated weights)
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Add fractional scaling factor
                scale_factor = 0.4 + 0.6 * np.sin(np.log(dist + 1))
                coupling_term += (x[i]**3 + x[j]**3) * np.exp(-0.5 * dist) * scale_factor
        
        # Chaotic local minima with irregular centers and varying depths (mutated depths)
        local_minima = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 5))
            depth = 1.2 + 0.3 * np.sin(i * np.pi / (self.dim + 2))  # Increased variation
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2)**2
        
        # Multi-scale chaotic symmetry with delayed feedback (mutated scales)
        symmetry_term = 0.0
        for scale in [0.15, 0.6, 1.2, 2.0]:  # Changed scale values
            # Add time-delayed component
            delayed_r = np.sum(np.roll(x, self.dim//4)**2)
            symmetry_term += np.sin(r_squared / scale) * np.cos(delayed_r / (scale + 1))
        
        # Add chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2)) * np.tan(x[i] / (i + 3))
        
        # Dimensionality-dependent chaotic scaling
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 4)
        
        return dim_factor * (0.2 * radial_term + 0.3 * saddle_term + 
                            0.25 * coupling_term + 0.2 * local_minima + 
                            0.03 * symmetry_term + 0.07 * noise)