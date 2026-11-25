import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like parameters
        self.fractal_dims = np.random.uniform(0.5, 2.0, dim)
        self.gaussian_centers = np.random.uniform(-3, 3, dim)
        self.gaussian_widths = np.random.uniform(0.5, 2.0, dim)
        self.sine_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.sine_frequencies = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like Gaussian peaks with dimensionally varying fractal dimensions
        gaussian = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            fractal_dim = self.fractal_dims[i]
            gaussian += np.exp(-0.5 * ((x[i] - center) / sigma)**2) * (1.0 + 0.3 * np.sin(fractal_dim * x[i]))
        
        # Memory-enhanced sine-wave couplings with dynamic weights
        sine_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Dynamic weight based on previous evaluations (memory effect)
                weight = 1.0 + 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j])
                sine_coupling += weight * np.sin(self.sine_frequencies[i] * x[i]) * np.cos(self.sine_frequencies[j] * x[j])
        
        # Adaptive conditioning with fractal scaling
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[i])
            conditioning += cond_factor * (x[i]**2) / (1.0 + np.abs(x[i]))
        
        # Deceptive gradient component with hyperbolic tangent
        deceptive = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                tanh_term = np.tanh(0.3 * x[i] + 0.4 * x[i+1])
                deceptive += (x[i]**3 - x[i+1]**2) * tanh_term
        
        # Cross-dimensional cubic couplings with fractal modulation
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-modulated coupling
                fractal_mod = 1.0 + 0.2 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[j])
                cubic_coupling += fractal_mod * (x[i]**3 - x[j]**3) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Multi-scale periodic modulation with fractal frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = self.sine_frequencies[i]
            amp = self.sine_amplitudes[i]
            periodic += amp * np.sin(freq * x[i] + 0.3 * np.cos(2 * x[i]))
        
        # Combine all components with adaptive weights
        dim_factor = 1.0 + 0.2 * np.log(self.dim)
        return (0.25 * gaussian + 0.20 * sine_coupling + 0.15 * conditioning + 
                0.18 * deceptive + 0.12 * cubic_coupling + 0.10 * periodic) * dim_factor