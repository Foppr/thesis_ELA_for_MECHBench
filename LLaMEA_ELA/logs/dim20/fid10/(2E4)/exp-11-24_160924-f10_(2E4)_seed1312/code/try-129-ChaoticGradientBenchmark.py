import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic sinusoidal components with varying scales and frequencies
        for i in range(self.dim):
            xi = x[i]
            freq = 2.0 + 1.5 * np.sin(0.3 * i) * np.cos(0.4 * i)
            scale = 1.0 + 0.8 * np.sin(0.5 * i) * np.cos(0.6 * i)
            result += scale * np.sin(freq * xi) * np.cos(freq * xi * 0.7)
            
        # Add multi-scale polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff1 = 1.0 + 0.5 * np.sin(0.8 * i)
            coeff2 = 0.3 + 0.2 * np.cos(0.6 * i)
            result += coeff1 * (xi**4 - 3*xi**2) + coeff2 * xi**3
            
        # Add cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity
                mod = 1.0 + 0.6 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                result += mod * np.sin(0.4 * xi) * np.cos(0.3 * x[j]) * (xi**2 + x[j]**2)
                
        # Add chaotic gradient inducing terms
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.0 + 0.7 * np.sin(0.9 * i) * np.cos(0.8 * i)
            result += chaos_factor * (xi**5 - 2*xi**3 + xi)
            
        # Add multi-modal structure with fractal-like peaks
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.0 / (1.0 + (xi - 2.0)**2 + 0.2 * np.sin(5.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.0)**2 + 0.2 * np.cos(4.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.0)**2 + 0.1 * np.sin(7.0 * xi))
            result += 0.6 * (peak1 + peak2 + peak3)
            
        # Add chaotic interaction terms between groups of dimensions
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 2):
                group_sum = x[i] + x[i+1] + x[i+2] + x[i+3]
                result += 0.5 * np.sin(1.5 * group_sum) * np.cos(1.2 * group_sum)
                
        # Add high-frequency oscillatory components for gradient complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(10.0 * xi) * np.cos(8.0 * xi) * np.exp(-0.1 * xi**2)
            
        return result