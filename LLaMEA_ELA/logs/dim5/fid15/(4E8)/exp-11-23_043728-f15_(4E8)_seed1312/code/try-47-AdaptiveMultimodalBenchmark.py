import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.conditioning_factors = np.linspace(1.0, 10.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Exponential decay component with adaptive conditioning
        exp_component = np.sum(self.conditioning_factors * np.exp(-self.conditioning_factors * np.abs(x_norm)))
        
        # Sinusoidal coupling between dimensions
        sin_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sin_coupling += np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Adaptive multimodal structure with varying frequencies
        modal_component = 0.0
        for i in range(self.dim):
            modal_component += (x_norm[i]**2) * np.sin(10 * np.pi * x_norm[i])**2 + \
                              0.5 * np.sin(5 * np.pi * x_norm[i])**4
        
        # Combine all components with a global scaling factor
        total_energy = exp_component + 0.3 * sin_coupling + modal_component
        
        # Add small noise to create ruggedness
        noise = 0.001 * np.random.rand()
        
        return total_energy + noise