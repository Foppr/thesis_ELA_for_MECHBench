import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Modified chaotic behavior with different logistic map parameter
        self.r = 3.7  # Slightly reduced chaos level
        self.freq = 3.0 * np.pi  # Increased frequency for more oscillations
        self.scale = 12.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with modified chaotic modulation
        r = np.sqrt(np.sum(x**2))
        chaotic_factor = 1.0
        if r > 1e-10:
            # Modified chaotic scaling with different logarithmic base
            chaotic_factor = 1.0 + 0.4 * np.sin(self.r * np.log10(r + 1e-10))
        
        # Trigonometric oscillation component with altered frequencies
        trig_component = 0
        for i in range(self.dim):
            trig_component += np.sin(self.freq * x[i]) * np.cos(self.freq * x[i] * 0.3)
        
        # Modified logistic map inspired interaction terms
        logistic_interaction = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                logistic_interaction += (x[i] * x[i+1]) * (self.r * x[i] * (1 - x[i]**2))  # Squared term added
        
        # Multi-scale oscillation with varying frequencies and modified exponential decay
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(15 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Enhanced radial symmetry with different decay rate
        radial_symmetry = np.exp(-0.3 * r**2) * np.cos(self.freq * r)
        
        # Combine all components with modified weights
        return (0.2 * r**2 + 
                2.5 * trig_component + 
                0.6 * logistic_interaction + 
                0.9 * multi_scale + 
                0.3 * radial_symmetry) * chaotic_factor