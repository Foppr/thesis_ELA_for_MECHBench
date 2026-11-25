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
            freq1 = 2.0 + 1.2 * np.sin(i * 0.7)
            freq2 = 3.5 + 0.6 * np.cos(i * 0.5)
            result += 0.9 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * \
                     np.exp(-0.2 * np.abs(x[i]))
            
        # Add polynomial interaction terms with high degree and cross-coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                result += 0.4 * (x[i]**5) * (x[j]**5) * np.sin(x[i] + x[j]) + \
                         0.3 * x[i]**4 * x[j]**6 * np.cos(x[i] - x[j])
                
        # Add a complex gradient structure using a modified logistic map
        for i in range(self.dim):
            logistic_val = 3.9 * x[i] * (1.0 - x[i])
            result += 0.5 * np.sin(logistic_val * 15) * np.cos(x[i]**2)
            
        # Add a highly oscillatory component with exponentially decaying amplitude
        for i in range(self.dim):
            result += 0.6 * np.sin(15 * x[i]) * np.exp(-0.25 * np.sum((x - x[i])**2)) + \
                     0.3 * np.cos(20 * x[i]) * np.exp(-0.35 * np.sum(x**2))
            
        # Add a non-smooth component with absolute value and step-like behavior
        result += 0.25 * np.sum(np.abs(x) ** 1.7) + 0.15 * np.sum(np.floor(np.abs(x)) * np.sin(x))
        
        # Add cross-dimensional coupling with sine and cosine interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * \
                         np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Add a new component with fractional powers and enhanced coupling
        for i in range(self.dim):
            result += 0.25 * np.abs(x[i])**1.9 * np.sin(5 * x[i]) + \
                     0.2 * (x[i]**2) * np.cos(5 * x[i])
        
        # Add a new enhanced multimodal component with additional sinusoidal and exponential terms
        for i in range(self.dim):
            result += 0.35 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.12 * np.abs(x[i])) + \
                     0.25 * np.sin(6 * x[i]**2) * np.cos(4 * x[i]**3)
        
        # Add a new high-dimensional coupling component
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if j < i + 3:  # Local coupling
                    result += 0.18 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * \
                             np.exp(-0.015 * (x[i]**2 + x[j]**2))
        
        # Add a new chaotic component with multiple sine terms
        for i in range(self.dim):
            result += 0.3 * np.sin(9 * x[i]) * np.cos(8 * x[i]) * np.sin(7 * x[i]) * \
                     np.exp(-0.15 * np.abs(x[i]))
        
        # Add noise to prevent trivial solutions
        result += 0.015 * np.random.random()
        
        return result