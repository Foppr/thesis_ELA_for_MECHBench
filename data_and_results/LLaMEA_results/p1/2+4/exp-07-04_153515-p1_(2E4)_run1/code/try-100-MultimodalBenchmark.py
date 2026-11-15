import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add enhanced chaotic sine-wave interactions with higher frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(15 * np.sin(x[i])) * np.cos(10 * x[i])
        
        # Add modified radial basis function components with adaptive widths
        centers = np.random.uniform(-5, 5, (7, self.dim))
        widths = np.random.uniform(0.3, 2.5, 7)
        for i in range(7):
            dist = np.sum((x - centers[i])**2)
            f_val += 0.25 * np.exp(-widths[i] * dist) * np.sin(4 * np.sum(x - centers[i]))
        
        # Add enhanced asymmetric polynomial terms with stronger modulation
        for i in range(self.dim):
            if x[i] >= 0:
                f_val += 0.08 * (x[i]**4) * np.sin(3 * x[i]) + 0.05 * (x[i]**6) * np.cos(0.7 * x[i])
            else:
                f_val += 0.07 * (x[i]**5) * np.cos(4 * x[i]) + 0.06 * (x[i]**7) * np.sin(0.4 * x[i])
        
        # Add enhanced interaction term between all pairs of variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.15 * np.sin(5 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.3 * (x[i] - x[j])**2)
        
        # Add a more complex global sinusoidal modulation
        norm = np.sqrt(np.sum(x**2))
        f_val += 0.15 * np.sin(0.7 * norm) * np.cos(0.4 * norm) * np.exp(-0.1 * norm)
        
        # Add a periodic component to increase multimodality
        periodic_term = 0.05 * np.sum(np.sin(2 * np.pi * x))
        f_val += periodic_term
        
        return f_val