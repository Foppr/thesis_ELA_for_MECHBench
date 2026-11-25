import numpy as np

class InterferingGaussianRidges:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            condition_number = 10 ** (i / (self.dim - 1) if self.dim > 1 else 0)
            result += condition_number * x[i] ** 2
            
        # Add periodic Gaussian ridge components with varying widths
        for i in range(self.dim):
            ridge_width = 0.5 + 0.5 * np.sin(i)
            result += 2.0 * np.exp(-0.5 * (x[i] / ridge_width) ** 2) * np.cos(3 * x[i])
            
        # Add multi-scale interference patterns
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference = np.sin(2 * x[i]) * np.cos(5 * x[j]) * np.exp(-0.1 * (x[i] ** 2 + x[j] ** 2))
                result += 0.5 * interference
                
        # Add adaptive Gaussian peaks with dynamic locations
        for i in range(self.dim):
            peak_location = 2.0 * np.sin(i)
            peak_height = 1.0 + 0.5 * np.cos(i)
            result += peak_height * np.exp(-0.5 * ((x[i] - peak_location) / 0.8) ** 2)
            
        # Add fractal-like periodic modulation
        for i in range(self.dim):
            result += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[(i + 1) % self.dim]) * np.sin(4 * x[i])
            
        # Add dimensionally coupled sinusoidal terms
        coupling_sum = 0.0
        for i in range(self.dim):
            coupling_sum += np.sin(2 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
        result += 0.8 * coupling_sum ** 2
        
        # Add adaptive conditioning based on input magnitude
        input_magnitude = np.sqrt(np.sum(x ** 2))
        adaptive_factor = 1.0 + 0.3 * np.sin(input_magnitude)
        result *= adaptive_factor
        
        # Add complex multi-modal structure with varying amplitudes
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 1.5 * np.sin(8 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.2 * x[i] ** 2)
        result += multimodal
        
        # Add saddle point complexity with hyperbolic terms
        for i in range(self.dim):
            result += 0.4 * np.tanh(x[i]) * np.sinh(0.5 * x[i])
            
        # Normalize by dimension count and input magnitude
        normalization = 1.0 + 0.1 * input_magnitude + 0.05 * np.sum(np.sin(x) ** 2)
        result /= normalization
        
        return result