import numpy as np

class AdaptiveEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic parameters based on dimensionality
        self.num_valleys = max(1, dim // 3)
        self.conditioning_factors = np.logspace(-0.5, 1.5, min(8, dim))
        self.noise_levels = np.linspace(0.01, 0.1, min(6, dim))
        self.elliptic_axes = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Adaptive elliptic valley structure
        valley_term = 0.0
        for i in range(self.num_valleys):
            # Create valley centers with dynamic positioning
            center = np.sin(i * np.pi / self.num_valleys) * 0.8
            # Elliptic valley with adaptive axes
            valley_val = np.sum(((x_norm - center) ** 2) / (self.elliptic_axes + 0.1))
            valley_term += np.exp(-valley_val)
            
        # Dynamic conditioning gradient across dimensions
        cond_term = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i % len(self.conditioning_factors)]
            cond_val = (x_norm[i] ** 2) * cond_factor
            cond_term += cond_val
            
        # Hybrid noise injection with dimension-specific amplitude
        noise_term = 0.0
        for i in range(self.dim):
            noise_level = self.noise_levels[i % len(self.noise_levels)]
            noise_val = np.random.normal(0, noise_level)
            noise_term += noise_val * (1.0 + 0.1 * i)
            
        # Cross-dimension coupling with adaptive weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                weight = 0.5 * (1.0 + np.sin(0.5 * (x_norm[i] + x_norm[j])))
                coupling = weight * (x_norm[i] - x_norm[j]) ** 2
                cross_term += coupling
                
        # Multi-scale modulation with chaotic frequency components
        mod_term = 0.0
        freqs = np.linspace(1.0, 5.0, min(5, self.dim))
        for i in range(self.dim):
            freq = freqs[i % len(freqs)]
            mod_val = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            mod_term += mod_val
            
        # Combine all terms with dynamic scaling
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        result = scale_factor * (0.6 * valley_term + 0.3 * cond_term + 0.2 * cross_term + 0.1 * mod_term) + noise_term
        
        # Add final chaotic perturbation
        chaos_perturb = 0.05 * np.sin(np.sum(x_norm) * 10.0)
        
        return result + chaos_perturb