import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay interactions with chaotic modulation
        decay_interaction = np.sum(np.exp(-np.abs(x_norm)) * np.cos(np.pi * x_norm**2))
        
        # Chaotic gradient components with periodic boundary effects
        grad_components = 0.0
        for i in range(self.dim):
            # Periodic boundary effect using sine and cosine
            boundary_effect = np.sin(np.pi * x_norm[i]) + np.cos(2 * np.pi * x_norm[i])
            # Chaotic modulation based on dimension index
            chaotic_mod = np.sin(2**(i+1) * np.pi * x_norm[i]) * np.cos(3**(i+1) * np.pi * x_norm[i])
            grad_components += boundary_effect * chaotic_mod
        
        # Multi-scale periodic potential with varying frequencies
        periodic_potential = 0.0
        for i in range(self.dim):
            freq = 2**(i+1) + np.sin(i * np.pi / self.dim)
            periodic_potential += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
        
        # Fractal-like exponential basin with dimension-dependent scaling
        fractal_basin = np.sum(np.exp(-np.abs(x_norm)**(1.0 + 0.5 * np.sin(self.dim * x_norm))) + 
                              0.2 * np.exp(-np.abs(x_norm)**(1.5 + 0.3 * np.cos(self.dim * x_norm))))
        
        # Dynamic noise component with time-like dimension scaling
        noise_amp = 0.05 / (1 + self.dim)
        noise_freq = 10**(self.dim % 5 + 1)
        dynamic_noise = noise_amp * np.sin(noise_freq * np.sum(x_norm**2))
        
        # Combine all components with dimensionality-dependent weights
        weight_decay = 1.0 + 0.1 * np.log(self.dim + 1)
        weight_grad = 0.8 + 0.2 * np.cos(self.dim * np.pi / 4)
        weight_periodic = 0.6 + 0.4 * np.sin(self.dim * np.pi / 3)
        weight_fractal = 0.5 + 0.3 * np.cos(self.dim * np.pi / 5)
        
        return (weight_decay * decay_interaction + 
                weight_grad * grad_components + 
                weight_periodic * periodic_potential + 
                weight_fractal * fractal_basin + 
                dynamic_noise)