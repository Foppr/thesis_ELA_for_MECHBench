import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with adaptive exponents
        poly_term = 0.8 * np.sum(x_norm**4) + 0.3 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8)
        
        # Trigonometric interference with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5)  # Exponentially increasing frequencies
            amp = 1.0 / (1.0 + 0.15 * i)  # Decreasing amplitudes
            trig_term += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial basis function component with dynamic centers
        rbf_term = 0.0
        for i in range(min(5, self.dim)):  # Limited to first 5 dimensions for efficiency
            center = 0.5 * np.sin(i * np.pi / 3.0)  # Modified dynamic centers
            sigma = 0.4 + 0.4 * np.cos(i * np.pi / 2.0)  # Adaptive widths
            rbf_term += np.exp(-((x_norm[i] - center)**2) / (2 * sigma**2))
        
        # Multi-scale chaotic modulation with adaptive coupling
        chaos_term = 0.0
        for i in range(self.dim):
            scale = 1.5 + 0.3 * np.sin(4 * np.pi * x_norm[i])  # Enhanced adaptive scaling
            freq_mod = 2.5 + 2.0 * np.cos(3 * np.pi * x_norm[i])  # Modified frequency modulation
            chaos_term += scale * np.sin(freq_mod * np.pi * x_norm[i]) * np.cos(freq_mod * np.pi * x_norm[i])
        
        # Adaptive conditioning based on dimensionality and input magnitude
        r = np.sqrt(np.sum(x_norm**2))
        cond_factor = 1.0 + 3.0 * (1.0 - np.exp(-0.3 * r)) * np.sin(3 * np.pi * r)**2
        
        # Cross-dimensional coupling with varying strength
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                coupling_strength = 0.6 + 0.2 * np.sin(3 * np.pi * (i + j))  # Different coupling
                cross_term += coupling_strength * x_norm[i] * x_norm[j]
        
        # Dimensionality-dependent weighting
        dim_weight = 1.2 + 0.15 * self.dim + 0.1 * np.sin(self.dim * np.pi / 4.0)
        
        # Combine all components with modified blending
        result = dim_weight * (0.35 * poly_term + 0.25 * trig_term + 0.18 * rbf_term + 
                              0.12 * chaos_term + 0.07 * cross_term) * cond_factor
        
        return result