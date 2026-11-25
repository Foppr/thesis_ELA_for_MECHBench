import numpy as np

class FractalGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters with enhanced chaos
        self.hurst = 0.2 + 0.5 * np.random.rand(dim)
        self.amplitude = 1.5 + 4.0 * np.random.rand(dim)
        self.frequency = 0.5 + 3.0 * np.random.rand(dim)
        # Saddle point configuration with memory effects
        self.saddle_centers = np.random.uniform(-4, 4, (dim, 2))
        # Memory coefficients for dynamic interactions
        self.memory_coeffs = 0.5 + 1.0 * np.random.rand(dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with enhanced harmonics
        fbm = 0.0
        for i in range(self.dim):
            noise = 0.0
            for k in range(1, 8):
                freq = self.frequency[i] * (2 ** k)
                amp = self.amplitude[i] / (freq ** (2 * self.hurst[i]))
                noise += amp * np.sin(freq * x[i])
            fbm += noise
        
        # Adaptive gradient field with memory-dependent steepness
        grad_field = 0.0
        for i in range(self.dim):
            # Memory-based dynamic steepness
            steepness = 1.5 + 0.7 * np.sin(0.4 * x[i]) + 0.4 * np.cos(0.3 * x[i]) + \
                       self.memory_coeffs[i] * np.tanh(0.1 * x[i])
            grad_field += steepness * (x[i] ** 3) / (1.0 + x[i]**2)
        
        # Saddle point structure with Gaussian coupling
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                center1, center2 = self.saddle_centers[i]
                # Gaussian coupling between dimensions
                coupling = np.exp(-0.05 * ((x[i] - center1)**2 + (x[i+1] - center2)**2))
                saddle += (x[i] - center1) * (x[i+1] - center2) * coupling
        
        # Multi-scale harmonic modulation with chaotic phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            mod_freq = 1.5 + 4.0 * np.sin(0.6 * x[i] + 0.3 * i)
            mod_amp = 0.8 + 1.2 * np.cos(0.5 * x[i] + 0.4 * i)
            harmonic += mod_amp * np.sin(mod_freq * x[i]) * np.cos(0.8 * x[i])
        
        # Asymmetric conditioning with exponential weighting and cubic terms
        cond_weight = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.4 * np.sin(0.7 * x[i]) + 0.3 * np.cos(0.9 * x[i])
            # Add cubic conditioning term for increased complexity
            cond_weight += weight * (x[i]**3) / (1.0 + np.exp(-x[i]))
        
        # Combine all components with modified dimensional scaling
        dim_factor = 1.0 + 0.1 * np.log(self.dim)
        return (0.30 * fbm + 0.25 * grad_field + 0.25 * saddle + 
                0.15 * harmonic + 0.05 * cond_weight) * dim_factor