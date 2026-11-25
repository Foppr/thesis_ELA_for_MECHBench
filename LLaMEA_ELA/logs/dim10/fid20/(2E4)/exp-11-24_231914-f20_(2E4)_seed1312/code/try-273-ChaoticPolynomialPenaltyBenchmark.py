import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic tent map parameters with higher randomness and sensitivity
        self.tent_r = np.random.uniform(2.8, 4.0, size=dim)
        self.tent_x0 = np.random.uniform(0.01, 0.99, size=dim)
        # Modified polynomial chaos expansion parameters with higher degree and complexity
        self.poly_chaos_degree = np.random.randint(3, 10, size=dim)
        self.poly_chaos_coeffs = np.random.uniform(-3.0, 3.0, size=(dim, 8))
        # Dynamic penalty function parameters with stronger penalties and more complex exponents
        self.penalty_strength = np.random.uniform(2.0, 7.0, size=dim)
        self.penalty_exponent = np.random.uniform(1.5, 5.0, size=dim)
        self.penalty_centers = np.random.uniform(-4.8, 4.8, size=dim)
        # Enhanced gradient-based terrain modulation with increased magnitude and directional complexity
        self.gradient_magnitude = np.random.uniform(1.2, 5.0, size=dim)
        self.gradient_direction = np.random.uniform(-1.5, 1.5, size=(dim, dim))
        # Multi-scale harmonic components with more aggressive frequency modulation and amplitude variation
        self.harmonic_freq = np.random.uniform(1.0, 10.0, size=dim)
        self.harmonic_amp = np.random.uniform(0.5, 4.0, size=dim)
        self.freq_modulation = np.random.uniform(0.2, 2.0, size=dim)
        # Basin-like regions with deeper variations, more centers, and fractal-like interactions
        self.basin_centers = np.random.uniform(-4.5, 4.5, size=10)
        self.basin_radii = np.random.uniform(0.1, 2.5, size=10)
        self.basin_depths = np.random.uniform(1.0, 8.0, size=10)
        # Dynamic scaling factors with heavier tail distribution
        self.scale_factors = np.random.exponential(1.5, size=dim)
        # Additional chaotic modulation parameters with higher frequency and amplitude
        self.modulation_freq = np.random.uniform(0.2, 2.0, size=dim)
        self.modulation_amp = np.random.uniform(0.2, 2.0, size=dim)
        # Fractal-based harmonic components with increased depth and complexity
        self.fractal_harmonic_freq = np.random.uniform(2.0, 12.0, size=dim)
        self.fractal_harmonic_amp = np.random.uniform(0.5, 3.5, size=dim)
        self.fractal_depth = np.random.uniform(0.2, 1.0, size=dim)
        # Cross-dimensional coupling terms with stronger interaction and non-linear effects
        self.coupling_strength = np.random.uniform(0.5, 3.0, size=(dim, dim))
        # Additional noise components with more chaotic behavior and varying intensities
        self.noise_amplitude = np.random.uniform(0.2, 2.0, size=dim)
        self.noise_frequency = np.random.uniform(1.5, 6.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced dynamics and higher sensitivity
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_x0[i]
            for _ in range(20):  # More iterations for stronger chaos
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
            tent_component += tent_val
            
        # Polynomial chaos expansion component with modified coefficients and higher degree
        poly_component = 0.0
        for i in range(self.dim):
            x_scaled = x[i] / 5.0  # Normalize to [-1, 1]
            poly_val = 0.0
            for j in range(self.poly_chaos_degree[i]):
                poly_val += self.poly_chaos_coeffs[i, j] * (x_scaled ** j)
            poly_component += poly_val
            
        # Gradient-based terrain modulation with enhanced complexity and magnitude
        grad_component = 0.0
        for i in range(self.dim):
            grad_val = 0.0
            for j in range(self.dim):
                grad_val += self.gradient_direction[i, j] * (x[j] - self.tent_x0[j])
            grad_component += self.gradient_magnitude[i] * grad_val
            
        # Multi-scale harmonic component with frequency modulation and enhanced amplitude
        harmonic_component = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freq[i] * self.freq_modulation[i]
            harmonic_val = self.harmonic_amp[i] * np.sin(freq * x[i])
            harmonic_component += harmonic_val
            
        # Basin-like regions with chaotic dynamics, enhanced depth variation and more centers
        basin_component = 0.0
        for i in range(10):
            min_dist = float('inf')
            for j in range(self.dim):
                dist = np.abs(x[j] - self.basin_centers[i])
                if dist < min_dist:
                    min_dist = dist
            if min_dist <= self.basin_radii[i]:
                basin_component += self.basin_depths[i] * (1 - min_dist / self.basin_radii[i])
                
        # Dynamic penalty function component with stronger penalties and more complex exponents
        penalty_component = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i] - self.penalty_centers[i])
            penalty_val = self.penalty_strength[i] * (dist_from_center ** self.penalty_exponent[i])
            penalty_component += penalty_val
            
        # Chaotic modulation component with higher frequency and amplitude
        modulation_component = 0.0
        for i in range(self.dim):
            mod_val = self.modulation_amp[i] * np.sin(self.modulation_freq[i] * x[i])
            modulation_component += mod_val
            
        # Fractal-based harmonic component for increased complexity and depth
        fractal_component = 0.0
        for i in range(self.dim):
            freq = self.fractal_harmonic_freq[i]
            amp = self.fractal_harmonic_amp[i]
            depth = self.fractal_depth[i]
            fractal_val = amp * np.sin(freq * x[i]) * depth
            fractal_component += fractal_val
            
        # Cross-dimensional coupling terms with stronger interaction and non-linear effects
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_strength[i, j] * x[i] * x[j]
                    
        # Noise component with more chaotic behavior and varying intensities
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Combined fitness function with balanced weights and enhanced complexity
        return (1.5 * tent_component + 
                1.6 * poly_component + 
                1.3 * grad_component + 
                1.4 * harmonic_component + 
                1.2 * basin_component + 
                1.4 * penalty_component + 
                0.9 * modulation_component +
                1.0 * fractal_component +
                0.8 * coupling_component +
                0.7 * noise_component)