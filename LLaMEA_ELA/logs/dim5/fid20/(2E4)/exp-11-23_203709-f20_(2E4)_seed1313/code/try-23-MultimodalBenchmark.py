import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with shifted local minima and altered nonlinear terms
        multimodal = 0
        for i in range(self.dim):
            shifted_x = x[i] - 1.2
            multimodal += (shifted_x**4 - 10 * shifted_x**2 + 2 * shifted_x)
        
        # Enhanced interaction term with higher frequency and modified amplitude
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt(x[i]**2 + x[j]**2)
                interaction += 0.3 * x[i] * x[j] * np.sin(4 * distance)
        
        # Add a sine-based cross-term interaction with modified frequency
        cross_term = 0
        for i in range(self.dim):
            cross_term += np.sin(0.7 * x[i])**3
        
        # Combine components with updated weights
        return 0.15 * sphere + 1.8 * multimodal + 0.4 * interaction + 0.25 * cross_term + 12 * self.dim