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
            freq1 = 2.0 + 0.8 * np.sin(i * 0.7)
            freq2 = 3.5 + 0.4 * np.cos(i * 0.5)
            result += 0.5 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * \
                     np.exp(-0.15 * np.abs(x[i]))
            
        # Add polynomial interaction terms with high degree and cross-coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling for better balance
                result += 0.2 * (x[i]**4) * (x[j]**2) * np.sin(x[i] + x[j]) + \
                         0.15 * x[i]**3 * x[j]**4 * np.cos(x[i] - x[j])
                
        # Add a complex gradient structure using a modified logistic map
        for i in range(self.dim):
            logistic_val = 3.8 * x[i] * (1.0 - x[i])
            result += 0.3 * np.sin(logistic_val * 12) * np.cos(x[i]**2)
            
        # Add a highly oscillatory component with exponentially decaying amplitude
        for i in range(self.dim):
            result += 0.35 * np.sin(12 * x[i]) * np.exp(-0.4 * np.sum((x - x[i])**2)) + \
                     0.15 * np.cos(18 * x[i]) * np.exp(-0.3 * np.sum(x**2))
            
        # Add a non-smooth component with absolute value and step-like behavior
        result += 0.12 * np.sum(np.abs(x) ** 1.8) + 0.06 * np.sum(np.floor(np.abs(x)) * np.sin(x))
        
        # Add cross-dimensional coupling with sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                         np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result