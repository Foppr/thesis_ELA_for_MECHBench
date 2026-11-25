import numpy as np

class SinusoidalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add separable sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = 1.0 + 0.2 * np.sin(0.5 * i)
            amp = 1.0 + 0.3 * np.cos(0.3 * i)
            result += amp * np.sin(freq * xi) * np.cos(0.7 * xi)
            
        # Add polynomial coupling terms with dimension-dependent coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff = 1.0 + 0.5 * np.sin(0.4 * i)
            result += coeff * (xi**3 - 2*xi**2 + xi)
            
        # Add non-separable interaction terms with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.4 * np.sin(0.3 * (i + j))
                result += mod * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.6 * (x[i] - x[j]))
                
        # Add saddle-point inducing terms with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            mod = 1.0 + 0.3 * np.sin(0.7 * i) * np.cos(0.5 * i)
            result += mod * (xi**4 - 2*xi**2)
            
        # Add multi-modal structure with peaks at specific locations
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.0 / (1.0 + (xi - 1.5)**2 + 0.1 * np.sin(3.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 1.5)**2 + 0.1 * np.cos(2.0 * xi))
            result += 0.5 * (peak1 + peak2)
            
        # Add gradient complexity through rational functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                numerator = np.sin(x[i]) + np.cos(x[i+1])
                denominator = 1.0 + 0.5 * (x[i]**2 + x[i+1]**2)
                result += 0.3 * (numerator / denominator)
                
        return result