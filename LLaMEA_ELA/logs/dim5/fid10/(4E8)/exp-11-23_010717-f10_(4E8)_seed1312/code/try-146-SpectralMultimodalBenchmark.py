import numpy as np

class SpectralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive frequency spectral component with dynamic modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i) + 0.8 * np.cos(0.4 * i**2)
            spectral_term += (1.2 * np.sin(freq * x[i]) * np.cos(1.5 * freq * x[i]) + 
                            0.8 * np.cos(freq * x[i])**2 * np.sin(2.0 * freq * x[i]))
        
        # Dynamic phase coupling with hierarchical structure
        phase_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hierarchical phase interaction with adaptive coupling strength
                coupling_strength = 0.5 + 0.3 * np.sin(0.2 * (i + j)) * np.cos(0.1 * i * j)
                phase_coupling += coupling_strength * np.sin(x[i] + x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Hierarchical basin structures with nested minima
        basin_terms = 0.0
        for i in range(self.dim):
            # Multiple basin scales with varying depths
            basin_terms += (0.7 * np.sin(3.0 * x[i])**3 * np.cos(4.0 * x[i]) + 
                           0.5 * np.cos(5.0 * x[i])**2 * np.sin(2.0 * x[i]) + 
                           0.3 * np.sin(7.0 * x[i]) * np.cos(3.0 * x[i]))
        
        # Adaptive frequency modulation with fractal characteristics
        modulated_freq = 0.0
        for i in range(self.dim):
            # Fractal-like modulation of frequencies
            mod_freq = 1.0 + 0.4 * np.sin(0.5 * i) * np.cos(0.3 * i**2)
            modulated_freq += (0.6 * np.sin(mod_freq * x[i]) + 
                             0.4 * np.cos(mod_freq * x[i])**2 + 
                             0.2 * np.sin(mod_freq * x[i])**3)
        
        # Cross-dimensional interference patterns
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += (0.3 * np.sin(2.0 * (x[i] + x[j])) * 
                               np.cos(1.5 * (x[i]**2 - x[j]**2)) * 
                               np.exp(-0.1 * (x[i]**2 + x[j]**2)))
        
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_component += (1.5 * np.sin(3.0 * x[i]) * np.cos(4.0 * x[i]) + 
                                1.0 * np.cos(6.0 * x[i])**2 * np.sin(2.0 * x[i]) + 
                                0.8 * np.sin(9.0 * x[i]) * np.cos(3.0 * x[i]))
        
        # Adaptive curvature with spectral scaling
        curvature = 0.0
        for i in range(self.dim):
            # Spectral-based curvature variation
            curv_factor = 1.0 + 0.6 * np.sin(0.2 * i) * np.cos(0.1 * i**2)
            curvature += curv_factor * x[i]**3 * (1.0 + 0.2 * np.cos(3.0 * x[i]))
        
        # Global scaling with spectral dimension characteristics
        scale = 1.0 + 0.3 * np.sum(np.sin(x)**2) + 0.2 * np.sum(np.cos(x)**3)
        
        # Penalty for being far from origin to encourage convergence
        r = np.sqrt(np.sum(x**2))
        penalty = 0.1 * r**4
        
        return scale * (spectral_term + phase_coupling + basin_terms + modulated_freq + interference + harmonic_component + curvature) + penalty