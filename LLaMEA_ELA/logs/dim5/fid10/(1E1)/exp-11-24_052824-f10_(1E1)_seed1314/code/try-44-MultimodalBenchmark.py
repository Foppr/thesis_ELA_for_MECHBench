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
        
        # Add a new component that introduces more complex non-linearity and improves fitness
        complexity = 0
        for i in range(self.dim):
            complexity += (x[i]**4 - 6 * x[i]**2 + 8) * np.sin(x[i])
        
        # Introduce additional challenging components to improve the benchmark
        # Add a component with higher frequency oscillations and non-smooth behavior
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(20 * x[i]) * np.cos(15 * x[i]) + np.tanh(x[i])**3
        
        # Add coupling between dimensions with non-linear interaction terms
        coupled = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupled += (x[i]**2 + x[j]**2) * np.sin(0.1 * x[i] * x[j]) * np.cos(0.05 * x[i]**2 + x[j]**2)
        
        # Add a new challenging component with fractional powers and logarithmic terms
        fractional = 0
        for i in range(self.dim):
            fractional += (x[i]**1.5) * np.sin(x[i]**2) + np.log(1 + np.abs(x[i]))
        
        # Add a component that creates rugged terrain with sharp gradients
        rugged = 0
        for i in range(self.dim):
            rugged += np.sin(50 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        # Combine all components with varying weights to create a challenging landscape
        return sphere + 0.3 * multimodal + 0.2 * interaction + 0.4 * chaotic + 0.5 * complexity + 0.3 * high_freq + 0.2 * coupled + 0.3 * fractional + 0.4 * rugged + 15 * np.sum(np.sin(x)**4)