import numpy as np

class SinusoidalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic function with global minimum at origin
        result = 0.2 * np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 1.8 + 0.5 * np.sin(i * 0.9)
            freq2 = 3.5 + 0.7 * np.cos(i * 0.5)
            result += 0.7 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * \
                     np.exp(-0.25 * np.abs(x[i]))
            
        # Add polynomial interaction terms with high degree and cross-coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling
                result += 0.3 * (x[i]**5) * (x[j]**3) * np.sin(x[i] + x[j]) + \
                         0.25 * x[i]**4 * x[j]**5 * np.cos(x[i] - x[j])
                
        # Add a complex gradient structure using a modified logistic map
        for i in range(self.dim):
            logistic_val = 3.8 * x[i] * (1.0 - x[i])
            result += 0.4 * np.sin(logistic_val * 16) * np.cos(x[i]**2)
            
        # Add a highly oscillatory component with exponentially decaying amplitude
        for i in range(self.dim):
            result += 0.45 * np.sin(16 * x[i]) * np.exp(-0.35 * np.sum((x - x[i])**2)) + \
                     0.25 * np.cos(21 * x[i]) * np.exp(-0.3 * np.sum(x**2))
            
        # Add a non-smooth component with absolute value and step-like behavior
        result += 0.18 * np.sum(np.abs(x) ** 1.6) + 0.1 * np.sum(np.floor(np.abs(x)) * np.sin(x))
        
        # Add cross-dimensional coupling with sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.12 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                         np.exp(-0.04 * (x[i]**2 + x[j]**2))
        
        # Add a new component with fractional powers and enhanced coupling
        for i in range(self.dim):
            result += 0.2 * np.abs(x[i])**1.8 * np.sin(6 * x[i]) + \
                     0.15 * (x[i]**3) * np.cos(4 * x[i])
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result