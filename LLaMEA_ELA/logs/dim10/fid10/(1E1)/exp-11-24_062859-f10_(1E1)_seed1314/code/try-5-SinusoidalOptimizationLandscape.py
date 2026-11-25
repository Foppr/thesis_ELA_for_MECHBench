import numpy as np

class SinusoidalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic function with global minimum at origin
        result = 0.3 * np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 2.5 + 0.5 * np.sin(i)
            freq2 = 3.0 + 0.3 * np.cos(i)
            result += 0.4 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * \
                     np.exp(-0.1 * np.abs(x[i]))
            
        # Add polynomial interaction terms with high degree and cross-coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for efficiency
                result += 0.15 * (x[i]**3) * (x[j]**2) * np.sin(x[i] + x[j]) + \
                         0.1 * x[i]**4 * x[j]**3 * np.cos(x[i] - x[j])
                
        # Add a complex gradient structure using a modified logistic map
        for i in range(self.dim):
            logistic_val = 4.0 * x[i] * (1.0 - x[i])
            result += 0.25 * np.sin(logistic_val * 10) * np.cos(x[i]**2)
            
        # Add a highly oscillatory component with exponentially decaying amplitude
        for i in range(self.dim):
            result += 0.3 * np.sin(10 * x[i]) * np.exp(-0.5 * np.sum((x - x[i])**2)) + \
                     0.1 * np.cos(15 * x[i]) * np.exp(-0.2 * np.sum(x**2))
            
        # Add a non-smooth component with absolute value and step-like behavior
        result += 0.1 * np.sum(np.abs(x) ** 1.7) + 0.05 * np.sum(np.floor(np.abs(x)))
        
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result