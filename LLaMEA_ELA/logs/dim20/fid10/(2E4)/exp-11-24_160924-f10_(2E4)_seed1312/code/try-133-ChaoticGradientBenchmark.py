import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add enhanced chaotic sinusoidal components with increased frequency modulation
        for i in range(self.dim):
            xi = x[i]
            freq = 3.0 + 2.0 * np.sin(0.4 * i) * np.cos(0.5 * i)
            scale = 1.5 + 1.2 * np.sin(0.6 * i) * np.cos(0.7 * i)
            result += scale * np.sin(freq * xi) * np.cos(freq * xi * 0.8) * np.exp(-0.05 * xi**2)
            
        # Add high-order polynomial terms with chaotic coefficients and increased complexity
        for i in range(self.dim):
            xi = x[i]
            coeff1 = 1.2 + 0.8 * np.sin(0.9 * i)
            coeff2 = 0.5 + 0.3 * np.cos(0.7 * i)
            coeff3 = 0.2 + 0.1 * np.sin(0.5 * i)
            result += coeff1 * (xi**6 - 4*xi**4 + 6*xi**2) + coeff2 * xi**5 + coeff3 * xi**3
            
        # Add enhanced cross-dimensional coupling with multi-scale chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                mod = 1.0 + 0.8 * np.sin(0.6 * (i + j)) * np.cos(0.4 * (i - j))
                result += mod * np.sin(0.5 * xi) * np.cos(0.4 * x[j]) * (xi**3 + x[j]**3)
                
        # Add enhanced chaotic gradient inducing terms with higher-order components
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.2 + 0.9 * np.sin(1.0 * i) * np.cos(0.9 * i)
            result += chaos_factor * (xi**7 - 3*xi**5 + 3*xi**3 - xi)
            
        # Add enhanced multi-modal structure with fractal-like peaks and increased complexity
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.0 / (1.0 + (xi - 2.5)**2 + 0.3 * np.sin(6.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.5)**2 + 0.3 * np.cos(5.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.5)**2 + 0.2 * np.sin(8.0 * xi))
            peak4 = 1.0 / (1.0 + (xi + 1.5)**2 + 0.2 * np.cos(7.0 * xi))
            result += 0.8 * (peak1 + peak2 + peak3 + peak4)
            
        # Add enhanced chaotic interaction terms between larger groups of dimensions
        if self.dim >= 6:
            for i in range(0, self.dim - 5, 3):
                group_sum = x[i] + x[i+1] + x[i+2] + x[i+3] + x[i+4] + x[i+5]
                result += 0.7 * np.sin(2.0 * group_sum) * np.cos(1.8 * group_sum)
                
        # Add ultra-high-frequency oscillatory components for extreme gradient complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * np.sin(15.0 * xi) * np.cos(12.0 * xi) * np.exp(-0.15 * xi**2)
            
        # Add additional chaotic noise terms to increase landscape ruggedness
        for i in range(self.dim):
            xi = x[i]
            noise = 0.1 * np.sin(20.0 * xi) * np.cos(18.0 * xi) * (1.0 + 0.5 * np.sin(0.3 * i))
            result += noise
            
        return result