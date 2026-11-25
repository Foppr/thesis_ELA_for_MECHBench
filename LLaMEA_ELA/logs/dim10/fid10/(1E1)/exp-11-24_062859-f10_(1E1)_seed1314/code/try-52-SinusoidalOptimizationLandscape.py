import numpy as np

class SinusoidalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic function with global minimum at origin
        result = 0.1 * np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq1 = 2.2 + 0.9 * np.sin(i * 0.6)
            freq2 = 3.8 + 0.5 * np.cos(i * 0.4)
            result += 0.75 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * \
                     np.exp(-0.18 * np.abs(x[i]))
            
        # Add polynomial interaction terms with high degree and cross-coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                result += 0.35 * (x[i]**4) * (x[j]**4) * np.sin(x[i] + x[j]) + \
                         0.28 * x[i]**3 * x[j]**5 * np.cos(x[i] - x[j])
                
        # Add a complex gradient structure using a modified logistic map
        for i in range(self.dim):
            logistic_val = 3.9 * x[i] * (1.0 - x[i])
            result += 0.42 * np.sin(logistic_val * 13) * np.cos(x[i]**2)
            
        # Add a highly oscillatory component with exponentially decaying amplitude
        for i in range(self.dim):
            result += 0.52 * np.sin(13 * x[i]) * np.exp(-0.22 * np.sum((x - x[i])**2)) + \
                     0.27 * np.cos(19 * x[i]) * np.exp(-0.32 * np.sum(x**2))
            
        # Add a non-smooth component with absolute value and step-like behavior
        result += 0.22 * np.sum(np.abs(x) ** 1.65) + 0.11 * np.sum(np.floor(np.abs(x)) * np.sin(x))
        
        # Add cross-dimensional coupling with sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.17 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                         np.exp(-0.025 * (x[i]**2 + x[j]**2))
        
        # Add a new component with fractional powers and enhanced coupling
        for i in range(self.dim):
            result += 0.23 * np.abs(x[i])**1.85 * np.sin(4.2 * x[i]) + \
                     0.17 * (x[i]**2) * np.cos(4.2 * x[i])
        
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result