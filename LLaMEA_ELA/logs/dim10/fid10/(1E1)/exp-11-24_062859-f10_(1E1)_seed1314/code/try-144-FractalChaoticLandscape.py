import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with highly conditioned eigenvalues
        result = 0.01 * np.sum(x**2)
        
        # Fractal-like exponential decay with trigonometric modulation
        for i in range(self.dim):
            result += 3.0 * np.exp(-0.5 * x[i]**2) * np.sin(8 * x[i])**3
        
        # Chaotic multi-scale wave interference with fractal coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended interaction range
                dist = np.abs(x[i] - x[j])
                result += 2.0 * np.exp(-dist**1.5) * np.sin(7 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Asymmetric polynomial field with chaotic exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**3.7 * np.exp(-0.15 * x[i])  # Increased exponent and coefficient
            else:
                result += 0.2 * x[i]**6.3 * np.exp(-0.25 * np.abs(x[i]))  # Higher degree and modified decay
        
        # Deterministic chaos component with fractional Brownian motion characteristics
        for i in range(self.dim):
            result += 2.5 * np.sin(19 * x[i]) * np.cos(9 * x[i]) * (1 + 0.6 * np.sin(0.8 * x[i])) * np.exp(-0.3 * x[i]**2)
        
        # Stronger cross-dimensional coupling with power-law decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 1.0 * np.exp(-0.7 * (np.abs(x[i] - x[j])**1.3)) * np.sin(3.2 * x[i]) * np.cos(4.8 * x[j])
        
        # Fractional power and logarithmic interaction with fractal scaling
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.6 * np.abs(x[i])**1.9 * np.log(np.abs(x[i]) + 1) * np.sin(2.5 * np.log(np.abs(x[i]) + 1))
        
        # Add chaotic noise component
        noise = 0.02 * np.random.random()
        for i in range(self.dim):
            noise += 0.005 * np.sin(13 * x[i])
        result += noise
        
        return result