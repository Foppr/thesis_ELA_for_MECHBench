import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic modulation coefficients
        self.coeffs = np.array([np.sin(i * 0.314) * np.cos(i * 0.456) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Exponentially decaying correlation structure with chaotic modulation
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.15 * np.abs(x[i])) * np.sin(3.1 * x[i] + self.coeffs[i])
            
        # Multi-scale sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.25)
            result += 0.6 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.33)
            
        # Cross-dimensional interaction with exponentially decaying weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.08 * np.abs(i - j))
                result += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Chaotic phase interactions with dynamic coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.05 * i))
        result += 0.4 * np.sin(phase_sum * 1.5) * np.cos(phase_sum * 0.8)
        
        # High-frequency oscillatory component
        for i in range(self.dim):
            result += 0.3 * np.sin(15.0 * x[i]) * np.cos(7.5 * x[i])
            
        # Non-separable higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.05 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.5)
                    
        # Asymmetric ruggedness with sharp peaks
        for i in range(self.dim):
            result += 0.2 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Memory-dependent term with historical influence
        if hasattr(self, 'history'):
            hist_influence = 0.0
            for i in range(self.dim):
                hist_influence += 0.08 * self.history[i] * np.sin(x[i] * 0.4)
            result += hist_influence
        self.history = x.copy()
        
        # Fractal-like self-similarity with multi-scale components
        fractal = 0.0
        for i in range(self.dim):
            fractal += self.coeffs[i] * np.sin(2.5 * x[i]) * np.cos(1.25 * x[i])
        result += 0.15 * fractal
        
        # Global minimum enforcing term with logarithmic penalty
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x)))
        
        return result