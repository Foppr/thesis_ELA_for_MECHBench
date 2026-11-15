import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay radial component with trigonometric modulation
        r = np.sqrt(np.sum(x_normalized**2))
        radial = np.exp(-r**2 * 0.5) * (1.0 + 0.3 * np.sin(15 * r) * np.cos(10 * r))
        
        # Trigonometric wave interference pattern
        wave_interference = 0.0
        for i in range(self.dim):
            wave_interference += np.sin(20 * x_normalized[i]) * np.cos(15 * x_normalized[i])
        
        # Adaptive conditioning based on gradient magnitude
        grad_magnitude = np.sum(np.abs(x_normalized))
        conditioning = 0.2 * grad_magnitude * (1.0 + 0.1 * r)
        
        # Exponential decay interaction terms with multiple peaks
        interactions = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                interactions += np.exp(-dist * 5.0) * np.sin(10 * dist)
        
        # Rugged landscape with multiple local minima
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += 0.1 * np.sin(50 * x_normalized[i]) * np.cos(25 * x_normalized[i])
        
        # Global optimum at origin with enhanced local optima distribution
        return radial + 0.3 * wave_interference + 0.1 * conditioning + 0.05 * interactions + 0.1 * ruggedness + 1.0