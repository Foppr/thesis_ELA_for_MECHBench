import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic cosine oscillatory component with dynamic frequency modulation
        cos_osc = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.4 * np.cos(0.5 * x[i]) + 0.3 * np.sin(0.7 * x[i])
            mod = 1.0 + 0.2 * np.tanh(0.6 * x[i])
            cos_osc += mod * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Asymmetric Gaussian mixture with dynamic centers and varying weights
        gaussian_mixture = 0.0
        for i in range(self.dim):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance_pos = 0.2 + 0.5 * np.cos(0.6 * x[i])
            variance_neg = 0.1 + 0.4 * np.sin(0.8 * x[i])
            variance = np.where(x[i] >= center, variance_pos, variance_neg)
            gaussian_mixture += 0.4 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Coupled saddle-point structure with time-varying coupling coefficients
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coef = 0.6 + 0.4 * np.cos(0.5 * x[i]) * np.sin(0.4 * x[i+1])
                saddle += coef * (x[i]**2 - x[i+1]**2) * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i+1])
        
        # Fractal-inspired component with multi-scale logarithmic spiral
        fbm = 0.0
        for i in range(self.dim):
            spiral = np.exp(-0.3 * np.abs(x[i])) * np.cos(0.9 * x[i]) * np.sin(0.7 * x[i])
            fbm += spiral
        
        # Cross-dimensional coupling with higher-order polynomial interactions and adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.9 + 0.1 * np.cos(0.4 * (i - j))
                coupling += weight * (x[i] * x[j])**4 * np.sin(0.3 * (x[i] + x[j]))
        
        # Boundary penalty and dimension scaling for improved discrimination
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 1.5 * (np.abs(x[i]) > 4.7)
        
        # Combined function with enhanced adaptive weighting
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.15 * np.cos(0.6 * self.dim)
        complexity_factor = 1.0 + 0.25 * np.sin(0.4 * self.dim)
        
        return (0.3 * cos_osc + 0.35 * gaussian_mixture + 0.2 * saddle + 
                0.1 * fbm + 0.05 * coupling + 0.05 * boundary_penalty) * dim_factor * complexity_factor