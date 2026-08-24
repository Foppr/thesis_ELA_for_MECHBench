import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with enhanced exponential decay and trigonometric peaks
        multimodal = 0
        for i in range(self.dim):
            multimodal += (np.sin(7 * x[i]) * np.exp(-0.1 * x[i]**2) + 
                          0.7 * np.sin(4 * x[i]) * np.exp(-0.15 * (x[i] - 1.5)**2) + 
                          0.3 * np.sin(2 * x[i]) * np.exp(-0.05 * (x[i] + 2)**2))
        
        # Cross-dimensional interaction terms with stronger coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.5 * np.sin(3 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2)) + \
                              0.2 * np.cos(4 * x[i]) * np.sin(1.5 * x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
        
        # Additional high-frequency oscillation component with varying amplitudes
        high_freq = 0
        for i in range(self.dim):
            high_freq += 3 * np.sin(12 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.02 * (x[i] - 1)**2) + \
                        1.5 * np.cos(15 * x[i]) * np.sin(8 * x[i]) * np.exp(-0.01 * (x[i] + 1)**2)
        
        # Add a global shaping term to bias optimization towards the origin
        shaping = 0.1 * np.sum(np.abs(x)**3)
        
        # Combine all components with different weights
        result = 0.3 * sphere + 4 * multimodal + 1.2 * interaction + 2.0 * high_freq + shaping
        
        # Add a small noise term to make it more challenging
        result += 0.008 * np.random.random()
        
        return result