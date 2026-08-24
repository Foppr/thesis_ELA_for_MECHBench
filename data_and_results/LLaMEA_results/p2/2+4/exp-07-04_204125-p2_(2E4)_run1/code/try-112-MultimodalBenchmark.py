import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Convex quadratic base with dimensionality scaling
        result += 0.5 * np.sum(x**2)
        
        # Saddle-point inducing terms with sinusoidal modulation
        for i in range(self.dim):
            result += 0.3 * x[i]**2 * np.sin(3.0 * x[i])
            result += 0.2 * x[i]**3 * np.cos(2.0 * x[i])
        
        # Multi-frequency sinusoidal modulations with increasing complexity
        for i in range(self.dim):
            result += 0.4 * np.sin(5.0 * x[i]) + 0.3 * np.sin(10.0 * x[i]) + 0.2 * np.sin(15.0 * x[i])
        
        # Cross-term interactions with periodic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(2.0 * (x[i] + x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.15 * coupling
        
        # Chaotic component with exponential decay and sinusoidal perturbations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 0.25 * chaotic
        
        # Fractal-like perturbations with dimension-dependent scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(25.0 * x[i]) * np.cos(13.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += 0.18 * fractal
        
        # Dimensionality-dependent scaling factor
        dim_factor = 1.0 + 0.08 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result