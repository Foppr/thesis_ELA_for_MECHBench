import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced layered sinusoidal components with chaotic frequency modulation
        layer1 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        layer2 = np.sum(np.sin(12 * np.pi * x_norm**1.5) * np.cos(6 * np.pi * x_norm**1.5) * np.exp(-0.3 * x_norm**2))
        layer3 = np.sum(np.sin(15 * np.pi * x_norm**2.5) * np.cos(8 * np.pi * x_norm**2.5) * np.exp(-0.7 * x_norm**2))
        
        # Adaptive polynomial basin terms with dimension-dependent coefficients
        poly_basin = np.sum((0.6 * x_norm**5 + 0.4 * x_norm**4 + 0.2 * x_norm**3 + 0.1 * x_norm**2) / (1 + self.dim * 0.1))
        
        # Stronger cross-dimensional interaction with multiple kernel types
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_interaction += (np.exp(-dist**2) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) + 
                                   0.5 * np.exp(-dist**3) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j])))
        
        # Enhanced saddle structure with fractional powers and multi-scale modulation
        saddle = np.sum(x_norm**(3.5) * np.cos(3 * np.pi * x_norm) * np.sin(1.5 * np.pi * x_norm))
        
        # Additional chaotic component with time-delayed feedback
        chaotic_component = 0.0
        if self.dim > 1:
            for i in range(self.dim):
                chaotic_component += np.sin(2 * np.pi * (x_norm[i] + 0.3 * x_norm[(i+1) % self.dim]))
        
        # Add noise and scale the function
        noise = 0.005 * np.random.random()
        
        return 2.0 * (layer1 + layer2 + layer3) + 1.2 * poly_basin + 0.8 * cross_interaction + 0.6 * saddle + 0.4 * chaotic_component + noise