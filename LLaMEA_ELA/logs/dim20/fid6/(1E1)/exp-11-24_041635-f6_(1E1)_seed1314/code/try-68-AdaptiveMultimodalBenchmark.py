import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive scaling
        poly_base = np.sum(x**4) / self.dim
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.5
            amp = 1.0 / (1.0 + i * 0.2)
            trig_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Logarithmic barrier terms to create complex terrain near boundaries
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += 0.1 * np.log(1.0 + (x[i] / 5.0)**2) * np.sin(x[i])
        
        # Cross-dimensional interaction with adaptive coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross_term += (1.0 / (1.0 + dist)) * np.sin(2.0 * x[i] * x[j])
        
        # Gaussian-like peaks with varying heights and widths
        peak_sum = 0.0
        for i in range(self.dim):
            peak_height = 1.0 + 0.5 * np.sin(i)
            peak_width = 0.5 + 0.3 * np.cos(i)
            peak_sum += peak_height * np.exp(-0.5 * ((x[i] - 1.0) / peak_width)**2)
        
        # Final combined function
        result = poly_base + trig_sum + log_barrier + cross_term - peak_sum
        
        return result