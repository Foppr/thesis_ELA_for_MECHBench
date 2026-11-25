import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like parameters
        self.gaussian_centers = np.random.uniform(-4, 4, (dim, 3))
        self.gaussian_heights = np.random.uniform(0.5, 2.0, (dim, 3))
        self.gaussian_widths = np.random.uniform(0.3, 1.5, (dim, 3))
        self.sine_frequencies = np.random.uniform(1.0, 6.0, dim)
        self.memory_weights = np.random.uniform(0.1, 0.5, dim)
        self.conditioning_factors = np.random.uniform(0.8, 1.5, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like Gaussian peaks with multiple local minima
        gaussian_sum = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = self.gaussian_centers[i, j]
                height = self.gaussian_heights[i, j]
                width = self.gaussian_widths[i, j]
                gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Memory-enhanced sine-wave couplings with adaptive weights
        sine_coupling = 0.0
        for i in range(self.dim):
            freq = self.sine_frequencies[i]
            weight = self.memory_weights[i]
            if i > 0:
                memory_effect = np.sin(0.5 * x[i-1]) * weight
            else:
                memory_effect = 0.0
            sine_coupling += (np.sin(freq * x[i]) + memory_effect) * np.cos(0.3 * x[i])
        
        # Adaptive conditioning with fractal-like scaling
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i]
            conditioning += cond_factor * (x[i]**2 + 0.1 * np.sin(5 * x[i])**2)
        
        # Cross-dimensional cubic coupling with fractal structure
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                diff = x[i] - x[j]
                weight = 1.0 + 0.3 * np.sin(0.4 * x[i]) * np.cos(0.2 * x[j])
                cubic_coupling += weight * diff**3 * np.exp(-0.1 * abs(diff))
        
        # Fractal-like periodic modulation with multiple scales
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.2 * x[i])
            mod_freq = 2.0 + 3.0 * np.cos(0.3 * x[i])
            fractal_mod += scale * np.sin(mod_freq * x[i]) * np.cos(0.5 * x[i]**2)
        
        # Add a new component: hyperbolic tangent-based saddle structure
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.3 * x[i] + 0.4 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * tanh_term
        
        # Combine all components with dimensionally varying weights
        dim_factor = 1.0 + 0.2 * np.log(self.dim)
        return (0.25 * gaussian_sum + 0.20 * sine_coupling + 
                0.18 * conditioning + 0.22 * cubic_coupling + 
                0.10 * fractal_mod + 0.05 * saddle) * dim_factor