import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with sinusoidal modulation and chaotic perturbation
        r = np.sqrt(np.sum(x_norm**2))
        radial_component = np.exp(-0.5 * r**2) * (1 + 0.3 * np.sin(10 * r * np.pi))
        
        # Multi-sinusoidal wave component with varying frequencies and amplitudes
        wave_component = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 1.0 / (i + 1)
            wave_component += amp * np.sin(freq * x_norm[i] * np.pi) * np.cos(freq * x_norm[i] * np.pi)
        
        # Radial basis function component with chaotic modulation
        rbf_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                rbf_component += np.exp(-0.5 * dist**2) * np.sin(5 * dist * np.pi)
        
        # Chaotic perturbation using logistic map with time-varying parameter
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            logistic_input = 3.8 * (x_norm[i] + 0.2) % 1.0
            chaotic_perturbation += np.sin(logistic_input * 15 * np.pi) * np.cos(x_norm[i] * 8 * np.pi)
        
        # Cross-dimensional polynomial interaction with trigonometric coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + x_norm[j]**3) * np.sin(3 * x_norm[i] * x_norm[j]) * np.cos(2 * x_norm[i] * x_norm[j])
        
        # Multi-modal component with multiple peaks and varying heights
        multimodal_component = 0.0
        for i in range(self.dim):
            multimodal_component += np.sin(4 * x_norm[i] * np.pi) * np.cos(2 * x_norm[i] * np.pi) * np.exp(-0.2 * x_norm[i]**2)
        
        # Combined fitness function with adaptive weights
        return radial_component + 0.5 * wave_component + 0.3 * rbf_component + 0.2 * chaotic_perturbation + 0.25 * poly_interaction + 0.15 * multimodal_component