import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with enhanced nonlinearity and interactions
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i]**4 - 10 * x[i]**2 + 6 * x[i] * np.sin(2.5 * np.pi * x[i]) + 0.3 * x[i]**3)
        
        # Add interaction terms between dimensions with varying coefficients
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.15 * x[i] * x[j] * np.sin(np.pi * (x[i]**2 + x[j]**2))
        
        # Add cross-terms and higher-order interactions
        cross_terms = 0
        for i in range(self.dim):
            cross_terms += 0.05 * x[i]**3 * np.cos(1.5 * np.pi * x[i])
            
        # Combined function with different weights to create challenging landscape
        return 0.02 * sphere + multimodal + interaction + cross_terms + 15 * self.dim