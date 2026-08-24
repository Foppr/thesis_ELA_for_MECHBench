import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 1.5  # Fractional dimension for fractal behavior
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        base = np.sum(x**2)
        
        # Fractal-like component with self-similarity
        fractal = 0
        for i in range(self.dim):
            # Use fractional power for fractal behavior
            fractal += np.sum(np.abs(x)**(1.5 + 0.5 * np.sin(i))) * np.sin(0.3 * x[i])
        
        # Fractional Brownian motion approximation
        fbm = 0
        for i in range(self.dim):
            # Approximate fractional Brownian motion with Hurst parameter ~0.7
            fbm += (np.sin(x[i]) * np.cos(0.5 * x[i]) * 
                   np.exp(-0.1 * np.abs(x[i])) * 
                   np.log(1 + 0.1 * x[i]**2))
        
        # Scale-invariant interference patterns
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Scale-invariant coupling with fractal scaling
                interference += (np.sin(3 * x[i]) * np.cos(2 * x[j]) * 
                               np.exp(-0.05 * (x[i] - x[j])**2) * 
                               (1 + 0.1 * np.sin(0.1 * (x[i] + x[j]))))
        
        # Nested multimodal structure with multiple local minima
        nested = 0
        for i in range(self.dim):
            # Create multiple nested minima using polynomial modulations
            nested += (np.sin(5 * x[i]) * np.cos(3 * x[i]) * 
                      np.exp(-0.02 * x[i]**2) * 
                      (1 + 0.3 * np.sin(0.5 * x[i]**3)))
        
        # Non-smooth component with sharp transitions
        nonsmooth = 0
        for i in range(self.dim):
            # Sharp transitions using absolute value and step functions
            nonsmooth += np.abs(x[i]) * np.sin(2 * x[i]) * np.exp(-0.01 * np.abs(x[i]))
        
        # Global scaling factor with fractal dimension influence
        scaling = 1.0 + 0.5 * (self.fractal_dim - 1.0) * np.sin(np.sum(x) / self.dim)
        
        return scaling * (base + fractal + fbm + interference + nested + nonsmooth)