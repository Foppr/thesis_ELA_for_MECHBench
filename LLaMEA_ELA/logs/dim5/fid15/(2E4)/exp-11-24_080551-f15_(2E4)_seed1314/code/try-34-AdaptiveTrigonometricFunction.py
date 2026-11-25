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
            freq = 3.5 * (i + 1)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]) * (1.0 / (i + 1)**1.5)
            
        # Cross-dimensional interaction with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + (i + j) * 0.25)
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] - x[j]) * np.exp(-abs(x[i] - x[j]))
                
        # Novel sharp ridge terms
        for i in range(self.dim):
            result += 0.35 * np.sin(5.0 * x[i])**2 * np.cos(2.0 * x[i])**2
            
        # Adaptive penalty term based on distance from origin with additional oscillation
        dist = np.sqrt(np.sum(x**2))
        result += 0.65 * dist * np.exp(-dist / 4.0) * np.sin(dist / 2.0)
        
        # Additional high-frequency cross-dimensional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    result += 0.22 * np.sin(10.0 * x[i] * x[j]) * (1.0 / (i + j + 1)**1.2)
        
        # Additional quartic cross-dimensional terms for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.09 * (x[i]**4 + x[j]**4) * np.sin(3.0 * x[i] * x[j])
                
        # Central peak term to create a more challenging landscape
        result += 0.42 * np.exp(-np.sum((x - 0.5)**2) / 1.5)
        
        return result