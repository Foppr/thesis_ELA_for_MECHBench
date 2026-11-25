import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add enhanced chaotic sinusoidal components with dynamic frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = 1.5 + 2.0 * np.sin(0.4 * i) * np.cos(0.3 * i)
            amp = 0.8 + 1.2 * np.sin(0.6 * i) * np.cos(0.5 * i)
            result += amp * np.sin(freq * xi) * np.cos(freq * xi * 0.6)
            
        # Add enhanced multi-scale polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff1 = 0.5 + 1.5 * np.sin(0.7 * i)
            coeff2 = 0.2 + 0.8 * np.cos(0.5 * i)
            result += coeff1 * (xi**4 - 2*xi**2) + coeff2 * xi**3
            
        # Add enhanced cross-dimensional coupling with adaptive modulation
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling for better control
                mod = 0.8 + 1.0 * np.sin(0.6 * (i + j)) * np.cos(0.4 * (i - j))
                result += mod * np.sin(0.5 * xi) * np.cos(0.4 * x[j]) * (xi**2 + x[j]**2)
                
        # Add enhanced chaotic gradient inducing terms
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 0.7 + 1.3 * np.sin(0.8 * i) * np.cos(0.7 * i)
            result += chaos_factor * (xi**5 - xi**3 + xi**2)
            
        # Add enhanced multi-modal structure with more complex peaks
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.0 / (1.0 + (xi - 2.5)**2 + 0.3 * np.sin(6.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.5)**2 + 0.3 * np.cos(5.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.5)**2 + 0.2 * np.sin(8.0 * xi))
            result += 0.7 * (peak1 + peak2 + peak3)
            
        # Add enhanced chaotic interaction terms between groups of dimensions
        if self.dim >= 4:
            for i in range(0, self.dim - 3, 2):
                group_sum = x[i] + x[i+1] + x[i+2] + x[i+3]
                result += 0.6 * np.sin(2.0 * group_sum) * np.cos(1.5 * group_sum)
                
        # Add enhanced high-frequency oscillatory components
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.sin(12.0 * xi) * np.cos(10.0 * xi) * np.exp(-0.15 * xi**2)
            
        # Add novel fractal-like term to increase complexity
        fractal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            fractal_term += np.sin(3.0 * xi) * np.cos(2.0 * xi) * np.exp(-0.05 * xi**2)
        result += 0.3 * fractal_term
        
        return result