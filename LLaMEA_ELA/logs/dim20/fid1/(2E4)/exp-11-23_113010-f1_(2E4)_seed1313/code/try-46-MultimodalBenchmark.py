import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal components with irrational frequencies
        layer1 = np.sum(np.sin(np.pi * np.sqrt(2) * x_norm) * np.cos(np.pi * np.e * x_norm))
        layer2 = np.sum(np.sin(np.pi * np.sqrt(3) * x_norm**1.5) * np.cos(np.pi * np.pi * x_norm**1.5))
        layer3 = np.sum(np.sin(np.pi * np.sqrt(5) * x_norm**2.5) * np.cos(np.pi * np.sqrt(7) * x_norm**2.5))
        
        # Coupled polynomial basins with adaptive exponents
        poly_basin = np.sum(0.8 * x_norm**6 + 0.5 * x_norm**5 + 0.3 * x_norm**4 + 0.1 * x_norm**3)
        
        # Adaptive cross-dimensional coupling with dynamic weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                weight = 1.0 / (1.0 + np.exp(-10 * (dist - 0.5)))
                cross_interaction += weight * np.sin(3 * np.pi * (x_norm[i]**2 + x_norm[j]**2))
        
        # Sharp funnel structure with exponential decay
        funnel = np.sum(np.exp(-5 * np.abs(x_norm)) * np.sin(10 * x_norm))
        
        # Saddle point with mixed harmonic and hyperbolic components
        saddle = np.sum(x_norm**7 * np.tanh(2 * x_norm) + 0.5 * x_norm**3 * np.cosh(x_norm))
        
        # Add chaotic noise term
        noise = 0.02 * np.random.random() * np.sin(np.pi * np.random.random() * x_norm[0])
        
        return 2.0 * (layer1 + layer2 + layer3) + 1.2 * poly_basin + 0.9 * cross_interaction + 0.7 * funnel + 0.5 * saddle + noise