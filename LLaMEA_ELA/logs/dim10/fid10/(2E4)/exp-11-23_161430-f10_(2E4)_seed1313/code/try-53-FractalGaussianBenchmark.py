import numpy as np

class FractalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters for multi-scale structure
        self.fractal_dims = 1.2 + 0.8 * np.sin(np.arange(dim) * 0.3)
        self.gauss_components = max(3, dim // 3)
        # Gaussian mixture centers and covariances
        self.centers = np.random.uniform(-4.0, 4.0, (self.gauss_components, dim))
        self.covariances = [np.diag(np.exp(np.random.normal(0, 0.5, dim))) for _ in range(self.gauss_components)]
        # Chaos-based perturbation parameters
        self.chaos_params = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**4 - 6*x[i]**2 + 9) * np.sin(0.5 * x[i]) * np.exp(-0.1 * i)
        
        # Gaussian mixture model
        gauss_sum = 0.0
        for i in range(self.gauss_components):
            diff = x - self.centers[i]
            inv_cov = np.linalg.inv(self.covariances[i])
            det_cov = np.linalg.det(self.covariances[i])
            gauss_sum += np.exp(-0.5 * diff @ inv_cov @ diff) / np.sqrt(det_cov)
        
        # Fractal perturbation using chaotic map
        fractal_pert = 0.0
        for i in range(self.dim):
            chaos_val = self.chaos_params[i] * (x[i] % 1.0) * (1 - x[i] % 1.0)
            fractal_pert += chaos_val * np.sin(2 * np.pi * x[i]) * np.cos(0.3 * x[i])
        
        # Cross-dimensional coupling with varying interaction strength
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            weight = 0.5 + 0.5 * np.sin(0.2 * x[i] + 0.3 * x[j]) * np.cos(0.4 * x[k])
            cross_coupling += weight * np.sin(3.1 * x[i]) * np.cos(2.7 * x[j]) * np.tanh(x[k])
        
        # Multi-scale sinusoidal modulation
        scale_mod = 0.0
        for i in range(self.dim):
            scale_mod += np.sin(10 * x[i]) * np.cos(7 * x[i]) * (1 + 0.2 * np.sin(i * 0.5))
        
        # Combine all components with adaptive weights
        result = 0.3 * np.sum(x**2) + 0.25 * poly_chaos + 0.2 * gauss_sum + \
                 0.15 * fractal_pert + 0.1 * cross_coupling + 0.05 * scale_mod
        
        return result