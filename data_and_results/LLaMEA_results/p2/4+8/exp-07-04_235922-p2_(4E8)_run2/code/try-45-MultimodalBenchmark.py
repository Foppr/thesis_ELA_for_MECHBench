import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic sinusoidal waves with enhanced exponential decay
        for i in range(self.dim):
            xi = x[i]
            result += (np.sin(2.5 * xi) * np.exp(-0.15 * xi**2) + 
                      0.6 * np.cos(3.5 * xi) * np.exp(-0.08 * xi**2) + 
                      0.4 * np.sin(4.5 * xi) * np.exp(-0.03 * xi**2) +
                      0.2 * np.cos(6.0 * xi) * np.exp(-0.01 * xi**2))
        
        # Add complex interaction terms with higher-order polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced cross-term with quartic decay and trigonometric coupling
                cross_term = np.exp(-0.02 * (x[i]**4 + x[j]**4)) * (x[i]**2 * x[j]**2)
                result += 0.3 * np.sin(x[i] * x[j] * 0.5) * cross_term
        
        # Add higher-order polynomial interaction terms for increased complexity
        for i in range(self.dim):
            result += 0.15 * x[i]**3 + 0.08 * x[i]**4 + 0.03 * x[i]**5
        
        # Add a global scaling factor and noise
        result = result * (1.0 + 0.03 * np.random.random())
        
        return result