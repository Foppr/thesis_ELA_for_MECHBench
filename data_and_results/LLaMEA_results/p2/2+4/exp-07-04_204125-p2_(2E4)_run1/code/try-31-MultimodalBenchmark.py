import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Exponential terms with chaotic coupling
        for i in range(self.dim):
            # Base exponential term
            result += np.exp(0.4 * x[i]**2) - 1.0
            
            # Multi-frequency sinusoidal modulations
            result += 0.5 * np.sin(4.0 * np.pi * x[i]) + 0.3 * np.cos(3.0 * np.pi * x[i]) + 0.2 * np.sin(5.0 * np.pi * x[i])
            
            # Chaotic coupling between adjacent variables
            if i < self.dim - 1:
                result += 0.2 * np.exp(-0.2 * (x[i]**2 + x[i+1]**2)) * np.sin(3.0 * (x[i] - x[i+1]))
            
            # Saddle-point inducing terms with asymmetric coefficients
            result += 0.2 * x[i]**3 * np.cos(0.8 * x[i]) + 0.05 * x[i]**4 * np.sin(0.6 * x[i])
            
            # Higher-order polynomial with alternating signs and variable exponents
            exp_factor = 5 + (i % 3)
            result += 0.08 * (-1)**i * x[i]**exp_factor
        
        # Add inter-variable coupling with exponential decay and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.05 * (i - j)**2) * np.sin(0.5 * (x[i] + x[j]) + 0.3 * (i - j))
                result += 0.15 * coupling
        
        # Add noise-like perturbations for non-convexity with variable intensity
        result += 0.02 * np.sum(np.abs(x)**1.9)
        
        # Add asymmetric cross-dimensional terms
        for i in range(self.dim):
            result += 0.1 * x[i] * np.sin(2.0 * x[(i+1) % self.dim]) * np.cos(1.5 * x[(i+2) % self.dim])
        
        # Add a global scaling factor to increase landscape complexity
        result *= 1.2 + 0.3 * np.sin(0.5 * np.sum(x**2))
        
        return result