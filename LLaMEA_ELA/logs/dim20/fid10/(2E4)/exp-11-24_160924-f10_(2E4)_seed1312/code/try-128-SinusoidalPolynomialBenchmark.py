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
            freq = 1.0 + 0.3 * np.sin(0.6 * i)
            amp = 1.0 + 0.4 * np.cos(0.4 * i)
            result += amp * np.sin(freq * xi) * np.cos(0.8 * xi)
            
        # Add polynomial coupling terms with dimension-dependent coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff = 1.0 + 0.6 * np.sin(0.5 * i)
            result += coeff * (xi**4 - 3*xi**3 + 2*xi**2 - xi)
            
        # Add non-separable interaction terms with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 1.0 + 0.5 * np.sin(0.4 * (i + j))
                result += mod * np.sin(0.6 * (x[i] + x[j])) * np.cos(0.7 * (x[i] - x[j]))
                
        # Add saddle-point inducing terms with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            mod = 1.0 + 0.4 * np.sin(0.8 * i) * np.cos(0.6 * i)
            result += mod * (xi**5 - 3*xi**3 + 2*xi)
            
        # Add multi-modal structure with peaks at specific locations
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.0 / (1.0 + (xi - 2.0)**2 + 0.15 * np.sin(4.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.0)**2 + 0.15 * np.cos(3.0 * xi))
            result += 0.6 * (peak1 + peak2)
            
        # Add gradient complexity through rational functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                numerator = np.sin(x[i]) + np.cos(x[i+1])
                denominator = 1.0 + 0.6 * (x[i]**2 + x[i+1]**2)
                result += 0.4 * (numerator / denominator)
                
        # Add higher-order cross-terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    mod = 1.0 + 0.2 * np.sin(0.3 * (i + j + k))
                    result += mod * np.sin(0.4 * x[i]) * np.cos(0.5 * x[j]) * np.sin(0.3 * x[k])
                    
        # Add chaotic noise component to increase landscape irregularity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(10.0 * x[i] + i) * np.cos(7.0 * x[i] - i)
        result += noise
        
        return result