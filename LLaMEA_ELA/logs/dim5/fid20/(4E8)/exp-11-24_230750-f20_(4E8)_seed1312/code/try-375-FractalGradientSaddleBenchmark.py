import numpy as np

class FractalGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.hurst = 0.3 + 0.4 * np.random.rand(dim)
        self.amplitude = 2.0 + 3.0 * np.random.rand(dim)
        self.frequency = 1.0 + 2.0 * np.random.rand(dim)
        # Saddle point configuration
        self.saddle_centers = np.random.uniform(-3, 3, (dim, 2))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component
        fbm = 0.0
        for i in range(self.dim):
            # Generate fractal noise using harmonic sum
            noise = 0.0
            for k in range(1, 6):
                freq = self.frequency[i] * (2 ** k)
                amp = self.amplitude[i] / (freq ** (2 * self.hurst[i]))
                noise += amp * np.sin(freq * x[i])
            fbm += noise
        
        # Adaptive gradient field with varying steepness
        grad_field = 0.0
        for i in range(self.dim):
            # Dynamic steepness based on position and dimension
            steepness = 1.0 + 0.5 * np.sin(0.3 * x[i]) + 0.3 * np.cos(0.2 * x[i])
            grad_field += steepness * (x[i] ** 3) / (1.0 + x[i]**2)
        
        # Saddle point structure with multi-dimensional coupling
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                center1, center2 = self.saddle_centers[i]
                saddle += (x[i] - center1) * (x[i+1] - center2) * np.exp(-0.1 * ((x[i] - center1)**2 + (x[i+1] - center2)**2))
        
        # Multi-scale harmonic modulation
        harmonic = 0.0
        for i in range(self.dim):
            mod_freq = 2.0 + 3.0 * np.sin(0.5 * x[i])
            mod_amp = 1.0 + 0.8 * np.cos(0.4 * x[i])
            harmonic += mod_amp * np.sin(mod_freq * x[i]) * np.cos(0.7 * x[i])
        
        # Asymmetric conditioning with exponential weighting
        cond_weight = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.sin(0.6 * x[i]) + 0.2 * np.cos(0.8 * x[i])
            cond_weight += weight * (x[i]**2) / (1.0 + np.exp(-x[i]))
        
        # Combine all components with dimension-dependent scaling
        dim_factor = 1.0 + 0.05 * np.log(self.dim)
        return (0.25 * fbm + 0.30 * grad_field + 0.20 * saddle + 
                0.15 * harmonic + 0.10 * cond_weight) * dim_factor