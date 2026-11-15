import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r * (1.0 + 0.3 * np.sin(15 * r))) * (1.0 + 0.4 * np.sin(8 * r))
        
        # Angular components with multiple frequencies and chaotic interference
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i] * (1.0 + 0.2 * np.sin(5 * x_norm[i]))) * np.cos((i + 1) * np.pi * x_norm[i] * (1.0 + 0.2 * np.cos(7 * x_norm[i])))
        
        # Additional multimodal term with chaotic periodicity and saddle points
        periodic = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * (1.0 + 0.3 * np.sin(12 * x_norm)))
        
        # Add chaotic cross-terms for increased complexity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(4 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[j]) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all components with different weights
        return 0.25 * radial + 0.35 * angular + 0.25 * periodic + 0.15 * cross_terms + 1.5