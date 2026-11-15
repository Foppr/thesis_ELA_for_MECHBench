import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with condition number scaling
        base = np.sum(x_norm**2)
        
        # Adaptive sinusoidal components with dimensionality-dependent frequencies
        adaptive_sine = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.5 * np.sin(i * 0.3))
            amp = 1.5 + 0.8 * np.cos(i * 0.4)
            adaptive_sine += amp * np.sin(freq * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Cross-dimensional chaotic interaction with dynamic coupling
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(20 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
                distance = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.01)
                chaotic_interaction += 0.5 * coupling * np.exp(-2.0 * distance)
        
        # Multi-scale penalty with varying exponents and local minima
        penalty = 0.0
        for i in range(self.dim):
            exponent = 2 + 2 * np.sin(i * 0.5)
            penalty += 0.4 * (x_norm[i]**exponent - 2 * x_norm[i]**(exponent/2) + 1)
        
        # Dynamic global minimum attraction with variable strength
        global_attraction = 0.0
        for i in range(self.dim):
            strength = 1.0 + 0.3 * np.sin(i * 0.7)
            global_attraction += strength * np.sin(10 * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Dimensionality-adaptive oscillatory term
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 15 + 5 * np.sin(i * 0.2)
            oscillatory += 0.3 * np.sin(freq * x_norm[i]) * np.cos(12 * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Variable amplitude multi-modal component
        multimodal = 0.0
        for i in range(self.dim):
            amp = 2.0 + 1.2 * np.sin(i * 0.6)
            multimodal += amp * np.sin(8 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Exponential repulsion from center with dynamic radius
        center_repulsion = 0.0
        dist = np.sqrt(np.sum(x_norm**2))
        radius = 1.0 + 0.5 * np.sin(self.dim * 0.3)
        center_repulsion = 2.0 * np.exp(-dist**2 / (2 * radius**2)) * (1.0 + 0.6 * np.sin(10 * dist))
        
        # Asymmetric penalty with directional dependence
        asymmetric = 0.0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.4 * np.sin(i * 0.5)
            asymmetric += asym_factor * (x_norm[i]**4 - 2 * x_norm[i]**2 + 1) * np.exp(-0.3 * np.abs(x_norm[i]))
        
        # Add all components together
        return base + adaptive_sine + chaotic_interaction + penalty + global_attraction + oscillatory + multimodal + center_repulsion + asymmetric