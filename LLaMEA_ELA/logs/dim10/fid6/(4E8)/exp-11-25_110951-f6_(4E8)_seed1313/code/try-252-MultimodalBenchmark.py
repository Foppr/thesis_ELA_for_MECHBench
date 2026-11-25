import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base multimodal potential with exponential scaling and chaotic modulation
        result = 0.0
        for i in range(self.dim):
            # Chaotic modulation using multiple sine waves for increased complexity
            chaotic_factor = 1.0 + 0.4 * np.sin(5 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(7 * x_norm[i])
            # Exponential potential with sinusoidal modulation
            exp_potential = np.exp(0.5 * x_norm[i]**2) * (1.0 + 0.3 * np.sin(11 * x_norm[i]))
            result += chaotic_factor * exp_potential
        
        # Multi-scale sinusoidal modulations with asymmetric elliptic components
        elliptic_term = 0.0
        for i in range(self.dim):
            # Asymmetric elliptic structure with multi-scale sinusoidal modulation
            scale_factor = 1.0 + 0.25 * np.sin(2 * x_norm[i]) + 0.15 * np.cos(4 * x_norm[i])
            elliptic_term += scale_factor * (x_norm[i]**2) * (1.0 + 0.3 * np.sin(9 * x_norm[i]))
        
        # Cross-dimensional interaction with fractal-like coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction using exponential and trigonometric components
                interaction = np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2)) * \
                             np.sin(5 * (x_norm[i] + x_norm[j])) * \
                             np.cos(3 * (x_norm[i] - x_norm[j]))
                coupling += interaction
        
        # High-frequency oscillatory component with adaptive amplitude
        oscillatory = 0.0
        for i in range(self.dim):
            # Multi-scale frequency components with dynamic amplitude modulation
            freq1 = 8 + 3 * np.sin(2 * x_norm[i])
            freq2 = 12 + 4 * np.cos(3 * x_norm[i])
            oscillatory += np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i])
        
        # Dynamic weighting based on solution proximity to optima
        distance_from_origin = np.sum(x_norm**2)
        dynamic_weight = 1.0 + 0.5 * np.exp(-0.2 * distance_from_origin)
        
        # Asymmetric elliptic basin structure with exponential potentials
        basin_term = 0.0
        for i in range(self.dim):
            # Asymmetric elliptic basin with exponential scaling
            basin_term += (x_norm[i]**2) * np.exp(-0.5 * x_norm[i]**2) * (1.0 + 0.4 * np.sin(6 * x_norm[i]))
        
        # Combine all components with optimized weights
        return dynamic_weight * (0.8 * result + 0.3 * elliptic_term + 0.4 * coupling + 0.25 * oscillatory + 0.35 * basin_term)