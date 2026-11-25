import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos with exponential modulation
        poly_chaos = np.sum((x_norm**2 + 0.1 * np.sin(10 * x_norm))**3)
        
        # Exponential gradient field with dynamic scaling
        exp_gradient = np.sum(np.exp(-np.abs(x_norm)) * np.cos(np.pi * x_norm) * (1 + 0.5 * np.sin(self.dim * x_norm)))
        
        # Multi-resolution frequency coupling with adaptive weights
        freq_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2**(i+1) * (1 + 0.1 * np.cos(j))
                freq_j = 3**(j+1) * (1 + 0.1 * np.sin(i))
                coupling = np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * np.cos(freq_i * x_norm[i] - freq_j * x_norm[j])
                freq_coupling += coupling * (i + 1) * (j + 1)
        
        # Dynamic basin scaling with fractal-like exponent modulation
        basin_scaling = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(self.dim * np.pi * x_norm)) + 
                              0.3 * np.abs(x_norm)**(2.0 + 0.4 * np.cos(self.dim * np.pi * x_norm)))
        
        # Hybrid polynomial-exponential interaction terms
        hybrid_interaction = np.sum((x_norm**4 + 0.2 * np.exp(-x_norm**2)) * np.sin(np.pi * x_norm))
        
        # Dimensionality-dependent noise with chaotic distribution
        noise_amp = 0.1 / (1 + self.dim)
        noise_freq = 2**(self.dim + 4) * (1 + 0.3 * np.cos(np.sum(x_norm**2)))
        noise = noise_amp * np.sin(noise_freq * np.pi * np.sum(x_norm)) * np.cos(np.pi * self.dim * x_norm[0])
        
        # Combine all components with dynamic weighting
        weight_poly = 1.0 + 0.2 * np.sin(self.dim * np.pi / 4)
        weight_grad = 0.8 + 0.1 * np.cos(self.dim * np.pi / 3)
        weight_freq = 0.6 + 0.2 * np.sin(self.dim * np.pi / 5)
        weight_basin = 0.9 + 0.1 * np.cos(self.dim * np.pi / 6)
        weight_hybrid = 0.7 + 0.1 * np.sin(self.dim * np.pi / 7)
        
        return (weight_poly * poly_chaos + 
                weight_grad * exp_gradient + 
                weight_freq * freq_coupling + 
                weight_basin * basin_scaling + 
                weight_hybrid * hybrid_interaction + 
                noise)