import numpy as np

class SphericalExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical harmonic component with radial frequency
        result = 0.0
        r_squared = np.sum(x**2)
        if r_squared > 1e-10:
            r = np.sqrt(r_squared)
            # Add spherical harmonic terms with different frequencies
            for i in range(self.dim):
                result += 1.5 * np.sin(3 * r) * np.cos(2 * x[i]) * np.exp(-0.1 * r_squared)
        
        # Exponential decay components with varying rates and centers
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.5 * (x[i] - 1.5)**2) + 1.8 * np.exp(-0.3 * (x[i] + 2.0)**2) + 1.2 * np.exp(-0.7 * (x[i] - 3.0)**2)
        
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
                result += 0.8 * coupling
        
        # High-frequency oscillatory terms
        for i in range(self.dim):
            result += 1.3 * np.sin(20 * x[i]) * np.cos(18 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Asymmetric boundary penalties with logarithmic scaling
        for i in range(self.dim):
            if x[i] < 0:
                result += 2.5 * np.log(1 + 0.5 * np.abs(x[i])) * np.exp(-0.3 * x[i]**2)
            else:
                result += 2.0 * np.log(1 + 0.4 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Polynomial interaction terms with cross-dimension coupling
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += x[i]**6 - 2.0 * x[i]**4 + 1.5 * x[i]**2
        result += 1.0 * poly_sum * np.cos(3 * np.sum(x))
        
        # Multi-scale radial components with different decay rates
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.1 * (x[i] - 2.5)**2) * np.sin(4 * x[i])
        
        # Coupling between dimensions using cosine modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.6 * np.cos(7 * (x[i] - x[j])) * np.exp(-0.15 * (x[i] + x[j])**2)
        
        # Fractal-like structure with recursive terms
        fractal_term = 1.0
        for i in range(self.dim):
            fractal_term *= np.sin(8 * x[i]) + np.cos(6 * x[i])
        result += 1.4 * fractal_term
        
        # Additional high-frequency chaotic modulation
        chaos_sum = 0.0
        for i in range(self.dim):
            chaos_sum += np.sin(25 * x[i]) * np.cos(23 * x[i])
        result += 0.9 * chaos_sum
        
        return result