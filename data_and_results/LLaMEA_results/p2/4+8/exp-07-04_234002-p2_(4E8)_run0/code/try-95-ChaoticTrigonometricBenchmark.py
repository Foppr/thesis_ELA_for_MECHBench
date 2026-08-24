import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential and trigonometric base terms
        for i in range(self.dim):
            result += np.exp(0.1 * x[i]) * np.sin(2.0 * x[i]) + 0.5 * np.cos(3.0 * x[i]) + 0.1 * x[i]**4
            
        # Cross-dimensional chaotic coupling with sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(2.5 * x[i] + 1.2 * x[j]) * np.cos(1.8 * x[i] - 0.9 * x[j]) + \
                          0.2 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(4.0 * (x[i] + x[j]))
                
        # Add fractal-like irregularities using multiple sine waves with different frequencies
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += 0.05 * np.sin(10.0 * x[i]) + 0.03 * np.sin(17.0 * x[i]) + \
                           0.02 * np.sin(23.0 * x[i]) + 0.01 * np.sin(31.0 * x[i])
            
        result += fractal_term
        
        # Add a conditioning factor that increases with dimensionality and includes higher-order terms
        conditioning = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.1 * np.sum(x**3) + 0.05 * np.sum(x**5)
        result *= conditioning
        
        return result