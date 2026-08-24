import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base
        result = np.sum(x**2) * 0.5
        
        # Multi-modal component with exponential decay
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.1 * i) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-dimensional interactions with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                strength = 0.5 * np.exp(-0.05 * (j - i))
                result += strength * x[i] * x[j] * np.sin(x[i] + x[j])
                
        # Chaotic modulation with time-varying parameters
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(x[i] * (1.0 + 0.1 * np.sin(i)))
        result += 1.5 * np.sin(chaotic_sum) * np.cos(0.5 * chaotic_sum)
        
        # Fractal-like self-similarity with multiple scales
        for i in range(self.dim):
            result += 0.8 * np.sin(self.coeffs[i] * x[i]) * np.cos(self.coeffs[i] * x[i] * 0.3) * np.exp(-0.02 * i)
            
        # High-frequency oscillations
        for i in range(self.dim):
            result += 0.3 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        # Asymmetric ruggedness
        for i in range(self.dim):
            result += 0.6 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.01 * x[i]**2)
            
        # Memory-dependent term
        if hasattr(self, 'prev_x'):
            mem_term = 0.0
            for i in range(self.dim):
                mem_term += 0.2 * (x[i] - self.prev_x[i]) * np.sin(x[i])
            result += mem_term
        self.prev_x = x.copy()
        
        # Basin boundary complexity
        for i in range(self.dim):
            result += 0.4 * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.03 * np.abs(x[i]))
            
        # Multi-scale harmonic components
        for i in range(self.dim):
            result += 0.25 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i]) * np.exp(-0.005 * i)
            
        return result