import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = r * np.sin(10.0 * r) * np.exp(-0.5 * r**2)
        
        # Angular components with nested sinusoidal modulations
        angular = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[i], x_norm[(i+1) % self.dim])
            angular += np.sin(3.0 * angle + 2.0 * r) * np.cos(5.0 * angle - r)
        
        # Non-separable interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Chaotic gradient-dependent conditioning
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1.0 + 0.5 * np.sin(20.0 * x_norm[i])) * x_norm[i]**2
        
        # Combine all components
        result = 0.5 * radial + 0.3 * angular + 0.1 * interaction + 0.1 * conditioning
        
        return result