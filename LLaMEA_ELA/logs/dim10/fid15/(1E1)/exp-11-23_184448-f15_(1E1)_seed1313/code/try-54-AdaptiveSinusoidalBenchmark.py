import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with adaptive conditioning
        conditioning = np.arange(1, self.dim + 1)
        base_term = np.sum(conditioning * x**2)
        
        # Multiscale sinusoidal modulation with adaptive frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1) / self.dim
            amp = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            sinusoidal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Cross-dimension gradient modulation with polynomial coupling
        gradient_mod = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i] + x[j])**2 + (x[i] - x[j])**2
                gradient_mod += coupling * np.sin(x[i] * x[j] * 0.1) * (i + j)
        
        # Adaptive local minima with elliptical positioning
        local_min = 0.0
        for i in range(self.dim):
            center = 2.5 * np.cos(i * np.pi / (self.dim + 2))
            eccentricity = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 3))
            local_min += eccentricity * (x[i] - center)**2 * np.exp(-0.1 * (x[i] - center)**2)
        
        # Asymmetric barrier with exponential weighting
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(2.0 * np.abs(x[i]) - x[i]**2) * np.sin(x[i] * np.pi / 2)
        
        # Dimensionality scaling and normalization
        dim_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return dim_scale * (base_term + 0.4 * sinusoidal + 0.3 * gradient_mod + 
                           0.2 * local_min + 0.1 * barrier)