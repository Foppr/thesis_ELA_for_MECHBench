import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Logarithmic-modulated sine waves to create deep, narrow valleys
        f2 = 0.3 * np.sum(np.sin(np.log(np.abs(x) + 1.0)) * np.cos(3.0 * x))
        
        # Trigonometric coupling with dynamic frequency modulation based on input magnitude
        f3 = 0.25 * np.sum(np.sin(5.0 * x + np.cos(2.0 * x)) * np.cos(4.0 * x + np.sin(3.0 * x)))
        
        # Nested exponential and logarithmic interactions to create complex ridges
        f4 = 0.2 * np.sum(np.exp(-np.abs(x)) * np.log(np.abs(x) + 2.0) * np.sin(6.0 * x))
        
        # Adaptive conditioning based on distance from origin with polynomial modulation
        f5 = 0.15 * np.sum((1.0 + 0.5 * np.sum(x**2)) * np.sin(8.0 * x) * np.cos(7.0 * x))
        
        # Coupled sine-cosine waves with logarithmic amplitude scaling
        f6 = 0.1 * np.sum(np.sin(10.0 * x) * np.cos(9.0 * x) * np.log(np.abs(x) + 1.5))
        
        # Multi-scale chaotic modulation with exponential decay
        f7 = 0.12 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Polynomial coupling with trigonometric modulation for enhanced multimodality
        f8 = 0.08 * np.sum((x**5) * np.sin(4.0 * x) * np.cos(5.0 * x))
        
        # Cross-dimensional interaction with nested logarithmic scaling
        f9 = 0.06 * np.sum(np.log(np.abs(x) + 1.0) * np.sin(7.0 * x) * np.cos(6.0 * x))
        
        # Adaptive noise modulation with exponential decay and sine coupling
        f10 = 0.05 * np.sum(np.sin(12.0 * x) * np.cos(11.0 * x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Combine all terms with adjusted weights for better balance
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10