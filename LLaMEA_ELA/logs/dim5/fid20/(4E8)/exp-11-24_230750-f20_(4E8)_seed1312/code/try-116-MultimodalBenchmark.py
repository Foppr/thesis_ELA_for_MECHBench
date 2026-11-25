import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-adaptive polynomial potentials with dynamic exponents
        poly_potential = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(i * 0.7)
            poly_potential += (x[i]**(2 + exp_factor) + 0.5 * x[i]**(3 + exp_factor))
        
        # Dynamic sine-cosine coupling with frequency modulation
        coupling = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.cos(i * 0.4)
            coupling += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Fractal-like geometric scaling with multi-resolution features
        fractal = 0.0
        for i in range(1, min(5, self.dim + 1)):
            scale = 3 ** (-i * 0.8)
            fractal += scale * np.sum(np.sin(scale * x) * np.cos(scale * x**2))
        
        # Non-uniform basin distribution with radial basis function modulation
        basin_mod = 0.0
        for i in range(min(3, self.dim)):
            center = 2.0 * np.sin(i * 0.6)
            width = 1.0 + 0.2 * np.cos(i * 0.5)
            basin_mod += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Emergent optima clustering with dynamic interaction terms
        cluster_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.abs(x[i] - x[j])
                cluster_interaction += dist * np.sin(0.5 * (x[i] + x[j]))
        
        # Dynamic conditioning based on input magnitude and dimensionality
        condition = 1.0 + 0.4 * np.sin(self.dim * 0.2) * np.mean(np.abs(x)) + \
                   0.2 * np.cos(self.dim * 0.3) * np.std(x)
        
        # Combined function with noise and scaling
        base_value = condition * (np.sum(x**4) + 0.3 * np.sum(x**3) + 0.1 * np.sum(x**2))
        
        # Add adaptive noise component
        noise = 0.03 * np.random.rand() * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        return base_value + poly_potential + coupling + fractal + basin_mod + cluster_interaction + noise