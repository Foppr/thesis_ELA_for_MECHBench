import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal-like Gaussian peak parameters with self-similar structure
        self.gauss_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.gauss_heights = 2.0 + 3.0 * np.random.rand(dim, 5)
        self.gauss_widths = 0.2 + 1.0 * np.random.rand(dim, 5)
        # Sine-wave coupling with fractal frequency modulation
        self.sin_freq = 2.0 + 3.0 * np.random.rand(dim)
        self.sin_amp = 1.0 + 2.0 * np.random.rand(dim)
        # Memory-enhanced coupling coefficients
        self.memory_weights = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Adaptive conditioning factors with chaotic scaling
        self.conditioning_factors = 1.0 + 0.8 * np.random.rand(dim)
        # Fractal dimension scaling factor
        self.fractal_dim = 1.0 + 0.5 * np.sin(0.3 * dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Gaussian peaks with self-similar structure
        gauss_peaks = 0.0
        for i in range(self.dim):
            peak_sum = 0.0
            for j in range(5):
                center = self.gauss_centers[i, j]
                height = self.gauss_heights[i, j]
                width = self.gauss_widths[i, j]
                # Fractal scaling with dimension-dependent factor
                fractal_scale = (1.0 + 0.2 * np.sin(0.5 * x[i] + 0.3 * i)) ** self.fractal_dim
                peak_sum += height * np.exp(-0.5 * ((x[i] - center) / (width * fractal_scale)) ** 2)
            gauss_peaks += peak_sum
        
        # Memory-enhanced sine-wave couplings
        sine_coupling = 0.0
        for i in range(self.dim):
            mod_freq = self.sin_freq[i] * (1.0 + 0.3 * np.sin(0.4 * x[i] + 0.2 * i))
            mod_amp = self.sin_amp[i] * (1.0 + 0.2 * np.cos(0.5 * x[i] + 0.3 * i))
            # Memory effect from neighboring dimensions
            mem_effect = 1.0 + 0.1 * np.sum(self.memory_weights[i, :] * x)
            sine_coupling += mod_amp * np.sin(mod_freq * x[i]) * mem_effect
        
        # Adaptive conditioning with chaotic scaling
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i] * (1.0 + 0.5 * np.sin(0.6 * x[i] + 0.4 * i))
            conditioning += cond_factor * (x[i]**2) * np.exp(-0.1 * abs(x[i]))
        
        # Cross-dimensional fractal coupling
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Fractal-like coupling with dimension-dependent scaling
                    scale_factor = (1.0 + 0.3 * np.sin(0.5 * x[i] + 0.2 * j)) ** self.fractal_dim
                    fractal_coupling += self.memory_weights[i, j] * x[i] * x[j] * scale_factor
        
        # Combine components with dynamic weighting
        dim_factor = 1.0 + 0.25 * np.log(self.dim)
        return (0.30 * gauss_peaks + 0.25 * sine_coupling + 0.20 * conditioning + 
                0.25 * fractal_coupling) * dim_factor