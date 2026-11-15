import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic and sinusoidal components
        for i in range(self.dim):
            result += 0.5 * x[i]**2 + 0.3 * np.sin(5.0 * x[i]) + 0.2 * np.cos(3.0 * x[i])
        
        # Asymmetric saddle point terms with varying coefficients
        for i in range(self.dim):
            result += 0.4 * x[i]**3 + 0.1 * x[i]**5 + 0.3 * np.abs(x[i]) * np.sin(2.0 * x[i])
        
        # Cross-dimensional coupling with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(2.0 * (x[i] - x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.2 * coupling
        
        # Non-smooth perturbations with exponential decay
        for i in range(self.dim):
            result += 0.15 * np.abs(x[i])**1.7 + 0.1 * np.sin(20.0 * x[i])
        
        # Fractal-like irregularity with dimension-dependent scaling
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(10.0 * x[i]) * np.cos(15.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        result += 0.2 * fractal_term
        
        # Dimensionality scaling factor
        result *= (1.0 + 0.05 * self.dim)
        
        return result