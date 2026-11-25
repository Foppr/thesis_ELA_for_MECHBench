import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic spiral radial component with angular dependence
        r = np.sqrt(np.sum(x**2))
        if r == 0:
            r = 1e-10
        theta = np.arctan2(x[1], x[0]) if self.dim >= 2 else 0.0
        spiral_term = r * np.exp(-0.05 * r) * np.sin(3.0 * theta + 0.5 * r)
        
        # Self-similar fractal pattern using recursive scaling
        fractal_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply multiple scales of sinusoidal modulation
            scale1 = np.sin(2.0 * xi) * np.cos(1.5 * xi)
            scale2 = np.sin(4.0 * xi) * np.cos(3.0 * xi)
            scale3 = np.sin(6.0 * xi) * np.cos(5.0 * xi)
            fractal_sum += (scale1 + 0.5 * scale2 + 0.3 * scale3) ** 2
        
        # Discrete symmetry operations (reflection and rotation)
        sym_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i < len(x) and j < len(x):
                    sym_term += (x[i] * x[j]) * np.sin(2.0 * (x[i] + x[j]))
        
        # Non-smooth component using absolute value and step functions
        smoothness_break = np.sum(np.abs(x) ** 1.3) * np.exp(-0.1 * r)
        
        # Combine all components with adaptive weights based on dimensionality
        weight_spiral = 0.35
        weight_fractal = 0.30
        weight_sym = 0.20
        weight_smooth = 0.15
        
        result = weight_spiral * spiral_term + weight_fractal * fractal_sum + \
                 weight_sym * sym_term + weight_smooth * smoothness_break
        
        # Add small chaotic perturbation for increased complexity
        chaos = 0.005 * np.sum(np.sin(13.0 * x) * np.cos(7.0 * x))
        
        return result + chaos