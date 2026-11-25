import numpy as np

class HierarchicalGaussianSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Hierarchical Gaussian mixture components
        gaussian_term = 0.0
        for i in range(self.dim):
            # Multiple Gaussian peaks with varying scales and positions
            peak_positions = [np.sin(i * 0.5), np.cos(i * 0.3), np.tan(i * 0.2)]
            peak_scales = [1.0 + 0.5 * np.sin(i * 0.4), 0.8 + 0.3 * np.cos(i * 0.6), 1.2 + 0.4 * np.sin(i * 0.7)]
            
            for pos, scale in zip(peak_positions, peak_scales):
                gaussian_term += np.exp(-0.5 * ((x[i] - pos) / scale)**2)
        
        # Saddle-point induced chaos through adaptive harmonic modulation
        saddle_term = 0.0
        for i in range(self.dim):
            # Create chaotic behavior using sine and cosine combinations with adaptive frequencies
            freq1 = 2.0 + 1.5 * np.sin(i * 0.3)
            freq2 = 1.0 + 0.8 * np.cos(i * 0.4)
            saddle_term += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + 
                           np.cos(freq1 * x[i]) * np.sin(freq2 * x[i]))
        
        # Adaptive dimensional correlation structure
        correlation_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Correlation based on distance and adaptive weights
                dist = abs(x[i] - x[j])
                weight = 0.5 + 0.5 * np.sin((i + j) * 0.2)
                correlation_term += weight * np.exp(-dist**2 / (2.0 * (i + 1)**2))
        
        # Multi-scale fractal-like dimensionality with recursive pattern
        fractal_term = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.8)
            for k in range(1, 4):
                fractal_term += (scale_factor / (k**1.5)) * np.sin(k * x[i] * 2.0) * np.cos(k * x[i] * 1.5)
        
        # Global conditioning with dimension-dependent scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Apply a global transformation that scales based on the dimension
            scale = 1.0 + 0.2 * np.sin(i * 0.5) + 0.1 * np.cos(i * 0.3)
            condition_term += (x[i]**2) / (scale**2)
        
        # Combine all terms with dynamic weights
        total = (0.25 * gaussian_term + 
                0.20 * saddle_term + 
                0.25 * correlation_term + 
                0.20 * fractal_term + 
                0.10 * condition_term)
        
        # Add a global phase modulation based on sum of inputs
        global_mod = 1.0 + 0.2 * np.sin(np.sum(x) * 0.3)
        
        return total * global_mod