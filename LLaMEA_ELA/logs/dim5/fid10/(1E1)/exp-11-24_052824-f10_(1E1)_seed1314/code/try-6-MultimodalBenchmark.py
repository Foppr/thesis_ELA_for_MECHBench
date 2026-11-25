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
            # Multiple trigonometric terms with different frequencies
            term1 = x[i]**2 - 10 * np.cos(2 * np.pi * x[i])
            term2 = 5 * np.sin(3 * np.pi * x[i])
            term3 = 3 * np.cos(5 * np.pi * x[i])
            multimodal += term1 + term2 + term3
        
        # Exponential and polynomial interactions between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(0.5 * x[i] * x[j])
        
        # Add chaotic component with high frequency oscillations
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(100 * x[i]) * np.cos(50 * x[i]) + np.log(1 + x[i]**2)
        
        # Add a new complex non-linear component with higher-order polynomial and sine modulation
        complexity = 0
        for i in range(self.dim):
            complexity += (x[i]**6 - 15 * x[i]**4 + 75 * x[i]**2 - 125) * np.sin(x[i] / 2)
        
        # Introduce a novel coupling term that creates stronger dependency between variables
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i]**3 + x[j]**3) * np.sin(0.3 * (x[i] + x[j]))
        
        # Combine all components with varying weights to create a challenging landscape
        return sphere + 0.3 * multimodal + 0.2 * interaction + 0.4 * chaotic + 0.5 * complexity + 0.6 * coupling + 20 * np.sum(np.sin(x)**6)