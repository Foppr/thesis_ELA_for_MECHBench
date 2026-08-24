import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.1 * np.sum(x**2)
        
        # Radial Basis Functions with chaotic centers and varying widths
        f2 = 0.0
        centers = np.array([[np.sin(0.3 * i), np.cos(0.4 * i)] + [0.0] * (self.dim - 2) for i in range(8)])[:self.dim]
        for i in range(8):
            center = centers[i % len(centers)]
            sigma = 0.5 + 0.5 * np.sin(0.2 * i)
            height = 1.0 + 2.0 * np.cos(0.3 * i)
            rbf = height * np.exp(-0.5 * np.sum(((x - center) / sigma)**2))
            f2 += rbf
        
        # Sinusoidal modulation with chaotic frequency and amplitude
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.sin(2.0 * x[i] + 0.5 * np.sin(3.0 * x[i])) * np.cos(1.5 * x[i] + 0.3 * np.sin(2.5 * x[i]))
        
        # Polynomial interactions with chaotic coefficients
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.1 + 0.2 * np.sin(0.5 * (i + j))
                f4 += coeff * x[i]**2 * x[j]**3 * np.sin(0.2 * x[i] + 0.3 * x[j])
        
        # Cross-term interactions with exponential decay
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f5 += np.exp(-0.1 * (x[i] - x[j])**2) * np.cos(2.0 * x[i] * x[j])
        
        # Asymmetric peaks with chaotic positioning and varying heights
        f6 = 0.0
        for i in range(12):
            mu = np.array([3.0 * np.sin(0.4 * i), 2.0 * np.cos(0.3 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.3 + 0.4 * np.sin(0.6 * i)
            height = 0.5 + 1.5 * np.cos(0.5 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            f6 += peak
        
        # Add chaotic noise component
        noise = 0.02 * np.random.rand() * (1.0 + 0.3 * np.sin(np.sum(x**2)))
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise