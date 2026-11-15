import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add chaotic sine-wave interactions with varying frequencies
        for i in range(self.dim):
            f_val += 0.15 * np.sin(10 * np.sin(x[i])) * np.cos(7 * x[i])
        
        # Add radial basis function components with random centers and widths
        centers = np.random.uniform(-5, 5, (5, self.dim))
        widths = np.random.uniform(0.5, 2.0, 5)
        for i in range(5):
            dist = np.sum((x - centers[i])**2)
            f_val += 0.2 * np.exp(-widths[i] * dist) * np.sin(3 * np.sum(x - centers[i]))
        
        # Add asymmetric polynomial terms with sinusoidal modulation
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.05 * (x[i]**4) * np.sin(2 * x[i]) + 0.02 * (x[i]**6) * np.cos(0.5 * x[i])
            else:
                f_val += 0.05 * (x[i]**5) * np.cos(3 * x[i]) + 0.03 * (x[i]**7) * np.sin(0.3 * x[i])
        
        # Add a complex interaction term between all pairs of variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.sin(4 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Add a global sinusoidal modulation based on the norm of x
        norm = np.sqrt(np.sum(x**2))
        f_val += 0.1 * np.sin(0.5 * norm) * np.cos(0.3 * norm)
        
        return f_val