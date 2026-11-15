import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Fractal-like self-similar structure using recursive sine-cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            term = 0.0
            for k in range(1, 6):  # Depth of recursion
                term += np.sin(k * x_norm[i]) * np.cos(k * x_norm[i] * 0.5) * np.exp(-0.1 * k**2)
            fractal += term**2
        
        # Hybrid polynomial-exponential interaction terms
        hybrid = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_part = (x_norm[i]**3 + x_norm[j]**3)
                exp_part = np.exp(-0.02 * (x_norm[i]**2 + x_norm[j]**2))
                hybrid += poly_part * exp_part * np.sin(5 * (x_norm[i] - x_norm[j]))
        
        # Adaptive conditioning based on dimensionality
        adapt_cond = np.sum(np.abs(x_norm)**(1 + 0.1 * self.dim))
        
        # Multi-scale oscillatory component with varying frequencies
        multi_scale = 0.0
        for k in range(1, 8):
            freq = k * (1 + 0.2 * np.sin(0.5 * k))
            multi_scale += np.sin(freq * x_norm).sum()**2
        
        # Chaotic perturbation with time-delayed feedback
        chaotic = 0.0
        for i in range(self.dim):
            delayed = x_norm[i] if i == 0 else x_norm[i-1]
            chaotic += np.sin(10 * x_norm[i] + 0.5 * np.sin(15 * delayed)) * np.cos(7 * x_norm[i])
        
        # Global optimum shift with non-linear transformation
        shift = np.sum((x_norm - 0.2 * np.sin(x_norm))**2)
        
        # Combine all components with dynamic weights
        return 0.3 * quadratic + 1.2 * fractal + 1.5 * hybrid + 0.7 * adapt_cond + 1.0 * multi_scale + 0.8 * chaotic + 0.4 * shift