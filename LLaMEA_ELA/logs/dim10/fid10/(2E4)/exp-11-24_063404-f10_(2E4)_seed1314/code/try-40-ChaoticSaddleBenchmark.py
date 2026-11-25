import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Exponentially decaying sinusoidal waves with chaotic frequencies
        wave_component = 0.0
        for i in range(self.dim):
            freq = 2 ** (i + 1) * (1 + 0.1 * np.sin(i * 3.14159 / 3))
            wave_component += np.exp(-0.1 * i) * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Cross-dimensional coupling with chaotic interaction weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(i * j * 0.5) * np.cos(i + j * 0.3)
                coupling += weight * (x_scaled[i]**2 + x_scaled[j]**2) * np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Saddle-point structure with multiple local minima and maxima
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_scaled[i]**4 - 2 * x_scaled[i]**2) * np.sin(5 * x_scaled[i])
        
        # Non-smooth chaotic perturbation with discontinuous gradients
        perturb = 0.0
        for i in range(self.dim):
            perturb += np.sin(100 * x_scaled[i]) * np.tanh(10 * x_scaled[i]) * np.exp(-0.5 * x_scaled[i]**2)
        
        # Asymmetric exponential decay with directional bias
        decay = 0.0
        for i in range(self.dim):
            decay += np.exp(-np.abs(x_scaled[i]) * (1 + 0.2 * np.sin(i * 2 * 3.14159 / self.dim)))
        
        # Combine all components with adaptive weights
        return (wave_component + 0.8 * coupling + 0.6 * saddle + 
                0.4 * perturb + 0.2 * decay + 0.01 * np.sum(x_scaled**8))