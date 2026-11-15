import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaos and variance modulation
        self.chaos_freq = 10.0
        self.variance_scale = 2.0
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian components with adaptive variance and position
        result = 0.0
        for i in range(self.dim):
            # Adaptive variance based on dimension index
            var = self.variance_scale * (1.0 + 0.5 * np.sin(i * 0.7))
            # Shifted center for each dimension
            center = 0.5 * np.cos(i * 0.3)
            # Gaussian term
            gauss = np.exp(-0.5 * ((x_norm[i] - center) / var) ** 2)
            # Multiply by a dimension-specific weight
            weight = 1.0 + 0.3 * np.sin(i * 0.5)
            result += weight * gauss
            
        # Add chaotic sine-wave interference
        chaos = 0.0
        for i in range(self.dim):
            freq = self.chaos_freq * (1.0 + 0.2 * np.sin(i * 0.4))
            chaos += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5)
            
        # Add a polynomial penalty term to increase complexity
        poly_penalty = 0.0
        for i in range(self.dim):
            poly_penalty += 0.1 * x_norm[i]**6 - 0.5 * x_norm[i]**4 + 0.3 * x_norm[i]**2
            
        # Combine all terms
        total = result + chaos + poly_penalty
        
        # Normalize by dimension for scalability
        return total / self.dim