import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(10 * r) * np.exp(-0.5 * r**2) + 0.1 * np.sin(50 * r)
        
        # Sinusoidal waves with varying frequencies and amplitudes
        wave_sum = 0.0
        for i in range(self.dim):
            wave_sum += np.sin((i + 1) * x_norm[i] * np.pi) * np.cos((i + 1) * x_norm[i] * np.pi / 2)
        
        # Polynomial chaos component with cross-dimensional interactions
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += x_norm[i]**4 + 0.5 * x_norm[i]**3 + 0.2 * x_norm[i]**2
        
        # Cross-dimensional coupling with chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j] * np.pi) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
                cross_coupling += coupling
        
        # Radial basis function component with chaotic scaling
        rbf_sum = 0.0
        for i in range(self.dim):
            rbf_sum += np.exp(-0.5 * (x_norm[i] - 0.5)**2) * np.sin(10 * x_norm[i])
        
        # Chaotic modulation using logistic map
        logistic_mod = 0.0
        for i in range(self.dim):
            logistic_input = 3.8 * (x_norm[i] + 0.2) % 1.0
            logistic_mod += np.sin(logistic_input * 8 * np.pi) * np.cos(x_norm[i] * 4 * np.pi)
        
        # Multimodal component with polynomial interactions and sinusoidal coupling
        multimodal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multimodal += (x_norm[i]**3 + x_norm[j]**3) * np.sin(2 * x_norm[i] * x_norm[j]) * np.cos(3 * x_norm[i] * x_norm[j])
        
        # Combine all components with adaptive weights
        return (0.3 * radial + 0.25 * wave_sum + 0.2 * poly_sum + 0.15 * cross_coupling + 
                0.1 * rbf_sum + 0.05 * logistic_mod + 0.1 * multimodal)