import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slight mutation: adjusted chaotic parameters for enhanced conditioning
        self.r_values = np.linspace(3.95, 4.15, min(dim, 20))
        self.scale_factor = 1.6 + 0.4 * np.sin(np.arange(min(dim, 20)) * 0.35)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Mutated chaotic map with slightly altered sensitivity and memory effects
        chaos_term = 0.0
        for i in range(min(self.dim, 20)):
            if i == 0:
                x_prev = 0.5
            else:
                x_prev = np.abs(x[i-1]) / 5.0 + 0.35
            r_val = self.r_values[i] * (1.0 + 0.12 * np.sin(i * 0.75))
            chaos_term += r_val * x_prev * (1 - x_prev) * np.exp(-0.12 * i)
        
        # Slight modification in radial basis functions with altered sigma modulation
        rbfs = 0.0
        levels = min(5, self.dim // 2 + 1)
        for level in range(levels):
            num_centers = max(3, self.dim // (level + 1))
            centers = np.linspace(-4.7, 4.9, num_centers)
            for i, center in enumerate(centers):
                sigma = 1.1 + 0.4 * np.sin(level * 0.65 + x[i % self.dim] * 0.22) * \
                       (1.0 + 0.35 * np.cos(i * 0.42))
                rbfs += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                       np.cos(6.2 * np.pi * (x[i % self.dim] - center) / (3.1 + 0.12 * level))
        
        # Saddle point structure remains similar but with slight coefficient adjustments
        saddle = 0.0
        for i in range(self.dim):
            base = x[i]
            saddle += (base**9 - 9*base**7 + 28*base**5 - 36*base**3 + 10*base) * \
                     np.sin(0.62 * base + 0.21 * np.cos(base)) + \
                     0.21 * (base - np.mean(x))**9
        
        # Cross-dimensional coupling with slightly modified interaction weights
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            k = (i + 7) % self.dim
            l = (i + 11) % self.dim
            weight = 1.25 + 0.55 * np.sin(i * 0.42 + x[j] * 0.32) * \
                    np.cos(0.52 * x[k]) * np.exp(-0.052 * i)
            cross_term += weight * np.sin(4.1 * x[i]) * np.cos(3.1 * x[j]) * \
                         np.tanh(0.82 * (x[k] - x[i])) * \
                         np.exp(-0.155 * (x[i]**2 + x[j]**2 + x[k]**2)) * \
                         np.log(1.0 + 0.51 * np.abs(x[l]))
        
        # High-frequency oscillation component slightly modified
        freq_term = 0.0
        for i in range(self.dim):
            freq_term += np.sin(12.2 * x[i]) * np.cos(8.2 * x[i]) * \
                        np.exp(-0.032 * x[i]**2) * (1.0 + 0.21 * np.sin(i * 0.52))
        
        # Combine all components with refined weights
        result = 0.41 * np.sum(x**2) + 0.29 * chaos_term + 0.26 * rbfs + \
                 0.36 * saddle + 0.21 * cross_term + 0.11 * freq_term
        
        return result