import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multi-scale sinusoidal components with modified exponentially increasing frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 3**(i % 5 + 1)  # Changed base frequency from 2 to 3
            f2 += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Fractal-like discontinuity using modified step functions and probabilistic shifts
        f3 = 0.0
        for i in range(self.dim):
            shift = 0.15 * np.random.random()  # Increased shift magnitude
            f3 += np.abs(np.sin(12 * x_norm[i] + shift)) * np.exp(-np.abs(x_norm[i]))  # Increased frequency
        
        # Cross-dimensional coupling with enhanced chaotic mixing through nested trigonometric terms
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(2 * np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(3 * np.pi * (x_norm[i] - x_norm[i+1]))  # Changed coupling
        
        # Asymmetric exponential decay with modified phase shifts
        f5 = 0.0
        for i in range(self.dim):
            phase = np.random.random() * np.pi * 1.5  # Increased phase range
            f5 += np.exp(-np.abs(x_norm[i]) ** 1.7) * np.sin(6 * x_norm[i] + phase)  # Changed exponent and frequency
        
        # Probabilistic basin term with modified weights
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.6 + 0.4 * np.random.random()  # Changed weight range
            f6 += weight * np.tanh(x_norm[i]**4)  # Changed power to 4
        
        # Combined chaotic interaction term with modified parameters
        f7 = np.sum(np.sin(4 * x_norm) * np.cos(8 * x_norm) * np.exp(-x_norm**2))  # Changed frequencies
        
        # Add noise and scale
        noise = 0.015 * np.random.random()  # Increased noise level
        
        return 0.3 * f1 + 1.7 * f2 + 0.7 * f3 + 0.8 * f4 + 0.9 * f5 + 0.6 * f6 + 1.0 * f7 + noise