import numpy as np

class RadialMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial distance from origin
        r = np.sqrt(np.sum(x**2))
        
        # Base radial multimodal component with multiple global minima
        result = 0.0
        for i in range(self.dim):
            result += (x[i]**2 - 10 * np.cos(0.5 * x[i]))**2
        
        # Add radial sinusoidal pattern to create multiple global minima
        radial_pattern = np.sin(0.3 * r) * np.cos(0.7 * r)
        result += 0.5 * radial_pattern * r**2
        
        # Add saddle point structure through polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * x[i]**2 * x[j]**2
        
        # Add a global scaling factor based on distance from origin
        result = result * (1.0 + 0.05 * r)
        
        # Add noise-like perturbations to increase complexity
        noise = 0.01 * np.sum(np.sin(3 * x) * np.cos(2 * x))
        result += noise
        
        return result