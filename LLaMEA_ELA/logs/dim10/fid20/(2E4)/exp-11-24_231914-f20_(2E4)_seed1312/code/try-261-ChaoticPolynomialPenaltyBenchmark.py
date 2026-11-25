import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters with higher dimensionality influence
        self.tent_r = np.random.uniform(1.5, 3.9, size=dim)
        self.tent_x0 = np.random.uniform(0.01, 0.99, size=dim)
        # Polynomial chaos expansion parameters with higher order terms
        self.poly_degree = np.random.randint(4, 10, size=dim)
        self.poly_coeffs = np.random.uniform(-5.0, 5.0, size=(dim, 12))
        # Dynamic penalty function parameters
        self.penalty_strength = np.random.uniform(3.0, 7.0, size=dim)
        self.penalty_centers = np.random.uniform(-4.8, 4.8, size=dim)
        self.penalty_widths = np.random.uniform(0.2, 2.0, size=dim)
        # Multi-scale harmonic components with frequency modulation
        self.harmonic_freq = np.random.uniform(1.0, 12.0, size=dim)
        self.harmonic_amp = np.random.uniform(1.0, 6.0, size=dim)
        self.harmonic_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Basin-like regions with varying depths and radii
        self.basin_centers = np.random.uniform(-4.5, 4.5, size=9)
        self.basin_radii = np.random.uniform(0.2, 3.0, size=9)
        self.basin_depths = np.random.uniform(2.0, 8.0, size=9)
        # Adaptive scaling factors
        self.scale_factors = np.random.uniform(0.2, 3.0, size=dim)
        # Additional chaotic modulation parameters
        self.modulation_freq = np.random.uniform(0.05, 1.2, size=dim)
        self.modulation_amp = np.random.uniform(0.05, 1.5, size=dim)
        # Fractal-like irregularity components
        self.fractal_freq = np.random.uniform(0.3, 2.0, size=dim)
        self.fractal_amp = np.random.uniform(0.5, 3.0, size=dim)
        # Cross-dimensional interaction terms
        self.cross_terms = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced sensitivity
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_x0[i]
            for _ in range(30):  # More iterations for chaos
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            tent_component += tent_val
            
        # Polynomial chaos expansion component
        poly_component = 0.0
        for i in range(self.dim):
            x_scaled = x[i] / 5.0  # Normalize to [-1, 1]
            poly_val = 0.0
            for j in range(self.poly_degree[i]):
                poly_val += self.poly_coeffs[i, j] * (x_scaled ** j)
            poly_component += poly_val
            
        # Dynamic penalty function component
        penalty_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.penalty_centers[i])
            penalty_val = self.penalty_strength[i] * np.exp(-dist / self.penalty_widths[i])
            penalty_component += penalty_val
            
        # Multi-scale harmonic component with phase modulation
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_val = self.harmonic_amp[i] * np.sin(self.harmonic_freq[i] * x[i] + self.harmonic_phase[i])
            harmonic_component += harmonic_val
            
        # Basin-like regions with chaotic dynamics and variable depths
        basin_component = 0.0
        for i in range(9):
            min_dist = float('inf')
            for j in range(self.dim):
                dist = np.abs(x[j] - self.basin_centers[i])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[i]:
                basin_component += self.basin_depths[i] * (1 - min_dist / self.basin_radii[i])
                
        # Adaptive scaling and modulation
        modulated_component = 0.0
        for i in range(self.dim):
            mod_val = self.modulation_amp[i] * np.sin(self.modulation_freq[i] * x[i])
            modulated_component += mod_val
            
        # Fractal-like irregularity component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_val = self.fractal_amp[i] * np.sin(self.fractal_freq[i] * x[i]) * np.cos(self.fractal_freq[i] * x[i])
            fractal_component += fractal_val
            
        # Cross-dimensional interaction terms
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_component += self.cross_terms[i, j] * x[i] * x[j]
                    
        # Combined fitness function with adjusted weights
        return (2.0 * tent_component + 
                2.5 * poly_component + 
                2.0 * penalty_component + 
                2.2 * harmonic_component + 
                1.5 * basin_component + 
                1.0 * modulated_component + 
                0.8 * fractal_component + 
                0.5 * cross_component)