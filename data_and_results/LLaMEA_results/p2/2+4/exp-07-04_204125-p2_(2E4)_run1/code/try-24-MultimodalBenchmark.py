import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Hyperbolic tangent exponential terms with chaotic coupling
        for i in range(self.dim):
            # Base hyperbolic tangent term
            result += np.tanh(0.5 * x[i]) ** 2
            
            # Complex sinusoidal modulation with varying frequency and amplitude
            result += 0.4 * np.sin(3.0 * np.pi * x[i]) * np.cos(2.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
            
            # Chaotic coupling between adjacent variables with hyperbolic coupling
            if i < self.dim - 1:
                coupling = np.tanh(0.3 * (x[i] - x[i+1])) * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
                result += 0.25 * coupling * np.sin(4.0 * (x[i] + x[i+1]))
            
            # Saddle-point inducing terms with hyperbolic sine
            result += 0.15 * x[i] * np.sinh(0.4 * x[i]) * np.cos(0.3 * x[i])
            
            # Higher-order polynomial with alternating signs and exponential decay
            result += 0.08 * (-1)**i * np.exp(-0.01 * i) * x[i]**4
        
        # Add inter-variable coupling with hyperbolic decay and complex modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.tanh(0.2 * (i - j)) * np.sin(0.5 * (x[i] - x[j]))
                result += 0.12 * coupling * np.cos(0.2 * (x[i] + x[j]))
        
        # Add noise-like perturbations with fractional exponents and hyperbolic functions
        result += 0.02 * np.sum(np.abs(np.tanh(x))**1.3)
        
        # Add a complex global modulation term
        global_mod = np.sin(0.1 * np.sum(x**2)) * np.cos(0.05 * np.sum(x))
        result += 0.3 * global_mod
        
        return result