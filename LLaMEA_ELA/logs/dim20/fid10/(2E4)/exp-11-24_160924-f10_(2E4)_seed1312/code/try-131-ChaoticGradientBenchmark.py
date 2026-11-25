import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add enhanced chaotic sinusoidal components with varying scales and frequencies
        for i in range(self.dim):
            xi = x[i]
            freq = 2.5 + 2.0 * np.sin(0.4 * i) * np.cos(0.3 * i)
            scale = 1.5 + 1.2 * np.sin(0.6 * i) * np.cos(0.5 * i)
            result += scale * np.sin(freq * xi) * np.cos(freq * xi * 0.8)
            
        # Add enhanced multi-scale polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff1 = 1.2 + 0.8 * np.sin(0.9 * i)
            coeff2 = 0.4 + 0.3 * np.cos(0.7 * i)
            result += coeff1 * (xi**5 - 4*xi**3 + xi**2) + coeff2 * xi**4
            
        # Add enhanced cross-dimensional coupling with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                mod = 1.2 + 0.8 * np.sin(0.6 * (i + j)) * np.cos(0.4 * (i - j))
                result += mod * np.sin(0.5 * xi) * np.cos(0.4 * x[j]) * (xi**3 + x[j]**3)
                
        # Add enhanced chaotic gradient inducing terms
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.2 + 0.9 * np.sin(1.0 * i) * np.cos(0.9 * i)
            result += chaos_factor * (xi**6 - 3*xi**4 + 2*xi**2)
            
        # Add enhanced multi-modal structure with fractal-like peaks
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.0 / (1.0 + (xi - 2.5)**2 + 0.3 * np.sin(6.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.5)**2 + 0.3 * np.cos(5.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.5)**2 + 0.2 * np.sin(8.0 * xi))
            result += 0.8 * (peak1 + peak2 + peak3)
            
        # Add enhanced chaotic interaction terms between groups of dimensions
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 2):
                group_sum = x[i] + x[i+1] + x[i+2] + x[i+3]
                result += 0.7 * np.sin(2.0 * group_sum) * np.cos(1.5 * group_sum)
                
        # Add enhanced high-frequency oscillatory components for gradient complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * np.sin(12.0 * xi) * np.cos(10.0 * xi) * np.exp(-0.15 * xi**2)
            
        # Add additional chaotic noise term
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += 0.1 * np.sin(3.0 * i + x[i]) * np.cos(2.0 * i - x[i])
        result += noise_term
        
        return result