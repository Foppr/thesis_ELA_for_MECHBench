import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave modulation component with time-varying frequency and amplitude
        sine_mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            amp = 1.0 + 0.5 * np.tanh(0.4 * x[i])
            sine_mod += amp * np.sin(freq * x[i]) * np.cos(2.0 * x[i])
        
        # Dynamic multi-peak Gaussian mixture with time-varying means, variances, and skewness
        gaussian_mixture = 0.0
        for i in range(self.dim):
            mean = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.2 + 0.6 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            skew = 1.0 + 0.3 * np.sin(0.7 * x[i])
            gaussian_mixture += skew * np.exp(-0.5 * ((x[i] - mean) / variance)**2)
        
        # Fractal-like recursive saddle structure with multi-scale coupling
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                scale = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.6 * x[i+1])
                saddle += scale * (x[i]**3 - x[i+1]**3) * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i+1])
        
        # Recursive fractal component with nested logarithmic spirals and multi-scale oscillations
        fbm = 0.0
        for i in range(self.dim):
            spiral = np.exp(-0.3 * np.abs(x[i])) * np.sin(1.2 * x[i]) * np.cos(1.1 * x[i])
            fbm += spiral
        
        # Cross-dimensional polynomial coupling with dynamic interaction weights and multi-scale terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin(0.4 * (i - j)) * np.cos(0.3 * (i + j))
                coupling += weight * (x[i]**2 * x[j]**2) * np.sin(0.3 * (x[i] + x[j]))
        
        # Boundary penalty and dimension scaling with enhanced complexity factors
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 3.0 * (np.abs(x[i]) > 4.8)
        
        # Combined function with dynamic weighting based on dimension, fractal complexity, and interaction strength
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.2 * np.sin(0.6 * self.dim)
        complexity_factor = 1.0 + 0.4 * np.cos(0.4 * self.dim)
        
        return (0.3 * sine_mod + 0.25 * gaussian_mixture + 0.2 * saddle + 
                0.15 * fbm + 0.05 * coupling + 0.05 * boundary_penalty) * dim_factor * complexity_factor