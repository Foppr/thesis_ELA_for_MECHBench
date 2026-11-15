import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base exponential and sinusoidal components with varying frequencies
        for i in range(self.dim):
            result += 0.5 * (np.exp(0.5 * x[i]**2) - 1.0)
            result += 0.6 * np.sin(4.0 * x[i]) + 0.4 * np.sin(8.0 * x[i])
        
        # Asymmetric coupling terms with dimension-dependent strength
        for i in range(self.dim):
            if i < self.dim - 1:
                strength = 0.3 * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
                asymmetry = np.sin(3.0 * x[i]) * np.cos(2.0 * x[i+1])
                result += strength * asymmetry
        
        # Saddle-point inducing cubic and quartic terms with sign modulation
        for i in range(self.dim):
            result += 0.3 * x[i]**3 * np.sin(0.5 * x[i]) + 0.2 * x[i]**4
        
        # Adaptive noise injection based on dimension and position
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(20.0 * x[i]) * np.cos(10.0 * x[i]) * (1.0 + 0.1 * self.dim)
        result += noise
        
        # Cross-dimensional interaction with varying coupling weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(2.0 * (x[i] + x[j]))
                result += 0.2 * coupling
        
        # Fractal-like scaling with dimension-dependent modulation
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(50.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 0.15 * fractal
        
        # Dimensionality scaling factor
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result