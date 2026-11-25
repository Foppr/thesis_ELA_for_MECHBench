import numpy as np

class FractalGradientSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic fractal parameters with memory effects
        self.hurst = 0.2 + 0.5 * np.random.rand(dim)
        self.amplitude = 1.5 + 4.0 * np.random.rand(dim)
        self.frequency = 0.5 + 3.0 * np.random.rand(dim)
        # Memory-dependent saddle configurations
        self.saddle_centers = np.random.uniform(-4, 4, (dim, 3))
        # Time-varying conditioning factors
        self.time_factor = 1.0 + 0.5 * np.sin(0.1 * dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic fractal Brownian motion with memory
        fbm = 0.0
        for i in range(self.dim):
            noise = 0.0
            for k in range(1, 8):
                freq = self.frequency[i] * (2 ** k)
                amp = self.amplitude[i] / (freq ** (2 * self.hurst[i]))
                # Add memory effect through previous dimensions
                mem_factor = 1.0 + 0.1 * np.sin(0.5 * x[max(0, i-1)])
                noise += amp * np.sin(freq * x[i]) * mem_factor
            fbm += noise
        
        # Memory-dependent adaptive gradient field
        grad_field = 0.0
        for i in range(self.dim):
            # Steepness varies with memory of previous evaluations
            steepness = 1.5 + 0.8 * np.sin(0.4 * x[i]) + 0.4 * np.cos(0.3 * x[max(0, i-1)])
            grad_field += steepness * (x[i] ** 4) / (1.0 + x[i]**2)
        
        # Multi-scale saddle structure with cross-dimensional coupling
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                center1, center2, center3 = self.saddle_centers[i]
                # Add temporal component to saddle positions
                temporal_factor = 1.0 + 0.2 * np.sin(0.2 * (i + self.time_factor))
                saddle += (x[i] - center1) * (x[i+1] - center2) * (x[i+2] - center3) * temporal_factor
        
        # Asymmetric harmonic modulation with dynamic frequencies
        harmonic = 0.0
        for i in range(self.dim):
            # Dynamic modulation based on position and dimension
            mod_freq = 3.0 + 2.0 * np.sin(0.6 * x[i]) + 0.5 * np.cos(0.4 * i)
            mod_amp = 1.2 + 0.9 * np.cos(0.5 * x[i]) * np.sin(0.3 * i)
            harmonic += mod_amp * np.sin(mod_freq * x[i]) * np.cos(0.8 * x[i])
        
        # Memory-dependent conditioning with exponential weighting
        cond_weight = 0.0
        for i in range(self.dim):
            # Conditioning varies based on previous dimension and time
            weight = 1.0 + 0.4 * np.sin(0.7 * x[i]) + 0.3 * np.cos(0.9 * x[max(0, i-1)]) + 0.2 * np.sin(0.3 * self.time_factor)
            cond_weight += weight * (x[i]**3) / (1.0 + np.exp(-x[i]))
        
        # Combine all components with enhanced dimension scaling
        dim_factor = 1.0 + 0.1 * np.log(self.dim) + 0.05 * np.sin(0.2 * self.dim)
        return (0.30 * fbm + 0.25 * grad_field + 0.20 * saddle + 
                0.15 * harmonic + 0.10 * cond_weight) * dim_factor