import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (1.0 + 0.3 * np.sin(15 * r) * np.cos(7 * r))
        
        # Angular components with multiple frequencies and chaotic interactions
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i] * (1.0 + 0.1 * np.sin(5 * x_norm[i]))) * \
                      np.cos((i + 1) * np.pi * x_norm[i] * (1.0 + 0.1 * np.cos(3 * x_norm[i])))
        
        # Additional multimodal term with chaotic periodicity and saddle points
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(5 * np.pi * x_norm[i] + np.sin(3 * np.pi * x_norm[i])) * \
                       np.cos(4 * np.pi * x_norm[i] + np.cos(2 * np.pi * x_norm[i]))
        
        # Cross-terms creating complex interaction landscape
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(np.pi * x_norm[i] * x_norm[j]) * np.cos(2 * np.pi * x_norm[i] * x_norm[j])
        
        # Combine all components with different weights
        return 0.25 * radial + 0.35 * angular + 0.25 * periodic + 0.15 * cross + 1.0