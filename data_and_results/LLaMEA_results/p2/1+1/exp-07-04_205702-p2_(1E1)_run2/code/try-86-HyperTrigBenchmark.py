import numpy as np

class HyperTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.1 * np.sum(x**2)
        
        # Hyperbolic sine and cosine peaks for multimodality
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sinh(0.5 * x[i]) * np.cosh(0.3 * x[i])
        
        # Interconnected trigonometric terms with varying frequencies
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.sin(0.7 * x[(i+1) % self.dim])
        
        # Cross-dimensional interaction with exponential decay
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3.0 * (x[i] + x[j]))
        
        # Asymmetric basin structure using piecewise functions
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                f5 += 2.0 * np.exp(-0.5 * x[i]**2) * np.cos(1.2 * x[i])
            else:
                f5 += 0.5 * np.exp(-0.3 * x[i]**2) * np.sin(1.8 * x[i])
        
        # Add periodic modulation with varying amplitude
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]) * (1.0 + 0.2 * np.sin(2.0 * x[i]))
        
        # Combine all components with noise
        noise = 0.01 * np.random.rand()
        
        return f1 + f2 + f3 + f4 + f5 + f6 + noise