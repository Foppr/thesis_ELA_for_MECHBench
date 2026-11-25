import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for stability
        self.r_params = np.linspace(3.5, 4.0, dim) if dim > 1 else np.array([3.9])
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component with varying r values
        chaotic = 0.0
        for i in range(min(5, self.dim)):  # Limit iterations for stability
            if i == 0:
                x_prev = x_scaled[i] if self.dim > 1 else x_scaled[0]
            else:
                x_prev = x_scaled[i-1] if i < len(x_scaled) else x_scaled[-1]
            chaotic += self.r_params[min(i, len(self.r_params)-1)] * x_prev * (1 - x_prev)
        
        # Radial basis function with fractal-like scaling
        rbf = 0.0
        centers = np.linspace(-1, 1, min(8, self.dim))
        for i in range(len(centers)):
            if i < len(x_scaled):
                rbf += np.exp(-5.0 * (x_scaled[i] - centers[i])**2) * np.sin(10.0 * x_scaled[i])
        
        # Fractal interference pattern with multi-scale sinusoids
        fractal = 0.0
        for i in range(self.dim):
            if i < len(x_scaled):
                fractal += (np.sin(2**(i+1) * x_scaled[i]) + 
                           np.cos(3**(i+1) * x_scaled[i]) + 
                           0.5 * np.sin(5**(i+1) * x_scaled[i]))
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            if i < len(x_scaled) - 1:
                coupling += np.exp(-2.0 * (x_scaled[i]**2 + x_scaled[i+1]**2)) * \
                           np.sin(5.0 * (x_scaled[i] + x_scaled[i+1]))
        
        # Asymmetric penalty with cubic terms
        penalty = np.sum(0.3 * np.abs(x_scaled)**3 + 0.7 * x_scaled**4)
        
        # Combine all components with dynamic weights
        return 0.25 * chaotic + 0.35 * rbf + 0.2 * fractal + 0.15 * coupling + 0.05 * penalty + 2.1