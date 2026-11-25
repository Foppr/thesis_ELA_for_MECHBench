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
        
        # Add coupling between dimensions with non-linear interaction terms - modified coefficients
        coupled = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupled += (x[i]**3 + x[j]**3) * np.sin(0.15 * x[i] * x[j]) * np.cos(0.07 * x[i]**2 + x[j]**2)
        
        # Combine all components with modified weights to create a more challenging landscape
        return sphere + 0.4 * multimodal + 0.15 * interaction + 0.35 * chaotic + 0.55 * complexity + 0.25 * high_freq + 0.25 * coupled + 18 * np.sum(np.sin(x)**4)