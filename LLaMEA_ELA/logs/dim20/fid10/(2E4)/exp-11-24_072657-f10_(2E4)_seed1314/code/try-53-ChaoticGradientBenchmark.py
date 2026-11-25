import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Multi-scale sinusoidal components with exponentially increasing frequencies and dynamic phase shifts
        f2 = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            phase = np.sin(i * 0.785) * np.cos(i * 0.523)
            f2 += np.sin(freq * np.pi * x_norm[i] + phase) * np.cos(freq * np.pi * x_norm[i] + phase)
        
        # Fractal-like discontinuity using step functions and probabilistic shifts with memory effect
        f3 = 0.0
        for i in range(self.dim):
            shift = 0.1 * np.random.random()
            # Memory effect: previous dimension influences current
            if i > 0:
                shift += 0.05 * np.sin(x_norm[i-1])
            f3 += np.abs(np.sin(15 * x_norm[i] + shift)) * np.exp(-np.abs(x_norm[i]))
        
        # Cross-dimensional coupling with chaotic mixing through nested trigonometric terms and dynamic weights
        f4 = 0.0
        for i in range(self.dim - 1):
            weight = 0.8 + 0.2 * np.sin(i * 0.314)
            f4 += weight * np.sin(np.pi * (x_norm[i] + x_norm[i+1])) * np.cos(3 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Asymmetric exponential decay with random phase shifts and dynamic exponent
        f5 = 0.0
        for i in range(self.dim):
            phase = np.random.random() * np.pi
            exp_factor = 1.2 + 0.3 * np.sin(i * 0.5)
            f5 += np.exp(-np.abs(x_norm[i]) ** exp_factor) * np.sin(7 * x_norm[i] + phase)
        
        # Probabilistic basin term with varying weights and dynamic thresholds
        f6 = 0.0
        for i in range(self.dim):
            weight = 0.4 + 0.3 * np.random.random()
            threshold = 0.2 + 0.1 * np.sin(i * 0.6)
            if np.abs(x_norm[i]) > threshold:
                f6 += weight * np.tanh(x_norm[i]**3)
            else:
                f6 += weight * x_norm[i]**3
        
        # Combined chaotic interaction term with nested fractal structure
        f7 = 0.0
        for i in range(self.dim):
            inner_sum = 0.0
            for j in range(1, min(4, self.dim - i)):
                inner_sum += np.sin(5 * (x_norm[i] + x_norm[i+j])) * np.cos(9 * (x_norm[i] - x_norm[i+j]))
            f7 += inner_sum * np.exp(-x_norm[i]**2)
        
        # Add noise and scale
        noise = 0.01 * np.random.random()
        
        # Dynamic scaling factor based on problem dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        
        return scale_factor * (0.5 * f1 + 2.0 * f2 + 0.7 * f3 + 0.8 * f4 + 0.9 * f5 + 0.6 * f6 + 1.1 * f7) + noise