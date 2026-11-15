import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Fractal-like rugged component with nested oscillations
        for i in range(self.dim):
            result += 0.8 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Dynamic phase coupling with recursive scaling
        phase_sum = 0.0
        for i in range(self.dim):
            phase_sum += np.sin(x[i] * np.exp(-0.05 * i)) * np.cos(x[i] * 0.3)
        result += 0.5 * np.sin(phase_sum * 2.0) * np.cos(phase_sum * 0.7)
        
        # Multi-scale fractal oscillations with varying frequencies
        for i in range(self.dim):
            freq = 2.0 + 6.0 * np.sin(i * 0.3) * np.cos(i * 0.1)
            amp = 1.5 + 0.5 * np.sin(i * 0.5)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.02 * x[i]**2)
            
        # Cross-dimensional fractal interaction with power-law decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                decay = (i + j + 1)**(-1.5)
                interaction = x[i] * x[j] * np.sin(x[i] + x[j] + 0.5 * x[i] * x[j])
                result += decay * interaction
                
        # Asymmetric fractal peaks with sharp transitions
        for i in range(self.dim):
            result += 0.2 * np.sin(15 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Nested chaotic attractor with dynamic feedback
        dynamic_scale = np.sum(np.sin(x)**2) + 1.5
        result += 0.3 * np.sin(np.sum(x) * dynamic_scale * 1.2) * np.cos(np.sum(x) * 0.5 * dynamic_scale)
        
        # High-order fractal interactions with exponentially increasing complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.12 * x[i] * x[j] * x[k] * np.sin(x[i] * x[j] * x[k] * 0.5)
                    
        # Fractal penalty term for global minimum localization
        result += 0.03 * np.sum(np.log(1.0 + np.abs(x))) * np.exp(-0.01 * np.sum(x**2))
        
        # Nested fractal minimum attractor
        result += 0.15 * np.prod(np.cos(0.3 * x) + 0.2 * np.sin(x))
        
        # Add fractal basin complexity through recursive oscillation
        for i in range(self.dim):
            result += 0.05 * np.sin(20 * x[i] * np.cos(x[i])) * np.exp(-0.03 * x[i]**2)
            
        return result