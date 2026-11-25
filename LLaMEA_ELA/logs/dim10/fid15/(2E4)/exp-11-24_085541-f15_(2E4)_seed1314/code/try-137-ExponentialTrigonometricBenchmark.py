import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term
        result = np.sum(np.exp(-0.5 * x**2)) * 0.1
        
        # Trigonometric coupling with adaptive amplitudes and frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.3 * i + 1.0)
            freq = 1.0 + 0.4 * np.cos(0.2 * i + 0.5)
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        result += 2.5 * trig_sum
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_sum = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.6 * i + 0.8)
            cond_sum += scale * x[i]**4
        result += 1.2 * cond_sum
        
        # Cross-dimension interaction with varying coupling strengths
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                strength = 0.8 + 0.4 * np.cos(0.5 * (i + j) + 1.2)
                cross_sum += strength * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(x[i] * x[j])
        result += 1.8 * cross_sum
        
        # Multi-scale oscillatory components with varying periods
        multi_sum = 0.0
        for i in range(self.dim):
            period = 2.0 + 1.5 * np.sin(0.4 * i)
            multi_sum += np.sin(period * x[i]) * np.cos(period * x[i] * 0.5) * np.exp(-0.05 * x[i]**2)
        result += 1.5 * multi_sum
        
        # Fractal-like structure with recursive trigonometric terms
        fractal_sum = 0.0
        for i in range(self.dim):
            val = x[i]
            for k in range(1, 4):
                coeff = 0.5 + 0.3 * np.sin(0.3 * k)
                fractal_sum += coeff * np.sin(k * val) * np.cos(k * val * 0.6)
                val = np.sin(val)
        result += 0.9 * fractal_sum
        
        # Memory-like effects with weighted previous dimension interactions
        if self.dim > 1:
            mem_sum = 0.0
            for i in range(1, self.dim):
                weight = 0.7 + 0.3 * np.cos(0.5 * i)
                mem_sum += weight * np.exp(-0.2 * (x[i-1] - x[i])**2) * np.sin(x[i-1] * x[i])
            result += 1.3 * mem_sum
            
        # Asymmetric exponential modulation
        asym_sum = 0.0
        for i in range(self.dim):
            asym_factor = 0.5 + 0.5 * np.sin(0.4 * i + 0.7)
            asym_sum += asym_factor * np.exp(-0.3 * x[i]**2) * np.cos(1.5 * x[i])
        result += 1.6 * asym_sum
        
        return result