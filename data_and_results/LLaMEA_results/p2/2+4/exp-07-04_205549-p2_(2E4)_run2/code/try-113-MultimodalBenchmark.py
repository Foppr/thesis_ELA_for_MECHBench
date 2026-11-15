import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Fractional Brownian motion inspired component with varying Hurst parameter
        fbm = 0.0
        for i in range(self.dim):
            # Varying Hurst parameter for each dimension
           hurst = 0.3 + 0.4 * np.sin(i * 0.5)
            # Fractional noise component
            fbm += 0.5 * np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i]) * (1.0 + 0.3 * np.sin(5 * np.pi * x_norm[i]))
        
        # Multi-scale sinusoidal waves with dynamic frequencies
        waves = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1) + 0.5 * np.sin(i * 0.3)
            amp = 1.5 + 0.8 * np.cos(i * 0.4)
            waves += amp * np.sin(freq * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Cross-dimensional interaction with dynamic phase shifts
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimensionality
                phase_shift = 0.2 * np.sin(i * 0.3 + j * 0.4)
                cross_interaction += 0.3 * np.sin(25 * np.pi * (x_norm[i] + x_norm[j] + phase_shift)) * np.cos(20 * np.pi * (x_norm[i] - x_norm[j] + phase_shift))
        
        # Dynamic penalty landscape that changes with input magnitude
        penalty = 0.0
        for i in range(self.dim):
            # Variable penalty strength based on position
            penalty_strength = 1.0 + 0.5 * np.sin(3 * np.pi * x_norm[i])
            penalty += penalty_strength * (x_norm[i]**6 - 3 * x_norm[i]**4 + 3 * x_norm[i]**2 - 1)
        
        # Chaotic component with logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r = 3.8 + 0.2 * np.sin(i * 0.5)
            chaotic += 0.4 * np.sin(60 * np.pi * x_norm[i]) * np.cos(50 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Radial basis function component with variable centers
        radial = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.7)
            radial += 0.25 * np.exp(-5.0 * (x_norm[i] - center)**2) * np.sin(30 * np.pi * (x_norm[i] - center))
        
        # Time-varying oscillation component
        time_osc = 0.0
        t = 0.5 * np.sin(np.sum(x_norm) * 0.5)
        for i in range(self.dim):
            time_osc += 0.3 * np.sin(40 * np.pi * x_norm[i] + t) * np.cos(35 * np.pi * x_norm[i] + t)
        
        # Asymmetric penalty with local minima
        asym_penalty = 0.0
        for i in range(self.dim):
            asym_penalty += 0.35 * (x_norm[i]**8 - 4 * x_norm[i]**6 + 6 * x_norm[i]**4 - 4 * x_norm[i]**2 + 1) * np.exp(-0.4 * x_norm[i]**2)
        
        # Combined result
        return quadratic + fbm + waves + cross_interaction + penalty + chaotic + radial + time_osc + asym_penalty