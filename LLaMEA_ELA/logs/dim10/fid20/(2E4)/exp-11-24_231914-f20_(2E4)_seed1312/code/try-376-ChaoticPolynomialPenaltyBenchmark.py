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
        # New chaotic logistic map component for increased complexity
        self.logistic_r = np.random.uniform(3.5, 4.0, size=dim)
        self.logistic_x0 = np.random.uniform(0.1, 0.9, size=dim)
        # Enhanced multi-peak harmonic components with dynamic phase shifts
        self.multi_peak_freq = np.random.uniform(1.0, 20.0, size=dim)
        self.multi_peak_amp = np.random.uniform(0.5, 5.0, size=dim)
        self.phase_shift = np.random.uniform(0.0, 2*np.pi, size=dim)
        # Cross-dimensional interaction with non-linear coupling
        self.nonlinear_coupling = np.random.uniform(0.1, 2.5, size=(dim, dim))
        # Memory-based penalty with exponential decay
        self.memory_penalty = np.random.uniform(0.5, 3.0, size=dim)
        self.decay_rate = np.random.uniform(0.1, 0.8, size=dim)
        # Increased basin complexity with overlapping regions and varying depths
        self.overlapping_basins = np.random.randint(3, 8, size=5)
        self.basin_overlap_radii = np.random.uniform(0.2, 2.0, size=5)
        self.basin_overlap_depths = np.random.uniform(1.0, 6.0, size=5)
        # New hyper-chaotic component with multiple feedback loops
        self.hyperchaos_r = np.random.uniform(3.8, 4.0, size=dim)
        self.hyperchaos_x0 = np.random.uniform(0.01, 0.99, size=dim)
        # Multi-scale fractal modulation with recursive patterns
        self.fractal_scale = np.random.uniform(0.5, 2.0, size=dim)
        self.fractal_power = np.random.uniform(0.1, 0.9, size=dim)
        # Enhanced dynamic penalty with time-dependent components
        self.time_penalty = np.random.uniform(0.1, 1.0, size=dim)
        self.time_freq = np.random.uniform(0.5, 3.0, size=dim)
        # Additional basin interaction with spatial correlation
        self.spatial_correlation = np.random.uniform(0.2, 0.8, size=dim)
        # New harmonic resonance components with phase coupling
        self.resonance_freq = np.random.uniform(1.0, 15.0, size=dim)
        self.resonance_amp = np.random.uniform(0.3, 2.5, size=dim)
        self.phase_coupling = np.random.uniform(0.1, 1.0, size=dim)
        # Increased chaotic complexity with additional chaotic systems
        self.chebyshev_r = np.random.uniform(1.5, 3.5, size=dim)
        self.chebyshev_x0 = np.random.uniform(0.01, 0.99, size=dim)
        # Added quantum-like interference terms for enhanced multimodality
        self.quantum_freq = np.random.uniform(0.5, 8.0, size=dim)
        self.quantum_amp = np.random.uniform(0.2, 2.5, size=dim)
        # Multi-dimensional correlation effects with higher-order interactions
        self.correlation_order = np.random.randint(3, 6, size=dim)
        # Dynamic basin shifting for time-varying landscape
        self.basin_shift_speed = np.random.uniform(0.1, 0.5, size=dim)
        self.basin_shift_phase = np.random.uniform(0.0, 2*np.pi, size=dim)
        # New hyper-chaotic cross-dimensional coupling component for enhanced complexity
        self.hyperchaos_coupling = np.random.uniform(0.1, 1.0, size=(dim, dim))
        self.hyperchaos_feedback = np.random.uniform(0.5, 2.0, size=dim)
        # Additional chaotic tent map with varying r values and feedback
        self.tent_r_vary = np.random.uniform(3.0, 4.0, size=dim)
        self.tent_feedback_strength = np.random.uniform(0.1, 1.0, size=dim)
        # New chaotic sine map component
        self.sine_r = np.random.uniform(2.0, 3.5, size=dim)
        self.sine_x0 = np.random.uniform(0.01, 0.99, size=dim)
        # Enhanced fractal harmonic components with recursive depth
        self.fractal_recursive_depth = np.random.randint(2, 6, size=dim)
        self.fractal_recursive_amp = np.random.uniform(0.1, 1.5, size=dim)
        # Cross-dimensional harmonic interference
        self.harmonic_interference = np.random.uniform(0.5, 3.0, size=(dim, dim))
        # Multi-scale penalty with exponential decay
        self.multi_scale_penalty_strength = np.random.uniform(1.0, 5.0, size=dim)
        self.multi_scale_penalty_decay = np.random.uniform(0.2, 1.0, size=dim)
        # Quantum-inspired interference with phase modulation
        self.quantum_phase_mod = np.random.uniform(0.1, 2.0, size=dim)
        # Enhanced basin shifting with sinusoidal dynamics
        self.basin_shift_sine_amp = np.random.uniform(0.1, 0.5, size=dim)
        self.basin_shift_sine_freq = np.random.uniform(0.5, 2.0, size=dim)
        # New chaotic Arnold map component for even higher complexity
        self.arnold_a = np.random.uniform(0.1, 0.9, size=dim)
        self.arnold_b = np.random.uniform(0.1, 0.9, size=dim)
        # Multi-scale hyper-chaotic components with varying feedback strengths
        self.hyperchaos_feedback_strength = np.random.uniform(0.2, 2.0, size=dim)
        # Enhanced basin interaction with dynamic scaling
        self.basin_scaling = np.random.uniform(0.5, 2.5, size=10)
        # Cross-dimensional fractal harmonic components
        self.fractal_harmonic_cross_dim = np.random.uniform(0.5, 3.0, size=(dim, dim))
        # Multi-peak harmonic with time-varying frequencies and amplitudes
        self.multi_peak_time_freq = np.random.uniform(1.0, 25.0, size=dim)
        self.multi_peak_time_amp = np.random.uniform(0.3, 6.0, size=dim)
        # Adaptive basin interaction with memory effects
        self.adaptive_basin_interaction = np.random.uniform(0.1, 1.5, size=dim)
        self.basin_memory_factor = np.random.uniform(0.05, 0.5, size=dim)
        # Enhanced penalty with multi-scale dynamics and time-varying parameters
        self.penalty_multi_scale = np.random.uniform(1.0, 6.0, size=dim)
        self.penalty_time_var = np.random.uniform(0.1, 2.0, size=dim)
        
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
            
        # Logistic map component for additional chaotic behavior
        logistic_component = 0.0
        for i in range(self.dim):
            log_val = self.logistic_x0[i]
            for _ in range(30):  # More iterations for stronger chaos
                log_val = self.logistic_r[i] * log_val * (1 - log_val)
            logistic_component += log_val
            
        # Hyper-chaotic component with multiple feedback loops
        hyperchaos_component = 0.0
        for i in range(self.dim):
            hyper_val = self.hyperchaos_x0[i]
            for _ in range(25):  # Even more iterations for stronger hyper-chaos
                hyper_val = self.hyperchaos_r[i] * hyper_val * (1 - hyper_val)
            hyperchaos_component += hyper_val
            
        # Chebyshev map component for added complexity
        chebyshev_component = 0.0
        for i in range(self.dim):
            cheby_val = self.chebyshev_x0[i]
            for _ in range(20):
                cheby_val = np.cos(self.chebyshev_r[i] * np.arccos(cheby_val))
            chebyshev_component += cheby_val
            
        # Arnold map component for even higher chaos
        arnold_component = 0.0
        for i in range(self.dim):
            x1, x2 = self.tent_x0[i], self.tent_x0[(i+1) % self.dim]
            for _ in range(30):
                new_x1 = (x1 + self.arnold_a[i] * x2) % 1.0
                new_x2 = (x2 + self.arnold_b[i] * x1) % 1.0
                x1, x2 = new_x1, new_x2
            arnold_component += x1
            
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
            
        # Multi-peak harmonic component with dynamic phase shifts
        multi_peak_component = 0.0
        for i in range(self.dim):
            freq = self.multi_peak_freq[i]
            amp = self.multi_peak_amp[i]
            phase = self.phase_shift[i]
            peak_val = amp * np.sin(freq * x[i] + phase)
            multi_peak_component += peak_val
            
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
                
        # Overlapping basin regions with varying depths and radii
        overlapping_basin_component = 0.0
        for i in range(5):
            center_idx = np.random.randint(0, len(self.basin_centers))
            radius = self.basin_overlap_radii[i]
            depth = self.basin_overlap_depths[i]
            dist = 0.0
            for j in range(self.dim):
                dist += (x[j] - self.basin_centers[center_idx]) ** 2
            dist = np.sqrt(dist)
            if dist <= radius:
                overlapping_basin_component += depth * (1 - dist / radius)
                
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
            
        # Multi-scale fractal modulation with recursive patterns
        fractal_scale_component = 0.0
        for i in range(self.dim):
            scale_val = self.fractal_scale[i] * (np.sin(x[i] * self.fractal_power[i]) + 1.0)
            fractal_scale_component += scale_val
            
        # Cross-dimensional coupling terms
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_strength[i, j] * x[i] * x[j]
                    
        # Non-linear cross-dimensional interaction
        nonlinear_coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    nonlinear_coupling_component += self.nonlinear_coupling[i, j] * np.sin(x[i]) * x[j]
                    
        # Noise component with varying intensities
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Interference harmonic components for multi-modal complexity
        interference_component = 0.0
        for i in range(self.dim):
            inf_val = self.interference_amp[i] * np.sin(self.interference_freq[i] * x[i])
            interference_component += inf_val
            
        # Adaptive penalty with memory effects
        adaptive_penalty_component = 0.0
        for i in range(self.dim):
            adaptive_val = self.adaptive_penalty[i] * (x[i] ** 2) * self.memory_factor[i]
            adaptive_penalty_component += adaptive_val
            
        # Memory-based penalty with exponential decay
        memory_penalty_component = 0.0
        for i in range(self.dim):
            mem_val = self.memory_penalty[i] * np.exp(-self.decay_rate[i] * np.abs(x[i]))
            memory_penalty_component += mem_val
            
        # Time-dependent dynamic penalty component
        time_penalty_component = 0.0
        for i in range(self.dim):
            time_val = self.time_penalty[i] * np.cos(self.time_freq[i] * x[i])
            time_penalty_component += time_val
            
        # Resonance harmonic components with phase coupling
        resonance_component = 0.0
        for i in range(self.dim):
            freq = self.resonance_freq[i]
            amp = self.resonance_amp[i]
            phase = self.phase_coupling[i]
            resonance_val = amp * np.sin(freq * x[i] + phase)
            resonance_component += resonance_val
            
        # Spatial correlation basin interaction
        spatial_basin_component = 0.0
        for i in range(self.dim):
            spatial_val = self.spatial_correlation[i] * np.sum(np.abs(x - self.basin_centers[i % len(self.basin_centers)]))
            spatial_basin_component += spatial_val
            
        # Quantum-like interference terms
        quantum_component = 0.0
        for i in range(self.dim):
            freq = self.quantum_freq[i]
            amp = self.quantum_amp[i]
            quantum_val = amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            quantum_component += quantum_val
            
        # Correlation-based multi-dimensional effects
        correlation_component = 0.0
        for i in range(self.dim):
            corr_val = 0.0
            for j in range(self.correlation_order[i]):
                corr_val += np.sin(x[i] * (j + 1))
            correlation_component += corr_val
            
        # Dynamic basin shifting effect
        basin_shift_component = 0.0
        for i in range(self.dim):
            shift_val = self.basin_shift_speed[i] * np.sin(self.basin_shift_phase[i] + x[i])
            basin_shift_component += shift_val
            
        # Hyper-chaotic cross-dimensional coupling component
        hyperchaos_coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    hyperchaos_coupling_component += self.hyperchaos_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Additional chaotic tent map with varying parameters
        tent_vary_component = 0.0
        for i in range(self.dim):
            tent_val = self.tent_x0[i]
            feedback = 0.0
            for _ in range(15):
                if tent_val < 0.5:
                    tent_val = self.tent_r_vary[i] * tent_val
                else:
                    tent_val = self.tent_r_vary[i] * (1 - tent_val)
                feedback += self.tent_feedback_strength[i] * np.sin(tent_val)
            tent_vary_component += tent_val + feedback
            
        # Sine map component for additional chaotic behavior
        sine_component = 0.0
        for i in range(self.dim):
            sine_val = self.sine_x0[i]
            for _ in range(25):
                sine_val = np.sin(self.sine_r[i] * sine_val)
            sine_component += sine_val
            
        # Fractal recursive harmonic components
        fractal_recursive_component = 0.0
        for i in range(self.dim):
            depth = self.fractal_recursive_depth[i]
            amp = self.fractal_recursive_amp[i]
            val = 0.0
            for j in range(depth):
                val += amp * np.sin((j + 1) * x[i])
            fractal_recursive_component += val
            
        # Harmonic interference across dimensions
        harmonic_interference_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    harmonic_interference_component += self.harmonic_interference[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Multi-scale penalty with exponential decay
        multi_scale_penalty_component = 0.0
        for i in range(self.dim):
            scale_val = self.multi_scale_penalty_strength[i] * np.exp(-self.multi_scale_penalty_decay[i] * np.abs(x[i]))
            multi_scale_penalty_component += scale_val
            
        # Quantum phase modulation component
        quantum_phase_component = 0.0
        for i in range(self.dim):
            freq = self.quantum_freq[i]
            amp = self.quantum_amp[i]
            phase_mod = self.quantum_phase_mod[i]
            quantum_val = amp * np.sin(freq * x[i] + phase_mod) * np.cos(freq * x[i])
            quantum_phase_component += quantum_val
            
        # Basin shifting with sinusoidal dynamics
        basin_shift_sine_component = 0.0
        for i in range(self.dim):
            shift_val = self.basin_shift_sine_amp[i] * np.sin(self.basin_shift_sine_freq[i] * x[i])
            basin_shift_sine_component += shift_val
            
        # Enhanced basin interaction with dynamic scaling
        adaptive_basin_component = 0.0
        for i in range(10):
            dist = 0.0
            for j in range(self.dim):
                dist += (x[j] - self.basin_centers[i]) ** 2
            dist = np.sqrt(dist)
            if dist <= self.basin_radii[i]:
                adaptive_basin_component += self.basin_scaling[i] * self.basin_depths[i] * (1 - dist / self.basin_radii[i])
                
        # Cross-dimensional fractal harmonic components
        cross_dim_fractal_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_dim_fractal_component += self.fractal_harmonic_cross_dim[i, j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Multi-peak harmonic with time-varying parameters
        time_vary_peak_component = 0.0
        for i in range(self.dim):
            freq = self.multi_peak_time_freq[i]
            amp = self.multi_peak_time_amp[i]
            time_val = np.sin(freq * x[i])
            peak_val = amp * time_val
            time_vary_peak_component += peak_val
            
        # Enhanced penalty with multi-scale dynamics and time-varying parameters
        enhanced_penalty_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.penalty_centers[i])
            scale = self.penalty_multi_scale[i]
            time_factor = np.sin(self.penalty_time_var[i] * x[i])
            penalty_val = scale * (dist ** self.penalty_exponent[i]) * time_factor
            enhanced_penalty_component += penalty_val
            
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
                0.4 * logistic_component +
                0.3 * multi_peak_component +
                0.2 * nonlinear_coupling_component +
                0.1 * overlapping_basin_component +
                0.05 * memory_penalty_component +
                0.03 * hyperchaos_component +
                0.02 * fractal_scale_component +
                0.04 * time_penalty_component +
                0.06 * resonance_component +
                0.07 * spatial_basin_component +
                0.08 * chebyshev_component +
                0.09 * quantum_component +
                0.10 * correlation_component +
                0.11 * basin_shift_component +
                0.12 * hyperchaos_coupling_component +
                0.01 * tent_vary_component +
                0.02 * sine_component +
                0.03 * fractal_recursive_component +
                0.04 * harmonic_interference_component +
                0.05 * multi_scale_penalty_component +
                0.06 * quantum_phase_component +
                0.07 * basin_shift_sine_component +
                0.08 * arnold_component +
                0.09 * adaptive_basin_component +
                0.10 * cross_dim_fractal_component +
                0.11 * time_vary_peak_component +
                0.12 * enhanced_penalty_component)