import numpy as np

class AsymmetricConditioningLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with varying exponents per dimension
        result = 0.0
        for i in range(self.dim):
            result += 0.1 * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i])
        
        # Trigonometric modulation with dimensionally varying frequencies
        for i in range(self.dim):
            freq = 2.0 + 0.5 * i  # Increasing frequency with dimension
            result += 2.0 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Exponential decay with asymmetric scaling per dimension
        for i in range(self.dim):
            scale = 1.0 + 0.3 * i  # Increasing scale with dimension
            result += 1.5 * np.exp(-scale * np.abs(x[i])) * np.sin(3 * x[i])
        
        # Cross-dimensional interaction with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.1 * (i + j)  # Varying coupling strength
                result += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric polynomial terms with different exponents for positive/negative regions
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.8 * x[i]**2.5
            else:
                result += 0.3 * np.abs(x[i])**3.2
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 1.2 * np.sin(15 * x[i]) * np.cos(7 * x[i]) * (1 + 0.3 * np.sin(0.8 * x[i]))
        
        # Noise term to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result