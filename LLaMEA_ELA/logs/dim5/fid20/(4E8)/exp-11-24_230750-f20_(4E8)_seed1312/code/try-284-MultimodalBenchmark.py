import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic quaternion-inspired oscillations with dynamic phase modulation
        quat_osc = 0.0
        for i in range(self.dim):
            phase = 1.0 + 0.5 * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            amp = 1.0 + 0.3 * np.tanh(0.5 * x[i])
            freq = 2.0 + 1.2 * np.sin(0.4 * x[i])
            quat_osc += amp * np.sin(freq * x[i] + phase) * np.cos(1.5 * x[i])
        
        # Dynamic multi-peak Gaussian distributions with time-varying skewness and kurtosis
        gaussian_mixture = 0.0
        for i in range(self.dim):
            mean = -4.5 + 9.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            variance = 0.1 + 0.7 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            skew = 1.0 + 0.4 * np.sin(0.8 * x[i])
            kurt = 1.0 + 0.2 * np.cos(0.6 * x[i])
            gaussian_mixture += skew * np.exp(-0.5 * ((x[i] - mean) / variance)**2) * (1.0 + 0.1 * kurt * np.sin(1.3 * x[i]))
        
        # Fractal-like recursive saddle structures with multi-scale coupling and dynamic dimensionality
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                scale = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.7 * x[i+1])
                dim_scale = 1.0 + 0.3 * np.sin(0.4 * self.dim)
                saddle += scale * (x[i]**3 - x[i+1]**3) * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i+1]) * dim_scale
        
        # Adaptive neural-network-like coupling with dynamic weights and recursive feedback
        nn_coupling = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[i])
            feedback = 0.3 * np.tanh(x[i])
            nn_coupling += weight * (x[i]**2) * np.sin(0.7 * x[i] + feedback)
        
        # Cross-dimensional polynomial couplings with chaotic interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_weight = 1.0 + 0.6 * np.sin(0.3 * (i - j)) * np.cos(0.5 * (i + j))
                coupling += chaotic_weight * (x[i]**2 * x[j]**2) * np.sin(0.4 * (x[i] + x[j])) * np.cos(0.2 * (x[i] - x[j]))
        
        # Boundary penalty with enhanced complexity and dimension-dependent scaling
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 2.5 * (np.abs(x[i]) > 4.7) + 0.5 * np.sin(1.2 * x[i])
        
        # Combined function with enhanced dynamic weighting and fractal complexity factors
        dim_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.3 * np.sin(0.7 * self.dim)
        complexity_factor = 1.0 + 0.5 * np.cos(0.5 * self.dim) + 0.2 * np.tanh(0.3 * self.dim)
        
        return (0.25 * quat_osc + 0.3 * gaussian_mixture + 0.25 * saddle + 
                0.1 * nn_coupling + 0.08 * coupling + 0.07 * boundary_penalty) * dim_factor * complexity_factor