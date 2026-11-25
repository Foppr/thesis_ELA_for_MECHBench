import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with adaptive scaling
        r_squared = np.sum(x**2)
        radial_term = np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Chaotic saddle points with dynamic coupling
        saddle_term = 0.0
        for i in range(self.dim):
            delay_idx = (i + self.dim//3) % self.dim
            freq = 2.5 + 1.5 * np.sin(i * np.pi / (self.dim + 1))
            coupling_strength = 1.0 + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            saddle_term += coupling_strength * np.cos(x[i] * freq) * np.sin(x[i] * freq) * np.cos(x[delay_idx] * 0.5)
        
        # Fractional Brownian motion inspired multi-scale coupling
        coupling_term = 0.0
        scales = [0.5, 1.0, 2.0]
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                scale_factor = 0.4 + 0.6 * np.sin(np.log(dist + 1))
                # Add adaptive scaling based on dimension
                dim_scale = 1.0 + 0.1 * np.sin(self.dim * np.pi / (i + j + 1))
                coupling_term += dim_scale * (x[i]**3 + x[j]**3) * np.exp(-0.5 * dist) * scale_factor
        
        # Adaptive local minima with dynamic centers and depths
        local_minima = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 5))
            depth = 1.2 + 0.4 * np.sin(i * np.pi / (self.dim + 2))
            # Add adaptive weight scaling
            weight_scale = 1.0 + 0.2 * np.cos(i * np.pi / (self.dim + 4))
            weight = weight_scale * np.exp(-0.25 * (x[i] - center)**2)
            local_minima += weight * depth * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2)**2
        
        # Dynamic symmetry-breaking with multi-scale feedback
        symmetry_term = 0.0
        for scale in [0.1, 0.5, 1.2, 2.0]:
            delayed_r = np.sum(np.roll(x, self.dim//4)**2)
            # Add dynamic phase factor
            phase = 0.5 * np.sin(self.dim * np.pi / (scale + 1))
            symmetry_term += np.sin(r_squared / scale + phase) * np.cos(delayed_r / (scale + 1))
        
        # Chaotic noise with adaptive frequency components
        noise = 0.0
        for i in range(self.dim):
            freq1 = i + 1 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            freq2 = i + 2 + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            freq3 = i + 3 + 0.4 * np.sin(i * np.pi / (self.dim + 3))
            noise += np.sin(x[i] * freq1) * np.cos(x[i] * freq2) * np.tan(x[i] / freq3)
        
        # Adaptive dimensionality factor with enhanced complexity
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * np.pi / 4) + 0.05 * np.cos(self.dim * np.pi / 6)
        
        # Add adaptive weighting to balance terms
        weights = [0.3, 0.2, 0.25, 0.15, 0.05, 0.05]
        
        return dim_factor * (weights[0] * radial_term + 
                            weights[1] * saddle_term + 
                            weights[2] * coupling_term + 
                            weights[3] * local_minima + 
                            weights[4] * symmetry_term + 
                            weights[5] * noise)