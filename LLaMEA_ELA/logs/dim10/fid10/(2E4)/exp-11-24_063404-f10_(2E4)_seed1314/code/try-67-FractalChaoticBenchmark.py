import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly mutated logistic map parameters for increased chaos
        self.r_values = 3.8 + 0.2 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal component using self-similar cosine patterns at multiple scales
        fractal_sum = 0.0
        scales = [1, 2, 3, 4]
        for scale in scales:
            for i in range(self.dim):
                xi = x_scaled[i]
                # Mutated frequencies and exponential decay
                freq = scale * (i + 1) * np.pi / (self.dim + 2)
                fractal_sum += np.cos(freq * xi) * np.exp(-0.3 * (xi**2) / scale)
        
        # Chaotic component using logistic maps with mutated parameters
        chaotic_sum = 0.0
        x_logistic = 0.4 * np.ones(self.dim)
        for t in range(15):  # More iterations for stronger chaos
            for i in range(self.dim):
                r = self.r_values[i]
                x_logistic[i] = r * x_logistic[i] * (1 - x_logistic[i])
        
        for i in range(self.dim):
            chaotic_sum += x_logistic[i] * np.sin((i + 2) * np.pi * x_scaled[i])
        
        # Mutated cross-dimensional interaction with altered weighting
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                # Modified fractal distance weighting
                weight = 1.0 / (1 + 0.2 * dist**4)
                interaction += weight * np.sin(7 * (x_scaled[i] + x_scaled[j]))
        
        # Enhanced multi-modal component with different amplitudes
        modal_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Changed sine waves with new amplitudes and frequencies
            modal_component += (0.6 * np.sin(12 * xi) + 0.4 * np.sin(25 * xi) + 
                              0.3 * np.sin(35 * xi)) * np.exp(-0.15 * xi**2)
        
        # Mutated combination with adjusted weights
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return dim_factor * (0.5 * fractal_sum + 0.35 * chaotic_sum + 
                           0.25 * interaction + 0.45 * modal_component)