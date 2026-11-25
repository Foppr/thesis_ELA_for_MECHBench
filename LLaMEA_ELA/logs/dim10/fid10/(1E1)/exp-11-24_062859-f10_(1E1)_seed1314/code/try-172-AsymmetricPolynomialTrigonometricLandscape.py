import numpy as np

class AsymmetricPolynomialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying exponents
        result = 0.01 * np.sum(x**4)
        
        # Asymmetric polynomial terms with different exponents per dimension
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * x[i]**3 + 0.2 * x[i]**5
            else:
                result += 0.3 * x[i]**4 - 0.1 * x[i]**6
        
        # Trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 1.5 * np.sin(2 * x[i]) * np.cos(3 * x[i]) + 0.8 * np.sin(5 * x[i])
        
        # Logarithmic interaction terms with cross-dimensional coupling
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.3 * np.log(np.abs(x[i]) + 1) * np.sin(x[i]**2)
        
        # Cross-dimensional interactions with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.5 * (i + 1) / (j + 1)  # Varying coupling strength
                result += coupling * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # High-frequency oscillatory components with amplitude modulation
        for i in range(self.dim):
            result += 2.0 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * (1 + 0.3 * np.sin(0.5 * x[i]))
        
        # Asymmetric conditioning with different weights per dimension
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.8 * x[i]**2 * np.exp(-0.05 * x[i]**2)
            else:
                result += 1.2 * x[i]**2 * np.exp(-0.03 * x[i]**2)
        
        # Add small random noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result