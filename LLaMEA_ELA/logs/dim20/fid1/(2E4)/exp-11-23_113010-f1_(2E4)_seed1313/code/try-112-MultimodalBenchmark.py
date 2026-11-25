import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-like interference pattern with complex amplitude modulation
        quantum_pattern = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                phase = 2 * np.pi * distance * (i + j + 1)
                amplitude = np.exp(-distance**2) * np.sin(phase) * np.cos(phase)
                quantum_pattern += amplitude
        
        # Radial basis function with adaptive center placement and varying widths
        rbf_sum = 0.0
        num_centers = min(10, self.dim)
        for k in range(num_centers):
            center = np.sin(k * np.pi / (num_centers + 1)) * 0.8
            width = 0.5 + 0.3 * np.cos(k * np.pi / (num_centers + 1))
            rbf_sum += np.exp(-width * (x_norm - center)**2)
        
        # Time-varying sinusoidal modulation with dimension-dependent frequency
        time_mod = 0.0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(i * np.pi / (self.dim + 1))
            time_mod += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Multi-scale oscillatory components with exponentially decaying amplitudes
        oscillatory = 0.0
        for i in range(self.dim):
            for scale in [1, 2, 3]:
                freq = scale * 5 * (i + 1)
                amplitude = np.exp(-scale * 0.5)
                oscillatory += amplitude * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric potential wells with varying depth and width
        potential_wells = 0.0
        for i in range(self.dim):
            well_depth = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            well_width = 0.3 + 0.2 * np.cos(i * np.pi / (self.dim + 1))
            potential_wells += well_depth * np.exp(-0.5 * ((x_norm[i] - 0.2)**2 / well_width**2 + (x_norm[i] + 0.3)**2 / (well_width*0.7)**2))
        
        # Adaptive noise with dynamic frequency and amplitude based on dimension
        noise_amplitude = 0.05 * np.log(self.dim + 2)
        noise_frequency = 100 * np.sqrt(self.dim + 1)
        noise = noise_amplitude * np.sin(noise_frequency * np.sum(x_norm**3))
        
        # Combined weighted sum with dynamic scaling factor
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (1.5 * quantum_pattern + 1.2 * rbf_sum + 0.8 * time_mod + 0.6 * oscillatory + 0.4 * potential_wells + noise)