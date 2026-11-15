import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic modulation coefficients
        self.coeffs = np.array([np.sin(i * 0.31) * np.cos(i * 0.57) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Multi-modal sinusoidal components with varying frequencies
        for i in range(self.dim):
            freq = 2.1 + 3.7 * np.sin(i * 0.42)
            result += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.31)
            
        # Exponentially decaying correlation structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.12 * np.abs(i - j))
                result += 0.23 * x[i] * x[j] * decay
                
        # Chaotic modulation with dynamic scaling
        modulator = 0.0
        for i in range(self.dim):
            modulator += self.coeffs[i] * np.sin(x[i] * 1.5)
        result += 0.37 * np.sin(modulator) * np.cos(modulator * 0.67)
        
        # Logarithmic barrier to enforce global minimum
        result += 0.05 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Multi-scale interaction terms with increasing complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.04 * x[i] * x[j] * x[k] * np.sin(x[i] + x[j] + x[k])
                    
        # Enhanced ruggedness with asymmetric peaks
        for i in range(self.dim):
            result += 0.19 * np.sin(7.3 * x[i]) * np.cos(3.7 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Global minimum attractor with multi-dimensional cosine product
        result += 0.15 * np.prod(np.cos(0.47 * x))
        
        # Noise component with chaotic frequency modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.28 * np.sin(9.6 * x[i]) * np.cos(4.8 * x[i]) * np.exp(-0.03 * i)
        result += noise
        
        # Memory-based influence with historical tracking
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.07 * self.history[i] * np.sin(x[i] * 0.41)
            result += hist_influence
        self.history = x.copy()
        
        # Fractal-like self-similarity with multi-scale oscillations
        fractal = 0.0
        for i in range(self.dim):
            fractal += self.coeffs[i] * np.sin(4.2 * x[i]) * np.cos(2.1 * x[i])
        result += 0.11 * fractal
        
        return result