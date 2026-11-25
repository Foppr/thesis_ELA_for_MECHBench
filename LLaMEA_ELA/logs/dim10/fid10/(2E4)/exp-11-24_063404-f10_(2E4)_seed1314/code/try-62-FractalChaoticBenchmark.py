import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters for chaotic behavior
        self.r_values = 3.9 + 0.1 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Fractal component using self-similar cosine patterns at multiple scales
        fractal_sum = 0.0
        scales = [1, 2, 3, 5]
        for scale in scales:
            for i in range(self.dim):
                xi = x_scaled[i]
                # Multi-scale cosine pattern with varying frequencies
                freq = scale * (i + 1) * np.pi / (self.dim + 1)
                fractal_sum += np.cos(freq * xi) * np.exp(-0.5 * (xi**2) / scale)
        
        # Chaotic component using logistic maps with dimension-dependent parameters
        chaotic_sum = 0.0
        x_logistic = 0.5 * np.ones(self.dim)
        for t in range(10):  # Iterate chaotic map
            for i in range(self.dim):
                r = self.r_values[i]
                x_logistic[i] = r * x_logistic[i] * (1 - x_logistic[i])
        
        for i in range(self.dim):
            chaotic_sum += x_logistic[i] * np.sin((i + 1) * np.pi * x_scaled[i])
        
        # Cross-dimensional interaction with fractal scaling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                # Fractal distance weighting
                weight = 1.0 / (1 + 0.1 * dist**3)
                interaction += weight * np.sin(5 * (x_scaled[i] + x_scaled[j]))
        
        # Multi-modal component with varying amplitudes
        modal_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Multiple sine waves with different amplitudes and frequencies
            modal_component += (0.5 * np.sin(10 * xi) + 0.3 * np.sin(20 * xi) + 
                              0.2 * np.sin(30 * xi)) * np.exp(-0.1 * xi**2)
        
        # Combine all components with adaptive weights based on dimensionality
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        return dim_factor * (0.6 * fractal_sum + 0.3 * chaotic_sum + 
                           0.2 * interaction + 0.4 * modal_component)