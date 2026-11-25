import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic tent map parameters with enhanced randomness
        self.tent_r = np.random.uniform(1.8, 3.5, size=dim)
        self.tent_x0 = np.random.uniform(0.05, 0.95, size=dim)
        # Polynomial chaos expansion parameters
        self.poly_chaos_degree = np.random.randint(3, 8, size=dim)
        self.poly_chaos_coeffs = np.random.uniform(-3.0, 3.0, size=(dim, 8))
        # Dynamic penalty function parameters
        self.penalty_strength = np.random.uniform(2.0, 6.0, size=dim)
        self.penalty_exponent = np.random.uniform(1.5, 4.0, size=dim)
        self.penalty_centers = np.random.uniform(-4.5, 4.5, size=dim)
        # Enhanced gradient-based terrain modulation
        self.gradient_magnitude = np.random.uniform(1.0, 4.0, size=dim)
        self.gradient_direction = np.random.uniform(-1.5, 1.5, size=(dim, dim))
        # Multi-scale harmonic components with frequency modulation
        self.harmonic_freq = np.random.uniform(0.3, 6.0, size=dim)
        self.harmonic_amp = np.random.uniform(0.2, 2.5, size=dim)
        self.freq_modulation = np.random.uniform(0.5, 2.0, size=dim)
        # Basin-like regions with varying depths and radii
        self.basin_centers = np.random.uniform(-4.2, 4.2, size=7)
        self.basin_radii = np.random.uniform(0.3, 2.5, size=7)
        self.basin_depths = np.random.uniform(0.8, 6.0, size=7)
        # Dynamic scaling factors with exponential distribution
        self.scale_factors = np.random.exponential(1.5, size=dim)
        # Additional chaotic modulation parameters
        self.modulation_freq = np.random.uniform(0.1, 1.0, size=dim)
        self.modulation_amp = np.random.uniform(0.1, 1.5, size=dim)
        # Enhanced interaction terms between dimensions
        self.interaction_strength = np.random.uniform(0.5, 2.0, size=(dim, dim))
        self.nonlinear_exponent = np.random.uniform(1.2, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced dynamics
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_x0[i]
            for _ in range(15):  # More iterations for stronger chaos
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
            for j in range(self.poly_chaos_degree[i]):
                poly_val += self.poly_chaos_coeffs[i, j] * (x_scaled ** j)
            poly_component += poly_val
            
        # Gradient-based terrain modulation with enhanced complexity
        grad_component = 0.0
        for i in range(self.dim):
            grad_val = 0.0
            for j in range(self.dim):
                grad_val += self.gradient_direction[i, j] * (x[j] - self.tent_x0[j])
            grad_component += self.gradient_magnitude[i] * grad_val
            
        # Multi-scale harmonic component with frequency modulation
        harmonic_component = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freq[i] * self.freq_modulation[i]
            harmonic_val = self.harmonic_amp[i] * np.sin(freq * x[i])
            harmonic_component += harmonic_val
            
        # Basin-like regions with chaotic dynamics and enhanced depth variation
        basin_component = 0.0
        for i in range(7):
            min_dist = float('inf')
            for j in range(self.dim):
                dist = np.abs(x[j] - self.basin_centers[i])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[i]:
                basin_component += self.basin_depths[i] * (1 - min_dist / self.basin_radii[i])
                
        # Dynamic penalty function component
        penalty_component = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i] - self.penalty_centers[i])
            penalty_val = self.penalty_strength[i] * (dist_from_center ** self.penalty_exponent[i])
            penalty_component += penalty_val
            
        # Chaotic modulation component
        modulation_component = 0.0
        for i in range(self.dim):
            mod_val = self.modulation_amp[i] * np.sin(self.modulation_freq[i] * x[i])
            modulation_component += mod_val
            
        # Enhanced interaction terms between dimensions
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_component += self.interaction_strength[i, j] * (x[i] ** self.nonlinear_exponent[i]) * x[j]
                    
        # Combined fitness function with balanced weights and enhanced complexity
        return (1.2 * tent_component + 
                1.5 * poly_component + 
                1.0 * grad_component + 
                1.3 * harmonic_component + 
                0.9 * basin_component + 
                1.1 * penalty_component + 
                0.7 * modulation_component + 
                0.5 * interaction_component)