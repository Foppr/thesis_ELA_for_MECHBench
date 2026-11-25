import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent oscillatory component with dynamic frequency
        tanh_osc = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.tanh(0.3 * x[i])
            tanh_osc += np.tanh(freq * x[i]) * np.sin(2.0 * x[i])
        
        # Multi-resolution Gaussian mixture with varying covariances
        gaussian_mixture = 0.0
        centers = [np.linspace(-4, 4, 5)] * self.dim
        for i in range(self.dim):
            for j in range(5):
                center = centers[i][j]
                variance = 0.5 + 0.3 * np.sin(0.5 * x[i])
                gaussian_mixture += 0.2 * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Dynamic saddle-point structure with dimensionally coupled terms
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                saddle += (x[i]**2 - x[i+1]**2) * np.cos(0.5 * x[i]) * np.sin(0.3 * x[i+1])
        
        # Fractional Brownian motion inspired fractal component
        fbm = 0.0
        for i in range(self.dim):
            fbm += np.sin(x[i]) * np.cos(0.7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with polynomial interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j])**2 * np.sin(0.1 * (x[i] + x[j]))
        
        # Combined function with adaptive weighting based on dimension
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        return (0.3 * tanh_osc + 0.25 * gaussian_mixture + 0.2 * saddle + 
                0.15 * fbm + 0.1 * coupling) * dim_factor