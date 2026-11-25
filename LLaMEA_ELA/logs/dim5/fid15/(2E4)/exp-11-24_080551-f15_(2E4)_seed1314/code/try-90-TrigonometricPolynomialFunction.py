import numpy as np

class TrigonometricPolynomialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base trigonometric polynomial components
        result = 0.0
        for i in range(self.dim):
            result += np.sin(x[i])**2 + np.cos(x[i])**2
            
        # Polynomial chaos expansion with varying degrees
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(1, 5):
                poly_term += (x[i]**j) * np.sin(j * x[i])
            result += 0.3 * poly_term
            
        # Multi-scale periodic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.25 * interaction * (1.0 / (1.0 + 0.1 * abs(x[i] - x[j])))
                
        # Adaptive coupling with dynamic weights
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(i * 0.8)
            result += weight * np.sin(x[i]**3) * np.cos(x[i])
            
        # High-frequency oscillatory components
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(i * 0.3)
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Multi-modal basin structure with varying depths
        for i in range(self.dim):
            basin = (x[i]**2 - 4.0)**2 + 0.5 * (x[i]**3 - x[i])**2
            result += 0.15 * basin * np.exp(-abs(x[i]) * 0.2)
            
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2)
                result += 0.2 * coupling * np.exp(-0.5 * (x[i] - x[j])**2)
                
        # Nonlinear transformation with sigmoidal behavior
        for i in range(self.dim):
            sig = 1.0 / (1.0 + np.exp(-x[i]))
            result += 0.3 * sig * (1.0 - sig) * np.sin(2.0 * x[i])
            
        # Dynamic penalty with polynomial scaling
        penalty = 0.0
        for i in range(self.dim):
            penalty += (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2)
        result += 0.1 * penalty * np.exp(-np.sum(x**2) / 20.0)
        
        # Asymmetric harmonic components
        for i in range(self.dim):
            asym = (x[i] - 1.0)**3 + 0.7 * (x[i] + 1.0)**3
            result += 0.2 * asym * np.exp(-abs(x[i]) * 0.3)
            
        # Resonance interactions with frequency modulation
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(i * 0.4)
            result += 0.25 * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.8) * (1.0 + 0.3 * np.sin(x[i]))
            
        return result