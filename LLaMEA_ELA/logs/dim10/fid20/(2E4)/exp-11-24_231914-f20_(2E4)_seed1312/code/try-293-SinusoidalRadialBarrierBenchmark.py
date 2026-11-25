import numpy as np

class SinusoidalRadialBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        # Radial basis functions with random centers and variances
        self.rb_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rb_variances = np.random.uniform(0.1, 2.0, size=15)
        # Asymmetric barrier potentials with configurable steepness and position
        self.barrier_positions = np.random.uniform(-4.8, 4.8, size=dim)
        self.barrier_steepness = np.random.uniform(2.0, 10.0, size=dim)
        self.barrier_asymmetry = np.random.uniform(0.5, 3.0, size=dim)
        # Cross-dimensional interaction terms
        self.interaction_strength = np.random.uniform(0.1, 2.0, size=(dim, dim))
        # Additional noise parameters for added complexity
        self.noise_amp = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_freq = np.random.uniform(0.5, 4.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i])
            
        # Radial basis function component
        rb_component = 0.0
        for i in range(15):
            diff = x - self.rb_centers[i]
            rb_val = np.exp(-np.sum(diff**2) / (2 * self.rb_variances[i]**2))
            rb_component += rb_val
            
        # Asymmetric barrier potentials
        barrier_component = 0.0
        for i in range(self.dim):
            dist = x[i] - self.barrier_positions[i]
            if dist < 0:
                barrier_val = self.barrier_steepness[i] * (dist**2) * self.barrier_asymmetry[i]
            else:
                barrier_val = self.barrier_steepness[i] * (dist**2)
            barrier_component += barrier_val
            
        # Cross-dimensional interactions
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_strength[i, j] * x[i] * x[j]
                    
        # Noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += self.noise_amp[i] * np.sin(self.noise_freq[i] * x[i])
            
        # Combine all components with appropriate weights
        return (1.2 * sin_component + 
                1.0 * rb_component + 
                0.8 * barrier_component + 
                0.6 * interaction_component + 
                0.4 * noise_component)