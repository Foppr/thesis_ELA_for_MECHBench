import numpy as np

class ChaoticTemporalBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced dynamic parameters based on dimensionality
        self.num_wells = max(3, dim // 3)
        self.phase_shifts = np.linspace(0, 4*np.pi, min(15, dim + 3))
        self.time_factors = np.logspace(0, 3, min(8, dim))
        self.fractal_dims = np.linspace(0.3, 2.5, min(10, dim))
        self.coupling_strengths = np.random.uniform(0.5, 2.0, min(12, dim))
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced fractal-like basin structure with varying dimensions
        basin_term = 0.0
        for i in range(self.dim):
            fractal_dim = self.fractal_dims[i % len(self.fractal_dims)]
            basin_val = (x_norm[i] ** 2) ** fractal_dim
            basin_term += basin_val
            
        # Enhanced multi-well potential with dynamic phase transitions
        well_term = 0.0
        for i in range(self.num_wells):
            well_center = np.sin(i * np.pi / self.num_wells) * np.cos(i * np.pi / (self.num_wells + 1))
            well_val = (x_norm - well_center) ** 6
            well_term += np.sum(well_val)
            
        # Enhanced temporal coupling with time-varying factors
        temporal_term = 0.0
        for i in range(self.dim):
            time_factor = self.time_factors[i % len(self.time_factors)]
            phase_shift = self.phase_shifts[i % len(self.phase_shifts)]
            temporal_val = time_factor * np.sin(x_norm[i] + phase_shift) * np.cos(x_norm[i] + phase_shift) * np.tan(x_norm[i])
            temporal_term += temporal_val
            
        # Enhanced cross-dimension coupling with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, min(self.dim, i + 5)):
                coupling_strength = self.coupling_strengths[i % len(self.coupling_strengths)]
                coupling = coupling_strength * np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.15 * (x_norm[i] - x_norm[j])**2) * np.log(1 + abs(x_norm[i] * x_norm[j]))
                cross_term += coupling
                
        # Enhanced dynamic scaling with dimensionality
        scale_factor = 1.0 + 0.15 * self.dim
        
        # Combine all terms with enhanced weighting
        result = scale_factor * (0.8 * basin_term + 0.6 * well_term + 0.4 * temporal_term + 0.5 * cross_term)
        
        # Add enhanced chaotic noise with dynamic amplitude
        noise_amplitude = 0.03 * (1.0 + 0.03 * self.dim)
        noise = noise_amplitude * np.random.randn() * np.sin(self.dim)
        
        return result + noise