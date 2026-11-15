import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(3.0 * x[i]) + 0.3 * np.sin(7.0 * x[i]) + 0.2 * np.sin(11.0 * x[i])
        
        # Radial basis function components with asymmetric scaling
        for i in range(self.dim):
            # Asymmetric radial component
            r = np.sqrt(np.sum(x**2))
            result += 0.4 * np.exp(-0.1 * (x[i] - 2.0)**2) * np.sin(2.0 * r)
        
        # Saddle-point inducing terms with directional asymmetry
        for i in range(self.dim):
            result += 0.3 * x[i]**2 * np.cos(0.5 * x[i]) - 0.1 * x[i]**3
        
        # Cross-term interactions with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.2 * np.sin(2.0 * (x[i] + x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                result += coupling
        
        # Add a structured fractal-like component
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 0.2 * fractal_term
        
        # Add dimensionality-dependent scaling to increase complexity with dimension
        dim_factor = 1.0 + 0.05 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result