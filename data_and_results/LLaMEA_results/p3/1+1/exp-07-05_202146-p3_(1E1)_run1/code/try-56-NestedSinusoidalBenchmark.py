import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        result = 0.5 * np.sum(x**2)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Multi-scale interaction terms with dynamic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                coupling = 0.3 * np.sin(0.5 * (x[i] + x[j]))
                result += coupling * np.exp(-0.1 * np.abs(x[i] - x[j]))
                
        # Dynamic scaling based on coordinate positions
        scale_factor = 1.0 + 0.2 * np.sum(np.sin(x)**2)
        result *= scale_factor
        
        # Gradient-based conditioning with directional sensitivity
        grad_penalty = 0.0
        for i in range(self.dim):
            grad_penalty += np.abs(x[i]) * np.sin(x[i] * 2.0)
        result += 0.1 * grad_penalty
        
        # Asymmetric ruggedness with sharp local minima
        for i in range(self.dim):
            result += 0.2 * np.sin(10 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # High-order non-separability with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.05 * x[i]**2 * x[j] * x[k] * np.cos(x[i] + x[j] + x[k])
                    
        # Global minimum attractor with soft constraint
        result += 0.05 * np.sum(np.cos(0.3 * x) - 1.0)
        
        return result