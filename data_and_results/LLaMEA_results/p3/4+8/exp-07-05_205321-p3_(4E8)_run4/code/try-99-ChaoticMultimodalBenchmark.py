import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (1.0 + 0.5 * np.sin(15 * r) + 0.3 * np.cos(12 * r))
        
        # Angular component with non-separable interactions
        angular = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angular += np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[j]) * np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Sinusoidal periodicity with varying frequencies and phases
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin((i + 1) * 2 * np.pi * x_norm[i] + 0.5 * np.sin(7 * x_norm[i])) * np.cos((i + 1) * 3 * np.pi * x_norm[i] + 0.3 * np.cos(5 * x_norm[i]))
        
        # Cross-dimensional interaction terms with chaotic behavior
        cross = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross += 0.1 * np.sin(8 * np.pi * x_norm[i] + 0.2 * x_norm[j]) * np.cos(7 * np.pi * x_norm[j] + 0.1 * x_norm[i])
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.2 * np.sin(20 * np.pi * x_norm[i]) * np.cos(18 * np.pi * x_norm[i]) * np.sin(16 * np.pi * x_norm[i])
        
        # Combine all components
        return 0.4 * radial + 0.3 * angular + 0.2 * periodic + 0.08 * cross + 0.02 * chaotic + 1.0