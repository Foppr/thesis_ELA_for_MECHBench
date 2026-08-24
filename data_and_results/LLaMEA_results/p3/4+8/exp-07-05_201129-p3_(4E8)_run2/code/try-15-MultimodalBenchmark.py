import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Enhanced multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(5 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Interaction terms with higher frequency oscillations
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.2 * np.sin(2 * (x[i] + x[j])) * np.cos(0.5 * (x[i] - x[j]))
                
        # Additional high-frequency component to increase conditioning difficulty
        high_freq = 0
        for i in range(self.dim):
            high_freq += 0.5 * np.sin(10 * x[i]) * np.cos(3 * x[i])
            
        return sphere + multimodal + interaction + high_freq