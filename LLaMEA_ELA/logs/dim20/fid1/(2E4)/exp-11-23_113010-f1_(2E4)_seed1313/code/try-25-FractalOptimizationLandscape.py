import numpy as np

class FractalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component using recursive diamond-square like pattern
        fractal = 0.0
        for i in range(self.dim):
            # Multi-scale fractal with varying exponents
            scale = 2 ** (i % 3)
            fractal += np.sin(scale * np.pi * x_norm[i]) * np.cos(scale * np.pi * x_norm[i])
        
        # Gradient-dependent curvature with implicit constraints
        curvature = 0.0
        for i in range(self.dim):
            # Varying curvature based on gradient magnitude
            grad_mag = abs(x_norm[i])
            curvature += (grad_mag ** 3) * np.sin(5 * np.pi * x_norm[i]) + \
                        (grad_mag ** 2) * np.cos(7 * np.pi * x_norm[i])
        
        # Self-similar geometric patterns with varying dimensions
        geo_pattern = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimension interaction
                geo_pattern += np.exp(-((x_norm[i] - x_norm[j])**2)) * \
                              np.sin(np.pi * (x_norm[i] + x_norm[j]) * (i + j + 1))
        
        # Multi-scale noise with varying amplitudes
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(10 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i])
        
        # Asymmetric scaling based on dimension parity
        asymmetry = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                asymmetry += x_norm[i] ** 4
            else:
                asymmetry += x_norm[i] ** 5
        
        # Combine all components with varying weights and scaling factors
        return (1.2 * fractal + 0.8 * curvature + 0.6 * geo_pattern + 
                0.3 * noise + 0.4 * asymmetry + 0.01 * np.random.random())