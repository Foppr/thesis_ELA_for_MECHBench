import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial layers with varying degrees and interaction terms
        poly_layer1 = np.sum(x_norm**6 + 0.5 * x_norm**4 + 0.2 * x_norm**2)
        poly_layer2 = np.sum(0.3 * x_norm**8 + 0.1 * x_norm**6 + 0.05 * x_norm**4)
        
        # Sinusoidal modulation with frequency that increases with dimension
        freq_mod = np.sum(np.sin((self.dim + 1) * np.pi * x_norm) * np.cos((self.dim + 2) * np.pi * x_norm))
        
        # Cross-dimensional coupling with gradient-dependent interaction
        grad_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_norm[i] - x_norm[j]
                grad_interaction += np.exp(-diff**2) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Saddle point structure with directional dependency
        saddle = np.sum(x_norm * np.cos(4 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Asymmetric hill structure with polynomial and trigonometric components
        hill_structure = np.sum(0.5 * x_norm**3 * np.sin(3 * np.pi * x_norm) + 0.3 * x_norm**5)
        
        # Add noise and scale the function
        noise = 0.01 * np.random.random()
        
        return 1.2 * (poly_layer1 + poly_layer2) + 0.8 * freq_mod + 0.6 * grad_interaction + 0.4 * saddle + 0.3 * hill_structure + noise