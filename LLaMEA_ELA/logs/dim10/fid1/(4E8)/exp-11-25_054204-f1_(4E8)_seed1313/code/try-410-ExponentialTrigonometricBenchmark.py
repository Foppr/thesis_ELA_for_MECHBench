import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential chaotic sequence for dynamic scaling
        self.exp_sequence = np.exp(np.arange(1, dim + 1) / (dim + 1)) - 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential quadratic term
        f1 = np.sum(np.exp(0.1 * x**2) - 1.0)
        
        # Trigonometric coupling with exponential modulation
        f2 = 0.0
        for i in range(self.dim):
            modulator = self.exp_sequence[i] * 2.0 + 1.0
            f2 += np.sin(modulator * x[i]) * np.cos(modulator * x[i])
        
        # Radial fractal-like interaction with exponential weights
        radial_term = 0.0
        for i in range(self.dim):
            weight = np.exp(-i / (self.dim + 2))
            radial_term += weight * np.sin(x[i] * np.exp(0.5 * x[i]))
        f3 = 1.5 * radial_term
        
        # Exponential chaotic harmonic with dynamic frequency
        f4 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * self.exp_sequence[i]
            f4 += np.exp(-x[i]**2) * np.sin(freq * x[i])
        
        # Cross-dimensional exponential coupling
        cross_exp = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-(i + 1) / (self.dim + 1))
            cross_exp += weight * np.exp(x[i] * x[i+1])
        f5 = 0.8 * cross_exp
        
        # Multi-scale trigonometric modulation with exponential scaling
        f6 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 2.0 * self.exp_sequence[i]
            f6 += np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.5)
        
        # Fractal-like exponential interaction with higher-order terms
        f7 = 0.0
        for i in range(self.dim):
            f7 += np.exp(-x[i]**4) * np.sin(x[i]**3)
        
        # Exponential radial basis with trigonometric modulation
        f8 = 0.0
        for i in range(self.dim):
            f8 += np.exp(-np.abs(x[i])) * np.cos(3.0 * x[i])
        
        # Multi-dimensional exponential coupling with inverse weights
        inv_coupling = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1.0 + i * 0.5)
            inv_coupling += weight * np.exp(x[i] + x[i+1])
        f9 = 0.6 * inv_coupling
        
        # Enhanced exponential trigonometric with fractal scaling
        f10 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 1.5 * self.exp_sequence[i]
            f10 += np.sin(scale_factor * x[i]) * np.cos(scale_factor * x[i] * 2.0)
        
        # Combined dimensionally scaled exponential term
        dim_scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Additional exponential harmonic with modified frequency
        f11 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 4.0 * self.exp_sequence[i]
            f11 += np.exp(-x[i]**2) * np.sin(freq * x[i] * 0.7)
        
        # Complex exponential radial interaction with cosine modulation
        f12 = 0.0
        for i in range(self.dim):
            f12 += np.exp(-np.abs(x[i])) * np.cos(2.0 * x[i])
        
        # Final combined function with refined scaling
        return dim_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)