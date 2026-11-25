import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic hyperbolic tangent oscillatory component with asymmetric skewness
        tanh_osc = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.tanh(0.4 * x[i]) + 0.2 * np.sin(0.6 * x[i])
            skew = 1.0 + 0.4 * np.cos(0.5 * x[i])
            tanh_osc += skew * np.tanh(freq * x[i]) * np.sin(3.0 * x[i])
        
        # Adaptive Gaussian mixture with asymmetric variances and skewed peaks
        gaussian_mixture = 0.0
        for i in range(self.dim):
            center = -3.0 + 6.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance_pos = 0.3 + 0.4 * np.sin(0.7 * x[i])
            variance_neg = 0.2 + 0.3 * np.cos(0.8 * x[i])
            variance = np.where(x[i] >= center, variance_pos, variance_neg)
            gaussian_mixture += 0.3 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Dynamic saddle-point structure with coupled terms and time-varying coefficients
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coef = 0.5 + 0.3 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i+1])
                saddle += coef * (x[i]**2 - x[i+1]**2) * np.cos(0.6 * x[i]) * np.sin(0.4 * x[i+1])
        
        # Fractal-inspired component with logarithmic spiral structure
        fbm = 0.0
        for i in range(self.dim):
            spiral = np.exp(-0.2 * np.abs(x[i])) * np.sin(0.8 * x[i]) * np.cos(0.9 * x[i])
            fbm += spiral
        
        # Cross-dimensional coupling with polynomial interaction and dimensionally varying weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 + 0.2 * np.sin(0.3 * (i + j))
                coupling += weight * (x[i] * x[j])**3 * np.cos(0.2 * (x[i] + x[j]))
        
        # Add boundary penalty and dimension scaling for enhanced discrimination
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 2.0 * (np.abs(x[i]) > 4.5)
        
        # Combined function with adaptive weighting based on dimension and complexity factors
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(0.5 * self.dim)
        complexity_factor = 1.0 + 0.3 * np.cos(0.3 * self.dim)
        
        return (0.25 * tanh_osc + 0.3 * gaussian_mixture + 0.25 * saddle + 
                0.15 * fbm + 0.05 * coupling + 0.1 * boundary_penalty) * dim_factor * complexity_factor