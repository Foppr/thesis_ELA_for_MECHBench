import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.frequency_scale = 5.0
        self.conditioning_factor = 3.0
        
    def f(self, x):
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial quadratic term with modified bias towards origin
        radial_term = 0.3 * np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Enhanced multimodal sinusoidal components with higher frequency variations
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sinusoidal components with different frequencies and amplitudes
            freq = (i + 1) * self.frequency_scale
            multimodal_term += np.sin(freq * xi) * np.cos(0.5 * freq * xi) + \
                              0.5 * np.sin(2 * freq * xi) * np.cos(freq * xi) + \
                              0.3 * np.sin(3 * freq * xi) * np.sin(0.7 * freq * xi)
        
        # Stronger cross-dimensional interaction terms creating complex correlations
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-separable interaction with exponential decay and additional trigonometric coupling
                diff = x[i] - x[j]
                interaction_term += diff**2 * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) + \
                                   0.5 * np.cos(x[i] + x[j]) * np.sin(0.3 * x[i] * x[j])
        
        # Enhanced chaotic modulation using a modified sine map with additional nonlinear transformations
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Sine-based chaotic component with non-linear transformation and phase shifts
            chaotic_component = np.sin(xi * 3.0 + np.sin(xi * 1.5) + np.cos(xi * 0.8))
            chaotic_term += chaotic_component * np.cos(xi * 2.0 + i * 0.4 + np.sin(xi * 0.6))
        
        # Enhanced conditioning term that increases difficulty with dimension
        conditioning_term = 0.0
        for i in range(self.dim):
            conditioning_term += (i + 1) * self.conditioning_factor * x[i]**4 + \
                               0.5 * (i + 1)**2 * x[i]**6
        
        # Additional higher-order polynomial interaction terms
        high_order_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    high_order_term += x[i] * x[j] * x[k] * np.sin(0.1 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        # Combine all terms with appropriate weights
        return radial_term + 1.5 * multimodal_term + 1.0 * interaction_term + 0.8 * chaotic_term + 0.5 * conditioning_term + 0.2 * high_order_term