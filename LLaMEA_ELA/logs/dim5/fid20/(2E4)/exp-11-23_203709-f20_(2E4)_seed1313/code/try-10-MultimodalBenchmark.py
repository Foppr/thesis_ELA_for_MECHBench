import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Enhanced multimodal component with multiple local minima and peaks
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i]**6 - 15 * x[i]**4 + 75 * x[i]**2 - 50) * np.cos(0.5 * x[i])
        
        # Add a complex interaction term between dimensions with varying weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x[i]**2 + x[j]**2)
                interaction += 0.5 * x[i] * x[j] * np.sin(dist) * np.exp(-0.1 * dist)
        
        # Add a global scaling factor and noise-like perturbation
        noise = 0.01 * np.sum(np.sin(0.7 * x) * np.cos(0.3 * x))
        
        # Combine components with different weights
        return 0.1 * sphere + multimodal + 0.3 * interaction + noise + 20 * self.dim