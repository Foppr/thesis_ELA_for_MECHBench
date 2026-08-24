import numpy as np

class HybridOscillatoryBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.oscillation_freq = np.linspace(1, 10, dim)
        self.basin_centers = np.random.uniform(-3, 3, (5, dim))
        self.saddle_points = np.random.uniform(-4, 4, (3, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sinusoidal oscillation component
        for i in range(self.dim):
            result += np.sin(self.oscillation_freq[i] * x[i]) * np.cos(self.oscillation_freq[i] * x[i])
            
        # Radial basin attraction
        for center in self.basin_centers:
            dist = np.sum((x - center)**2)
            result += 0.5 * np.exp(-dist / 10.0) * (dist - 1.0)**2
            
        # Saddle point repulsion
        for point in self.saddle_points:
            dist = np.sum((x - point)**2)
            result += 2.0 * np.exp(-dist / 5.0) / (dist + 1.0)
            
        # Cross-term coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i]) * np.cos(x[j]) * (x[i] - x[j])**2
                
        # Global scaling and noise
        result += 0.01 * np.sum(x**4) + 0.005 * np.sum(np.sin(10 * x))
        
        return result