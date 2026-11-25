import numpy as np

class QuantumHarmonicOptimaBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.oscillator_frequencies = np.random.uniform(0.5, 3.0, dim) * 2.0
        self.oscillator_amplitudes = np.logspace(1.0, 2.5, dim) * 1.2
        # Adaptive phase coupling strengths
        self.phase_couplings = np.random.uniform(0.1, 1.5, dim) * 0.8
        # Radial symmetry parameters
        self.symmetry_orders = np.random.randint(3, 8, dim)
        self.radial_amplitudes = np.logspace(0.5, 2.0, dim) * 1.8
        # Entropic conditioning factors
        self.conditioning_entropies = np.random.uniform(0.3, 1.2, dim) * 2.5
        # Quantum-like interference parameters
        self.interference_strengths = np.random.uniform(0.5, 2.5, dim) * 1.5
        self.quantum_phases = np.random.uniform(0, 2*np.pi, dim)
        # Basin boundary parameters
        self.basin_radii = np.random.uniform(1.0, 3.0, dim) * 1.2
        self.basin_well_depths = np.random.uniform(0.5, 2.0, dim) * 1.8
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Quantum harmonic oscillator terms
        quantum_term = 0.0
        for i in range(self.dim):
            freq = self.oscillator_frequencies[i]
            amp = self.oscillator_amplitudes[i]
            phase = self.quantum_phases[i]
            # Quantum harmonic potential with phase modulation
            quantum_val = amp * (freq * x_norm[i] - phase) ** 2 + np.sin(freq * x_norm[i] + phase)
            quantum_term += quantum_val
            
        # Radial symmetry patterns with quantum interference
        radial_term = 0.0
        for i in range(self.dim):
            order = self.symmetry_orders[i]
            amp = self.radial_amplitudes[i]
            # Radial pattern with symmetry breaking
            radial_val = amp * np.sin(order * np.arctan2(x_norm[i], 1.0)) ** 2
            # Add quantum-like phase coupling
            phase_coupling = self.phase_couplings[i] * np.cos(x_norm[i])
            radial_val *= (1.0 + 0.3 * phase_coupling)
            radial_term += radial_val
            
        # Entropic conditioning with adaptive complexity
        entropy_term = 0.0
        for i in range(self.dim):
            entropy = self.conditioning_entropies[i]
            # Entropic penalty with exponential scaling
            entropy_val = entropy * np.exp(0.5 * x_norm[i] ** 2)
            entropy_term += entropy_val
            
        # Quantum interference effects
        interference_term = 0.0
        for i in range(self.dim):
            strength = self.interference_strengths[i]
            # Interference pattern with quantum amplitude modulation
            interference_val = strength * np.sin(x_norm[i]) * np.cos(2.0 * x_norm[i])
            # Add coupling between dimensions
            coupling_effect = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_effect += np.sin(x_norm[i] - x_norm[j]) * 0.1
            interference_val *= (1.0 + 0.2 * coupling_effect)
            interference_term += interference_val
            
        # Basin boundary effects with quantum-like tunneling
        basin_term = 0.0
        for i in range(self.dim):
            radius = self.basin_radii[i]
            depth = self.basin_well_depths[i]
            # Basin potential with quantum-like tunneling
            distance_from_center = np.abs(x_norm[i])
            basin_val = depth * (1.0 + np.exp(-distance_from_center / radius))
            basin_term += basin_val
            
        # Combine all terms with dynamic weighting
        result = 1.3 * quantum_term + 1.1 * radial_term + 0.9 * entropy_term + 0.7 * interference_term + 1.2 * basin_term
        
        # Add quantum-like stochastic noise
        noise_amplitude = 0.05 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn() * np.cos(3.0 * np.random.rand())
        
        return result + noise