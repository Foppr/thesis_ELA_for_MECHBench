import numpy as np

class HarmonicResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Nested harmonic oscillator parameters
        self.oscillator_freqs = [2.0, 4.0, 8.0, 16.0]
        self.oscillator_amps = [1.0, 0.5, 0.25, 0.125]
        # Dynamic phase coupling
        self.phase_coupling_strength = 0.7
        self.phase_shift_range = np.pi / 4
        # Adaptive basin depth
        self.basin_depth_factor = 2.5
        self.basin_exponent = 3.0
        # Resonance interaction
        self.resonance_strength = 1.5
        self.resonance_decay = 0.8
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Nested harmonic oscillators with varying frequencies and amplitudes
        harmonic_energy = 0.0
        for i in range(self.dim):
            oscillator_term = 0.0
            for j, (freq, amp) in enumerate(zip(self.oscillator_freqs, self.oscillator_amps)):
                if j < self.dim:
                    phase_shift = np.sin(i * freq * 0.1) * self.phase_shift_range
                    oscillator_term += amp * np.sin(freq * x_norm[i] + phase_shift)
            harmonic_energy += oscillator_term**2
        
        # Dynamic phase coupling between adjacent dimensions
        coupling_energy = 0.0
        for i in range(self.dim - 1):
            phase_diff = x_norm[i+1] - x_norm[i]
            coupling_term = np.sin(self.phase_coupling_strength * phase_diff)
            coupling_energy += coupling_term**2
        
        # Adaptive basin depth with non-linear scaling
        basin_energy = 0.0
        for i in range(self.dim):
            # Depth varies based on position and dimension index
            depth_factor = self.basin_depth_factor * (1 + 0.5 * np.sin(i * 0.5))
            basin_term = depth_factor * np.abs(x_norm[i])**self.basin_exponent
            basin_energy += basin_term
        
        # Resonance interaction with decay
        resonance_energy = 0.0
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    weight = self.resonance_decay**(np.abs(i - j))
                    interaction_sum += weight * np.sin(self.resonance_strength * distance)
            resonance_energy += interaction_sum**2
        
        # Combine all components
        total_energy = (harmonic_energy + coupling_energy + basin_energy + 
                       resonance_energy) / self.dim
        
        # Add controlled noise for ruggedness
        noise = 0.02 * np.random.rand() * (1 + 0.3 * np.sin(np.sum(x_norm**3)))
        
        return total_energy + noise