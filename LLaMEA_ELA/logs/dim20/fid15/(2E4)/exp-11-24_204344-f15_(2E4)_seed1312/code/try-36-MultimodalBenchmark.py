import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial term with mixed degrees
        poly = np.sum(x**4) / self.dim + 0.5 * np.sum(x**2) / self.dim
        
        # Trigonometric component with varying frequencies and amplitudes
        trig = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i)
            amp = 1.0 + 0.3 * np.cos(i)
            trig += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis function with adaptive scaling
        rbf = 0.0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * (x[i] - 1.0)**2) + np.exp(-0.3 * (x[i] + 1.0)**2)
        
        # Cross-dimensional coupling with asymmetric interactions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] - x[j]))
        
        # Asymmetric distortion with different scaling per dimension
        asym = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                asym += 0.1 * x[i]**3 + 0.05 * x[i]**2
            else:
                asym += 0.2 * x[i]**3 - 0.1 * x[i]**2
        
        # Multi-scale sinusoidal modulation with phase shifts
        mod = 0.0
        for i in range(self.dim):
            mod += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive noise component with dimension-dependent strength
        noise = 0.0
        for i in range(self.dim):
            noise += 0.01 * (i + 1) * np.sin(10 * x[i])
        
        return poly + trig + rbf + cross + asym + mod + noise