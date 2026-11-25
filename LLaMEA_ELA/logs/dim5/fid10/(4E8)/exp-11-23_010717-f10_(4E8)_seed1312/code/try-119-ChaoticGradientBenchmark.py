import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for time-varying components
        self.harmonic_coeffs = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        time_factor = 1.0 + 0.3 * np.sin(0.1 * r) * np.cos(0.05 * r)
        radial_term = 0.5 * r**2 * time_factor
        
        # Dynamic saddle-point repulsion with varying strength
        saddle_repulsion = 0.0
        for i in range(self.dim):
            # Varying repulsion strength based on dimension and position
            repulsion_strength = 1.0 + 0.5 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[i])
            saddle_repulsion += repulsion_strength * (x[i]**2 - 0.5 * x[i]**4)
        
        # Multi-scale harmonic interference patterns
        harmonic_sum = 0.0
        for i in range(self.dim):
            # Combine multiple frequencies with dynamic amplitudes
            freqs = [1.0, 2.0, 3.0, 4.0]
            amps = [1.5, 1.0, 0.7, 0.5]
            for freq, amp in zip(freqs, amps):
                harmonic_sum += amp * np.sin(freq * x[i] + self.harmonic_coeffs[i]) * \
                               np.cos(0.5 * freq * x[i] + 0.3 * self.harmonic_coeffs[i])
        
        # Chaotic cross-dimensional coupling with dynamic interaction weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic weight based on position and chaotic modulation
                dynamic_weight = 0.3 + 0.2 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[j])
                coupling += dynamic_weight * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Non-stationary noise-like component with position-dependent chaos
        noise_component = 0.0
        for i in range(self.dim):
            # Position-dependent chaotic modulation
            chaos_factor = 0.1 * np.sin(3.0 * x[i] + 2.0 * r) * np.cos(2.0 * x[i] - 0.5 * r)
            noise_component += chaos_factor * (x[i]**3 - 0.3 * x[i])
        
        # Global scaling with chaotic variation
        global_scale = 1.0 + 0.2 * np.sin(0.2 * r) * np.cos(0.1 * r) + 0.1 * np.sum(np.sin(x))
        
        # Penalty for boundary proximity with dynamic threshold
        penalty = 0.05 * r**3 + 0.02 * r**4
        
        return global_scale * (radial_term + saddle_repulsion + harmonic_sum + coupling + noise_component) + penalty