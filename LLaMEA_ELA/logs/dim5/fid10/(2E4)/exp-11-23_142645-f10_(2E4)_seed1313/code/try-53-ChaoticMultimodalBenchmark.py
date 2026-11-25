import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_seq = np.sin(np.arange(dim) * np.pi / (dim + 1)) * np.exp(-np.arange(dim) * 0.1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_wave = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * (1 + 0.5 * np.sin(x)))
        
        # Polynomial interaction terms with cross-terms and variable exponents
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        
        # Chaotic modulation component using precomputed sequence
        chaotic_mod = np.sum(self.chaotic_seq * np.sin(5 * x))
        
        # Adaptive noise component that scales with dimensionality
        noise_amp = 0.1 * np.log(self.dim + 1)
        adaptive_noise = np.random.normal(0, noise_amp, self.dim)
        noise_component = np.sum(adaptive_noise * x**2)
        
        # Multi-modal potential wells with dynamic depth and position
        potential_wells = 0.0
        well_centers = np.linspace(-4, 4, min(7, self.dim // 2 + 1))
        for i in range(len(well_centers)):
            for j in range(self.dim):
                center = well_centers[i % len(well_centers)]
                potential_wells += np.exp(-0.5 * ((x[j] - center) / (0.5 + 0.1 * i))**2) * np.cos(2 * np.pi * (x[j] - center))
        
        # Combined objective with dynamic weighting
        total = 0.3 * sin_wave + 0.25 * poly_interaction + 0.2 * chaotic_mod + 0.15 * noise_component + 0.1 * potential_wells
        
        # Add boundary penalty and scaling factor
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.8, (np.abs(x) - 4.8)**3, 0.0))
        scaling_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scaling_factor * total + boundary_penalty