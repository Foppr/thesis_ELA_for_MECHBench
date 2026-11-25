import numpy as np

class AdaptiveTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with adaptive scaling
        result = np.sum(x**6) / 6.0
        
        # Trigonometric coupling terms with adaptive frequencies
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1.0 / (i + 1)**1.5)
            
        # Cross-dimensional interaction with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + (i + j) * 0.2)
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] - x[j]) * np.exp(-abs(x[i] - x[j]))
                
        # Novel sharp ridge terms
        for i in range(self.dim):
            result += 0.3 * np.sin(5.0 * x[i])**2 * np.cos(2.0 * x[i])**2
            
        # Adaptive penalty term based on distance from origin with additional oscillation
        dist = np.sqrt(np.sum(x**2))
        result += 0.7 * dist * np.exp(-dist / 4.0) * np.sin(dist / 2.0)
        
        # Additional high-frequency cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    result += 0.2 * np.sin(10.0 * x[i] * x[j]) * (1.0 / (i + j + 1))
        
        return result