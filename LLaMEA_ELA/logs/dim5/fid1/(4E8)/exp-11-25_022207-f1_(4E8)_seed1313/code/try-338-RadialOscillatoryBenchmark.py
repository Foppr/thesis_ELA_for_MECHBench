import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters that adapt to dimensionality
        self.num_rings = max(4, dim // 2)
        self.oscillation_freqs = np.linspace(2.0, 12.0, min(12, dim))
        self.conditioning_factors = np.logspace(-2, 3, min(10, dim))
        self.symmetry_orders = np.arange(2, min(8, dim + 2))
        # Dynamic time-varying parameters
        self.time_factor = np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Radial component with dynamic ring structure
        radius = np.sqrt(np.sum(x_norm ** 2))
        
        # Dynamic ring structure with time-varying depths and radii
        ring_term = 0.0
        for i in range(self.num_rings):
            ring_radius = 0.3 + 1.2 * i / (self.num_rings - 1) if self.num_rings > 1 else 1.0
            ring_depth = 3.0 + 2.0 * np.sin(0.5 * i + self.time_factor)
            ring_val = ring_depth * (radius - ring_radius) ** 2
            ring_term += ring_val
            
        # Oscillatory components with time-varying frequencies and amplitudes
        osc_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i % len(self.oscillation_freqs)] * (1.0 + 0.3 * np.sin(self.time_factor + i))
            amp = 1.5 + 0.8 * np.cos(self.time_factor + i)
            osc_val = amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            osc_term += osc_val
            
        # Adaptive conditioning with chaotic variation
        cond_term = 0.0
        for i in range(self.dim):
            factor = self.conditioning_factors[i % len(self.conditioning_factors)] * (1.0 + 0.5 * np.sin(self.time_factor + i))
            cond_val = factor * (x_norm[i] ** 2)
            cond_term += cond_val
            
        # Symmetry-breaking terms with dynamic radial patterns
        sym_term = 0.0
        for i in range(self.dim):
            order = self.symmetry_orders[i % len(self.symmetry_orders)] * (1.0 + 0.4 * np.cos(self.time_factor + i))
            angle = np.arctan2(x_norm[i], x_norm[(i + 1) % self.dim])
            sym_val = np.sin(order * angle) * (x_norm[i] ** 2)
            sym_term += sym_val
            
        # Cross-dimension coupling with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = np.sin(3.0 * (x_norm[i] + x_norm[j]) + self.time_factor) * (x_norm[i] ** 2 + x_norm[j] ** 2)
                cross_term += coupling
                
        # Chaotic additional term
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_val = np.sin(5.0 * x_norm[i] + self.time_factor) * np.cos(7.0 * x_norm[i] + self.time_factor)
            chaotic_term += chaotic_val
            
        # Combine all terms with dynamic weights
        result = 0.7 * ring_term + 0.4 * osc_term + 0.5 * cond_term + 0.6 * sym_term + 0.3 * cross_term + 0.2 * chaotic_term
        
        # Add chaotic noise with amplitude that increases with dimensionality
        noise_amplitude = 0.02 * (1.0 + 0.05 * self.dim) * (1.0 + 0.3 * np.sin(self.time_factor))
        noise = noise_amplitude * np.random.randn()
        
        return result + noise