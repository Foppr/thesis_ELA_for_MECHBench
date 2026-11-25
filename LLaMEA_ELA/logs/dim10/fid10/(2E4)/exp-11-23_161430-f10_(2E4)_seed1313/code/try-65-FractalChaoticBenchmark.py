import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic tent map parameters with dynamic scaling
        self.amp = 2.0 + 1.0 * np.sin(np.arange(dim) * 0.5)
        self.beta = 0.8 + 0.4 * np.cos(np.arange(dim) * 0.6)
        # Fractal Brownian motion parameters with adaptive Hurst
        self.hurst = 0.2 + 0.6 * np.random.rand(dim)
        self.fractal_scale = 3.0 + 2.0 * np.sin(np.arange(dim) * 0.3)
        # Additional chaotic modulation parameters
        self.chaos_factor = 1.5 + 0.5 * np.cos(np.arange(dim) * 0.4)
        self.modulation_freq = 0.5 + 0.5 * np.sin(np.arange(dim) * 0.2)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic tent map component with multiple iterations
        tent_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-iteration chaotic tent map
            tent_val = xi
            for _ in range(3):
                if tent_val < 0.5:
                    tent_val = self.amp[i] * tent_val
                else:
                    tent_val = self.amp[i] * (1 - tent_val)
            # Enhanced chaotic modulation with frequency and amplitude
            tent_term += tent_val * np.sin(self.beta[i] * xi + self.modulation_freq[i]) * \
                        np.cos(self.chaos_factor[i] * xi) * np.exp(-0.08 * i)
        
        # Fractal Brownian motion component with enhanced noise
        fbm_term = 0.0
        for i in range(self.dim):
            # Generate fractal noise using Hurst parameter with multiple octaves
            noise_val = np.random.normal(0, 1) * self.fractal_scale[i]
            # Enhanced scaling with dynamic frequency components
            fbm_term += noise_val * np.cos(2.0 * np.pi * x[i] * (i + 1)) * \
                       np.sin(3.0 * np.pi * x[i] / (i + 1)) * \
                       np.exp(-0.03 * (x[i]**2 + i**2))
        
        # Enhanced multi-scale radial basis function component
        rbf_term = 0.0
        scales = np.linspace(0.3, 4.0, min(10, self.dim // 2 + 2))
        for level, scale in enumerate(scales):
            centers = np.linspace(-4.8, 4.8, max(4, self.dim // (level + 1) + 1))
            for i, center in enumerate(centers):
                sigma = scale * (1.0 + 0.3 * np.sin(i * 0.6))
                # Enhanced RBF with additional trigonometric modulation
                rbf_term += np.exp(-0.5 * ((x[i % self.dim] - center) / sigma)**2) * \
                           np.sin(4.0 * (x[i % self.dim] - center) / sigma) * \
                           np.cos(2.0 * (x[i % self.dim] - center) / sigma)
        
        # Enhanced saddle point structure
        saddle_term = 0.0
        for i in range(self.dim):
            base = x[i]
            # Higher-order polynomial with enhanced trigonometric coupling
            saddle_term += (base**7 - 7*base**5 + 15*base**3 - 9*base) * \
                          np.cos(0.6 * base) * np.sin(0.4 * base) * np.exp(-0.12 * i)
        
        # Enhanced cross-dimensional interaction with fractal coupling
        cross_term = 0.0
        for i in range(self.dim):
            j = (i + 3) % self.dim
            k = (i + 7) % self.dim
            l = (i + 11) % self.dim
            # Multi-dimensional weight with enhanced coupling
            weight = 1.2 + 0.4 * np.sin(i * 0.5) * np.cos(x[j] * 0.4) * np.sin(x[k] * 0.3)
            cross_term += weight * np.sin(3.0 * x[i]) * np.cos(2.0 * x[j]) * \
                         np.tanh(0.8 * (x[k] - x[i])) * np.exp(-0.15 * (x[i]**2 + x[j]**2)) * \
                         np.cos(0.3 * x[l])
        
        # Additional chaotic harmonic component
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(4.0 * x[i] + 0.5 * np.sin(i * 0.7)) * \
                           np.cos(3.0 * x[i] + 0.3 * np.cos(i * 0.8)) * \
                           np.exp(-0.05 * i**2)
        
        # Combine all components with enhanced weights
        result = 0.4 * np.sum(x**2) + 0.3 * tent_term + 0.25 * fbm_term + \
                 0.2 * rbf_term + 0.15 * saddle_term + 0.08 * cross_term + \
                 0.05 * harmonic_term
        
        return result