import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(3 * x[i]) * np.exp(-0.2 * (x[i] - 1.0)**2)
        
        # Additional oscillatory component with different frequency and shift
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.sin(5 * x[i] + 0.5) * np.exp(-0.05 * (x[i] + 1.0)**2)
        
        # Cross-term interactions with modified interaction strength and nonlinear terms
        cross_term = 0
        for i in range(self.dim-1):
            cross_term += x[i] * x[i+1] * np.sin(2 * (x[i] - x[i+1])**2)
        
        # Combine components with different weights
        return sphere + 0.7 * multimodal + 0.3 * oscillatory + 0.15 * cross_term