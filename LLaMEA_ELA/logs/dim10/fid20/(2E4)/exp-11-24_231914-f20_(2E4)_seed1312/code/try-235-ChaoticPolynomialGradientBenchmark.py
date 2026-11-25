import numpy as np

class ChaoticPolynomialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters
        self.tent_r = np.random.uniform(1.5, 3.0, size=dim)
        self.tent_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Polynomial interpolation parameters
        self.poly_degree = np.random.randint(2, 6, size=dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=(dim, 6))
        # Gradient-based terrain modulation
        self.gradient_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.gradient_direction = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Multi-scale harmonic components
        self.harmonic_freq = np.random.uniform(0.5, 5.0, size=dim)
        self.harmonic_amp = np.random.uniform(0.1, 2.0, size=dim)
        # Basin-like regions with chaotic dynamics
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=5)
        self.basin_radii = np.random.uniform(0.5, 2.0, size=5)
        self.basin_depths = np.random.uniform(1.0, 5.0, size=5)
        # Dynamic scaling factors
        self.scale_factors = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        tent_component = 0.0
        for i in range(self.dim):
            # Generate chaotic sequence
            tent_val = self.tent_x0[i]
            for _ in range(10):  # Iterate to stabilize
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            tent_component += tent_val
            
        # Polynomial interpolation component
        poly_component = 0.0
        for i in range(self.dim):
            x_scaled = x[i] / 5.0  # Normalize to [-1, 1]
            poly_val = 0.0
            for j in range(self.poly_degree[i]):
                poly_val += self.poly_coeffs[i, j] * (x_scaled ** j)
            poly_component += poly_val
            
        # Gradient-based terrain modulation
        grad_component = 0.0
        for i in range(self.dim):
            grad_val = 0.0
            for j in range(self.dim):
                grad_val += self.gradient_direction[i, j] * (x[j] - self.tent_x0[j])
            grad_component += self.gradient_magnitude[i] * grad_val
            
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_val = self.harmonic_amp[i] * np.sin(self.harmonic_freq[i] * x[i])
            harmonic_component += harmonic_val
            
        # Basin-like regions with chaotic dynamics
        basin_component = 0.0
        for i in range(5):
            min_dist = float('inf')
            for j in range(self.dim):
                dist = np.abs(x[j] - self.basin_centers[i])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[i]:
                basin_component += self.basin_depths[i] * (1 - min_dist / self.basin_radii[i])
                
        # Combined fitness function with balanced weights
        return (1.0 * tent_component + 
                1.2 * poly_component + 
                0.9 * grad_component + 
                1.1 * harmonic_component + 
                0.8 * basin_component)