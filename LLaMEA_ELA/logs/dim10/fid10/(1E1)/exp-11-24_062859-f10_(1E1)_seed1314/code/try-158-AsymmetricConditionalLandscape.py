import numpy as np

class AsymmetricConditionalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric conditioning
        result = 0.01 * np.sum(x**2)
        
        # Polynomial terms with varying exponents and coefficients
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * x[i]**4 + 0.3 * x[i]**3
            else:
                result += 0.7 * x[i]**5 + 0.2 * x[i]**2
                
        # Exponential decay with trigonometric modulation
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.2 * np.abs(x[i])) * np.sin(3 * x[i])**2
            
        # Cross-dimensional coupling with exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.8 * np.exp(-dist) * np.sin(2 * x[i]) * np.cos(2 * x[j])
                
        # Asymmetric exponential terms with different decay rates
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.6 * np.exp(-0.5 * x[i]) * (1 + 0.3 * np.sin(5 * x[i]))
            else:
                result += 0.4 * np.exp(-0.8 * np.abs(x[i])) * (1 + 0.2 * np.cos(4 * x[i]))
                
        # High-frequency trigonometric interference
        for i in range(self.dim):
            result += 0.9 * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Fractional power and logarithmic terms
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.3 * np.abs(x[i])**1.8 * np.log(np.abs(x[i]) + 1)
                
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result