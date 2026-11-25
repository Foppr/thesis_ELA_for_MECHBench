import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher sensitivity
        self.r_values = np.linspace(3.9, 4.2, min(dim, 20))
        self.scale_factor = 1.5 + 0.5 * np.sin(np.arange(min(dim, 20)) * 0.3)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic map with time-varying parameters and memory effects
        chaos_term = 0.0
        for i in range(min(self.dim, 20)):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = np.abs(x[i-1]) / 5.0 + 0.3
            r_val = self.r_values[i] * (1.0 + 0.1 * np.sin(i * 0.7))
            chaos_term += r_val * x_prev * (1 - x_prev) * np.exp(-0.1 * i)
        
        # Nested radial basis functions with hierarchical centers and varying sigmas
        rbfs = 0.0
        levels = min(5, self.dim // 2 + 1)
        for level in range(levels):
            num_centers = max(3, self.dim // (level + 1))
            centers = np.linspace(-4.8, 4.8, num_centers)
            for i, center in enumerate(centers):
                sigma = 1.0 + 0.5 * np.sin(level * 0.6 + x[i % self.dim] * 0.2) * \
                       (1.0 + 0.3 * np.cos(i * 0.4))
                rbfs += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                       np.cos(6.0 * np.pi * (x[i % self.dim] - center) / (3.0 + 0.1 * level))
        
        # Dynamic saddle points with fractional powers and multi-scale trigonometric mixing
        saddle = 0.0
        for i in range(self.dim):
            base = x[i]
            saddle += (base**9 - 9*base**7 + 28*base**5 - 36*base**3 + 10*base) * \
                     np.sin(0.6 * base + 0.2 * np.cos(base)) + \
                     0.2 * (base - np.mean(x))**9
        
        # Multi-scale cross-dimensional coupling with adaptive weights and non-linear interactions
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            k = (i + 7) % self.dim
            l = (i + 11) % self.dim
            weight = 1.2 + 0.6 * np.sin(i * 0.4 + x[j] * 0.3) * \
                    np.cos(0.5 * x[k]) * np.exp(-0.05 * i)
            cross_term += weight * np.sin(4.0 * x[i]) * np.cos(3.0 * x[j]) * \
                         np.tanh(0.8 * (x[k] - x[i])) * \
                         np.exp(-0.15 * (x[i]**2 + x[j]**2 + x[k]**2)) * \
                         np.log(1.0 + 0.5 * np.abs(x[l]))
        
        # Additional high-frequency oscillation component
        freq_term = 0.0
        for i in range(self.dim):
            freq_term += np.sin(12.0 * x[i]) * np.cos(8.0 * x[i]) * \
                        np.exp(-0.03 * x[i]**2) * (1.0 + 0.2 * np.sin(i * 0.5))
        
        # Combine all components with refined weights
        result = 0.4 * np.sum(x**2) + 0.3 * chaos_term + 0.25 * rbfs + \
                 0.35 * saddle + 0.2 * cross_term + 0.1 * freq_term
        
        return result