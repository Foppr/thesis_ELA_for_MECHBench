import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frequency_scale = 2.5
        self.conditioning_factor = 1.5
        
    def f(self, x):
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial quadratic term with stronger bias towards origin
        radial_term = 0.3 * np.sum(x**2)
        
        # Modified multimodal sinusoidal components with higher frequency variations
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced sinusoidal components with varying amplitudes and frequencies
            freq1 = (i + 1) * self.frequency_scale
            freq2 = (i + 1) * self.frequency_scale * 1.5
            multimodal_term += np.sin(freq1 * xi) * np.cos(0.3 * freq1 * xi) + \
                              0.7 * np.sin(freq2 * xi) * np.cos(freq1 * xi) + \
                              0.3 * np.sin(3 * freq1 * xi)
        
        # Enhanced cross-dimensional interaction terms
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger non-separable interaction with polynomial decay
                diff = x[i] - x[j]
                interaction_term += diff**2 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) + \
                                   0.1 * x[i]**3 * x[j]**2 * np.cos(x[i] + x[j])
        
        # Modified chaotic modulation with more pronounced irregularities
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # More complex chaotic component with multiple sine transformations
            chaotic_component = np.sin(xi * 3.0 + np.sin(xi * 1.5) + np.sin(xi * 0.7))
            chaotic_term += chaotic_component * np.cos(xi * 2.0 + i * 0.4) * (1 + 0.1 * np.sin(i * 1.2))
        
        # Improved conditioning term with dimension-dependent scaling
        conditioning_term = 0.0
        for i in range(self.dim):
            # More aggressive conditioning with higher-order terms
            conditioning_term += (i + 1) * self.conditioning_factor * (x[i]**4 + 0.5 * x[i]**6)
        
        # Combine all terms with adjusted weights for better balance
        return radial_term + 1.5 * multimodal_term + 1.0 * interaction_term + 0.8 * chaotic_term + 0.5 * conditioning_term