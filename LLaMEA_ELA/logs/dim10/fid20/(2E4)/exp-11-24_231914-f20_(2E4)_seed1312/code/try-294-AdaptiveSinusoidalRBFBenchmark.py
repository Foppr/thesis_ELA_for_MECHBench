import numpy as np

class AdaptiveSinusoidalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Radial Basis Functions with random centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=15)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 4.0, size=dim)
        self.noise_decay = np.random.uniform(0.1, 0.8, size=dim)
        
        # Condition number variation
        self.condition_factors = np.random.uniform(0.1, 10.0, size=dim)
        
        # Cross-dimensional interactions
        self.interaction_strength = np.random.uniform(0.1, 2.0, size=(dim, dim))
        
        # Global scaling and offset
        self.global_scale = np.random.uniform(0.5, 2.0)
        self.offset = np.random.uniform(-1.0, 1.0)
        
    def f(self, x):
        # Ensure input is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
        
        # Radial Basis Function component
        rbf_component = 0.0
        for i in range(15):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_component += self.rbf_weights[i] * np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
        
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val * np.exp(-self.noise_decay[i] * np.abs(x[i]))
        
        # Condition number effect
        condition_component = 0.0
        for i in range(self.dim):
            condition_component += self.condition_factors[i] * x[i]**2
        
        # Cross-dimensional interactions
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_strength[i, j] * x[i] * x[j]
        
        # Combine all components with appropriate weights
        total = (1.5 * sin_component + 
                 2.0 * rbf_component + 
                 0.8 * noise_component + 
                 1.2 * condition_component + 
                 0.6 * interaction_component)
        
        return self.global_scale * total + self.offset