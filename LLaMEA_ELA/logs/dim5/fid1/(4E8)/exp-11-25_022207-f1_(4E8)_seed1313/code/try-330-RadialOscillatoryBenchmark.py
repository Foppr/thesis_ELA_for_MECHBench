import numpy as np

class RadialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters that adapt to dimensionality
        self.num_rings = max(3, dim // 3)
        self.oscillation_freqs = np.linspace(1.0, 8.0, min(10, dim))
        self.conditioning_factors = np.logspace(-1, 2, min(8, dim))
        self.symmetry_orders = np.arange(3, min(7, dim + 3))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Radial component with concentric rings
        radius = np.sqrt(np.sum(x_norm ** 2))
        
        # Ring structure with varying depths
        ring_term = 0.0
        for i in range(self.num_rings):
            ring_radius = 0.5 + 0.8 * i / (self.num_rings - 1) if self.num_rings > 1 else 1.0
            ring_depth = 2.0 + 1.5 * np.sin(0.3 * i)
            ring_val = ring_depth * (radius - ring_radius) ** 2
            ring_term += ring_val
            
        # Oscillatory components in each dimension
        osc_term = 0.0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i % len(self.oscillation_freqs)]
            osc_val = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            osc_term += osc_val
            
        # Adaptive conditioning across dimensions
        cond_term = 0.0
        for i in range(self.dim):
            factor = self.conditioning_factors[i % len(self.conditioning_factors)]
            cond_val = factor * (x_norm[i] ** 2)
            cond_term += cond_val
            
        # Symmetry-breaking terms with radial patterns
        sym_term = 0.0
        for i in range(self.dim):
            order = self.symmetry_orders[i % len(self.symmetry_orders)]
            angle = np.arctan2(x_norm[i], x_norm[(i + 1) % self.dim])
            sym_val = np.sin(order * angle) * (x_norm[i] ** 2)
            sym_term += sym_val
            
        # Cross-dimension coupling with periodic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = np.sin(2.0 * (x_norm[i] + x_norm[j])) * (x_norm[i] ** 2 + x_norm[j] ** 2)
                cross_term += coupling
                
        # Combine all terms with dynamic weights
        result = 0.6 * ring_term + 0.3 * osc_term + 0.4 * cond_term + 0.5 * sym_term + 0.2 * cross_term
        
        # Add noise with amplitude that increases with dimensionality
        noise_amplitude = 0.01 * (1.0 + 0.03 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise