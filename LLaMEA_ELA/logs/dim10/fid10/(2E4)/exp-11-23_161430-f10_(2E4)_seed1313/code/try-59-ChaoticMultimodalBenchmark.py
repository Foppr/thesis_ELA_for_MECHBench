import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for stronger sensitivity
        self.r_values = np.linspace(3.98, 4.12, min(dim, 20))
        self.scale_factor = 1.7 + 0.3 * np.sin(np.arange(min(dim, 20)) * 0.4)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic map with increased sensitivity and memory effects
        chaos_term = 0.0
        for i in range(min(self.dim, 20)):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = np.abs(x[i-1]) / 5.0 + 0.38
            r_val = self.r_values[i] * (1.0 + 0.15 * np.sin(i * 0.8))
            chaos_term += r_val * x_prev * (1 - x_prev) * np.exp(-0.15 * i)
        
        # Modified radial basis functions with dynamic sigma and phase adjustments
        rbfs = 0.0
        levels = min(6, self.dim // 2 + 1)
        for level in range(levels):
            num_centers = max(4, self.dim // (level + 1))
            centers = np.linspace(-4.8, 4.8, num_centers)
            for i, center in enumerate(centers):
                sigma = 1.2 + 0.35 * np.sin(level * 0.7 + x[i % self.dim] * 0.25) * \
                       (1.0 + 0.4 * np.cos(i * 0.45))
                phase_shift = 0.6 * np.sin(0.5 * i + level * 0.3)
                rbfs += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                       np.cos(7.0 * np.pi * (x[i % self.dim] - center) / (3.2 + 0.15 * level) + phase_shift)
        
        # Refined saddle point structure with modified polynomial terms
        saddle = 0.0
        for i in range(self.dim):
            base = x[i]
            saddle += (base**9 - 9*base**7 + 28*base**5 - 36*base**3 + 10*base) * \
                     np.sin(0.7 * base + 0.25 * np.cos(base)) + \
                     0.25 * (base - np.mean(x))**9
        
        # Improved cross-dimensional coupling with modified interaction weights
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 4) % self.dim
            k = (i + 8) % self.dim
            l = (i + 12) % self.dim
            weight = 1.3 + 0.6 * np.sin(i * 0.5 + x[j] * 0.35) * \
                    np.cos(0.6 * x[k]) * np.exp(-0.06 * i)
            cross_term += weight * np.sin(4.5 * x[i]) * np.cos(3.5 * x[j]) * \
                         np.tanh(0.9 * (x[k] - x[i])) * \
                         np.exp(-0.18 * (x[i]**2 + x[j]**2 + x[k]**2)) * \
                         np.log(1.0 + 0.6 * np.abs(x[l]))
        
        # Adjusted high-frequency oscillation component
        freq_term = 0.0
        for i in range(self.dim):
            freq_term += np.sin(13.0 * x[i]) * np.cos(9.0 * x[i]) * \
                        np.exp(-0.04 * x[i]**2) * (1.0 + 0.25 * np.sin(i * 0.6))
        
        # Combine all components with adjusted weights
        result = 0.45 * np.sum(x**2) + 0.32 * chaos_term + 0.28 * rbfs + \
                 0.38 * saddle + 0.23 * cross_term + 0.13 * freq_term
        
        return result