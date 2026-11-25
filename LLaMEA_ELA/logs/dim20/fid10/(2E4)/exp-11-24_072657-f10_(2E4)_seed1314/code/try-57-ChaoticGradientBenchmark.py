import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multi-scale sinusoidal components with exponentially increasing frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            f2 += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Fractal-like discontinuity using step functions and probabilistic shifts
        f3 = 0.0
        for i in range(self.dim):
            shift = 0.1 * np.random.random()
            f3 += np.abs(np.sin(10 * x_norm[i] + shift)) * np.exp(-np.abs(x_norm[i]))
        
        # Cross-dimensional coupling with chaotic mixing through nested trigonometric terms
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Asymmetric exponential decay with random phase shifts
        f5 = 0.0
        for i in range(self.dim):
            phase = np.random.random() * np.pi
            f5 += np.exp(-np.abs(x_norm[i]) ** 1.5) * np.sin(5 * x_norm[i] + phase)
        
        # Probabilistic basin term with varying weights
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.random.random()
            f6 += weight * np.tanh(x_norm[i]**3)
        
        # Combined chaotic interaction term
        f7 = np.sum(np.sin(3 * x_norm) * np.cos(7 * x_norm) * np.exp(-x_norm**2))
        
        # Add noise and scale
        noise = 0.01 * np.random.random()
        
        return 0.4 * f1 + 1.5 * f2 + 0.6 * f3 + 0.7 * f4 + 0.8 * f5 + 0.5 * f6 + 0.9 * f7 + noise