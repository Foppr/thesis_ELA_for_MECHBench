import numpy as np

class FractalGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters with enhanced chaos
        self.hurst = 0.2 + 0.5 * np.random.rand(dim)
        self.amplitude = 1.5 + 4.0 * np.random.rand(dim)
        self.frequency = 0.8 + 2.5 * np.random.rand(dim)
        # Enhanced saddle point configuration with stronger coupling
        self.saddle_centers = np.random.uniform(-4, 4, (dim, 2))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with higher frequency harmonics
        fbm = 0.0
        for i in range(self.dim):
            noise = 0.0
            for k in range(1, 8):  # Increased harmonic count
                freq = self.frequency[i] * (2 ** k)
                amp = self.amplitude[i] / (freq ** (2 * self.hurst[i]))
                noise += amp * np.sin(freq * x[i])
            fbm += noise
        
        # Adaptive gradient field with enhanced nonlinearity
        grad_field = 0.0
        for i in range(self.dim):
            steepness = 1.5 + 0.7 * np.sin(0.4 * x[i]) + 0.5 * np.cos(0.3 * x[i])
            grad_field += steepness * (x[i] ** 4) / (1.0 + x[i]**2)
        
        # Saddle point structure with increased coupling strength
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                center1, center2 = self.saddle_centers[i]
                saddle += (x[i] - center1) * (x[i+1] - center2) * np.exp(-0.15 * ((x[i] - center1)**2 + (x[i+1] - center2)**2))
        
        # Modified harmonic modulation with additional nonlinear terms
        harmonic = 0.0
        for i in range(self.dim):
            mod_freq = 1.5 + 4.0 * np.sin(0.6 * x[i])
            mod_amp = 2.0 + 1.2 * np.cos(0.5 * x[i]) + 0.5 * np.sin(1.2 * x[i])
            harmonic += mod_amp * np.sin(mod_freq * x[i]) * np.cos(0.8 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Enhanced asymmetric conditioning with polynomial weighting
        cond_weight = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.4 * np.sin(0.7 * x[i]) + 0.3 * np.cos(0.9 * x[i]) + 0.1 * np.sin(1.5 * x[i])
            cond_weight += weight * (x[i]**3) / (1.0 + np.exp(-x[i]))
        
        # Combine all components with modified scaling
        dim_factor = 1.0 + 0.08 * np.log(self.dim)
        return (0.20 * fbm + 0.35 * grad_field + 0.25 * saddle + 
                0.15 * harmonic + 0.05 * cond_weight) * dim_factor