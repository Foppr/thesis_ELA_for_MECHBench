import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive scaling
        r_squared = np.sum(x**2)
        base_term = 0.5 * r_squared * (1.0 + 0.1 * np.sin(self.dim))
        
        # Chaotic saddle with enhanced nonlinearity and time-delayed feedback
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//4) % self.dim
            freq = 2.0 + 1.5 * np.cos(i * np.pi / (self.dim + 2))
            saddle_term += np.sin(x[i] * freq) * np.cos(x[i] * freq) * np.sin(x[delay_idx] * 0.7)
        
        # Fractional Brownian motion inspired coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                scale_factor = 0.3 + 0.7 * np.cos(np.log(dist + 1) * 0.5)
                coupling_term += (x[i]**2 + x[j]**2) * np.exp(-0.5 * dist) * scale_factor
        
        # Enhanced local minima with variable depths and positions
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.cos(i * np.pi / (self.dim + 4)) * np.sin(i * np.pi / (self.dim + 6))
            depth = 1.5 + 0.8 * np.cos(i * np.pi / (self.dim + 3))
            weight = np.exp(-0.2 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**4 - 2*x[i]**2)**2
        
        # Multi-scale symmetry with enhanced chaotic behavior
        symmetry_term = 0.0
        scales = [0.1, 0.5, 1.0, 2.0]
        for scale in scales:
            delayed_r = np.sum(np.roll(x, self.dim//3)**2)
            symmetry_term += np.cos(r_squared / scale) * np.sin(delayed_r / (scale + 0.5))
        
        # Add adaptive chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += np.tan(x[i] * (i + 1)) * np.sin(x[i] * (i + 2)) * np.cos(x[i] / (i + 4))
        
        # Adaptive dimensionality scaling with improved conditioning
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.08 * np.cos(self.dim * np.pi / 6)
        
        return dim_factor * (0.3 * base_term + 0.2 * saddle_term + 
                            0.25 * coupling_term + 0.15 * local_minima + 
                            0.05 * symmetry_term + 0.05 * noise)