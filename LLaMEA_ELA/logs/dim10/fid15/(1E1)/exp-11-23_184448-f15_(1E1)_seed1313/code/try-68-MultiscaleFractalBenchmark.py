import numpy as np

class MultiscaleFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term
        base_term = np.sum(x**2)
        
        # Recursive Gaussian peaks with fractal scaling
        fractal_peaks = 0.0
        for i in range(self.dim):
            scale = 2.0**(i % 3)  # Scale changes every 3 dimensions
            peak_height = 1.0 / (1.0 + 0.1 * i)
            peak_center = 2.0 * np.sin(i * np.pi / (self.dim + 1))
            fractal_peaks += peak_height * np.exp(-0.5 * ((x[i] - peak_center) / scale)**2)
        
        # Logarithmic barrier terms
        barriers = 0.0
        for i in range(self.dim):
            dist_from_bounds = min(abs(x[i] + 5.0), abs(x[i] - 5.0))
            if dist_from_bounds < 1.0:
                barriers -= np.log(dist_from_bounds + 1e-8)
        
        # Quaternion-inspired cross-dimension coupling
        quaternion_coupling = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                # Simulate quaternion-like interaction
                q_real = x[i]**2 + x[i+1]**2
                q_imag = x[i] * x[i+1]
                quaternion_coupling += np.sin(q_real) * np.cos(q_imag)
        
        # Multi-scale sine waves with varying amplitudes
        multi_scale_sine = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4)  # Frequencies: 1, 2, 4, 8, 1, 2, 4, 8...
            amp = 1.0 / (1.0 + 0.1 * i)
            multi_scale_sine += amp * np.sin(freq * x[i])
        
        # Dimensionality-dependent normalization
        norm_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return norm_factor * (base_term + 0.3 * fractal_peaks + 0.2 * barriers + 
                             0.4 * quaternion_coupling + 0.1 * multi_scale_sine)