import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # High-frequency trigonometric terms creating many local minima
        trig_term = np.sum(np.sin(35 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm))
        
        # Radial basin with exponential decay and multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial_basin = np.exp(-r**2) * (1 + 0.9 * np.sin(15 * r) * np.cos(10 * r))
        
        # Cross-dimensional coupling with chaotic interaction strength
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(12 * np.pi * (x_norm[i] - x_norm[i+1])) * np.cos(6 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Multi-scale fractal-like structure with dynamic centers and scaling
        fractal = 0.0
        for i in range(self.dim):
            scale = 6**(i // 2 + 1)
            center_shift = 0.35 * np.sin(i * np.pi / 4)
            fractal += np.sin(scale * np.pi * (x_norm[i] + center_shift)) * np.cos(scale * np.pi * (x_norm[i] - center_shift))
        
        # Dynamic conditioning based on dimensionality and chaos
        condition = 1.0 + 0.7 * (self.dim - 1) + 0.3 * np.sin(self.dim * np.pi / 6)
        
        # Add a global distortion term for increased challenge
        global_distortion = 0.9 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Add a cubic interaction term to increase solution sensitivity
        cubic_term = 0.2 * np.sum(x_norm**3)
        
        # Combine all components with appropriate scaling
        return condition * (trig_term + radial_basin + coupling + fractal + global_distortion + cubic_term)