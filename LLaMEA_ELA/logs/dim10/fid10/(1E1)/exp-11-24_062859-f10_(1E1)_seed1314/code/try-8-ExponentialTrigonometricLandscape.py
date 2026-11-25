import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic function
        result = 0.5 * np.sum(x**2)
        
        # Add exponential decay terms with trigonometric modulation
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.1 * x[i]**2) * np.sin(3 * x[i]) * np.cos(2 * x[i])
            
        # Add coupled trigonometric interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.3 * coupling * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Add polynomial cross-terms with varying exponents
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                result += 0.1 * x[i]**3 * x[j]**5 * np.sin(x[i] * x[j])
                
        # Add random perturbations to increase complexity
        for i in range(self.dim):
            result += 0.2 * np.random.random() * np.exp(-0.2 * np.abs(x[i]))
            
        # Add a highly oscillatory component with varying frequency
        oscillation = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            oscillation += np.sin(freq * x[i]) * np.cos(freq * x[i])
        result += 0.4 * oscillation
            
        # Add a non-smooth component using absolute value and step functions
        result += 0.15 * np.sum(np.abs(x)**1.5) + 0.1 * np.sum(np.floor(np.abs(x)) * np.cos(x))
        
        return result