import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying centers and widths
        rb = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        widths = 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.3)
        for i in range(self.dim):
            center = centers[i % len(centers)] if len(centers) > 0 else 0
            rb += np.exp(-0.5 * ((x[i] - center) / widths[i % len(widths)])**2)
        
        # Sinusoidal modulation component with multi-frequency interactions
        sin_mod = 0
        frequencies = [1.0, 1.5, 2.0, 2.5, 3.0]
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            sin_mod += np.sin(frequencies[freq_idx] * x[i]) * np.cos(frequencies[freq_idx] * x[i])
            
        # Cross-dimensional interaction with exponential decay
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                cross_interaction += np.exp(-dist) * np.sin(x[i] * x[j])
        
        # Polynomial chaos component with asymmetric terms
        poly_chaos = 0
        for i in range(self.dim):
            poly_chaos += (x[i]**4 - 2*x[i]**2 + 1) * np.sin(0.5 * x[i]) + \
                          (x[i]**3 - x[i]) * np.cos(0.3 * x[i])
        
        # Dynamic conditioning component with variable exponents
        cond = 0
        for i in range(self.dim):
            exponent = 1.0 + 0.5 * np.sin(i * 0.4)
            cond += (x[i]**2) ** exponent
        
        # Multimodal Gaussian peaks with dynamic scaling
        multi_peak = 0
        peak_positions = np.linspace(-3, 3, min(7, self.dim))
        for i in range(self.dim):
            pos_idx = i % len(peak_positions)
            peak_height = 1.0 + 0.3 * np.cos(i * 0.5)
            multi_peak += peak_height * np.exp(-0.5 * ((x[i] - peak_positions[pos_idx]) / 0.8)**2)
        
        # Asymmetric saddle component
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1.0)**3 * np.sin(0.4 * x[i])
        
        # Final combination with optimized weights
        return (rb * 0.6 +
                sin_mod * 0.5 +
                cross_interaction * 0.4 +
                poly_chaos * 0.7 +
                cond * 0.3 +
                multi_peak * 0.8 +
                saddle * 0.5)