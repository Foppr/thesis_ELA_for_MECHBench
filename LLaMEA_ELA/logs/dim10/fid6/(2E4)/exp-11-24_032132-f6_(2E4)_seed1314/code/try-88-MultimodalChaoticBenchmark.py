import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frequency_scale = 3.0
        self.conditioning_factor = 2.0
        
    def f(self, x):
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic term with bias towards origin
        radial_term = 0.5 * np.sum(x**2)
        
        # Multimodal sinusoidal components with varying frequencies
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sinusoidal components with different frequencies and amplitudes
            freq = (i + 1) * self.frequency_scale
            multimodal_term += np.sin(freq * xi) * np.cos(0.5 * freq * xi) + \
                              0.5 * np.sin(2 * freq * xi) * np.cos(freq * xi)
        
        # Cross-dimensional interaction terms creating complex correlations
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-separable interaction with exponential decay
                diff = x[i] - x[j]
                interaction_term += diff**2 * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Chaotic modulation using a modified sine map
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Sine-based chaotic component with non-linear transformation
            chaotic_component = np.sin(xi * 2.5 + np.sin(xi * 1.3))
            chaotic_term += chaotic_component * np.cos(xi * 1.7 + i * 0.3)
        
        # Conditioning term that increases difficulty with dimension
        conditioning_term = 0.0
        for i in range(self.dim):
            conditioning_term += (i + 1) * self.conditioning_factor * x[i]**4
        
        # Combine all terms with appropriate weights
        return radial_term + 1.2 * multimodal_term + 0.8 * interaction_term + 0.6 * chaotic_term + 0.3 * conditioning_term