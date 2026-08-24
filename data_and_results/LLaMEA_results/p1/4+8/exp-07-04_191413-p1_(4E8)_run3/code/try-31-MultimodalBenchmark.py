import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with exponential decay and trigonometric peaks
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(5 * x[i]) * np.exp(-0.05 * x[i]**2) + 0.5 * np.sin(3 * x[i]) * np.exp(-0.1 * (x[i] - 2)**2)
        
        # Cross-dimensional interaction terms with varying weights
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.3 * np.sin(2 * x[i]) * np.cos(1.5 * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Additional high-frequency oscillation component
        high_freq = 0
        for i in range(self.dim):
            high_freq += 2 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.01 * (x[i] - 1)**2)
        
        # Combine all components with different weights
        result = 0.5 * sphere + 3 * multimodal + 0.8 * interaction + 1.5 * high_freq
        
        # Add a small noise term to make it more challenging
        result += 0.005 * np.random.random()
        
        return result