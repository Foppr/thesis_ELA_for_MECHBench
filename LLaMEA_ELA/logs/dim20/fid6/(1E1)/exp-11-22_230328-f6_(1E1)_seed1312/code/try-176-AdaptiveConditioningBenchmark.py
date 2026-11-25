import numpy as np

class AdaptiveConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.5, 2.0, dim)
        self.frequency_scalers = np.random.uniform(1.0, 3.0, dim)
        self.amplitude_scalers = np.random.uniform(0.5, 1.5, dim)
        # Create rotation matrix for directional complexity
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation for directional complexity
        x_rotated = self.rotation_matrix @ x_norm
        
        # Radial component with adaptive conditioning
        radial_distance = np.sqrt(np.sum(x_rotated**2))
        radial_term = radial_distance * np.exp(-0.5 * radial_distance**2)
        
        # Multi-frequency sinusoidal components
        sinusoidal_term = 0.0
        for i in range(self.dim):
            freq = self.frequency_scalers[i] * (1.0 + 0.3 * np.sin(i))
            amp = self.amplitude_scalers[i] * (1.0 + 0.2 * np.cos(i))
            sinusoidal_term += amp * np.sin(freq * x_rotated[i]) * np.cos(freq * x_rotated[i])
        
        # Multi-modal energy wells with varying depths
        energy_well = 0.0
        for i in range(self.dim):
            depth = 2.0 + 3.0 * np.sin(i * 0.5)
            well_term = depth * np.exp(-self.conditioning_factors[i] * (x_rotated[i] - np.sin(x_rotated[i]))**2)
            energy_well += well_term
        
        # Cross-dimension interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = (i + j) / (self.dim * (self.dim + 1))
                interaction_term += coupling_strength * np.sin(x_rotated[i] + x_rotated[j]) * \
                                  np.cos(2 * x_rotated[i] - x_rotated[j])
        
        # Periodic boundary effect
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        
        # Combined fitness function with adaptive scaling
        combined = radial_term + sinusoidal_term + energy_well + interaction_term + periodic_term
        
        # Add noise component for increased complexity
        noise = 0.01 * np.random.uniform(-1, 1) * (1.0 + 0.1 * np.sin(np.sum(x_norm)))
        
        return combined + noise