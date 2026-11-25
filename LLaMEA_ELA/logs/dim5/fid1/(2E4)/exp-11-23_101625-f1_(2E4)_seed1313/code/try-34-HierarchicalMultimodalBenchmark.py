import numpy as np

class HierarchicalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        result = 0.1 * np.sum(x**2)
        
        # Hierarchical sinusoidal structure with cascading frequencies
        for i in range(self.dim):
            # Adaptive frequency based on dimension index
            freq = 2**(i % 5 + 1) * (1 + 0.3 * np.cos(i * 0.5))
            # Cascading amplitude modulation
            amp = 1.0 + 0.5 * np.sin(i * 0.7)
            result += amp * np.sin(freq * x[i]) * np.cos(0.5 * freq * x[i])
            
        # Ridge-based structure with varying curvature
        for i in range(self.dim):
            # Multi-scale ridge pattern
            ridge_freq = 3**(i % 3 + 1)
            result += 0.7 * np.sin(ridge_freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Nested valley structure with scale-invariant properties
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Interaction strength decays with distance
                strength = 1.0 / (1 + abs(i-j))
                result += strength * np.cos(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Multi-scale harmonic modulation
        scale_factors = [1, 2, 3, 4]
        for scale in scale_factors:
            if self.dim >= scale:
                sub_x = x[:scale]
                # Harmonic combination with varying weights
                weight_sum = np.sum(np.arange(1, scale+1) * sub_x**2)
                result += 0.4 * np.sin(weight_sum / scale) * np.cos(np.sum(sub_x) / scale)
                
        # Asymmetric curvature field with hierarchical critical points
        for i in range(min(5, self.dim)):
            # Different scaling for different dimensions
            scale = 2**(i % 3 + 1)
            result += 0.6 * (x[i]**4 - scale * x[i]**2) * np.exp(-0.05 * abs(x[i]))
            
        # Global scaling and noise modulation
        global_factor = 1.0 + 0.2 * np.sin(np.sum(x**3) * 0.1)
        result *= global_factor
        
        return result