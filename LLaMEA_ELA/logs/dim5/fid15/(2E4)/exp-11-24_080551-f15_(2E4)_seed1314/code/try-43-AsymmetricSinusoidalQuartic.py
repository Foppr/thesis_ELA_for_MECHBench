import numpy as np

class AsymmetricSinusoidalQuartic:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Quartic potential base
        result = np.sum(x**4) / 4.0
        
        # Sinusoidal modulations with varying amplitudes and frequencies
        for i in range(self.dim):
            amplitude = 1.0 + 0.5 * np.sin(i)
            frequency = 2.0 + 0.3 * i
            result += amplitude * np.sin(frequency * x[i]) * np.cos(frequency * x[i])
            
        # Asymmetric saddle points with exponential decay
        for i in range(self.dim):
            result += 0.8 * np.exp(-abs(x[i] - 1.0)) * np.sin(3.0 * x[i])**2
            
        # Non-linear cross-dimensional couplings with power-law interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (i + 1) * (j + 1) / (self.dim**2)
                result += coupling * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j])
                
        # Additional asymmetric ridge terms
        for i in range(self.dim):
            result += 0.5 * np.sin(4.0 * x[i])**3 * np.cos(2.0 * x[i])**3
            
        # Adaptive penalty term based on deviation from asymmetric center
        center = np.array([1.0] * self.dim)
        dist = np.sum((x - center)**2)
        result += 0.7 * np.exp(-dist / 3.0) * np.sin(dist / 2.0)
        
        # High-frequency oscillatory cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if (i + j) % 3 == 0:
                    result += 0.3 * np.sin(8.0 * x[i] * x[j]) * np.cos(5.0 * x[i] - 2.0 * x[j])
                    
        # Central repulsion term to increase basin complexity
        result += 0.6 * np.exp(-np.sum(x**2) / 2.0)
        
        return result