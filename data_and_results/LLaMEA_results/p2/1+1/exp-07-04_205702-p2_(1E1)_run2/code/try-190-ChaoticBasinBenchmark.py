import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Asymmetric Gaussian peaks with chaotic positioning
        f2 = 0.0
        for i in range(8):
            mu = np.array([3.0 * np.sin(0.3 * i), 2.0 * np.cos(0.4 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.3 + 0.4 * np.sin(0.5 * i)
            height = 2.0 + 3.0 * np.cos(0.6 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            f2 += peak
        
        # Sine-based cross-terms with chaotic modulation
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f3 += 0.5 * np.sin(2.0 * x[i] + 0.3 * np.sin(1.5 * x[j])) * np.cos(1.2 * x[j] + 0.4 * np.cos(1.8 * x[i]))
        
        # Asymmetric basin structure with exponential and trigonometric components
        f4 = 0.0
        for i in range(self.dim):
            f4 -= 0.8 * np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(0.8 * x[i] + 0.3 * np.cos(1.2 * x[i]))
        
        # Polynomial interaction terms with chaotic coefficients
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f5 += 0.1 * x[i]**3 * x[j]**2 * np.sin(0.5 * x[i] + 0.6 * x[j] + 0.2 * np.sin(x[i] * x[j]))
        
        # Chaotic sine modulation with higher-order terms
        f6 = 0.0
        for i in range(self.dim):
            f6 += 0.3 * np.sin(2.5 * x[i] + 0.1 * np.sin(3.0 * x[i]**2)) * np.cos(0.7 * x[i]**3 + 0.2 * np.cos(1.5 * x[i]))
        
        # Add noise for robustness
        noise = 0.02 * np.random.rand() * (1.0 + 0.3 * np.sin(np.sum(x**2)))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise