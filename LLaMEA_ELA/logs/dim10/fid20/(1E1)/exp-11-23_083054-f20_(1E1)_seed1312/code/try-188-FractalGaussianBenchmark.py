import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for each dimension
        self.fractal_dims = [0.3 + 0.4 * np.sin(0.5 * i) for i in range(dim)]
        self.gauss_means = np.array([np.cos(i * 0.8) * 2.0 for i in range(dim)])
        self.gauss_stds = np.array([0.5 + 0.3 * np.sin(0.6 * i) for i in range(dim)])
        # Fractal scaling factors
        self.scale_factors = np.array([1.0 + 0.5 * np.cos(0.7 * i) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian mixture component with varying means and stds
        f1 = 0.0
        for i in range(self.dim):
            mean = self.gauss_means[i]
            std = self.gauss_stds[i]
            f1 += np.exp(-0.5 * ((x_norm[i] - mean) / std)**2) / (std * np.sqrt(2 * np.pi))
        
        # Fractal periodic component with varying dimensions and scales
        f2 = 0.0
        for i in range(self.dim):
            scale = self.scale_factors[i]
            fractal_dim = self.fractal_dims[i]
            period = 2.0 + 1.5 * np.sin(0.4 * i)
            f2 += scale * np.sin(period * x_norm[i]) * np.abs(x_norm[i])**fractal_dim
        
        # Multi-scale harmonic component with exponentially decaying amplitudes
        f3 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.cos(0.6 * i)
            freq = 3.0 + 2.0 * np.sin(0.8 * i)
            decay = 0.1 + 0.05 * np.sin(0.9 * i)
            f3 += amp * np.sin(freq * x_norm[i]) * np.exp(-decay * np.abs(x_norm[i]))
        
        # Asymmetric polynomial with fractal-like exponents
        f4 = 0.0
        for i in range(self.dim):
            exp_base = 2.0 + 1.2 * np.sin(0.7 * i)
            exp_var = 0.5 * np.cos(0.8 * i)
            exp = exp_base + exp_var
            asymmetry = 1.0 + 0.3 * np.sin(1.1 * i)
            f4 += asymmetry * (x_norm[i]**exp) * (1.0 + 0.2 * np.cos(2.0 * x_norm[i]))
        
        # Combined with dynamic weights
        weights = [0.2 + 0.03 * np.sin(0.5 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4