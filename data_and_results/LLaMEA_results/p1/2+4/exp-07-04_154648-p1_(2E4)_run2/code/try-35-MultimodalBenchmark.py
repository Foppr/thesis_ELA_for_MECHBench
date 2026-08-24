import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for global minimum shift
        self.r = 3.8  # Slightly different logistic map parameter
        self.x_logistic = 0.5  # Initial value for logistic map
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees (slightly modified)
        f1 = np.sum(x_norm**3 + 0.15 * x_norm**5 + 0.03 * x_norm**7)
        
        # Trigonometric components with multiple frequencies (changed frequencies)
        f2 = np.sum(np.sin(7 * np.pi * x_norm)**2 + np.cos(9 * np.pi * x_norm)**2)
        f3 = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Exponential interaction terms (modified decay)
        f4 = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(3 * np.pi * x_norm)**2)
        
        # Cross-dimensional interactions with exponential decay (modified strength)
        cross_term = 0.03 * np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                  np.sin(4 * np.pi * (x_norm[:-1] + x_norm[1:]))**2)
        
        # Chaotic shift based on logistic map (modified impact)
        shift = 0.0
        for i in range(self.dim):
            self.x_logistic = self.r * self.x_logistic * (1 - self.x_logistic)
            shift += self.x_logistic * np.sin(1.5 * np.pi * x_norm[i])
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + cross_term + 0.15 * shift**2