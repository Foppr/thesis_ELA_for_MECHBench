import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Fractal-like component with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            # Use a fractal-like function with multiple scales
            scale = 2.0**(i % 4 + 1)
            fractal += 0.5 * np.sin(scale * np.pi * x_normalized[i]) * np.cos(scale * np.pi * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Asymmetric hill-climbing basins
        asym_hill = 0.0
        for i in range(self.dim):
            # Create asymmetric attraction towards different regions
            if x_normalized[i] < 0:
                asym_hill += 0.3 * np.exp(-0.5 * (x_normalized[i] + 0.5)**2) * np.sin(10 * np.pi * x_normalized[i])
            else:
                asym_hill += 0.3 * np.exp(-0.5 * (x_normalized[i] - 0.5)**2) * np.cos(10 * np.pi * x_normalized[i])
        
        # Gradient-based attraction-repulsion mechanism
        gradient_attraction = 0.0
        for i in range(self.dim):
            # Simulate gradient-based attraction to nearby local minima
            dist_to_min = np.abs(x_normalized[i] - 0.3)
            dist_to_max = np.abs(x_normalized[i] + 0.3)
            gradient_attraction += 0.4 * (np.exp(-dist_to_min**2) - np.exp(-dist_to_max**2))
        
        # Multi-scale oscillatory component with varying amplitudes
        multi_osc = 0.0
        for i in range(self.dim):
            freq = 3.0**(i % 5 + 1)
            amp = 1.0 + 0.5 * np.sin(i * 0.5)
            multi_osc += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Cross-dimensional interaction with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += 0.25 * np.exp(-2.0 * (x_normalized[i]**2 + x_normalized[j]**2)) * np.sin(25 * np.pi * (x_normalized[i] + x_normalized[j]))
        
        # Novel penalty term with fractal-like structure
        penalty = 0.0
        for i in range(self.dim):
            # Use a polynomial with fractal-like coefficients
            penalty += 0.6 * (x_normalized[i]**11 - 5 * x_normalized[i]**9 + 10 * x_normalized[i]**7 - 10 * x_normalized[i]**5 + 5 * x_normalized[i]**3 - x_normalized[i])
        
        # Add a central repulsion term with fractal scaling
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_normalized**2))
        center_repulsion = 2.5 * np.exp(-0.5 * dist_from_origin**2) * (1.0 + 0.5 * np.sin(10 * dist_from_origin))
        
        # Add a term for enhanced basin complexity
        basin_complexity = 0.0
        for i in range(self.dim):
            basin_complexity += 0.2 * np.sin(30 * np.pi * x_normalized[i]) * np.cos(25 * np.pi * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Add a new cubic interaction term with asymmetric coupling
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += 0.2 * (x_normalized[i]**3 + x_normalized[j]**3) * np.sin(15 * np.pi * (x_normalized[i] - x_normalized[j]))
        
        return quadratic + fractal + asym_hill + gradient_attraction + multi_osc + cross_interaction + penalty + center_repulsion + basin_complexity + cubic_interaction