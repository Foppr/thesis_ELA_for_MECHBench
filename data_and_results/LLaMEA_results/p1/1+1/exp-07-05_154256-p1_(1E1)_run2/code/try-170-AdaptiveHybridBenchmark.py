import numpy as np

class AdaptiveHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.noise_level = 0.05
        self.step_threshold = 0.5
        self.sine_freq = 2 * np.pi
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        spherical = np.sum(x**2)
        
        # Step function component
        step = np.sum(np.where(np.abs(x) > self.step_threshold, 1.0, 0.0))
        
        # Sinusoidal oscillation component
        sine = np.sum(np.sin(self.sine_freq * x) * np.cos(self.sine_freq * x * 0.3))
        
        # Adaptive noise component that scales with dimensionality
        noise = np.random.normal(0, self.noise_level * np.sqrt(self.dim))
        
        # Cross-dimensional interaction terms
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x[i]**2 + x[j]**2) * np.sin(self.sine_freq * x[i] * x[j])
        
        # Asymmetric scaling component
        asymmetry = np.sum(np.abs(x)**1.5 * np.sign(x))
        
        # Combined fitness with dynamic weights
        return (0.5 * spherical + 
                2.0 * step + 
                1.5 * sine + 
                0.3 * interaction + 
                0.8 * asymmetry + 
                noise)