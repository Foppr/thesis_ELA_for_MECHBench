import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.adaptive_params = np.array([np.exp(-0.1 * i) + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with trigonometric modulation
        for i in range(self.dim):
            exp_term = self.adaptive_params[i] * np.exp(-0.5 * x[i]**2) * np.cos(2 * x[i])
            result += exp_term
            
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += coupling
                
        # Add higher-order polynomial with adaptive coefficients
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**6 * np.cos(3 * x[i]) * self.adaptive_params[i]
            result += poly_term
            
        # Introduce a global periodic modulation
        global_periodic = np.sin(0.2 * np.sum(x**2))
        result *= (1 + 0.2 * global_periodic)
        
        # Add noise to increase irregularity
        noise = 0.005 * np.sum(np.sin(x * 15) * np.cos(x * 7))
        result += noise
        
        # Include a modified Schwefel-like term for enhanced multimodality
        schwefel_term = 0.0
        for i in range(self.dim):
            schwefel_term += -x[i] * np.sin(np.sqrt(np.abs(x[i])))
        result += 0.01 * schwefel_term
        
        # Add a conditioning component that varies based on dimension
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (i + 1) * x[i]**4
        result += 0.005 * conditioning
        
        return result