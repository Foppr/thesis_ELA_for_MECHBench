import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher sensitivity and memory effects
        self.r_values = np.linspace(3.85, 4.25, min(dim, 25))
        self.scale_factor = 1.7 + 0.6 * np.sin(np.arange(min(dim, 25)) * 0.4)
        # Additional chaotic sequence for enhanced complexity
        self.chaos_sequence = np.random.rand(min(dim, 25)) * 2.0 - 1.0
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic map with time-varying parameters, memory effects and cross-dimensional coupling
        chaos_term = 0.0
        for i in range(min(self.dim, 25)):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = np.abs(x[i-1]) / 5.0 + 0.3
            
            # Dynamic parameter modulation based on current position and sequence
            r_val = self.r_values[i] * (1.0 + 0.15 * np.sin(i * 0.8) * np.cos(x[i % self.dim] * 0.2))
            chaos_term += r_val * x_prev * (1 - x_prev) * np.exp(-0.12 * i) * \
                         (1.0 + 0.3 * np.sin(self.chaos_sequence[i] * x[i % self.dim]))
        
        # Nested radial basis functions with hierarchical centers, varying sigmas and multi-scale interactions
        rbfs = 0.0
        levels = min(6, self.dim // 2 + 1)
        for level in range(levels):
            num_centers = max(4, self.dim // (level + 1) + 2)
            centers = np.linspace(-4.7, 4.7, num_centers)
            for i, center in enumerate(centers):
                # Adaptive sigma with multi-dimensional dependency
                sigma = 1.2 + 0.6 * np.sin(level * 0.7 + x[i % self.dim] * 0.3) * \
                       (1.0 + 0.4 * np.cos(i * 0.5 + level * 0.3))
                # Multi-scale cosine modulation
                rbfs += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                       np.cos(8.0 * np.pi * (x[i % self.dim] - center) / (4.0 + 0.15 * level)) * \
                       np.sin(0.5 * x[i % self.dim] * (level + 1))
        
        # Dynamic saddle points with fractional powers, multi-scale trigonometric mixing and cross-dimensional interactions
        saddle = 0.0
        for i in range(self.dim):
            base = x[i]
            # Fractional power dynamics with variable exponents
            exp_factor = 2.0 + 0.5 * np.sin(i * 0.6)
            saddle += (base**exp_factor - exp_factor*base**(exp_factor-1) + 
                      (exp_factor*(exp_factor-1)/2)*base**(exp_factor-2)) * \
                     np.sin(0.7 * base + 0.3 * np.cos(base)) + \
                     0.3 * (base - np.mean(x))**exp_factor
        
        # Multi-scale cross-dimensional coupling with adaptive weights, non-linear interactions and higher-order terms
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 4) % self.dim
            k = (i + 8) % self.dim
            l = (i + 12) % self.dim
            m = (i + 16) % self.dim
            
            # Complex weight function with multiple modulation factors
            weight = 1.5 + 0.7 * np.sin(i * 0.5 + x[j] * 0.4) * \
                    np.cos(0.6 * x[k]) * np.exp(-0.06 * i) * \
                    np.tanh(0.9 * (x[l] - x[i]))
            
            cross_term += weight * np.sin(5.0 * x[i]) * np.cos(4.0 * x[j]) * \
                         np.tanh(0.9 * (x[k] - x[i])) * \
                         np.exp(-0.2 * (x[i]**2 + x[j]**2 + x[k]**2)) * \
                         np.log(1.0 + 0.6 * np.abs(x[l])) * \
                         np.cos(0.3 * x[m])
        
        # Additional high-frequency oscillation component with multi-scale modulation
        freq_term = 0.0
        for i in range(self.dim):
            freq_term += np.sin(15.0 * x[i]) * np.cos(10.0 * x[i]) * \
                        np.exp(-0.04 * x[i]**2) * (1.0 + 0.3 * np.sin(i * 0.6)) * \
                        np.cos(0.4 * x[i] * (i % 5 + 1))
        
        # Combine all components with refined weights and scaling
        result = 0.5 * np.sum(x**2) + 0.35 * chaos_term + 0.3 * rbfs + \
                 0.4 * saddle + 0.25 * cross_term + 0.15 * freq_term
        
        return result