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
        # Quantum-enhanced harmonic interference with complex phase relationships
        self.quantum_interference_freq = np.random.uniform(2.0, 12.0, size=dim)
        self.quantum_interference_amp = np.random.uniform(0.1, 1.5, size=dim)
        self.quantum_phase_shift = np.random.uniform(0.0, 4*np.pi, size=dim)
        # Multi-scale chaotic feedback loops with varying time delays
        self.multi_scale_feedback = np.random.uniform(0.1, 2.0, size=dim)
        self.feedback_delay_scale = np.random.randint(1, 10, size=dim)
        # Enhanced basin connectivity with dynamic attraction basins
        self.basin_connectivity = np.random.uniform(0.5, 3.0, size=10)
        self.dynamic_basin_centers = np.random.uniform(-4.0, 4.0, size=(10, dim))
        # Fractional Brownian motion component for long-range dependencies
        self.fbm_hurst = np.random.uniform(0.1, 0.9, size=dim)
        # Complex multi-peak landscape with varying amplitudes and frequencies
        self.multi_peak_complex_freq = np.random.uniform(1.0, 25.0, size=dim)
        self.multi_peak_complex_amp = np.random.uniform(0.3, 6.0, size=dim)
        self.multi_peak_complex_phase = np.random.uniform(0.0, 4*np.pi, size=dim)
        
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
            
        # Quantum-enhanced harmonic interference with complex phase relationships
        quantum_interference_component = 0.0
        for i in range(self.dim):
            freq = self.quantum_interference_freq[i]
            amp = self.quantum_interference_amp[i]
            phase = self.quantum_phase_shift[i]
            interference_val = amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i])
            quantum_interference_component += interference_val
            
        # Multi-scale chaotic feedback loops with varying time delays
        multi_scale_feedback_component = 0.0
        for i in range(self.dim):
            delay = self.feedback_delay_scale[i]
            feedback_val = self.multi_scale_feedback[i] * np.sin(delay * x[i])
            multi_scale_feedback_component += feedback_val
            
        # Enhanced basin connectivity with dynamic attraction basins
        basin_connectivity_component = 0.0
        for i in range(10):
            dist = 0.0
            for j in range(self.dim):
                dist += (x[j] - self.dynamic_basin_centers[i, j]) ** 2
            dist = np.sqrt(dist)
            if dist <= self.basin_radii[i]:
                basin_connectivity_component += self.basin_connectivity[i] * (1 - dist / self.basin_radii[i])
                
        # Fractional Brownian motion component for long-range dependencies
        fbm_component = 0.0
        for i in range(self.dim):
            fbm_val = np.random.normal(0, 1) * np.power(np.abs(x[i]), self.fbm_hurst[i])
            fbm_component += fbm_val
            
        # Complex multi-peak landscape with varying amplitudes and frequencies
        complex_multi_peak_component = 0.0
        for i in range(self.dim):
            freq = self.multi_peak_complex_freq[i]
            amp = self.multi_peak_complex_amp[i]
            phase = self.multi_peak_complex_phase[i]
            complex_val = amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i])
            complex_multi_peak_component += complex_val
            
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
                0.12 * quantum_interference_component +
                0.13 * multi_scale_feedback_component +
                0.14 * basin_connectivity_component +
                0.15 * fbm_component +
                0.16 * complex_multi_peak_component)