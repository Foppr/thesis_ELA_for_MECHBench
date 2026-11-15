import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)
            amp = 1.5 + 0.8 * np.sin(i * 0.5)
            sinusoidal += amp * np.sin(freq * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Exponential decay cross-dimensional interactions
        cross_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_decay += 0.4 * np.exp(-2.0 * dist) * np.sin(25 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Adaptive penalty terms with multi-modal structure
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.6 * (x_norm[i]**8 - 4 * x_norm[i]**6 + 6 * x_norm[i]**4 - 4 * x_norm[i]**2 + 1)
        
        # Chaotic component with high-frequency oscillations
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.5 * np.sin(60 * np.pi * x_norm[i]) * np.cos(50 * np.pi * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
        
        # Multi-scale modulation with varying phase shifts
        modulation = 0.0
        for i in range(self.dim):
            phase = 0.3 * np.sin(i * 0.8) * np.cos(i * 0.6)
            modulation += 0.35 * np.sin(30 * np.pi * x_norm[i] + phase) * np.cos(25 * np.pi * x_norm[i] + phase)
        
        # Radial basis function with adaptive width
        radial = 0.0
        for i in range(self.dim):
            radial += 0.4 * np.exp(-1.5 * x_norm[i]**2) * np.sin(35 * np.pi * x_norm[i])
        
        # Cross-dimensional cubic interactions
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += 0.25 * (x_norm[i]**3 + x_norm[j]**3) * np.sin(20 * np.pi * (x_norm[i] - x_norm[j]))
        
        # High-order polynomial penalty with multiple local minima
        high_order = 0.0
        for i in range(self.dim):
            high_order += 0.7 * (x_norm[i]**10 - 5 * x_norm[i]**8 + 10 * x_norm[i]**6 - 10 * x_norm[i]**4 + 5 * x_norm[i]**2 - 1)
        
        # Basin boundary complexity with exponential repulsion
        basin_complexity = 0.0
        dist_from_origin = np.sqrt(np.sum(x_norm**2))
        basin_complexity = 2.0 * np.exp(-0.5 * dist_from_origin**2) * (1.0 + 0.5 * np.sin(10 * dist_from_origin))
        
        # Combined fitness function
        return quadratic + sinusoidal + cross_decay + penalty + chaotic + modulation + radial + cubic_interaction + high_order + basin_complexity