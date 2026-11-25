import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian mixture centers and weights for diversity
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.dirichlet(np.ones(10))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian mixture component
        gauss = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            gauss += self.weights[i] * np.exp(-0.5 * np.sum(diff**2 / (2.0 + 0.5 * np.abs(x))))
        
        # Trigonometric chaotic component with dynamic frequencies
        trig = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * 
                     np.exp(-0.1 * np.sum(x**2)))
        
        # Adaptive conditioning term that changes based on x magnitude
        cond = np.sum((1.0 + 0.1 * np.abs(x)) * x**2 + 0.05 * x**4)
        
        # Cross-term interactions with sigmoid modulation
        cross = np.sum(1.0 / (1.0 + np.exp(-x)) * np.sin(0.5 * x) * 
                      np.cos(0.3 * x) * np.exp(-0.01 * np.sum(x**2)))
        
        # Asymmetric noise with varying amplitude
        noise = np.sum(0.3 * np.sin(4.0 * x + 1.0) * np.cos(2.0 * x - 1.0) * 
                      (1.0 + 0.5 * np.sin(x)))
        
        # Global shaping with polynomial and exponential components
        global_term = 0.01 * np.sum(x**3 * np.exp(-0.05 * np.abs(x)) + 
                                  0.5 * x**6 * np.cos(0.2 * x))
        
        return gauss + trig + cond + cross + noise + global_term