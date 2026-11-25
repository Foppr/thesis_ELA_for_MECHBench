import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(5 * x) * np.cos(3 * x) * np.exp(-0.1 * x**2))
        
        # Polynomial penalty terms with multiple local minima
        polynomial = np.sum((x**4 - 6 * x**2 + 8)**2)
        
        # Radial symmetry component with nested optima
        r = np.sqrt(np.sum(x**2))
        radial = np.sin(10 * r) * np.exp(-0.05 * r**2) + 0.5 * np.cos(5 * r)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] * x[j])
                
        # Additional sharp gradient regions near boundaries
        boundary_penalty = 0
        for i in range(self.dim):
            if abs(x[i]) > 4:
                boundary_penalty += 10 * (abs(x[i]) - 4)**3
                
        return 0.8 * (sinusoidal + polynomial + radial + cross_coupling) + boundary_penalty