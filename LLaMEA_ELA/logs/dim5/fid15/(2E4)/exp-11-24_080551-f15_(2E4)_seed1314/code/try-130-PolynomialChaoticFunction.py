import numpy as np

class PolynomialChaoticFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion with mixed terms
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * x[i]**2 + 0.3 * x[i]**3 + 0.1 * x[i]**4
            
        # Radial basis functions with varying centers and widths
        centers = np.linspace(-3, 3, self.dim)
        widths = 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.8)
        for i in range(self.dim):
            result += 2.0 * np.exp(-np.sum((x - centers[i])**2) / (2.0 * widths[i]**2))
            
        # Asymmetric harmonic potentials
        for i in range(self.dim):
            asym_pot = 1.5 * (x[i] - 1.0)**2 + 0.8 * (x[i] + 1.0)**3
            result += 0.7 * asym_pot * np.exp(-0.5 * x[i]**2)
            
        # Cross-dimensional coupling with polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i] * x[j])**2 + 0.3 * np.sin(x[i] * x[j])
                result += 0.4 * coupling * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Multi-scale oscillatory terms
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.6)
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * (1.0 + 0.2 * np.cos(x[i]))
            
        # Chaotic sine coupling with varying frequencies
        for i in range(self.dim):
            freq1 = 4.0 + 2.0 * np.sin(i * 0.5)
            freq2 = 3.0 + 1.0 * np.cos(i * 0.7)
            result += 0.2 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.3 * abs(x[i]))
            
        # Penalty term with exponential decay
        dist = np.sqrt(np.sum(x**2))
        penalty = 1.5 * dist * np.exp(-dist / 5.0)
        result += penalty
        
        # Central attraction with asymmetric strength
        center_dist = np.sqrt(np.sum(x**2))
        result -= 0.8 * np.exp(-center_dist**2 / 2.0) * (1.0 + 0.3 * np.sin(center_dist))
        
        # Multi-modal structure with controlled complexity
        for i in range(self.dim):
            result += 0.5 * np.sin(x[i] * 4.0) * np.cos(x[i] * 2.0) * np.exp(-0.2 * x[i]**2)
            
        return result