import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with chaotic interactions
        multimodal = 0
        for i in range(self.dim):
            # Modified frequencies and weights for more complexity
            term1 = x[i]**2 - 10 * np.cos(2.5 * np.pi * x[i])
            term2 = 5.5 * np.sin(3.2 * np.pi * x[i])
            term3 = 3.5 * np.cos(4.8 * np.pi * x[i])
            multimodal += term1 + term2 + term3
        
        # Modified exponential and polynomial interactions between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.exp(-0.15 * (x[i]**2 + x[j]**2)) * np.sin(0.6 * x[i] * x[j])
        
        # Add chaotic component with high frequency oscillations
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(110 * x[i]) * np.cos(55 * x[i]) + np.log(1 + x[i]**2)
        
        # New component with quartic and higher-order polynomial terms
        complexity = 0
        for i in range(self.dim):
            complexity += (x[i]**4 - 7 * x[i]**2 + 9) * np.sin(1.5 * x[i])
        
        # Combine all components with new weights to create a more challenging landscape
        return sphere + 0.35 * multimodal + 0.25 * interaction + 0.45 * chaotic + 0.55 * complexity + 16 * np.sum(np.sin(x)**4)