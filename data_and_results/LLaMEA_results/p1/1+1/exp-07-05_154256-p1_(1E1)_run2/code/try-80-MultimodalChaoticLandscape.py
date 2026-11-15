import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_param = 4.0
        self.wave_freq = 2.0 * np.pi
        self.poly_degree = 4
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component
        r = np.sqrt(np.sum(x**2))
        radial_poly = 0.5 * r**self.poly_degree
        
        # Sinusoidal wave component with varying frequencies
        wave_component = 0
        for i in range(self.dim):
            wave_component += np.sin(self.wave_freq * x[i]) * np.cos(self.wave_freq * x[i] * 0.5)
        
        # Chaotic perturbation using logistic map
        chaotic_perturbation = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_perturbation += np.sin(self.chaos_param * x[i] * x[i+1]) * np.cos(x[i])
        
        # Cross-term interaction with exponential decay
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(3 * x[i] * x[j])
        
        # Multi-scale oscillation with different frequencies
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += np.sin(5 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Radial cosine modulation
        radial_cos = np.cos(2 * r) * np.exp(-0.2 * r**2)
        
        # Combine all components
        return (1.2 * radial_poly + 
                1.8 * wave_component + 
                0.8 * chaotic_perturbation + 
                0.6 * cross_term + 
                1.0 * multi_scale + 
                0.4 * radial_cos)