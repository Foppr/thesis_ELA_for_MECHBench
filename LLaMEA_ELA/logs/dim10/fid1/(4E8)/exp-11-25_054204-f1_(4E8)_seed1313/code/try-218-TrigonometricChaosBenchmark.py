import numpy as np

class TrigonometricChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Trigonometric chaos component with dynamic frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.6 * self.chaotic_sequence[i]
            f2 += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis function component with chaotic centers
        f3 = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(self.chaotic_sequence[i] * np.pi)
            f3 += 0.25 * np.exp(-0.5 * (x[i] - center)**2 / 1.0)
        
        # Cross-dimensional trigonometric coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += 0.15 * np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        
        # Dynamic polynomial exponents with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            exp_mod = 1.0 + 0.3 * np.sin(self.chaotic_sequence[i] * 2.0)
            f5 += 0.2 * (x[i]**(2.0 + exp_mod)) * np.cos(x[i])
        
        # Sine-cosine interaction with dynamic phase
        phase = 0.5 * np.sum(x**2) / self.dim
        f6 = 0.18 * np.sum(np.sin(x + phase) * np.cos(2.0 * x + phase))
        
        # Fractal-like coupling with multiple dimensions
        f7 = 0.0
        for i in range(self.dim - 2):
            f7 += 0.1 * np.sin(x[i] * x[i+1] * x[i+2])
        
        # Adaptive chaotic modulation with exponential scaling
        f8 = 0.0
        for i in range(self.dim):
            mod = np.exp(-np.abs(x[i]) / 3.0)
            f8 += 0.12 * np.sin(3.0 * x[i] + mod) * np.cos(2.0 * x[i])
        
        # Higher-order trigonometric terms
        f9 = 0.05 * np.sum(np.sin(4.0 * x) * np.cos(3.0 * x))
        
        # Multi-scale interaction with chaotic weights
        f10 = 0.0
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.sin(self.chaotic_sequence[i] * 3.0)
            f10 += weight * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Combined scaling factor
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Final function value
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)