import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2) * 0.5
        
        # Multi-modal component with exponential decay
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.1 * i) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-dimensional interaction with varying weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = np.exp(-0.05 * (j - i))
                result += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Chaotic modulation with dynamic frequency
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += np.sin(x[i] * (1.0 + 0.1 * np.sin(i)))
        result += 0.8 * np.sin(chaotic_sum) * np.cos(chaotic_sum * 0.5)
        
        # Fractal-like self-similarity with multi-scale oscillations
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.3)
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.02 * i)
            
        # Asymmetric ruggedness with varying amplitudes
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.7)
            result += amp * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Memory-dependent term with previous solution influence
        if hasattr(self, 'prev_x'):
            memory_term = 0.0
            for i in range(self.dim):
                memory_term += 0.3 * (x[i] - self.prev_x[i])**2
            result += memory_term
        self.prev_x = x.copy()
        
        # Global minimum attractor with enhanced penalty
        result += 0.1 * np.sum(np.abs(x)**3)
        
        return result