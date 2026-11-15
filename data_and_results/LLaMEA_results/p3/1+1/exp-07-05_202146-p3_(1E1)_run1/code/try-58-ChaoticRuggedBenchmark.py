import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced rugged component with stronger chaotic interactions
        for i in range(self.dim):
            result += 0.8 * np.exp(-0.2 * np.abs(x[i])) * np.sin(3.0 * np.pi * x[i])
            
        # Dynamic phase interactions with increased coupling strength
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.1 * i))
        result += 0.5 * np.sin(phase_sum) * np.cos(phase_sum * 0.7)
        
        # Multi-scale oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 2.0 + 5.0 * np.sin(i * 0.3)
            amp = 1.5 + 0.4 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional interaction with stronger exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.05 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Sharper asymmetric ruggedness with enhanced peak formation
        for i in range(self.dim):
            result += 0.2 * np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Dynamic scaling chaotic component with increased influence
        dynamic_scale = np.sum(np.sin(x)**2) + 1.5
        result += 0.3 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.5 * dynamic_scale)
        
        # Increased non-separable high-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.12 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Enhanced global minimum enforcing with logarithmic penalty
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Additional global minimum attractor with stronger influence
        result += 0.15 * np.prod(np.cos(0.6 * x))
        
        # Increased complexity through higher-order cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    for l in range(k+1, self.dim):
                        result += 0.05 * x[i] * x[j] * x[k] * x[l] * np.sin(x[i] + x[j] + x[k] + x[l])
        
        return result