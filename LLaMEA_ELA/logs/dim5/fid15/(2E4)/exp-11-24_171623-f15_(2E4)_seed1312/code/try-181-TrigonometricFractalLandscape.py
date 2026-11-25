import numpy as np

class TrigonometricFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Create fractal-based frequency patterns for trigonometric components
        self.freq_patterns = np.random.rand(dim, 8) * 10 + 1
        self.phase_offsets = np.random.rand(dim, 8) * 2 * np.pi
        # Adaptive conditioning with fractal scaling
        self.conditioning_factors = np.power(np.random.rand(dim) + 0.1, -1.5)
        # Create fractal-based dimensionality reduction patterns
        self.reduction_patterns = np.random.randint(1, dim//2 + 1, dim)
        # Add wave interference with multiple harmonic components
        self.harmonic_amplitudes = np.random.rand(dim, 6) * 2 + 0.5
        self.harmonic_frequencies = np.random.rand(dim, 6) * 5 + 1
        # Create basin structures with varying depths
        self.basin_depths = np.random.rand(dim) * 3 + 1
        # Add chaotic modulation parameters
        self.chaos_params = np.random.rand(dim) * 0.5 + 0.25
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Trigonometric wave interference component
        trig_sum = 0.0
        for i in range(self.dim):
            for j in range(6):
                freq = self.harmonic_frequencies[i, j]
                amp = self.harmonic_amplitudes[i, j]
                phase = self.phase_offsets[i, j % 8]
                trig_sum += amp * np.sin(freq * x_norm[i] + phase)
        
        # Fractal-based conditioning with dimensionality reduction
        cond_sum = 0.0
        for i in range(self.dim):
            # Apply fractal scaling to conditioning factors
            reduced_dim = max(1, int(self.reduction_patterns[i]))
            dim_factor = np.sum(x_norm[:reduced_dim]**2) / reduced_dim
            cond_sum += self.conditioning_factors[i] * dim_factor
        
        # Basin structure component with varying depths
        basin_sum = 0.0
        for i in range(self.dim):
            basin_sum += self.basin_depths[i] * (np.exp(-x_norm[i]**2) - 0.5)
        
        # Multi-scale harmonic interference
        multi_scale = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(x_norm[i] * 10)
            multi_scale += np.sum([amp * np.cos(freq * x_norm[i]) 
                                 for amp, freq in zip(self.harmonic_amplitudes[i], self.harmonic_frequencies[i])])
        
        # Chaotic modulation with fractal dimensionality
        chaos_mod = 0.0
        for i in range(self.dim):
            chaos_mod += self.chaos_params[i] * np.sin(x_norm[i] * np.pi * 5 + np.sum(x_norm[:i+1]))
        
        # Combine all components with adaptive weighting
        result = (0.3 * trig_sum + 0.25 * cond_sum + 0.2 * basin_sum + 
                 0.15 * multi_scale + 0.1 * chaos_mod)
        
        # Apply fractal transformation to create complex fitness landscape
        fractal_transform = np.prod(np.abs(x_norm) + 0.1)
        result = result * fractal_transform
        
        # Add final non-linear transformation for enhanced complexity
        result = np.tanh(result) * (1.0 + 0.3 * np.sin(result))
        
        return result