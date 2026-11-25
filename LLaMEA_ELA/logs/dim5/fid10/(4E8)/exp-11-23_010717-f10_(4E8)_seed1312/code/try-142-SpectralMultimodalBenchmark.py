import numpy as np

class SpectralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Frequency-domain harmonic components with varying amplitudes
        spectral_sum = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.3 * np.sin(0.4 * i)
            amp = 1.2 + 0.2 * np.cos(0.5 * i)
            spectral_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Adaptive phase-shifted coupling between dimensions
        phase_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_diff = np.sin(0.25 * (i - j)) * np.cos(0.35 * (i + j))
                phase_coupling += np.sin(x[i] + phase_diff) * np.cos(x[j] + phase_diff)
                
        # Hierarchical basin structure with nested exponential wells
        basin_terms = 0.0
        for i in range(self.dim):
            scale = 1.2 + 0.4 * np.sin(0.15 * i)
            basin_terms += scale * np.exp(-0.6 * (x[i] / (1.2 + 0.15 * i))**2) * (x[i]**2 + 0.15 * x[i]**4)
            
        # Multi-scale interference with adaptive frequency modulation
        interference = 0.0
        for i in range(self.dim):
            mod_freq = 2.5 + np.sin(0.6 * i) * 1.2
            interference += np.sin(mod_freq * x[i] + np.sin(mod_freq * x[i])) + \
                           0.8 * np.cos(mod_freq * x[i] + np.cos(mod_freq * x[i]))
            
        # Cross-dimensional polynomial coupling with varying degrees
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                degree = 3 + int((i + j) % 4)
                weight = 0.6 * (1.0 + np.sin(0.25 * (i + j)))
                poly_coupling += weight * (x[i]**degree) * (x[j]**degree)
                
        # Adaptive conditioning with dynamic scaling factors
        conditioning = 0.0
        for i in range(self.dim):
            dyn_scale = 1.1 + 0.25 * np.sin(0.6 * x[i])
            conditioning += dyn_scale * x[i]**3
            
        return spectral_sum + phase_coupling + basin_terms + interference + poly_coupling + conditioning