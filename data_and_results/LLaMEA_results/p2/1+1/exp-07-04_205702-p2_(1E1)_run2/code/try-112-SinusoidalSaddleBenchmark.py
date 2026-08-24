import numpy as np

class SinusoidalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.3 * np.sum(x**2)
        
        # Multiple sinusoidal wells with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            f2 -= 2.0 * np.cos(0.5 * x[i]) * np.sin(1.2 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add saddle point structure with cross-terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += 0.5 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[j]) * (x[i]**2 + x[j]**2)
        
        # Introduce asymmetric basin structure using piecewise exponential functions
        f4 = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                f4 += 1.5 * np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(0.7 * x[i])
            else:
                f4 += 1.0 * np.exp(-0.3 * (x[i] + 1.5)**2) * np.cos(0.9 * x[i])
        
        # Add high-frequency oscillations to increase gradient variation
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.8 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Include interaction terms that create complex landscape features
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.3 * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add noise term to increase robustness
        noise = 0.02 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise