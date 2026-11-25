import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add nested chaotic sinusoidal components with dynamic frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = 3.0 + 2.5 * np.sin(0.5 * i) * np.cos(0.4 * i) + 0.8 * np.sin(1.2 * i**1.5)
            amp = 2.0 + 1.5 * np.sin(0.7 * i) * np.cos(0.6 * i) + 0.5 * np.cos(1.3 * i**1.3)
            result += amp * np.sin(freq * xi) * np.cos(freq * xi * 0.7) * np.exp(-0.1 * xi**2)
            
        # Add adaptive polynomial terms with dynamic coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff1 = 1.5 + 1.0 * np.sin(1.0 * i) * np.cos(0.8 * i) + 0.3 * np.sin(2.0 * i)
            coeff2 = 0.5 + 0.4 * np.cos(0.9 * i) * np.sin(0.7 * i) + 0.2 * np.cos(1.5 * i)
            coeff3 = 0.2 + 0.1 * np.sin(1.1 * i) * np.cos(0.6 * i)
            result += coeff1 * (xi**6 - 5*xi**4 + 6*xi**2) + coeff2 * xi**5 + coeff3 * xi**3
            
        # Add dynamic cross-dimensional coupling with time-varying modulations
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended coupling range
                mod = 1.5 + 1.0 * np.sin(0.8 * (i + j)) * np.cos(0.5 * (i - j)) + 0.3 * np.cos(1.2 * (i*j))
                result += mod * np.sin(0.6 * xi) * np.cos(0.5 * x[j]) * (xi**4 + x[j]**4)
                
        # Add dynamic chaotic gradient inducing terms with variable exponents
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.5 + 1.2 * np.sin(1.2 * i) * np.cos(1.0 * i) + 0.4 * np.sin(2.5 * i)
            exponent = 2.0 + 0.8 * np.sin(0.9 * i)
            result += chaos_factor * (xi**exponent - 2*xi**(exponent-1) + xi**(exponent-2))
            
        # Add nested multi-modal structure with adaptive peak locations and heights
        for i in range(self.dim):
            xi = x[i]
            peak1 = 1.5 / (1.0 + (xi - 3.0)**2 + 0.4 * np.sin(7.0 * xi) * np.cos(5.0 * xi))
            peak2 = 2.0 / (1.0 + (xi + 3.0)**2 + 0.3 * np.cos(6.0 * xi) * np.sin(4.0 * xi))
            peak3 = 1.2 / (1.0 + (xi - 2.0)**2 + 0.5 * np.sin(8.0 * xi) * np.cos(3.0 * xi))
            peak4 = 1.8 / (1.0 + (xi + 2.0)**2 + 0.6 * np.cos(9.0 * xi) * np.sin(2.0 * xi))
            result += 1.0 * (peak1 + peak2 + peak3 + peak4)
            
        # Add dynamic group interaction terms with varying coupling strengths
        if self.dim >= 6:
            for i in range(0, self.dim - 5, 3):
                group_sum = x[i] + x[i+1] + x[i+2] + x[i+3] + x[i+4]
                coupling_strength = 1.0 + 0.5 * np.sin(0.8 * i) * np.cos(0.6 * i)
                result += coupling_strength * np.sin(3.0 * group_sum) * np.cos(2.0 * group_sum)
                
        # Add ultra-high frequency oscillatory components with adaptive decay
        for i in range(self.dim):
            xi = x[i]
            freq = 15.0 + 10.0 * np.sin(0.6 * i)
            result += 0.8 * np.sin(freq * xi) * np.cos(freq * xi * 0.9) * np.exp(-0.2 * xi**2)
            
        # Add dynamic noise terms with multi-scale correlations
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += 0.15 * np.sin(4.0 * i + x[i]) * np.cos(3.0 * i - x[i]) + \
                         0.05 * np.sin(2.0 * i**1.5 + x[i]) * np.cos(1.5 * i**1.3 - x[i])
        result += noise_term
        
        # Add adaptive dimensionality scaling factors
        dim_factor = 1.0 + 0.2 * np.sin(0.5 * self.dim) * np.cos(0.3 * self.dim)
        result *= dim_factor
        
        return result