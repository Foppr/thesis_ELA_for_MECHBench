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
            freq = 2.0 * (i + 1) * np.pi
            amp = 1.0 / (1.0 + 0.1 * i)
            nested_harmonics += amp * np.sin(freq * xi) * np.cos(freq * xi * 0.5)
        
        # Dynamic phase shift modulation based on dimension index
        phase_shift = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive phase shifts with dimension-dependent coefficients
            phase_coeff = 0.5 + 0.3 * np.sin(0.7 * i)
            phase_shift += phase_coeff * np.sin(3.0 * xi + 0.2 * i) * np.cos(2.0 * xi)
        
        # Adaptive ridge structure with dimensionally varying curvature
        ridges = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Ridge components with varying widths and heights
            ridge_width = 0.3 + 0.2 * np.cos(0.5 * i)
            ridge_height = 1.5 + 0.5 * np.sin(0.4 * i)
            ridges += ridge_height * np.exp(-0.5 * ((xi - 0.1 * i) / ridge_width)**2)
        
        # Cross-dimensional coupling with nested interaction patterns
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                xi, xj = x_norm[i], x_norm[j]
                # Nested coupling with dimensionally modulated strength
                coupling_strength = 0.8 + 0.2 * np.sin(0.3 * (i + j))
                cross_coupling += coupling_strength * np.sin(5.0 * (xi + xj)) * np.exp(-0.1 * (xi**2 + xj**2))
        
        # Time-varying modulation with dynamic scaling factors
        time_factor = 1.0 + 0.3 * np.sin(0.1 * self.dim)
        scaling = 0.5 + 0.5 * np.cos(0.2 * self.dim)
        
        # Combine all components with dynamic weighting
        total = (time_factor * 
                (0.4 * nested_harmonics + 
                 0.3 * phase_shift + 
                 0.2 * ridges + 
                 0.1 * cross_coupling) + 
                scaling * np.sin(2.0 * np.sum(x_norm)))
        
        return total