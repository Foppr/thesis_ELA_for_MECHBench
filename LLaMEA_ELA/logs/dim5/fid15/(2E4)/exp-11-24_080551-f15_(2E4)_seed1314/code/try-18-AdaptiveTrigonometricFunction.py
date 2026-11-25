import numpy as np

class AdaptiveTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with adaptive scaling
        result = np.sum(x**4) / 4.0
        
        # Trigonometric coupling terms with adaptive frequencies
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1.0 / (i + 1))
            
        # Cross-dimensional interaction with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + (i + j) * 0.15)
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] - x[j])
                
        # Additional nonlinear cross-dimensional terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i]**2 + x[j]**2) * (1.0 / (1.0 + abs(i-j)))
                
        # Adaptive penalty term based on distance from origin
        dist = np.sqrt(np.sum(x**2))
        result += 0.5 * dist * np.exp(-dist / 3.0)
        
        return result