import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial sinusoidal component with increasing frequency
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(10 * r) * np.exp(-0.5 * r**2)
        
        # Angular sinusoidal terms with varying frequencies and amplitudes
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 1) * np.pi * x_norm[i])
            angular += 0.5 * np.sin(2 * (i + 1) * np.pi * x_norm[i]) * np.cos(3 * (i + 1) * np.pi * x_norm[i])
        
        # Polynomial penalty terms to increase conditioning
        poly_penalty = 0.0
        for i in range(self.dim):
            poly_penalty += (x_norm[i]**4 + 0.5 * x_norm[i]**3 + 0.2 * x_norm[i]**2)
        
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += 0.1 * np.sin(5 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[j])
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(15 * x_norm[i]) * np.cos(13 * x_norm[i])
        
        # Combine components with appropriate weights
        return 0.4 * radial + 0.3 * angular + 0.2 * poly_penalty + 0.05 * cross_interaction + 0.05 * chaotic + 1.0