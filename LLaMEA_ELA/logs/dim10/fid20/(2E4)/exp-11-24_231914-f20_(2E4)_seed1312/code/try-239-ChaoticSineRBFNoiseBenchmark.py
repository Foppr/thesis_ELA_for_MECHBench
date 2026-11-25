import numpy as np

class ChaoticSineRBFNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine map parameters
        self.sine_r = np.random.uniform(0.5, 2.0, size=dim)
        self.sine_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(10, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=10)
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_frequency = np.random.uniform(1.0, 5.0, size=dim)
        # Multi-scale periodic components
        self.periodic_freq = np.random.uniform(0.5, 4.0, size=dim)
        self.periodic_amp = np.random.uniform(0.5, 2.0, size=dim)
        # Attractors with varying basins
        self.attractor_centers = np.random.uniform(-4.0, 4.0, size=(6, dim))
        self.attractor_strengths = np.random.uniform(1.0, 5.0, size=6)
        # Dynamic scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine map component
        sine_component = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence
            sine_val = self.sine_x0[i]
            for _ in range(15):  # Iterate to stabilize
                sine_val = np.sin(self.sine_r[i] * sine_val)
            sine_component += sine_val
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            dist = np.linalg.norm(x - self.rbf_centers[i])
            rbf_val = self.rbf_weights[i] * np.exp(-0.5 * (dist / self.rbf_widths[i])**2)
            rbf_component += rbf_val
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Multi-scale periodic component
        periodic_component = 0.0
        for i in range(self.dim):
            periodic_val = self.periodic_amp[i] * np.cos(self.periodic_freq[i] * x[i])
            periodic_component += periodic_val
            
        # Attractor-based component
        attractor_component = 0.0
        for i in range(6):
            dist = np.linalg.norm(x - self.attractor_centers[i])
            attractor_val = self.attractor_strengths[i] / (1.0 + dist)
            attractor_component += attractor_val
            
        # Combined fitness function with balanced weights
        return (1.2 * sine_component + 
                1.0 * rbf_component + 
                0.8 * noise_component + 
                1.1 * periodic_component + 
                0.9 * attractor_component)