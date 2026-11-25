import numpy as np

class ChaoticTemporalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic parameters based on dimensionality
        self.num_wells = max(2, dim // 4)
        self.phase_shifts = np.linspace(0, 2*np.pi, min(12, dim + 2))
        self.time_factors = np.logspace(0, 2, min(6, dim))
        self.fractal_dims = np.linspace(0.5, 2.0, min(8, dim))
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal-like basin structure with varying dimensions
        basin_term = 0.0
        for i in range(self.dim):
            fractal_dim = self.fractal_dims[i % len(self.fractal_dims)]
            basin_val = (x_norm[i] ** 2) ** fractal_dim
            basin_term += basin_val
            
        # Multi-well potential with dynamic phase transitions
        well_term = 0.0
        for i in range(self.num_wells):
            well_center = np.sin(i * np.pi / self.num_wells)
            well_val = (x_norm - well_center) ** 4
            well_term += np.sum(well_val)
            
        # Temporal coupling with time-varying factors
        temporal_term = 0.0
        for i in range(self.dim):
            time_factor = self.time_factors[i % len(self.time_factors)]
            phase_shift = self.phase_shifts[i % len(self.phase_shifts)]
            temporal_val = time_factor * np.sin(x_norm[i] + phase_shift) * np.cos(x_norm[i] + phase_shift)
            temporal_term += temporal_val
            
        # Cross-dimension coupling with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
                cross_term += coupling
                
        # Dynamic scaling with dimensionality
        scale_factor = 1.0 + 0.1 * self.dim
        
        # Combine all terms
        result = scale_factor * (0.7 * basin_term + 0.5 * well_term + 0.3 * temporal_term + 0.4 * cross_term)
        
        # Add chaotic noise with dynamic amplitude
        noise_amplitude = 0.02 * (1.0 + 0.02 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise