import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(8 * x[i]) * np.cos(3 * x[i]) + 0.1 * np.sin(5 * x[i])**2
        
        # Cross-dimensional interactions with more complex coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.07 * np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2)
        
        # Additional penalty term with shifted sinusoids and modified scaling
        result += 0.03 * np.sum(np.abs(x - 1.5)**1.5)
        
        # Add a small noise component to increase landscape complexity
        result += 0.005 * np.sum(np.sin(10 * x) * np.cos(10 * x))
        
        return result