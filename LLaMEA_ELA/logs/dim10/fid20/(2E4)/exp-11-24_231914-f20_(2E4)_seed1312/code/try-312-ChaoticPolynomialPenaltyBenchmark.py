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
        # Enhanced basin interaction with cross-dimensional coupling
        self.basin_coupling = np.random.uniform(0.1, 2.0, size=(10, dim))
        # Multi-modal harmonic interference patterns
        self.interference_freq = np.random.uniform(2.0, 15.0, size=dim)
        self.interference_amp = np.random.uniform(0.2, 3.0, size=dim)
        # Adaptive penalty function with memory effects
        self.adaptive_penalty = np.random.uniform(1.0, 5.0, size=dim)
        self.memory_factor = np.random.uniform(0.1, 0.9, size=dim)
        # New: Increased chaos and sensitivity through higher-order tent map iterations
        self.tent_iterations = np.random.randint(30, 50, size=dim)
        # New: Additional fractal dimensionality with recursive harmonic components
        self.fractal_dim = np.random.uniform(1.1, 2.5, size=dim)
        # New: Multi-scale basin interaction with dynamic radius adjustment
        self.basin_radius_scale = np.random.uniform(0.5, 2.0, size=10)
        # New: Enhanced harmonic interference with phase coupling
        self.phase_coupling = np.random.uniform(-np.pi, np.pi, size=dim)
        # New: Memory-based penalty with time-dependent factors
        self.memory_decay = np.random.uniform(0.8, 0.99, size=dim)
        # New: Cross-dimensional non-linear coupling terms
        self.nonlinear_coupling = np.random.uniform(0.1, 1.0, size=(dim, dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with enhanced dynamics and feedback
        tent_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_x0[i]
            feedback = 0.0
            for _ in range(self.tent_iterations[i]):  # More iterations for stronger chaos
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
            if min_dist <= self.basin_radii[i] * self.basin_radius_scale[i]:
                basin_component += self.basin_depths[i] * (1 - min_dist / (self.basin_radii[i] * self.basin_radius_scale[i]))
                
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
            fractal_val = amp * np.sin(freq * x[i]) * depth * (1 + 0.5 * np.sin(self.fractal_dim[i] * x[i]))
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
            
        # Interference harmonic components for multi-modal complexity
        interference_component = 0.0
        for i in range(self.dim):
            inf_val = self.interference_amp[i] * np.sin(self.interference_freq[i] * x[i] + self.phase_coupling[i])
            interference_component += inf_val
            
        # Adaptive penalty with memory effects
        adaptive_penalty_component = 0.0
        for i in range(self.dim):
            adaptive_val = self.adaptive_penalty[i] * (x[i] ** 2) * self.memory_factor[i]
            adaptive_penalty_component += adaptive_val
            
        # New: Memory-based penalty with time-dependent decay
        memory_penalty_component = 0.0
        for i in range(self.dim):
            memory_val = self.memory_decay[i] * x[i]**2
            memory_penalty_component += memory_val
            
        # New: Non-linear cross-dimensional coupling
        nonlinear_coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        nonlinear_coupling_component += self.nonlinear_coupling[i, j, k] * x[i] * x[j] * x[k]
        
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
                0.6 * interference_component +
                0.5 * adaptive_penalty_component +
                0.4 * memory_penalty_component +
                0.3 * nonlinear_coupling_component)