import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced rugged component with modified exponentially decaying correlation structure
        for i in range(self.dim):
            result += 0.7 * np.exp(-0.2 * np.abs(x[i])) * np.sin(3.0 * np.pi * x[i])
            
        # Chaotic phase interactions with stronger non-linear coupling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.05 * i))
        result += 0.5 * np.sin(phase_sum) * np.cos(phase_sum * 0.5)
        
        # Multi-scale oscillatory terms with enhanced frequency variations
        for i in range(self.dim):
            freq = 2.0 + 3.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.4 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Cross-dimensional interaction with modified exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = np.exp(-0.02 * (i + j))
                interaction = x[i] * x[j] * np.sin(x[i] + x[j])
                result += decay * interaction
                
        # Asymmetric ruggedness with sharper peaks
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Additional chaotic component with dynamic scaling
        dynamic_scale = np.sum(np.sin(x)**2) + 1.0
        result += 0.3 * np.sin(np.sum(x) * dynamic_scale) * np.cos(np.sum(x) * 0.3 * dynamic_scale)
        
        # Non-separable high-order interactions with increased influence
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.1 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k])
                    
        # Improved global minimum enforcing with logarithmic penalty
        result += 0.015 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Add a new global minimum attractor term
        result += 0.12 * np.prod(np.cos(0.4 * x))
        
        return result