import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal Gaussian parameters
        self.gauss_means = np.random.uniform(-3.0, 3.0, dim)
        self.gauss_stds = np.random.uniform(0.5, 2.0, dim)
        self.gauss_heights = np.random.uniform(1.0, 3.0, dim)
        # Memory-enhanced sine parameters
        self.sine_freqs = np.random.uniform(2.0, 6.0, dim)
        self.sine_ampls = np.random.uniform(0.5, 1.5, dim)
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        # Cross-dimensional couplings with memory effect
        self.memory_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        for i in range(self.dim):
            mean = self.gauss_means[i]
            std = self.gauss_stds[i]
            height = self.gauss_heights[i]
            gaussian_peaks += height * np.exp(-0.5 * ((x[i] - mean) / std) ** 2)
        
        # Memory-enhanced sine-wave couplings
        sine_couplings = 0.0
        for i in range(self.dim):
            freq = self.sine_freqs[i]
            ampl = self.sine_ampls[i]
            # Sine modulation influenced by previous dimensions
            memory_effect = 0.0
            for j in range(i):
                weight = self.memory_weights[i, j]
                memory_effect += weight * np.sin(freq * x[j])
            sine_couplings += ampl * np.sin(freq * (x[i] + memory_effect))
        
        # Adaptive conditioning with fractal-like scaling
        adaptive_cond = 0.0
        for i in range(self.dim):
            factor = self.conditioning_factors[i]
            # Fractal-like scaling using log-log relationship
            scale_factor = 1.0 + 0.2 * np.sin(np.log(x[i] ** 2 + 1.0))
            adaptive_cond += factor * (x[i] ** 2) * scale_factor
        
        # Cross-dimensional fractal couplings with chaotic modulation
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic modulation using logistic map
                logistic_val = 3.8 * (x[i] % 0.25)
                if x[i] >= 0.25:
                    logistic_val = 3.8 * (1.0 - (x[i] % 0.25))
                chaotic_mod = 1.0 + 0.1 * np.sin(logistic_val)
                fractal_coupling += chaotic_mod * self.memory_weights[i, j] * (x[i] - x[j]) ** 2
        
        # Combine all components with dynamic weighting
        return (0.40 * gaussian_peaks + 0.30 * sine_couplings + 
                0.20 * adaptive_cond + 0.10 * fractal_coupling)