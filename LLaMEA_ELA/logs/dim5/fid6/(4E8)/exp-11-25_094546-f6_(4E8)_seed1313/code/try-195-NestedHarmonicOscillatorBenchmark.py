import numpy as np

class NestedHarmonicOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested harmonic oscillators with varying frequencies and amplitudes
        nested_harmonics = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale harmonic components with nested structure
            freq = 2.5 * (i + 1) * np.pi
            amp = 1.0 / (1.0 + 0.15 * i)
            nested_harmonics += amp * np.sin(freq * xi) * np.cos(freq * xi * 0.6)
        
        # Dynamic phase shift modulation based on dimension index
        phase_shift = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive phase shifts with dimension-dependent coefficients
            phase_coeff = 0.6 + 0.25 * np.sin(0.8 * i)
            phase_shift += phase_coeff * np.sin(3.5 * xi + 0.25 * i) * np.cos(2.5 * xi)
        
        # Adaptive ridge structure with dimensionally varying curvature
        ridges = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Ridge components with varying widths and heights
            ridge_width = 0.35 + 0.15 * np.cos(0.6 * i)
            ridge_height = 1.8 + 0.4 * np.sin(0.5 * i)
            ridges += ridge_height * np.exp(-0.5 * ((xi - 0.15 * i) / ridge_width)**2)
        
        # Cross-dimensional coupling with nested interaction patterns
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                xi, xj = x_norm[i], x_norm[j]
                # Nested coupling with dimensionally modulated strength
                coupling_strength = 0.9 + 0.15 * np.sin(0.35 * (i + j))
                cross_coupling += coupling_strength * np.sin(6.0 * (xi + xj)) * np.exp(-0.12 * (xi**2 + xj**2))
        
        # Time-varying modulation with dynamic scaling factors
        time_factor = 1.1 + 0.25 * np.sin(0.12 * self.dim)
        scaling = 0.6 + 0.4 * np.cos(0.22 * self.dim)
        
        # Combine all components with dynamic weighting
        total = (time_factor * 
                (0.35 * nested_harmonics + 
                 0.35 * phase_shift + 
                 0.25 * ridges + 
                 0.05 * cross_coupling) + 
                scaling * np.sin(2.2 * np.sum(x_norm)))
        
        return total