import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term
        result = np.sum(np.exp(-0.1 * np.abs(x))) * 0.5
        
        # Trigonometric coupling with adaptive amplitudes and frequencies
        trig_sum = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.3 * i + 1.0)
            freq = 1.2 + 0.6 * np.cos(0.2 * i + 0.5)  # Slightly increased frequency range
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        result += 2.0 * trig_sum
        
        # Adaptive conditioning with dimension-specific scaling
        cond_sum = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.5 * i + 0.8)
            cond_sum += scale * x[i]**2 * np.exp(-0.05 * x[i]**2)
        result += 1.5 * cond_sum
        
        # Cross-dimensional interactions with varying coupling strengths
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                strength = 0.6 + 0.5 * np.cos(0.3 * (i - j) + 0.6)  # Reduced coupling strength
                cross_sum += strength * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        result += 1.8 * cross_sum
        
        # Multi-scale oscillatory components with varying periods
        multi_sum = 0.0
        for i in range(self.dim):
            period = 1.5 + 2.0 * np.sin(0.4 * i + 0.3)  # Increased period variation
            multi_sum += np.sin(period * x[i]) * np.cos(period * x[i] * 0.6) * np.exp(-0.02 * np.abs(x[i]))
        result += 1.2 * multi_sum
        
        # Fractal-like exponential structure with recursive interaction
        fractal_sum = 0.0
        for i in range(self.dim):
            val = x[i]
            for k in range(1, 4):
                decay = np.exp(-0.2 * k)  # Increased decay rate
                fractal_sum += decay * (np.exp(val) - 1.0) * np.sin(k * val)
                val = np.cos(val)
        result += 0.9 * fractal_sum
        
        # Memory-like effect with delayed interactions
        if self.dim > 1:
            mem_sum = 0.0
            for i in range(1, self.dim):
                delay = 0.3 + 0.4 * np.sin(0.2 * i + 0.7)  # Reduced delay range
                mem_sum += delay * x[i-1] * x[i] * np.exp(-0.05 * (x[i-1]**2 + x[i]**2))
            result += 1.3 * mem_sum
            
        # Asymmetric exponential modulation
        asym_sum = 0.0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.7 * np.sin(0.4 * i + 0.9)  # Increased asymmetry
            asym_sum += asym_factor * (np.exp(-x[i]) - np.exp(x[i])) * np.cos(0.5 * x[i])
        result += 1.1 * asym_sum
        
        return result