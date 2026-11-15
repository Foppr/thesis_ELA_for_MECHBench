import numpy as np

class LogisticChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
        # Logistic map parameter for chaotic behavior
        self.r = 3.95
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic component using logistic map dynamics
        chaotic_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply logistic map transformation
            for _ in range(10):
                xi = self.r * xi * (1 - xi)
            chaotic_penalty += xi**2
        
        # Add multi-modal structure with Gaussian peaks
        multimodal_penalty = 0.0
        peaks = 5
        for k in range(peaks):
            # Peak locations with chaotic distribution
            peak_loc = np.sin(k * np.pi / peaks) * 0.5 + 0.5
            # Add Gaussian peak
            peak_val = np.exp(-np.sum((x - peak_loc)**2) / (2 * 0.1**2))
            multimodal_penalty += peak_val
        
        # Add narrow valley structure
        valley_term = 0.0
        for i in range(self.dim - 1):
            valley_term += (x[i] - x[i+1])**4
        
        # Add saddle point structure
        saddle_term = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                saddle_term += (x[i]**2 - x[i+1]**2)**2
        
        result += 0.5 * chaotic_penalty + 0.3 * multimodal_penalty + 0.1 * valley_term + 0.2 * saddle_term
        
        return result