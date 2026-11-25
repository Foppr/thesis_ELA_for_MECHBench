import numpy as np

class ChaoticPolynomialPenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic tent map parameters with increased randomness and complexity
        self.tent_r = np.random.uniform(2.0, 4.0, size=dim)
        self.tent_x0 = np.random.uniform(0.01, 0.99, size=dim)
        # Modified polynomial chaos expansion with higher degree and more coefficients
        self.poly_chaos_degree = np.random.randint(3, 10, size=dim)
        self.poly_chaos_coeffs = np.random.uniform(-3.0, 3.0, size=(dim, 10))
        # Dynamic penalty function with more complex structure
        self.penalty_strength = np.random.uniform(2.0, 7.0, size=dim)
        self.penalty_exponent = np.random.uniform(1.5, 4.5, size=dim)
        self.penalty_centers = np.random.uniform(-4.8, 4.8, size=dim)
        # Enhanced gradient-based terrain modulation with additional complexity
        self.gradient_magnitude = np.random.uniform(1.0, 4.0, size=dim)
        self.gradient_direction = np.random.uniform(-1.5, 1.5, size=(dim, dim))
        # Multi-scale harmonic components with more complex frequency modulation
        self.harmonic_freq = np.random.uniform(0.8, 10.0, size=dim)
        self.harmonic_amp = np.random.uniform(0.5, 4.0, size=dim)
        self.freq_modulation = np.random.uniform(0.2, 2.0, size=dim)
        # Basin-like regions with increased complexity and depth variation
        self.basin_centers = np.random.uniform(-4.5, 4.5, size=10)
        self.basin_radii = np.random.uniform(0.1, 3.0, size=10)
        self.basin_depths = np.random.uniform(0.5, 7.0, size=10)
        # Dynamic scaling factors with more varied distribution
        self.scale_factors = np.random.exponential(1.5, size=dim)
        # Additional chaotic modulation parameters with higher sensitivity
        self.modulation_freq = np.random.uniform(0.1, 1.5, size=dim)
        self.modulation_amp = np.random.uniform(0.1, 2.0, size=dim)
        # Fractal-based harmonic components with increased complexity
        self.fractal_harmonic_freq = np.random.uniform(1.0, 12.0, size=dim)
        self.fractal_harmonic_amp = np.random.uniform(0.3, 3.5, size=dim)
        self.fractal_depth = np.random.uniform(0.1, 1.0, size=dim)
        # Cross-dimensional coupling terms with more complex interaction patterns
        self.coupling_strength = np.random.uniform(0.5, 3.0, size=(dim, dim))
        # Additional noise components with more varied intensities and frequencies
        self.noise_amplitude = np.random.uniform(0.1, 2.0, size=dim)
        self.noise_frequency = np.random.uniform(0.8, 6.0, size=dim)
        # Additional chaotic feedback loops for enhanced complexity
        self.feedback_strength = np.random.uniform(0.2, 1.5, size=dim)
        self.feedback_delay = np.random.randint(1, 5, size=dim)
        # New: Increased fractal dimensionality and chaotic sensitivity
        self.fractal_dim = np.random.uniform(1.1, 2.5, size=dim)
        self.sensitivity_factor = np.random.uniform(2.0, 8.0, size=dim)
        # New: Multi-modal harmonic with phase shifts and amplitude modulation
        self.phase_shifts = np.random.uniform(-np.pi, np.pi, size=dim)
        self.amplitude_mod = np.random.uniform(0.5, 3.0, size=dim)
        # New: Enhanced penalty with exponential scaling and multiple centers
        self.multi_penalty_centers = np.random.uniform(-4.9, 4.9, size=(dim, 5))
        self.penalty_exponent_multi = np.random.uniform(2.0, 6.0, size=dim)
        # New: Cross-dimensional chaos coupling with time-delayed interactions
        self.delay_coupling = np.random.randint(1, 4, size=(dim, dim))
        self.coupling_delay_strength = np.random.uniform(0.3, 2.0, size=(dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced dynamics and feedback
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_x0[i]
            feedback = 0.0
            for _ in range(20):  # More iterations for stronger chaos
                if tent_val < 0.5:
                    tent_val = self.tent_r[i] * tent_val
                else:
                    tent_val = self.tent_r[i] * (1 - tent_val)
                feedback += self.feedback_strength[i] * np.sin(self.feedback_delay[i] * tent_val)
            tent_component += tent_val + feedback
            
        # Polynomial chaos expansion component with modified coefficients
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
        for i in range(10):
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
            
        # Fractal-based harmonic component for increased complexity
        fractal_component = 0.0
        for i in range(self.dim):
            freq = self.fractal_harmonic_freq[i]
            amp = self.fractal_harmonic_amp[i]
            depth = self.fractal_depth[i]
            fractal_val = amp * np.sin(freq * x[i]) * depth
            fractal_component += fractal_val
            
        # Cross-dimensional coupling terms
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_strength[i, j] * x[i] * x[j]
                    
        # Noise component with varying intensities
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Enhanced multi-modal harmonic with phase shifts and amplitude modulation
        multimodal_component = 0.0
        for i in range(self.dim):
            base_harmonic = self.amplitude_mod[i] * np.sin(self.harmonic_freq[i] * x[i] + self.phase_shifts[i])
            fractal_harmonic = self.fractal_harmonic_amp[i] * np.sin(self.fractal_harmonic_freq[i] * x[i]) * self.fractal_depth[i]
            multimodal_component += base_harmonic + fractal_harmonic
            
        # Multi-center penalty with exponential scaling
        multi_penalty_component = 0.0
        for i in range(self.dim):
            penalty_sum = 0.0
            for center in self.multi_penalty_centers[i]:
                dist = np.abs(x[i] - center)
                penalty_sum += (dist ** self.penalty_exponent_multi[i])
            multi_penalty_component += penalty_sum
            
        # Delayed chaotic coupling component
        delay_coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    delayed_x = x[j - self.delay_coupling[i, j]] if j >= self.delay_coupling[i, j] else x[-1]
                    delay_coupling_component += self.coupling_delay_strength[i, j] * x[i] * delayed_x
                    
        # Sensitivity-based modulation
        sensitivity_component = 0.0
        for i in range(self.dim):
            sensitivity_component += self.sensitivity_factor[i] * np.exp(-x[i]**2 / 10)
            
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
                0.7 * noise_component +
                0.6 * multimodal_component +
                0.5 * multi_penalty_component +
                0.4 * delay_coupling_component +
                0.3 * sensitivity_component)