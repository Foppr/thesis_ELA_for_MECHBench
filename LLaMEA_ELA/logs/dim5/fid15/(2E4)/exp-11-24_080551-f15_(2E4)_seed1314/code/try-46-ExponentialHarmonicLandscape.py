import numpy as np

class ExponentialHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base exponential decay term
        r = np.sqrt(np.sum(x**2))
        result = np.exp(-r**2 / 10.0) * (1.0 + 0.5 * r**2)
        
        # Harmonic oscillations with adaptive frequencies
        for i in range(self.dim):
            freq = 2.0 + 0.5 * (i + 1)
            result += 1.5 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
            
        # Cross-dimensional harmonic couplings with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 * (1.0 + np.sin(0.5 * (i + j)))
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Adaptive dimensional scaling with exponential weights
        for i in range(self.dim):
            weight = np.exp(-i / (self.dim + 1.0))
            result += 0.8 * weight * (np.sin(3.0 * x[i])**2 + np.cos(2.0 * x[i])**2)
            
        # Non-smooth landscape features using absolute value potentials
        for i in range(self.dim):
            result += 0.5 * np.abs(x[i])**1.5
            
        # Multi-scale periodic components with different periods
        for i in range(self.dim):
            result += 0.3 * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-abs(x[i]) / 3.0)
            
        # Central repulsion with adaptive strength
        result += 1.2 * np.exp(-r**2 / 5.0) * np.sin(r * 2.0)
        
        # Asymmetric polynomial barriers
        for i in range(self.dim):
            if x[i] < 0:
                result += 0.4 * x[i]**3 * np.exp(x[i])
            else:
                result += 0.6 * x[i]**5 * np.exp(-x[i])
                
        return result