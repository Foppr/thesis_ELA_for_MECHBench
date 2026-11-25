import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(x[i]) * np.exp(-((x[i] - np.pi)**2 / 10.0))
            
        # Additional harmonic component
        harmonic = 0
        for i in range(self.dim):
            harmonic += np.cos(0.5 * x[i]) * np.exp(-((x[i] + np.pi)**2 / 20.0))
        
        # Combine components with different weights
        return sphere * 0.1 + multimodal * 0.3 + harmonic * 0.2