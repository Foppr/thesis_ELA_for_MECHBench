import numpy as np

class QuantumHarmonicSpinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic resonance parameters
        self.resonance_frequencies = np.random.uniform(0.5, 3.0, dim)
        self.quantum_levels = np.random.randint(2, 6, dim)
        self.spin_coupling_strengths = np.random.uniform(0.1, 1.5, (dim, dim))
        # Adaptive radial basis functions
        self.rb_centers = np.random.uniform(-3.0, 3.0, (dim, 10))
        self.rb_widths = np.random.uniform(0.5, 2.5, 10)
        # Cross-dimensional spin coupling
        self.spin_angles = np.random.uniform(0, 2*np.pi, dim)
        # Stochastic phase interference
        self.phase_noise_amplitude = 0.3 + np.random.rand() * 0.4
        self.phase_modulation_freq = 0.5 + np.random.rand() * 1.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Quantum harmonic resonance terms
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_frequencies[i]
            level = self.quantum_levels[i]
            # Quantum harmonic oscillation with energy levels
            quantum_val = (x_norm[i] ** 2) * np.sin(freq * x_norm[i]) + level * np.cos(freq * x_norm[i])
            quantum_term += quantum_val
            
        # Radial basis function terms with adaptive centers
        rb_term = 0.0
        for i in range(self.dim):
            center_vals = self.rb_centers[i]
            widths = self.rb_widths
            # Radial basis functions with multi-center influence
            for j, (center, width) in enumerate(zip(center_vals, widths)):
                rb_val = np.exp(-((x_norm[i] - center) ** 2) / (2 * width ** 2))
                rb_term += rb_val
                
        # Spin coupling between dimensions
        spin_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                strength = self.spin_coupling_strengths[i, j]
                angle_i = self.spin_angles[i]
                angle_j = self.spin_angles[j]
                # Cross-dimensional spin interaction
                spin_val = strength * np.sin(angle_i + x_norm[i]) * np.cos(angle_j + x_norm[j])
                spin_term += spin_val
                
        # Phase interference with stochastic modulation
        phase_term = 0.0
        for i in range(self.dim):
            freq = self.phase_modulation_freq
            noise_amp = self.phase_noise_amplitude
            # Stochastic phase modulation with quantum interference
            phase_val = np.sin(x_norm[i] * freq + noise_amp * np.random.randn()) * np.cos(x_norm[i])
            phase_term += phase_val
            
        # Combined function with weighted components
        result = 1.3 * quantum_term + 0.9 * rb_term + 0.7 * spin_term + 1.1 * phase_term
        
        # Add quantum-like noise with interference patterns
        noise_amplitude = 0.02 * (1.0 + 0.1 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise