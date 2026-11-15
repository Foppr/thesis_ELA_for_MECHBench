import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        # Initialize chaotic global minimum using logistic map
        self.global_min = np.array([2.5 * (1 - 2 * (i % 2)) * np.sin(0.5 * i + self.t) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial interaction with dynamic exponents
        f1 = np.sum((x - self.global_min)**4 + 0.3 * (x - self.global_min)**3)
        
        # Exponential barrier with dynamic scaling
        f2 = np.sum(np.exp(-0.3 * (x - self.global_min)**2) * np.sin(3.0 * x))
        
        # Trigonometric modulation with frequency modulation
        f3 = np.sum(np.cos(2.0 * x + np.sin(x)) * np.exp(-0.2 * np.abs(x)))
        
        # Time-varying global minimum using chaotic dynamics
        self.t += 0.02
        self.global_min = np.array([2.5 * (1 - 2 * (i % 2)) * np.sin(0.5 * i + self.t) for i in range(self.dim)])
        
        # Adaptive noise with dynamic variance
        noise = np.random.normal(0, 0.02 * (1 + 0.5 * np.sin(self.t)), self.dim)
        f4 = np.sum((x - self.global_min + noise)**2 * np.cos(x))
        
        # Hyperbolic and logarithmic coupling
        f5 = np.sum(np.log(1.0 + np.abs(x)) * np.tanh(x))
        
        # Combine all components with optimized weights
        return 0.25 * f1 + 0.2 * f2 + 0.25 * f3 + 0.15 * f4 + 0.15 * f5